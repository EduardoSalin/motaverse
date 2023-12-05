'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Students:
Brady Lamson, Emerson Hatton, Riley Moen, Ebenezer Addei, Eduardo Salinas
Description: Routes for the SQLAlchemy application
'''
from app import app, db, load_user
from app.models import User, Post, Comment
from app.forms import *
from flask import render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, login_user, logout_user, current_user
import bcrypt


@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/user/signup', methods=['GET', 'POST'])
def user_signup():
    form = SignUpForm()

    if form.validate_on_submit():
        passwd = form.passwd.data
        passwd_confirm = form.passwd_confirm.data

        # Check if passwords match
        if passwd != passwd_confirm:
            return '<p>Passwords do not match</p>'

        # Hash the password
        hashed = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())

        # Check if a user with the given ID already exists
        existing_user = User.query.filter_by(id=form.id.data).first()
        if existing_user:
            return '<p>User with this ID already exists!</p>'

        # Create a new user
        new_user = User(
            id=form.id.data,
            name=form.name.data,
            profile_picture=form.profile_picture.data,
            passwd=hashed
        )

        # Add the new user to the database and commit
        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('user_signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # Replace with the actual form you're using for login

    if form.validate_on_submit():
        id = form.id.data
        passwd = form.passwd.data

        user = User.query.filter_by(id=id).first()

        if user and bcrypt.checkpw(passwd.encode('utf-8'), user.passwd):
            # User login successful
            login_user(user)
            flash('User login successful', 'success')
            return redirect(url_for('motaverse'))
        else:
            flash('Invalid ID or password', 'danger')

    return render_template('login.html', form=form)


# This will log out the user and remove their information from the session
@app.route('/user/signout')
def user_signout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/user/signout')
def admin_signout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/save_post', methods=['POST'])
@login_required
def save_post():
    new_post_request = request.form['newPostContent']
    new_post = Post(content=new_post_request, user=current_user)

    # Add the post to the user and commit the change to the db
    current_user.posts.append(new_post)
    db.session.add(new_post)
    db.session.commit()

    print(f"New post created: {new_post.content}")
    return redirect(url_for('motaverse'))


@app.route('/like_post', methods=['POST'])
@login_required
def like_post():

    post_id = request.form['post']
    post = (
        Post
        .query
        .filter_by(id=post_id)
        .first()
    )

    # We need to remove the pre-existing like first to prevent
    # uniqueness errors in the other condition.
    if current_user in post.likes:
        post.likes.remove(current_user)
    else:
        post.likes.append(current_user)

    db.session.commit()
    return redirect(request.referrer)


@app.route('/submit_comment', methods=['POST'])
@login_required
def submit_comment():
    comment_content = request.form.get('comment_content')
    post_id = request.form.get('post_id')

    # Ensure the comment content and post ID are provided
    if not comment_content or not post_id:
        flash('Invalid comment submission', 'danger')
        return redirect(url_for('motaverse'))

    post = Post.query.get(post_id)

    # Create a new comment
    new_comment = Comment(content=comment_content, user=current_user)

    # Associate the comment with the post
    post.comments.append(new_comment)

    # Add the comment to the database and commit the change
    db.session.add(new_comment)
    db.session.commit()

    return redirect(request.referrer)


@app.route('/motaverse')
@login_required
def motaverse():
    all_posts = (
        Post
        .query
        .order_by(Post.id.desc())
        .limit(100)
        .all()
    )
    all_users = User.query.all()
    current_user_profile_pic_url = url_for(
        'static',
        filename='pic/' + current_user.profile_picture)
    current_user_display_name = current_user.name
    filtered_posts = filter_blocked_posts(all_posts,
                                          current_user.blocked_users)

    return render_template(
        'motaverse.html',
        all_users=all_users,
        current_user_profile_pic_url=current_user_profile_pic_url,
        current_user_display_name=current_user_display_name,
        posts=filtered_posts
    )


def filter_blocked_posts(posts, blocked_users):
    # Filter out posts from blocked users
    return [post for post in posts if post.user not in blocked_users]


@app.route('/block_user', methods=['POST'])
def block_user():
    user_id_to_block = request.form.get('user_id')
    user_to_block = User.query.filter_by(id=user_id_to_block).first()

    if user_to_block:
        current_user.blocked_users.append(user_to_block)
        db.session.commit()

    return redirect(request.referrer)


@app.route('/unblock_user', methods=['POST'])
def unblock_user():
    user_id_to_unblock = request.form.get('user_id')
    user_to_unblock = User.query.filter_by(id=user_id_to_unblock).first()

    if user_to_unblock:
        current_user.blocked_users.remove(user_to_unblock)
        db.session.commit()

    return redirect(request.referrer)


@app.route('/display_post/<int:post_id>')
@login_required
def display_post(post_id):
    # Retrieve the post and its comments based on the post_id
    post = get_post_by_id(post_id)
    all_users = User.query.all()
    current_user_prof_pic = url_for(
        'static',
        filename='pic/' + current_user.profile_picture)
    current_user_display_name = current_user.name

    return render_template('Display_Post.html',
                           post=post,
                           all_users=all_users,
                           current_user_profile_pic_url=current_user_prof_pic,
                           current_user_display_name=current_user_display_name)


def get_post_by_id(post_id):
    return Post.query.get(post_id)


# Route to delete a post and its associated comments
@app.route('/delete_post/<int:post_id>', methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    # Check if the current user is the author of the post
    if current_user.id == post.user_id:
        # Delete associated comments
        Comment.query.filter_by(post_id=post.id).delete()

        # Delete the post
        db.session.delete(post)
        db.session.commit()
        flash('Post and comments deleted successfully!', 'success')
    else:
        flash('You do not have permission to delete this post!', 'danger')

    return redirect(url_for('motaverse'))  # Redirect to the main page


# Route to delete a comment
@app.route('/delete_comment/<int:comment_id>', methods=['POST'])
@login_required
def delete_comment(comment_id):
    comment = Comment.query.get_or_404(comment_id)

    # Check if the current user is the author of the comment
    if current_user.id == comment.user_id:
        db.session.delete(comment)
        db.session.commit()
        flash('Comment deleted successfully!', 'success')
    else:
        flash('You do not have permission to delete this comment!', 'danger')

    return redirect(url_for('motaverse'))  # Redirect to the main page

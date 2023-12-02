from app import app, db
from app.models import User, Post, post_likes

with app.app_context():
    first_post = Post.query.first()
    print(f"Example Post id: {first_post.id}")
    print(f"Example post user: {first_post.user_id}")

    first_user = User.query.first()

    # if first_post in first_user.liked_posts:
    #     first_user.liked_posts.remove(first_post)

    if first_user in first_post.likes:
        first_post.likes.remove(first_user)

    first_user.liked_posts.append(first_post)
    print(f"Example User: {first_user.name}")

    print(f"Example Users liked posts: {first_user.liked_posts}")
    print(f"Example Post likes: {first_post.likes}")
    print(f"Number of Likes: {first_post.count_likes()}")
    # print(db.session.query())
    print("Remove the like")
    # first_user.liked_posts.remove(first_post)
    # first_post.likes.remove(first_user)
    # print(f"Example Post likes: {first_post.likes}")

    db.session.commit()

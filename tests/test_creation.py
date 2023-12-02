import unittest
from app import app, db
from app.models import User, Post, Comment

class ModelsTestCase(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()


    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


    def test_user_creation(self):
        user = User(id="testuser", name="Test User 1", profile_picture="pic1.jpg")
        db.session.add(user)
        db.session.commit()
        with db.session.begin():
            self.assertIsNotNone(db.session.get(User, "testuser"))


    def test_post_creation(self):
        user = User(id="testuser2", name="Test User 2", profile_picture="pic2.jpg")
        post = Post(content="Test Post", user=user)
        db.session.add_all([user, post])
        db.session.commit()
        self.assertEqual(len(user.posts), 1)


    def test_comment_creation(self):
        user = User(id="testuser3", name="Test User 3", profile_picture="pic3.jpg")
        post = Post(content="Test Post for Comment", user=user)
        comment = Comment(content="Test Comment", user=user, post=post)
        db.session.add_all([user, post, comment])
        db.session.commit()
        self.assertEqual(len(post.comments), 1)

    # Add more tests as needed

if __name__ == '__main__':
    unittest.main()

import unittest
from flask import url_for
from app import app, db
from app.models import User, Post
from unittest.mock import patch

class RoutesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app  # Use the app instance directly
        self.app.config['TESTING'] = True  # Enable testing mode
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()  # Initialize test client

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()


#This will allow the test to run without having to "log in"
    @patch('flask_login.utils._get_user')
    def test_save_post(self, current_user):
        # Mock a user
        user = User(id="testuser", name="Test User", profile_picture="pic1.jpg")
        db.session.add(user)
        db.session.commit()
        current_user.return_value = user

        # Simulate POST request to save_post
        response = self.client.post('/save_post', data={
            'newPostContent': 'Test Post'
        }, follow_redirects=True)

        # Check if the post was added
        post = Post.query.filter_by(content='Test Post').first()
        self.assertIsNotNone(post)
        self.assertEqual(response.status_code, 200)

    # Add more test cases for other routes

if __name__ == '__main__':
    unittest.main()

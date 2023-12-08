<p align="center">
    <img src="pics/motaverse.png" alt="motavese" width="500"/>
</p>

# Overview

## Mission Statement

- For a better universe, motaverse

"This web application seeks to inform its developers on the nuance and care taken into developing modern social media applications. By attempting to emulate basic functionality and recognizing the difficulty therein, a better appreciation for the tools we take for granted will be acquired."

### Use case Diagram

<p align="center">
    <img src="pics/UseCase.png" alt="Use Case Diagram"/>
</p>

# User stories

## User Story #1 - Sign up functionality

_As a user, I want to be able to register for an online blogging platform. Given that a user provides a username, their name, password and chooses profile picture, when the user clicks on the "Sign up" button then their user information is saved and a user profile is created._

**Additional Information**

- Profiles should be created to demonstrate functionality.

**For testing:**
Preloaded user profiles are available for testing, all of the passwords are `1`
You can create a new one or choose one of this usernames: `tmota`, `a`, `b`, `c`, `d`, or `e`

## User Story #2 - Post submission

_As a registered user, I want to log in to the online platform, so I can create new posts. Upon presenting valid credentials they are presented with the main page. User can create a new post in the given "New post" field, my post alongside other posts should appear in chronological order, showing the newest ones on top._

**Additional Information**

- If credentials are not valid a notice should appear at the log in page
- Posts should appear immediately and in chronological order, showing the newest ones on top.
- Users should not be able to submit an empty post.

### Sequence Diagram for Post Submission

<p align="center">
    <img src="pics/SequenceD.png" alt="Use Case Diagram"/>
</p>

## User Story #3 - Commenting on Posts

_As a registered user, I want to be able to comment on any already existing post. Since the post has already been created, I should be able to click "comment" button and write a reply to this post._

**Additional information**

- Comments should appear in chronological order showing the older ones on top and newer ones at the bottom.
- The name of the person that made that comment should appear next to the comment, along side the profile picture.

## User Story #4 - Like posts

_As a registered user, I want to be able to like any already existing post. I also want to be able to see how many likes any given post has._

**Additional information**

- Users should be able to like a post only once
- If a user has liked a post, they should be able to remove that like.

## User Story #5

_As a registered user, I want to block people, if I have blocked a profile, I expect their posts and comments to be immediately hidden from my feed._

**Additional information**

- The block button should not be on the actively logged in profile.
- To block someone you can find the block button next to their name in the "profile" list or on a post that they made.
- To unblock someone the unblock button should appear next to their name in the Profile list.

## User Story #6 - Deleting Posts

_As a registered user, if I have submitted a post or a comment, I want to be able to delete the post in case I made a mistake or no longer want it displayed._

**Additional information**

- There should be a delete button next to posts or comments that I have created.
- Deleting a post should also remove all associated comments and likes.
- The option should only be visible to me as the creator of the post or comment.

# Design

## Class Diagram

<p align="center">
    <img src="pics/classDiagram.png" alt="Class Diagram"/>
</p>

# Development Process

| Sprint# | Goals                        | Start    | End      | Done                                                                                                       | Observations                                                                                                                                                       |
| ------- | ---------------------------- | -------- | -------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1       | Design, US#1                 | 11/16/23 | 11/28/23 | Finilized Design and finished sign up implementation                                                       | Team took firm decision on where to take the project, started implementing sign in and sign up functionality                                                       |
| 2       | US#2, US#3, US#4             | 11/28/23 | 12/02/23 | Finished implementing post creation, comments to post as well as likes, started setting up for next sprint | Once User Story #2, implementation of posts, was implemented the other two user stories were not as comlpicated                                                    |
| 3       | US#5, US#6                   | 12/02/23 | 12/05/23 | Finished implementing user blocking feature as well as post and comment deletion                           | We were able to get the last two user stories done in a short amount of time giving us extra time to focus on the final touches, and make sure PEP8 was being used |
| Last    | Testing and containerization | 12/05/23 | 12/07/23 | Finalized Implementation, testing and containerization                                                     | This final sprint was dedicated for testing and containerization, as well as final touches in documentation and code review                                        |

You can find comprehensive details on our scrum meetings in the `scrum` folder. This folder contains detailed records of the development process, documenting each step and decision as the project evolved.

# Testing

## Unit testing coverage

_Testing using python's coverage package._ In `test` folder you will find `test_creation.py`. From there you can run

```
coverage run -m unittest tests/test_creation.py
```

**Models Testing:**

- Focuses on internal logic of data models (User, Post, Comment).
- Validates object creation and database persistence.
- Ensures correct relationships and associations between models.

**Routes Testing:**

- Evaluates the application's endpoints without delving into internal workings.
- Includes a test for the /save_post route, simulating a POST request and verifying the correct addition of posts to the database.
- Utilizes mocked user sessions to bypass authentication for route testing.

# Black-box Testing Steps

Black-box testing is performed without knowledge of the internal workings of the application. It's focused on testing the user interface and functionality against the requirements.

**Setting Up Cypress for Black-box Testing:**
1. Open the Cypress Test Runner using the command:
    ```shell
    node_modules/.bin/cypress open
    ```
    if on mac you might have to run:
    ```
    yarn add cypress --dev
    
    sudo node_modules/.bin/cypress open
    ```
2. Choose 'E2E Testing' from the Cypress dashboard.
3. Select your preferred browser; Chrome is recommended.
4. Click 'Start E2E Testing in Chrome' to proceed.

*Side note: you might need to have the Flask app running while testing for cypress to be able to open the page*

**Executing Black-box Test Scenarios:**
- **Sign Up Verification:**
  1. Ensure the 'Sign Up' button is visible on the homepage.
  2. Click the 'Sign Up' button and confirm that you're redirected to the sign-up page.
  3. Fill out the sign-up form with user details.
  4. Submit the form and verify that you're redirected to the index page.

- **Login Functionality Check:**
  1. Wait for 3 seconds to simulate user interaction time before clicking the 'Log In' button.
  2. Enter a valid username and password into the login form.
  3. Click the 'Log In' button.
  4. Confirm that the redirection to the motaverse page is successful after login.

# White-box Testing Steps

White-box testing examines the internal structures or workings of an application, which is mainly focused on the testing of the code.

**Verifying Internal Functions and Logic:**
- **Local Server Access Check:**
  1. Confirm that the local development server is reachable through the given URL.

- **Homepage Content Assessment:**
  1. Ensure that the homepage loads successfully.
  2. Verify that the correct onboarding text is displayed on the homepage.

- **Logo and UI Element Visibility:**
  1. Confirm the Motaverse logo is visible on the homepage.
  2. Check the visibility of key interactive buttons like 'Sign Up' and 'Log In'.

- **Form Functionality and Error Handling:**
  1. Navigate to the sign-up page and confirm the visibility of text fields.
  2. Input user details into the sign-up form fields.
  3. Click the 'Confirm' button on the sign-up form.
  4. Handle scenarios where the user already exists by checking the displayed error message.

- **Redirection and Response Validation:**
  1. Ensure that clicking the 'Log In' button redirects to the login page.
  2. Verify that the correct headings and form labels are displayed on the login page.
  3. Check the functionality of the login form by entering user credentials.
  4. Validate that the application redirects to the correct page upon successful login.

Each test suite in both black-box and white-box testing is designed to rigorously test different aspects of the application to ensure that all user-facing features and underlying code are functioning correctly.


# Deployment Instructions

Instructions for deploying this project are simple. All files necessary for image generation are present in the repository by default. Only some simple port mapping is required.

```
sudo docker build -t motaverse .
sudo docker run -p 5000:5000 motaverse
```

Then, when various urls are listed in the terminal, select `http://127.0.0.1:5000/`.


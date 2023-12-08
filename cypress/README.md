# README for Cypress Testing

This README documents the step-by-step process of what I based on to performed automated end-to-end testing on a web application using Cypress.


## Test Suites

### Local Server Accessibility Test

1. **Objective**: Verify that the homepage is accessible.
2. **Execution**: Run Cypress and execute the test suite named 'Local Server Accessibility Test'.
3. **Expected Outcome**: The homepage should load successfully at `http://127.0.0.1:5000`.

### Homepage Content Tests

1. **Objective**: Ensure the homepage displays the correct onboarding text.
2. **Execution**: Within the same test suite, check for the presence of an `<h2>` element containing the text 'Sign up or log in to get started'.
3. **Expected Outcome**: The specified `<h2>` text should be visible to the user.

### Homepage Logo Display Test

1. **Objective**: Confirm that the Motaverse logo is displayed on the homepage.
2. **Execution**: Look for an `<img>` element with the alt text 'Motaverse'.
3. **Expected Outcome**: The logo should be visible.

### Button Visibility Tests

1. **Objective**: Verify that the 'Sign Up' and 'Log In' buttons are visible.
2. **Execution**: Look for the buttons by their text content.
3. **Expected Outcome**: Both buttons should be visible to the user.

### Sign Up Button Functionality Test

1. **Objective**: Test the functionality of the 'Sign Up' button.
2. **Execution**: Click the 'Sign Up' button and verify that the URL changes to the sign-up page.
3. **Expected Outcome**: The user should be navigated to `http://127.0.0.1:5000/user/signup`.

### Sign Up Form Text and Profile Picture Visibility Test

1. **Objective**: Check the visibility of text fields and profile pictures on the sign-up page.
2. **Execution**: Verify the visibility of the 'Sign Up' heading, input labels, profile pictures, and the 'Confirm' button.
3. **Expected Outcome**: All elements should be visible and the profile pictures should be equal to 8 in count.

### Sign Up Form Functionality Test

1. **Objective**: Ensure the sign-up form handles both new and existing user scenarios.
2. **Execution**: Fill out the sign-up form and submit. Check for the presence of a user error message or redirection to the index page.
3. **Expected Outcome**: If a user exists, the URL should not change. Otherwise, expect redirection to `http://127.0.0.1:5000/index.html`.

### Log In Redirect Test

1. **Objective**: Test the redirection to the login page when the 'Log In' button is clicked.
2. **Execution**: Click the 'Log In' button after a brief wait.
3. **Expected Outcome**: The user should be redirected to `http://127.0.0.1:5000/login`.

### Login Page Visibility Tests

1. **Objective**: Confirm that the login page displays all necessary elements.
2. **Execution**: Check for the visibility of the 'Login' heading, username and password labels and inputs, and the 'Log In' button.
3. **Expected Outcome**: All elements should be visible.

### Login Functionality Test

1. **Objective**: Verify that a user can log in and be redirected to the motaverse page.
2. **Execution**: Enter credentials into the username and password fields, submit the form, and verify the redirection.
3. **Expected Outcome**: After clicking the 'Log In' button, the user should be redirected to `http://127.0.0.1:5000/motaverse`.

## Running the Tests

To run the tests, open your terminal, navigate to your project directory, and execute the following command:

```shell
node_modules/.bin/cypress open
```

This will open the Cypress Test Runner. From there, you can select and run individual test suites or run all tests together.

## Conclusion

Cypress provides a robust platform for performing automated end-to-end testing. By following the documented steps, you can ensure that your application functions correctly from a user's perspective.
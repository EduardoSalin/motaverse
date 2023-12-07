/**
 * Test Suite: Accessing the Local Development Server
 * This suite performs a simple test to verify that the local development server
 * can be accessed through the specified URL.
 */
describe('Local Server Accessibility Test', () => {
  it('should load the homepage at the specified local URL', () => {
    cy.visit('http://127.0.0.1:5000');
    // Additional assertions or interactions could be placed here if needed.
  });
});

/**
 * Test Suite: Homepage Content Verification
 * This suite ensures that essential content on the homepage is correctly displayed.
 */
describe('Homepage Content Tests', () => {
  before(() => {
    cy.visit('http://127.0.0.1:5000');
  });

  it('should display the correct <h2> text for user onboarding', () => {
    cy.get('h2').contains('Sign up or log in to get started').should('be.visible');
  });
});

/**
 * Test Suite: Homepage Logo Display
 * This suite verifies that the Motaverse logo is properly displayed.
 */
describe('Homepage Logo Display Test', () => {
  before(() => {
    cy.visit('http://127.0.0.1:5000');
  });

  it('should display the Motaverse logo', () => {
    cy.get('img[alt="Motaverse"]').should('be.visible');
  });
});

/**
 * Test Suite: Button Visibility Verification
 * This suite confirms that interactive buttons are visible to the user.
 */
describe('Button Visibility Tests', () => {
  before(() => {
    cy.visit('http://127.0.0.1:5000');
  });

  it('should display the Sign Up button', () => {
    cy.contains('Sign Up').should('be.visible');
  });

  describe('Log In Button Visibility Test', () => {
    before(() => {
      cy.visit('http://127.0.0.1:5000');
    });

    it('should display the Log In button', () => {
      cy.contains('button', 'Log In').should('be.visible');
    });
  });
});

/**
 * Black Box Test: Sign Up Button Functionality
 * This test checks the functionality of the Sign Up button.
 */
describe('Sign Up Button Test', () => {
  before(() => {
    cy.visit('http://127.0.0.1:5000');
  });

  it('should navigate to the Sign Up page when the Sign Up button is clicked', () => {
    cy.get('button.button').contains('Sign Up').should('be.visible').click();
    cy.url().should('include', '/user/signup');
  });
});

/**
 * Test Suite: Sign Up Form Text and Profile Picture Visibility
 * This suite checks the visibility of text fields and profile pictures on the sign up page.
 */
describe('Sign Up Form Text and Profile Picture Visibility Test', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:5000/user/signup');
  });

  it('should display all the necessary text fields on the sign up page', () => {
    cy.contains('Sign Up').should('be.visible');
    cy.contains('label', 'Username').should('be.visible');
    cy.contains('label', 'Name').should('be.visible');
    cy.contains('label', 'Password').should('be.visible');
    cy.contains('label', 'Confirm Password').should('be.visible');
    cy.contains('Profile Picture').should('be.visible');
    cy.get('.profile-picture-option').should('have.length', 8);
    cy.get('input[type="submit"][value="Confirm"]').should('be.visible');
  });
});

/**
 * Test Suite: Sign Up Form Functionality
 * This suite tests the functionality of the sign up form.
 */
describe('Sign Up Form Functionality Test', () => {
  it('should handle both new user signup and existing user scenario', () => {
    cy.visit('http://127.0.0.1:5000/user/signup');

    cy.get('input#id').type('test3');            
    cy.get('input#name').type('test3');          
    cy.get('input#passwd').type('1234');         
    cy.get('input#passwd_confirm').type('1234'); 
    cy.get('img[src="/static/pic/pic1.jpg"]').parent().click();

    cy.get('input[type="submit"]').click();

    cy.get('body').then(($body) => {
      if ($body.text().includes('User with this ID already exists')) {
        cy.url().should('include', '/user/signup');
      } else {
        cy.url().should('eq', 'http://127.0.0.1:5000/index.html');
      }
    });
  });
});

/**
 * Test Suite: Log In Redirect Functionality
 * This suite tests the redirection to the login page when the Log In button is clicked.
 */
describe('Log In Redirect Test', () => {
  it('should redirect to the login page when the Log In button is clicked', () => {
    cy.visit('http://127.0.0.1:5000');

    cy.wait(3000); // Waits for 3 seconds.

    cy.contains('button', 'Log In').click();

    cy.url().should('eq', 'http://127.0.0.1:5000/login');
  });
});

/**
 * Test Suite: Login Page Visibility Tests
 * This suite checks the visibility of elements on the login page.
 */
describe('Login Page Visibility Tests', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:5000/login');
  });

  it('should display the Login heading', () => {
    cy.contains('h1', 'Login').should('be.visible');
  });

  it('should display the Username label and input', () => {
    cy.contains('label', 'Username').should('be.visible');
    cy.get('input[id="id"]').should('be.visible');
  });

  it('should display the Password label and input', () => {
    cy.contains('label', 'Password').should('be.visible');
    cy.get('input[id="passwd"]').should('be.visible');
  });

  it('should display the Log In button', () => {
    cy.get('input[type="submit"][value="Log In"]').should('be.visible');
  });
});

/**
 * Test Suite: Login Functionality Test
 * This suite tests the login functionality and the subsequent redirection to the motaverse page.
 */
describe('Login Functionality Test', () => {
  beforeEach(() => {
    cy.visit('http://127.0.0.1:5000/login');
  });

  it('allows a user to log in and redirects to the motaverse page', () => {
    cy.get('input#id').type('test1');
    cy.get('input#passwd').type('1234');
    cy.wait(2000); // Waits for 2 seconds.
    cy.get('input#submit').click();
    cy.url().should('eq', 'http://127.0.0.1:5000/motaverse');
  });
});

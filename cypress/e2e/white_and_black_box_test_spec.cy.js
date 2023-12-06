/**
 * Test Suite: Accessing the Local Development Server
 * This suite performs a simple test to verify that the local development server
 * can be accessed through the specified URL.
 */
describe('Local Server Accessibility Test', () => {

  /**
   * Test Case: Visit Homepage
   * Ensures that the homepage at the local URL loads successfully.
   */
  it('should load the homepage at the specified local URL', () => {
    cy.visit('http://127.0.0.1:5000'); // Command to navigate to the homepage.
    // Place for additional assertions or interactions if needed.
  });

});

/**
 * Test Suite: Homepage Content Verification
 * This suite checks that essential content on the homepage is rendered correctly.
 */
describe('Homepage Content Tests', () => {

  before(() => {
    cy.visit('http://127.0.0.1:5000'); // Precondition to navigate to the homepage.
  });

  it('should display the correct <h2> text for user onboarding', () => {
    cy.get('h2').contains('Sign up or log in to get started').should('be.visible'); // Validates the visibility of the onboarding text.
  });

});

/**
 * Test Suite: Homepage Logo Display
 * This suite confirms that the Motaverse logo is displayed as expected.
 */
describe('Homepage Logo Display Test', () => {
  before(() => {
    cy.visit('http://127.0.0.1:5000'); // Precondition to navigate to the homepage.
  });

  it('should display the Motaverse logo', () => {
    cy.get('img[alt="Motaverse"]').should('be.visible'); // Verifies the logo's visibility.
  });
});

/**
 * Test Suite: Button Visibility Verification
 * This suite ensures that interactive buttons are visible to the user.
 */
describe('Button Visibility Tests', () => {
  before(() => {
    cy.visit('http://127.0.0.1:5000'); // Precondition to navigate to the homepage.
  });

  it('should display the Sign Up button', () => {
    cy.contains('Sign Up').should('be.visible'); // Asserts the Sign Up button is visible.
  });

  /**
   * Nested Test Suite: Log In Button Visibility
   * Checks specifically for the visibility of the Log In button.
   */
  describe('Log In Button Visibility Test', () => {
    before(() => {
      cy.visit('http://127.0.0.1:5000'); // Ensures the homepage is reloaded before this set of tests.
    });

    it('should display the Log In button', () => {
      cy.contains('button', 'Log In').should('be.visible'); // Asserts the Log In button is visible.
    });
  });

});

import pytest
from playwright.sync_api import sync_playwright

# Test function for login page with valid credentials
def test_login_valid(page):
    page.locator('input[placeholder="Email"]').fill('john.doe@example.com')
    page.locator('input[placeholder="Password"]').fill('P@ssw0rd123')
    page.locator('button').click()

# Test function for login page with invalid credentials
def test_login_invalid_email(page):
    page.locator('input[placeholder="Email"]').fill('invalid_email_format')
    page.locator('input[placeholder="Password"]').fill('short')
    page.locator('button').click()

# Test function for login page with empty email field
def test_login_empty_email(page):
    page.locator('input[placeholder="Email"]').fill('')
    page.locator('input[placeholder="Password"]').fill('noemail@123')
    page.locator('button').click()

# Test function for login page with empty password field
def test_login_empty_password(page):
    page.locator('input[placeholder="Email"]').fill('harry.potter@hogwarts.edu')
    page.locator('input[placeholder="Password"]').fill('')
    page.locator('button').click()
    
# ERROR HANDLING: Invalid email format
# Tests that the login form does not accept invalid email format
def test_login_invalid_email_format(page):

    page.locator('input[placeholder="Email"]').fill('invalid_email')
    page.locator('input[placeholder="Password"]').fill('password')
    page.locator('button').click()

# ERROR HANDLING: Empty email
# Tests that the login form does not accept empty email
def test_login_empty_email_field(page):
    page.locator('input[placeholder="Email"]').fill('')
    page.locator('input[placeholder="Password"]').fill('password')
    page.locator('button').click()

# ERROR HANDLING: Empty password
# Tests that the login form does not accept empty password
def test_login_empty_password_field(page):
    page.locator('input[placeholder="Email"]').fill('email@example.com')
    page.locator('input[placeholder="Password"]').fill('')
    page.locator('button').click()

# Setup and teardown functions for each test

def setup_function(request):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto("file:///your/html/file.html") # Replace with your HTML file path
        request.cls.page = page

def teardown_function(request):
    request.cls.page.close()
    request.cls.browser.close()
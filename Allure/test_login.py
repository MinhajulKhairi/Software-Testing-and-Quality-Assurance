import pytest
import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Scenario: login success
@allure.feature('SauceDemo')
@allure.story('Login Successfully and Checkout Item')
@pytest.mark.parametrize("username, password", [("standard_user", "secret_sauce")])
def test_successful_login_and_checkout(setup, username, password):
    driver = setup # Call fixture 'setup'

    # Step 1: Open SauceDemo website
    with allure.step("Open SauceDemo website"):
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

    # Step 2: Input Username
    with allure.step("Input Username"):
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "user-name"))
        )
        username_input.send_keys(username)
        time.sleep(1)

    # Step 3: Input Password
    with allure.step("Input Password"):
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        password_input.send_keys(password)
        time.sleep(1)

    # Step 4: Click Login Button
    with allure.step("Click Login Button"):
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()
        time.sleep(1)

    # Step 5: Verify successful login
    with allure.step("Verify successful login"):
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/inventory.html")
        )
        time.sleep(2)

    # Step 6: Add item to cart
    with allure.step("Add item to cart"):
        add_to_cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_to_cart_button.click()
        time.sleep(1)

    # Step 7: Go to Cart
    with allure.step("Go to Cart"):
        cart_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_button.click()
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/cart.html")
        )
        time.sleep(2)

    # Step 8: Proceed to Checkout
    with allure.step("Proceed to Checkout"):
        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()
        time.sleep(2)

    # Step 9: Fill Checkout Information
    with allure.step("Fill Checkout Information"):
        first_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name_input.send_keys("John")
        time.sleep(1)

        last_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "last-name"))
        )
        last_name_input.send_keys("Doe")
        time.sleep(1)

        postal_code_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "postal-code"))
        )
        postal_code_input.send_keys("12345")
        time.sleep(1)

    # Step 10: Click Continue to the next step
    with allure.step("Click Continue"):
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()
        time.sleep(2)

    # Step 11: Finish purchase and verify success message
    with allure.step("Finish purchase and verify success message"):
        finish_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "finish"))
        )
        finish_button.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        time.sleep(2)

    # Step 12: Back to Home
    with allure.step("Back to Home"):
        back_home = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "back-to-products"))
        )
        back_home.click()
        time.sleep(2)



# Scenario login failed
@allure.feature('SauceDemo')
@allure.story('Login Failed')
@pytest.mark.parametrize("username, password", [("locked_out_user", "secret_sauce")])
def test_failed_login(setup, username, password):
    driver = setup # Call fixture 'setup'
    
    # Step 1: Open SauceDemo website
    with allure.step("Open SauceDemo website"):
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)
        
    # Step 2: Input username
    with allure.step("Input Username"):
        username_input = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "user-name"))
        )
        username_input.send_keys(username)
        time.sleep(1)
        
    # Step 3: Input Password
    with allure.step("Input Password"):
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.ID, "password"))
        )
        password_input.send_keys(password)
        time.sleep(1)
    
    # Step 4: Clilck login button
    with allure.step("Click Login Button"):
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "login-button"))
        )
        login_button.click()
        time.sleep(1)
        
    # Step 5: Verify failed login (error message appears)
    with allure.step("Verify failed login"):
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "error-message-container"))
        )
        assert "Epic sadface" in error_message.text, "Failed login not detected"
        time.sleep(2)
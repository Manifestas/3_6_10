from selenium.webdriver.common.by import By


def test_product_page_contains_add_cart_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    browser.find_element(By.CSS_SELECTOR, '#add_to_basket_form button[type="submit"]')
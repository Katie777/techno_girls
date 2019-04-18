from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.XPATH, "//input[@type='submit' and @class='nav-input']")
RESULTS_INFO_BAR = (By.XPATH, "//span[@data-component-type='s-result-info-bar']/div")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Input {word} into Amazon search field')
def input_query(context, word):
    el = context.driver.find_element(*SEARCH_FIELD)
    el.clear()
    el.send_keys(word)


@when('Click on Amazon search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_ICON).click()


@then('Amazon product results for {word} are shown')
def verify_result_present(context, word):
    assert word in context.driver.find_element(*RESULTS_INFO_BAR).text
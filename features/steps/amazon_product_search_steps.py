from behave import given, when, then
from time import sleep
from pages.locators import *


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


@when('Click on Help button')
def click_help_button(context):
    context.driver.find_element(*HELP_BUTTON).click()


@when('Input {word} into Help search field')
def input_query(context, word):
    el = context.driver.find_element(*HELP_SEARCH_FIELD)
    el.clear()
    el.send_keys(word)


@when('Click Go button')
def click_go_button(context):
    context.driver.find_element(*HELP_GO_BUTTON).click()


@then('{word} text is shown')
def verify_result_present(context, word):
    assert word in context.driver.find_element(*HELP_INFO_BAR).text


@when('Click Orders button')
def click_orders_button(context):
    context.driver.find_element(*ORDERS_BUTTON).click()


@then('Verify {word} fields are shown')
def verify_result_present(context, word):
    context.driver.find_element(*SIGN_IN_BUTTON)

@when('Click Hamburger menu button')
def click_humburger_menu(context):
    context.driver.find_element(*HAMBURGER_MENU).click()


@then('Verify Shop by category text is present')
def verify_shop_category(context):
    context.driver.find_element(*SHOP_BY_CATEGORY)

@then('Click on closing X of the menu')
def click_close_button(context):
    context.driver.find_element(*HAMBURGER_CLOSE_BUTTON).click()


@then('Click on Try Prime button from Amazon logo')
def click_try_prime_button(context):
    context.driver.find_element(*TRY_PRIME_LOGO_BUTTON).click()


@then('Verify Try Prime button is present')
def verify_prime_button_present(context):
    context.driver.find_element(*TRY_PRIME_BUTTON)






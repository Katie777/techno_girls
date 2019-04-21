from selenium.webdriver.common.by import By

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.XPATH, "//input[@type='submit' and @class='nav-input']")
RESULTS_INFO_BAR = (By.XPATH, "//span[@data-component-type='s-result-info-bar']/div")
HELP_BUTTON = (By.XPATH, "//a[contains(@href, 'nav_cs_help')]")
HELP_SEARCH_FIELD = (By.XPATH, "//input[@type='search']")
HELP_INFO_BAR = (By.XPATH, "//div[contains(@class, 'a-box-inner')]")
HELP_GO_BUTTON = (By.ID, 'helpSearchSubmit')
ORDERS_BUTTON = (By.ID, 'nav-orders')
EMAIL_FIELD = (By.ID, 'ap_email')
PASSWORD_FIELD = (By.ID, 'ap_password')
SIGN_IN_BUTTON = (By.ID, 'signInSubmit')
SHOP_BY_CATEGORY = (By.XPATH, "//div[text()='SHOP BY CATEGORY']")
HAMBURGER_MENU = (By.ID, 'nav-hamburger-menu')
HAMBURGER_CLOSE_BUTTON = (By.XPATH, "//div[contains(@class, 'nav-sprite hmenu-close-icon')]")
TRY_PRIME_LOGO_BUTTON = (By.XPATH, "//a[contains(@class, 'nav-sprite nav-logo-tagline nav-prime-try')]")
TRY_PRIME_BUTTON = (By.XPATH, "//input[@class='prime-cta-signup-button-input']")

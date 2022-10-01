from seleniumpagefactory.Pagefactory import PageFactory

class Homepage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    "dropdown": ("ID", "loginSignupDropdown"),
    "sign_in":("CSS",".login-signup-button"),
    }

    def click_sign_in(self):
        self.dropdown.click()
        self.sign_in.click()



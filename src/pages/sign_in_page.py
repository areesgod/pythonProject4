from seleniumpagefactory.Pagefactory import PageFactory

class SignInPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
    'user_name': ("ID", "username"),
    'password': ("NAME", "password"),
    'login_btn': ("CSS", '.loyalty-submit-button-active')
    }

    def select_username(self):
        self.user_name.set_text('7085521350')

    def select_password(self):
        self.password.set_text('qwerty1234')

    def click_login(self):
        self.login_btn.click()
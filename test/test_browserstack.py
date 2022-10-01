from selenium import webdriver
from src.pages.homepage import Homepage
from src.pages.sign_in_page import  SignInPage
from src.pages.bookpage import BookPage
from time import sleep
def test_browserstack():
    driver = webdriver.Chrome(
        executable_path=r"C:\Users\webdriver\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://flyarystan.com/en")
    homepage = Homepage(driver)
    sign_in_page = SignInPage(driver)
    bookpage = BookPage(driver)
    homepage.click_sign_in()
    sign_in_page.select_password()
    sign_in_page.select_username()
    sign_in_page.click_login()
    bookpage.bookclick()
    bookpage.choosedestination()
    bookpage.choosedate()
    bookpage.submitb()
    sleep(5)


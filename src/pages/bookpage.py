from seleniumpagefactory.Pagefactory import PageFactory

class BookPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'droplist':("CSS",".filter-option-inner-inner"),
        'bookbutton': ("CSS", '.loyalty-new-reservation'),
        'droplistsec':("XPATH","(//div['filter-option-inner-inner' and contains(text(),'Select Arrival Flight')])"),
        'wherefrom':("XPATH","//a[@id = 'bs-select-1-6']"),
        'whereto':("XPATH","//a[@id = 'bs-select-2-3']"),
        'date':("ID","oneWayDepartureDate"),
        'submitbutton':("CSS",'.js-submit-button')

    }
    def bookclick(self):
        self.bookbutton.click()
    def choosedestination(self):
        self.droplist.click()
        self.wherefrom.click()
        self.droplistsec.click()
        self.whereto.click()
    def choosedate(self):
        self.date.click()
        self.date.set_text("22102022")
    def submitb(self):
        self.submitbutton.click()

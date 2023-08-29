from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shopTab = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.XPATH, "//label[text()='Name']/following-sibling::input")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    dob = (By.CSS_SELECTOR, "input[type='date']")
    button = (By.ID, "inlineRadio2")
    submit = (By.XPATH, "//input[@value='Submit']")
    msg = (By.CSS_SELECTOR, "[class*='alert-success']")

    def getShopTab(self):
        return self.driver.find_element(*HomePage.shopTab)

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def getCheckbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def getDob(self):
        return self.driver.find_element(*HomePage.dob)

    def getButton(self):
        return self.driver.find_element(*HomePage.button)

    def getSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def getMsg(self):
        return self.driver.find_element(*HomePage.msg)

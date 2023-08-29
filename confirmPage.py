from selenium.webdriver.common.by import By


class confirmPage:
    def __init__(self, driver):
        self.driver = driver

    country = (By.ID, "country")
    countryValue = (By.LINK_TEXT, "India")
    checkboxes = (By.XPATH, "//div[contains(@class,'checkbox-primary')]")
    purchase = (By.XPATH, "//input[@value='Purchase']")
    successMsg = (By.CSS_SELECTOR, "div[class*='alert-dismissible']")

    def getCountry(self):
        return self.driver.find_element(*confirmPage.country)

    def getCountryValue(self):
        return self.driver.find_element(*confirmPage.countryValue)

    def getCheckBoxes(self):
        return self.driver.find_element(*confirmPage.checkboxes)

    def getPurchase(self):
        return self.driver.find_element(*confirmPage.purchase)

    def getSuccessMsg(self):
        return self.driver.find_element(*confirmPage.successMsg)



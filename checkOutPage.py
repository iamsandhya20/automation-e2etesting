from selenium.webdriver.common.by import By


class checkOutPage:
    def __init__(self, driver):
        self.driver = driver

    checkOut = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    checkOutItems = (By.XPATH, "//h4[@class='card-title']/a")
    addToCart = (By.XPATH, "//div[@class='card-footer']/button")
    checkout2 = (By.CSS_SELECTOR, "button[class*='btn-success']")

    def getCheckOut(self):
        return self.driver.find_element(*checkOutPage.checkOut)

    def getCheckOutItem(self):
        return self.driver.find_elements(*checkOutPage.checkOutItems)

    def AddToCart(self):
        return self.driver.find_elements(*checkOutPage.addToCart)

    def getFinalCheckOut(self):
        return self.driver.find_element(*checkOutPage.checkout2)
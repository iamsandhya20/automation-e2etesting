import logging
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.HomePage import HomePage
from pageObjects.checkOutPage import checkOutPage
from pageObjects.confirmPage import confirmPage


@pytest.mark.usefixtures("setup")
class TestOne:

    def test_e2e(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        log.info("I am in Home Page")
        homePage.getName().send_keys("Sandhya")
        homePage.getEmail().send_keys("sandhya@gmail.com")
        homePage.getPassword().send_keys("sandhya@20")
        homePage.getCheckbox().click()
        drop = Select(homePage.getGender())
        drop.select_by_index(1)
        homePage.getDob().send_keys("26-06-2000")
        homePage.getButton().click()
        homePage.getSubmit().click()
        time.sleep(3)
        message = homePage.getMsg().text
        print(message)
        log.info("Submitted the form")
        log.debug("Debug")

        homePage.getShopTab().click()
        checkoutpage = checkOutPage(self.driver)
        log.info("Getting all the card titles")
        names = checkoutpage.getCheckOutItem()
        i = -1
        for name in names:
            i = i + 1
            cardtext = name.text
            if cardtext == 'Blackberry':
                checkoutpage.AddToCart()[i].click()
                checkoutpage.getCheckOut().click()
                checkoutpage.getFinalCheckOut().click()

        confirmpage = confirmPage(self.driver)
        confirmpage.getCountry().send_keys("ind")
        self.verifyPresenceOfElement("India")
        confirmpage.getCountryValue().click()
        confirmpage.getCheckBoxes().click()
        confirmpage.getPurchase().click()
        msg = confirmpage.getSuccessMsg().text
        assert ("Success" in msg)

    def verifyPresenceOfElement(self, text):
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def getLogger(self):
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logFile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger


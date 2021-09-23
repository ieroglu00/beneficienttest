import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import pytest
from selenium import webdriver
import allure

@allure.step("Entering username ")
def enter_username(username):
  driver.find_element_by_id("un").send_keys(username)

@allure.step("Entering password ")
def enter_password(password):
  driver.find_element_by_id("pw").send_keys(password)

@pytest.fixture()
def test_setup():
  global driver
  global TestName
  global description
  global TestResult
  global TestResultStatus
  global TestDirectoryName
  TestName = "test_CurrenciesSoSFunds"
  description = "This is regression test case to verify lsit of currencies at Sign Off Summary – Funds page inside Quarterly NAV Close module"
  TestResult = []
  TestResultStatus = []
  TestDirectoryName = "CompareAmountSOSandMissionControl"

  driver=webdriver.Chrome(executable_path="C:/BIDS/beneficienttest/Beneficient/Chrome/chromedriver.exe")
  driver.implicitly_wait(10)
  driver.maximize_window()
  driver.get("https://beneficienttest.appiancloud.com/suite/")
  enter_username("neeraj.kumar")
  enter_password("Crochet@786")
  driver.find_element_by_xpath("//input[@type='submit']").click()

  yield
  driver.quit()

@pytest.mark.regression
@allure.description("Test case to verify number of currencies in SoS Beneficient")
@allure.severity(severity_level="High")
def test_CurrencyListSoSFunds(test_setup):
    driver.find_element_by_xpath("//*[@title='Quarterly NAV Close']").click()
    time.sleep(5)
    PageTitle5 = driver.title
    #print(PageTitle5)
    ExpectedPageTitle = "Quarterly NAV Close - BIDS"
    if PageTitle5==ExpectedPageTitle :
        print("Quaterly NAV Close Page opened")
        time.sleep(5)
        driver.find_element_by_xpath("//*[text()='Sign-Off Summary: Beneficient']").click()
        time.sleep(7)
        PageTitle6 = driver.title
        ExpectedPageTitle = "User Input Task - BIDS"
        if PageTitle6 == ExpectedPageTitle:
            print("SoS Beneficient Page opened")
            time.sleep(5)

            driver.find_element_by_xpath("//div[contains(text(),'Select Currency')]").click()
            try:
             driver.find_element_by_xpath("//div[contains(text(),'Select Currencys')]").click()
            except NoSuchElementException:
             allure.attach(driver.get_screenshot_as_png(), name="Image1", attachment_type=allure.attachment_type.PNG)

        else:
            try:
             driver.find_element_by_xpath("//div[contains(text(),'Select Currencys')]").click()
            except NoSuchElementException:
             print("Exception found as SoS Beneficient Page not found")
             allure.attach(driver.get_screenshot_as_png(), name="Image1", attachment_type=allure.attachment_type.PNG)
             print(driver.title)
             pytest.fail("Failed to load SoS Beneficient Page")
    else:
        try:
         driver.find_element_by_xpath("//div[contains(text(),'Select Currencys')]").click()
        except NoSuchElementException:
         print("Exception found as Quaterly NAV Close Page not found")
         allure.attach(driver.get_screenshot_as_png(), name="Image1", attachment_type=allure.attachment_type.PNG)
         pytest.fail("Failed to load Quaterly NAV Close Page")

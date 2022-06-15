from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class usando_unnittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_estudio(self):
        driver=self.driver
        #1
        driver.get("https://rahulshettyacademy.com/AutomationPractice/")
        #2
        driver.find_element_by_css_selector("input[value='radio2']").click()
        time.sleep(3)
        driver.find_element_by_css_selector("input[value='radio3']").click()
        time.sleep(3)
        driver.find_element_by_css_selector("input[value='radio1']").click()
        time.sleep(3)
        #3
        suggestion = driver.find_element_by_xpath("//input[@id='autocomplete']")
        suggestion.send_keys("Me")
        time.sleep(3)
        for i in driver.find_elements_by_xpath('//div[contains(text(), "Mexico")]'):
             if i.text == 'Mexico':
                assert i.text=='Mexico'
                i.click()
             break
         #4   
        driver.find_element_by_xpath("//select[@id='dropdown-class-example']").click()
        time.sleep(3)
        
        drop = driver.find_element_by_xpath('//*[@id="dropdown-class-example"]').click()
        time.sleep(3)  
        driver.find_element_by_xpath('//*[@id="dropdown-class-example"]/option[3]').click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="dropdown-class-example"]/option[4]').click()
        time.sleep(3)

        #5
        driver.find_element_by_css_selector("#checkBoxOption1").click()
        time.sleep(3)
        driver.find_element_by_css_selector("#checkBoxOption2").click()
        time.sleep(3)

        #6
        swiAlert = driver.find_element_by_xpath("//input[@id='name']")
        swiAlert.send_keys("Stori Card")
        time.sleep(3)
        alertBtn = driver.find_element_by_css_selector("#alertbtn")
        alertBtn.click()

        alert = driver.switch_to.alert
        
        print(alert.text)
        time.sleep(3)
        alert.accept()
        time.sleep(3)

        #7
        element =driver.find_element_by_xpath("//input[@id='displayed-text']")
        
        if (element.is_displayed):
            print("ELEMENT IS DISPLAYED")
        elif():
            print("ELEMENT IS NO DISPLAYED")
        time.sleep(3)

            
        
if __name__ == '__main__':
  unittest.main()

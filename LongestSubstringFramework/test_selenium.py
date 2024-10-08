import unittest
import time
from selenium.webdriver.common.by import By
from longest_substring_finder import LongestSubstringFinder


def test_selenium_search(driver):
    input_string = "abcabcbb"

    driver.get("https://www.zomato.com/")
    time.sleep(5)

    search_box = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[2]/div/div[3]/input')
    search_box.send_keys(input_string)
    time.sleep(5)

    longestSubstringFinder = LongestSubstringFinder(input_string)
    result = longestSubstringFinder.find_longest_substring()

    print(f"The length of the longest substring without repeating characters is: {result}")

    unittest.TestCase().assertTrue(result == 3, f"Expected 3 but got {result}")
    print(f"Test passed: Length of longest substring is {result}.")




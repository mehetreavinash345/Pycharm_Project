from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from LongestSubString import LongestSubstringFinder


def selenium_test_case(longestSubString):

    driver_path = "C:/Users/Hp/chromedriver-win64/chromedriver.exe"

    service = Service(driver_path)
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.zomato.com/")

    search_box = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/div[2]/div[2]/div/div[3]/input')
    time.sleep(5)

    search_box.send_keys(longestSubString)
    time.sleep(5)

    longestSubstringFinder = LongestSubstringFinder(longestSubString)

    result = longestSubstringFinder.find_longest_substring()

    print(f"The length of the longest substring without repeating characters is: {result}")

    time.sleep(10)

    driver.quit()

    return result

if __name__ == "__main__":

    input_string = "abcabcbb"

    res=selenium_test_case(input_string)

    print(res)

    assert res == 3

    print("The test got successful: Length of longest substring is 3.")

    assert res == 4

    print("The test got failed: Length of longest substring is expected 3.")


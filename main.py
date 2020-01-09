from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

def fill_edom(score, username, password):
    driver = webdriver.Chrome()
    # Login to SIAKNG
    driver.get("https://academic.ui.ac.id/main/Academic/HistoryByTerm")
    elem = driver.find_element_by_id("u")
    elem.send_keys(username)
    elem = driver.find_element_by_name("p")
    elem.send_keys(password)
    elem.send_keys(Keys.RETURN)

    driver.get("https://academic.ui.ac.id/main/Academic/HistoryByTerm")

    while True:
        try:
            elem = driver.find_element_by_link_text("Isi EDOM")
            
            # EDOM page
            edom_link = elem.find_element_by_xpath("..")
            edom_link.click()

            # Filling edom with score
            score_format = "//input[@value='{}']".format(score)
            for choice in driver.find_elements_by_xpath(score_format):
                choice.click()
            driver.find_element_by_class_name("button").click()
        except:
            break
        

    driver.close()

if __name__ == "__main__":
    if len(sys.argv) - 1 > 0 :
        default_score = sys.argv[1]
        username = sys.argv[2]
        password = sys.argv[3]
        # Exec
        fill_edom(default_score, username, password)
    else:
        print("Usage: python main.py {{default_score}} {{username}} {{password}}")

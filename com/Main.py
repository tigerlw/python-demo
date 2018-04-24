from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Dbeauty&field-keywords=hair+wax")

webdriver.PhantomJS

#elem = driver.find_element_by_name("wd")

#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)

#elemTr=driver.find_element_by_xpath("/html/body/div[@id='wrapper']/div[@id='ftCon']/div[@class='ftCon-Wrapper']/div[@id='ftConw']/p[@id='lh']/a[@id='setf']")

#print  elemTr.text
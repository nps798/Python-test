from selenium import webdriver

driver.get("http://140.116.165.74/qry/qry001.php?dept_no=")
element = driver.find_element_by_xpath("/html/body/table/tbody/tr[1]")
print(element.text)
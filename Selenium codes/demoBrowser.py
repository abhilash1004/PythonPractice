from selenium import webdriver

#driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
#driver.get("https://www.apple.com")
#print(driver.title,"\n")
#print (driver.current_url)
#driver.maximize_window()
#driver.get("https://www.apple.com/mac/")
#river.get("https://rahulshettyacademy.com/ ")
#driver.close()
try:
    driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/ ")
    #driver.quit()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.find_element_by_name("name").send_keys("Perla ")
    driver.find_element_by_name("email").send_keys("xxx.@gmail.com")
    driver.find_element_by_id("exampleCheck1").click()
    #driver.find_element_by_id("exampleCheck1").click()
    driver.find_element_by_css_selector("input[name='name']").send_keys("abhilash")
    driver.find_element_by_css_selector("#exampleInputPassword1").send_keys("two")
    #driver.maximize_window()
    driver.find_element_by_xpath("//input[@type='submit']").click()
    #driver.find_element_by_id("exampleInptPasswoed1").send_keys("1234")
    #driver.refresh()
    #driver.back()
    #driver.minimize_window()
    #print(driver.find_element_by_class_name("alert").text)
    print(driver.find_element_by_css_selector("div[class *= 'alert-success']").text)
    print(driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissible']").text)

except Exception as e:
    print(e)
finally:
    #driver.quit()
    print("I dont want close")

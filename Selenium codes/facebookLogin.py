from selenium import webdriver

#try:
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
x="https://www.facebook.com/"
driver.get("https://www.facebook.com/")
email = input("Enter Email Id")
password = input("Enter Password")
driver.find_element_by_css_selector("#email").send_keys(email)
driver.find_element_by_css_selector("#pass").send_keys(password)
driver.find_element_by_css_selector("#u_0_b").click()
driver.maximize_window()
y=driver.current_url
print(y)
#driver.get("https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110")
#y = "https://www.facebook.com/"
if x != y:
    print("Wrong Username or Password")
else:
    print("Enjoy facebook")
#except Exception as e:
    #print(e)

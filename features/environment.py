from selenium import webdriver 
 
 
def before_all(context): 
  context.browser = webdriver.Chrome() 
  context.browser.implicitly_wait(1) 
 
def after_all(context): 
  if not context.failed: 
    context.browser.quit() 
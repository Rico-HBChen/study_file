from selenium import webdriver
browser=webdriver.Chrome ()
browser.get('http://inventwithpython.com')
try:
    elem=browser.find_element_by_class_name('card-img-top cover-thumb')
    print('Found<%s>element with that class name!'%(elem.tag_name))
except:
    print('was not able to find an element with that name.')

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_busket_button(browser):
    browser.get(link)
    
    browser.implicitly_wait(10)
    
    button = browser.find_element_by_css_selector("button.btn-add-to-basket")
    
    assert button, "Корзина не найдена "
   
    import requests
    from bs4 import beautifulsoup
    from selenium import webdriver
    from selenium.webdriver.chrome.options import options
    from selenium.webdriver.common.keys import keys
    from selenium.webdriver.common.by import by
    from time import sleep
  
    def isSolout(element):
        cname = element.get_attribute('class')
        if 'soldout' in cname:
            return True
        else:
            return False

    chrome_driver = webdriver.Chrome()
    chrome_driver.get('https://hoangcau.com/products/honda-beat')
    
    name = chrome_driver.find_element(By.TAG_NAME, 'h1').text
    status = chrome_driver.find_element(By.CLASS_NAME,'pro-stock').find_elements(By.TAG_NAME,'span')[-1].text
    brand = chrome_driver.find_element(By.CLASS_NAME,'pro-brand').find_element(By.TAG_NAME,'a').text
    lstColorEle = chrome_driver.find_element(By.CLASS_NAME, "select-swap").find_elements(By.TAG_NAME,'div')
    lst = chrome_driver.find_element(By.ID, 'product-select-watch').find_elements(By.CLASS_NAME, 'swatch')
    for colorEle in lstColorEle:
        color = colorEle.find_element(By.TAG_NAME, 'label').text
        if isSolout(colorEle) == colorEle.click()
            return False            
            print('co:', color)
        else:
            print('khong', color)

    len(lst)

    class HoangCau:
      def __init__(self):
        self.lstUrlProduct = []
        self.chrome_driver = webdriver.Chrome()
      def getAllUrlProduct(self)
        oriUrl = 'https://hoangcau.com/collections/all?page='
        for i in range(1,6):
          urlPage = oriUrl + str(i)
          page = requests.get(urlPage)
          soup = BeautifulSoup(page.text, 'html.parser')
          for div_product in soup.find_all( class_ = 'product-item'):    
            urlProduct = div_product.a['href']    
            self.lstUrlProduct.append(urlProduct)
    
      def getInforProducts(self):\n",
         assert len(self.lstUrlProduct) == 0, 'list url product empty'
        infoAllProduct = []
        for urlProduct in self.lstUrlProduct:
            lstStocking = []
            lstOutStock = []        
            self.chrome_driver.get(\"https://hoangcau.com\" + urlProduct)
            name = self.chrome_driver.find_element(By.TAG_NAME, 'h1').text
            brand = self.chrome_driver.find_element(By.CLASS_NAME,'pro-brand').find_element(By.TAG_NAME,'a').text,
            typeProduct = self.chrome_driver.find_element(By.CLASS_NAME,'pro-type').find_element(By.TAG_NAME,'a').text
            status = self.chrome_driver.find_element(By.CLASS_NAME,'pro-stock').find_elements(By.TAG_NAME,'span')[-1].text
            if len(self.chrome_driver.find_element(By.ID, 'product-select-watch').find_elements(By.CLASS_NAME,'swatch')) == 1:
                print('A')
                lstColorEle = self.chrome_driver.find_element(By.CLASS_NAME, \"select-swap"\).find_elements(By.TAG_NAME,'div')
                for colorEle in lstColorEle:
                    color = colorEle.find_element(By.TAG_NAME, 'label').text
    
                    if self.isSolout(colorEle) == False
                        colorEle.click()
                        price = self.chrome_driver.find_element(By.CLASS_NAME,'pro-price').find_element(By.TAG_NAME,'span').text
                        proStock = 'none' + '@' + color + '@' + price
                        lstStocking.append(proStock)
                    else:
                        proOutStock = 'none' + '@' + color  +\"@\"+ \"none\
                        lstOutStock.append(proOutStock)\n
                infoAllProduct.append([\"https://hoangcau.com"\ + urlProduct,name, brand, typeProduct, status, lstStocking, lstOutStock])
            else:
                print(\"B"\)
                buttonsVersion = self.chrome_driver.find_element(By.CLASS_NAME, \"select-swap"\).find_elements(By.TAG_NAME,'div')
                for button in buttonsVersion
                    version = button.find_element(By.TAG_NAME,'label').text
                    if self.isSolout(button) == False
                        button.click()
                        lstColorEle = self.chrome_driver.find_elements(By.CLASS_NAME, \"select-swap"\)[-1].find_elements(By.TAG_NAME,'div')
                        for colorEle in lstColorEle:
                            color = colorEle.find_element(By.TAG_NAME,'label').text
                            if self.isSolout(colorEle) == False
                                colorEle.click()
                                price = self.chrome_driver.find_element(By.CLASS_NAME,'pro-price').find_element(By.TAG_NAME,'span').text
                                proStock = version + '@'+ color + '@' + price
                                lstStocking.append(proStock)
                            else:
                                proOutStock = version + '@' + color  +\"@"\+ \"none"\
                                lstOutStock.append(proOutStock)
                    else:
                        proOutStock = version + '@' + 'none'+ \"@"\+ \"none"\
                        lstOutStock.append(proOutStock)
                infoAllProduct.append([\"https://hoangcau.com"\ + urlProduct,name, brand, typeProduct, status, lstStocking, lstOutStock])
            sleep(1)
        return infoAllProduct
    
      def isSolout(self, element):
        cname = element.get_attribute('class')
        if 'soldout' in cname:
            return True
        else:
            return False

    hoangcau = HoangCau()

    hoangcau.getAllUrlProduct()

    len (hoangcau.lstUrlProduct)

    inforAllProduct = hoangcau.getInforProducts()

    lstProduct

    import pandas as pd\n",
    df = pd.DataFrame (lstProduct, \n",
                       columns = ['url', 'Tên sản phẩm', 'Hãng', \"Loại xe"\, 'Tình trạng', 'Phiên bản', 'Màu', 'Giá'])
   

    df.iloc[184]

    df.to_csv('data_hoangcau.xlsx')


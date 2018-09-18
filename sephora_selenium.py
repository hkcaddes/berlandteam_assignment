from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re

# specify path to chrome driver
driver = webdriver.Chrome(r'C:\Users\hkcad\chromedriver.exe')

# go to webpage for all bestselling skincare products
driver.get("https://www.sephora.com/best-selling-skin-care/?products=all")

# create csv file and write

#csv_file2 = open('ingredients.csv', 'w', encoding='utf-8')
#writer2 = csv.writer(csv_file2)


time.sleep(1)

with open('products1.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    try:
        SCROLL_PAUSE_TIME = 2

        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")
        i = 1
        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            print("Scroll number: " + str(i))
            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            i += 1

        print("Finished Scrolling")

        wait_product = WebDriverWait(driver, 10)  # wait to make sure all products loaded
        Products = wait_product.until(EC.presence_of_all_elements_located((By.XPATH, './/div[@id="main"]/div[1]/div[2]/a')))

        product_urls = []
        product_ids = []
        # get info about every product
        for product in Products:
            product_dict = {}

            brand = product.find_element_by_xpath('.//div[@class="SkuItem-name"]/div[1]').text
            item = product.find_element_by_xpath('.//div[@class="SkuItem-name"]/div[2]').text
            try:
                price = product.find_element_by_xpath('.//div[@class="u-fwb ng-scope"]/span').text
            except:
                price = 'NA'
            try:
                stars = product.find_element_by_xpath('.//div[@class="u-db u-mxa u-mt2 u-mb2 StarRating u-relative u-oh ng-scope"]').get_attribute("seph-stars")
            except:
                stars =  product.find_element_by_xpath('.//div[@class="u-db u-mxa u-mt2 u-mb2 StarRating u-relative u-oh"]').get_attribute("seph-stars")
            try:
                url = product.get_attribute("href")
            except:
                pass
            product_id = str(url).split(':')[2]

            # save list of product urls and ids (to use for reviews api)
            product_urls.append(url)
            product_ids.append(product_id)

            # save to temporary dictionary
            product_dict['Brand'] =brand
            product_dict['Item'] = item
            product_dict['ProductId'] = product_id
            product_dict['Price'] = price
            product_dict['OverallStars'] = stars

            writer.writerow(product_dict.values())
            print(item)



        # try:
        #     for index, product in enumerate(product_urls):
        #         info_dict = {}
        #         # now get individual product info
        #         driver.get(product)
        #         time.sleep(3)
        #
        #         try:
        #             button = driver.find_element_by_xpath('//a[@class="acsCloseButton acsAbandonButton "]')
        #             button.click()
        #             print('popup closed')
        #         except:
        #             pass
        #         print("continue")
        #         # product loves
        #         try:
        #             loves = driver.find_element_by_xpath('.//span[@data-at="product_love_count"]').text
        #             loves = re.sub('K', '000', loves)
        #         except:
        #             loves = 'NA'
        #
        #         info_dict['ProductId'] = product_ids[index]
        #         info_dict['Loves'] = loves
        #         #details = driver.find_element_by_xpath('.//div[@class="css-1kianer"]/div[1]/div[1]').text
        #         # get "solutions for"
        #
        #         try:
        #             # Locate the next button element on the page and then call `button.click()` to click it.
        #             button = driver.find_element_by_xpath('.//div[@data-comp="Info"]/button[3]')
        #             button.click()
        #
        #             ingredients = driver.find_element_by_xpath('.//div[@class="css-1kianer"]/div[3]/div[1]').text
        #             ingredients = re.sub(":.*\n", "\n", ingredients)
        #             #ingredients = re.split(",|[\n]+", ingredients)
        #             ingredients = re.split("[,\n]+", ingredients)
        #             # create list of ingredients
        #             for i in range(len(ingredients)):
        #                 ingredients[i] = re.sub("^[-]|[.]$", "", ingredients[i]).strip()
        #
        #             # parse out important/non-trivial ingredients
        #             greds = []
        #             for i in ingredients:
        #                 if re.search('water', i, re.IGNORECASE) or re.search('glyce', i, re.IGNORECASE) or re.fullmatch('Glycol', i):
        #                     continue
        #                 if ingredients.index(i) < 5:
        #                         greds.append(i.split(':')[0])
        #                         continue
        #                 elif re.search('Complex|Extract|Oil|Leaf|Citrus|Seed|Hyaluron|Silk|Ceram|Coco|Fruit|Rose|Rosa|Oxide|Dioxide|Carbon|Magnesium|Acid|Benz|Ferment', i):
        #                     if re.search('\(.*\)', i):
        #                         m = re.search('\(.*\)', i).group(0)
        #                         m = re.sub('[\(\)]', '', m)
        #                         greds.append(str(m + ' ' + i.split()[-1]))
        #                     else:
        #                         greds.append(i)
        #
        #             if len(greds)< 10:
        #                 length = len(greds)
        #                 for i in range (0, 10-length):
        #                     greds.append('NA')
        #             print(greds)
        #         except:
        #             greds = ['NA' for i in range(0, 10)]
        #             print(greds)
        #
        #         # get number of reviews, number of loves
        #
        #
        #         # append values to dictionary
        #         info_dict['Ingredients'] = greds
        #         info_dict['Ingredient_1'] = greds[0]#.encode('utf-8')
        #         info_dict['Ingredient_2'] = greds[1]#.encode('utf-8')
        #         info_dict['Ingredient_3'] = greds[2]#.encode('utf-8')
        #         info_dict['Ingredient_4'] = greds[3]#.encode('utf-8')
        #         info_dict['Ingredient_5'] = greds[4]#.encode('utf-8')
        #         info_dict['Ingredient_6'] = greds[5]#.encode('utf-8')
        #         info_dict['Ingredient_7'] = greds[6]#.encode('utf-8')
        #         info_dict['Ingredient_8'] = greds[7]#.encode('utf-8')
        #         info_dict['Ingredient_9'] = greds[8]#.encode('utf-8')
        #         info_dict['Ingredient_10'] = greds[9]#.encode('utf-8')
        #         writer2.writerow(info_dict.values())
        #
        # except Exception as e:
        #     print(e)
        #     pass
        #





        #driver.close()

    except Exception as e:
        print(e)
        #driver.close()
        #break

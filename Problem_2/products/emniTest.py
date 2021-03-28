import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}


url = "https://www.amazon.in/Renewed-Razer-RZ04-02051000-R3M1-Spatial-Gaming/dp/B07W55PNL4/ref=sr_1_8?_encoding=UTF8&browseLadder=20690678031%2C12497409031%2C20348653031%2C11474197031%2C11474195031%2C1372805031&browseLadderData=%5B%7B%26quot%3BstoreContextName%26quot%3B%3A%26quot%3BLike+new+products+by+Amazon+Renewed%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B20690678031%26quot%3B%7D%2C%7B%26quot%3BstoreContextName%26quot%3B%3A%26quot%3BAmazon+Renewed%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B12497409031%26quot%3B%7D%2C%7B%26quot%3Bid%26quot%3B%3A%26quot%3B20348653031%26quot%3B%2C%26quot%3BsuppressLink%26quot%3B%3A%26quot%3B1%26quot%3B%7D%2C%7B%26quot%3Bid%26quot%3B%3A%26quot%3B11474197031%26quot%3B%2C%26quot%3BsuppressLink%26quot%3B%3A%26quot%3B1%26quot%3B%7D%2C%7B%26quot%3Bhidden%26quot%3B%3A%26quot%3B1%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B11474195031%26quot%3B%2C%26quot%3BsuppressLink%26quot%3B%3A%26quot%3B1%26quot%3B%7D%2C%7B%26quot%3Bhidden%26quot%3B%3A%26quot%3B1%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B1372805031%26quot%3B%2C%26quot%3BcontextFreeName%26quot%3B%3A%26quot%3BCross%26quot%3B%7D%5D&dchild=1&deviceOS=Windows&displayStyle=2-column&handlerName=BrowsePage&pageId=20690678031&pageType=Browse&pd_rd_r=0a627d8a-ed1a-4e19-8e6c-b7e6ef35f558&pd_rd_w=S3aRz&pd_rd_wg=H6BnZ&qid=1616946855&searchAlias=specialty-aps&softwareClass=Web+Browser&specialtyStoreType=cross-site&sr=8-8&storeContextName=Like+new+products+by+Amazon+Renewed"
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, "html.parser")
try:
    price = float(soup.find(id="priceblock_ourprice").get_text().replace(
        '₹', '').replace('ε', '').replace(',', '').strip()) * 100.0
except:
    price = 0.0
image_src = soup.find(id="landingImage")['src'].strip()

product = {
    'price': price,
    'image_src': image_src
}
products = []
products.append(product)
print(products)

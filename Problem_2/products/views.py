from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests


def index(request):

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    urls = ["https://www.amazon.in/Noise-Colorfit-Pro-Touch-Control/dp/B07YY1BY5B/ref=psdc_5605728031_t2_B08KDSRYDV",
            "https://www.amazon.in/Renewed-Texas-Instruments-Scientific-Calculator/dp/B07QX2NRSX/ref=sr_1_3?_encoding=UTF8&browseLadder=20690678031%2C12497409031%2C20348653031%2C11474197031%2C11474195031%2C1372805031&browseLadderData=%5B%7B%26quot%3BstoreContextName%26quot%3B%3A%26quot%3BLike+new+products+by+Amazon+Renewed%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B20690678031%26quot%3B%7D%2C%7B%26quot%3BstoreContextName%26quot%3B%3A%26quot%3BAmazon+Renewed%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B12497409031%26quot%3B%7D%2C%7B%26quot%3Bid%26quot%3B%3A%26quot%3B20348653031%26quot%3B%2C%26quot%3BsuppressLink%26quot%3B%3A%26quot%3B1%26quot%3B%7D%2C%7B%26quot%3Bid%26quot%3B%3A%26quot%3B11474197031%26quot%3B%2C%26quot%3BsuppressLink%26quot%3B%3A%26quot%3B1%26quot%3B%7D%2C%7B%26quot%3Bhidden%26quot%3B%3A%26quot%3B1%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B11474195031%26quot%3B%2C%26quot%3BsuppressLink%26quot%3B%3A%26quot%3B1%26quot%3B%7D%2C%7B%26quot%3Bhidden%26quot%3B%3A%26quot%3B1%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B1372805031%26quot%3B%2C%26quot%3BcontextFreeName%26quot%3B%3A%26quot%3BCross%26quot%3B%7D%5D&dchild=1&deviceOS=Windows&displayStyle=2-column&handlerName=BrowsePage&pageId=20690678031&pageType=Browse&pd_rd_r=0a627d8a-ed1a-4e19-8e6c-b7e6ef35f558&pd_rd_w=S3aRz&pd_rd_wg=H6BnZ&qid=1616946855&searchAlias=specialty-aps&softwareClass=Web+Browser&specialtyStoreType=cross-site&sr=8-3&storeContextName=Like+new+products+by+Amazon+Renewed",
            "https://www.amazon.in/Renewed-Razer-RZ04-02051000-R3M1-Spatial-Gaming/dp/B07W55PNL4/ref=sr_1_8?_encoding=UTF8&browseLadder=20690678031%2C12497409031%2C20348653031%2C11474197031%2C11474195031%2C1372805031&browseLadderData=%5B%7B%26quot%3BstoreContextName%26quot%3B%3A%26quot%3BLike+new+products+by+Amazon+Renewed%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B20690678031%26quot%3B%7D%2C%7B%26quot%3BstoreContextName%26quot%3B%3A%26quot%3BAmazon+Renewed%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B12497409031%26quot%3B%7D%2C%7B%26quot%3Bid%26quot%3B%3A%26quot%3B20348653031%26quot%3B%2C%26quot%3BsuppressLink%26quot%3B%3A%26quot%3B1%26quot%3B%7D%2C%7B%26quot%3Bid%26quot%3B%3A%26quot%3B11474197031%26quot%3B%2C%26quot%3BsuppressLink%26quot%3B%3A%26quot%3B1%26quot%3B%7D%2C%7B%26quot%3Bhidden%26quot%3B%3A%26quot%3B1%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B11474195031%26quot%3B%2C%26quot%3BsuppressLink%26quot%3B%3A%26quot%3B1%26quot%3B%7D%2C%7B%26quot%3Bhidden%26quot%3B%3A%26quot%3B1%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B1372805031%26quot%3B%2C%26quot%3BcontextFreeName%26quot%3B%3A%26quot%3BCross%26quot%3B%7D%5D&dchild=1&deviceOS=Windows&displayStyle=2-column&handlerName=BrowsePage&pageId=20690678031&pageType=Browse&pd_rd_r=0a627d8a-ed1a-4e19-8e6c-b7e6ef35f558&pd_rd_w=S3aRz&pd_rd_wg=H6BnZ&qid=1616946855&searchAlias=specialty-aps&softwareClass=Web+Browser&specialtyStoreType=cross-site&sr=8-8&storeContextName=Like+new+products+by+Amazon+Renewed",
            "https://www.amazon.in/Lava-Rose-Pink-32GB-Storage/dp/B08R79M3KN/ref=br_msw_pdt-3?_encoding=UTF8&smid=A14CZOWI0VEHLG&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=FB8Y3P1B7Y3K6K66T7BC&pf_rd_t=36701&pf_rd_p=5c669f94-aee5-4b22-81f8-1d301ca2c6a3&pf_rd_i=desktop",
            "https://www.amazon.in/Renewed-LG-Ultragear-Compatible-Monitor/dp/B0842V877R/ref=sr_1_30?_encoding=UTF8&browseLadder=20690678031%2C12497409031%2C20348653031%2C11474197031%2C11474195031%2C1372805031&browseLadderData=%5B%7B%26quot%3BstoreContextName%26quot%3B%3A%26quot%3BLike+new+products+by+Amazon+Renewed%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B20690678031%26quot%3B%7D%2C%7B%26quot%3BstoreContextName%26quot%3B%3A%26quot%3BAmazon+Renewed%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B12497409031%26quot%3B%7D%2C%7B%26quot%3Bid%26quot%3B%3A%26quot%3B20348653031%26quot%3B%2C%26quot%3BsuppressLink%26quot%3B%3A%26quot%3B1%26quot%3B%7D%2C%7B%26quot%3Bid%26quot%3B%3A%26quot%3B11474197031%26quot%3B%2C%26quot%3BsuppressLink%26quot%3B%3A%26quot%3B1%26quot%3B%7D%2C%7B%26quot%3Bhidden%26quot%3B%3A%26quot%3B1%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B11474195031%26quot%3B%2C%26quot%3BsuppressLink%26quot%3B%3A%26quot%3B1%26quot%3B%7D%2C%7B%26quot%3Bhidden%26quot%3B%3A%26quot%3B1%26quot%3B%2C%26quot%3Bid%26quot%3B%3A%26quot%3B1372805031%26quot%3B%2C%26quot%3BcontextFreeName%26quot%3B%3A%26quot%3BCross%26quot%3B%7D%5D&dchild=1&deviceOS=Windows&displayStyle=2-column&handlerName=BrowsePage&pageId=20690678031&pageType=Browse&pd_rd_r=0a627d8a-ed1a-4e19-8e6c-b7e6ef35f558&pd_rd_w=S3aRz&pd_rd_wg=H6BnZ&qid=1616946855&searchAlias=specialty-aps&softwareClass=Web+Browser&specialtyStoreType=cross-site&sr=8-30&storeContextName=Like+new+products+by+Amazon+Renewed",
            "https://www.amazon.in/dp/B019O8YZ4A/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B019O8YZ4A&pd_rd_w=kDeEP&pf_rd_p=b9175453-ca9b-41ce-82bc-58f20ea9bb05&pd_rd_wg=snjB5&pf_rd_r=FE05AAEDZVHNXJTM9RHZ&pd_rd_r=33674fb7-c95d-4089-b20c-ab9f16038b24&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNEtZTEZYWFBUMlJUJmVuY3J5cHRlZElkPUEwMDQwNzE3MzFSVUg2WjlJVVVQRCZlbmNyeXB0ZWRBZElkPUEwMTAyODE2MUpVMTBNWjkyMktJVyZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
            "https://www.amazon.in/Ant-Esports-VS500L-Power-Supply/dp/B08D6HKTH3/ref=pd_rhf_gw_s_pd_crcd_3?pd_rd_w=ZnnP0&pf_rd_p=0399dd58-3942-43f3-ba55-f3a880e8e961&pf_rd_r=XGBEGAD4K9ZKZNVAN14K&pd_rd_r=72a0901a-38a4-4c1e-924d-82d058c1c0f0&pd_rd_wg=urCF9&pd_rd_i=B08D6HKTH3&psc=1",
            "https://www.amazon.in/dp/B00E4NNCZO/ref=sspa_dk_detail_2?psc=1&pd_rd_i=B00E4NNCZO&pd_rd_w=TeeiM&pf_rd_p=b9175453-ca9b-41ce-82bc-58f20ea9bb05&pd_rd_wg=bHjsb&pf_rd_r=QPVGDWZQ37GZCQTJWPNH&pd_rd_r=5b4e8768-3573-4990-9f56-78678e8e955f&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExUUg5TkoxN1pJUlpEJmVuY3J5cHRlZElkPUEwMzAzODMwWlQ5UVc0MEpaQU9PJmVuY3J5cHRlZEFkSWQ9QTA1MDc1NzgxOExNTkRaN00xTUpEJndpZGdldE5hbWU9c3BfZGV0YWlsJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
            "https://www.amazon.in/Bassbuds-Pro-Bluetooth-Headphones-Resistance/dp/B08S16DMFH/ref=sr_1_5?_encoding=UTF8&dchild=1&pf_rd_i=desktop&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=5c669f94-aee5-4b22-81f8-1d301ca2c6a3&pf_rd_r=8TZMCFYDXQVE1ZCPHRPR&pf_rd_t=36701&qid=1616946834&smid=A14CZOWI0VEHLG&sr=8-5",
            "https://www.amazon.in/Studio-Classic-Headphones-Bluetooth-Ergonomic/dp/B08HKYTFPT/ref=sr_1_4?_encoding=UTF8&dchild=1&pf_rd_i=desktop&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=5c669f94-aee5-4b22-81f8-1d301ca2c6a3&pf_rd_r=8TZMCFYDXQVE1ZCPHRPR&pf_rd_t=36701&qid=1616946834&smid=A14CZOWI0VEHLG&sr=8-4"
            ]
    products = []
    for url in urls:
        page = requests.get(url, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        title = soup.find(id="productTitle").get_text().strip()
        try:
            price = float(soup.find(id="priceblock_ourprice").get_text().replace(
                '₹', '').replace('ε', '').replace(',', '').strip())
        except:
            price = 0.0
        image_src = soup.find(id="landingImage")['src']
        product = {
            'url': url,
            'title': title,
            'price': price,
            'image_src': image_src
        }
        products.append(product)
    return render(request, 'index.html', {'products': products})

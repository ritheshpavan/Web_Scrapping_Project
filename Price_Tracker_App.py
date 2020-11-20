import requests
from bs4 import BeautifulSoup

# URL='https://www.amazon.in/Redmi-9A-2GB-32GB-Storage/dp/B08696XB4B/ref=lp_22426818031_1_1?s=electronics&ie=UTF8&qid=1605704139&sr=1-1'
# URL='https://www.amazon.in/dp/B08GT299NQ?pf_rd_m=A1VBAL9TL5WCBF&pf_rd_t=30901&pf_rd_i=1389401031&pf_rd_s=mobile-browse-hero-5&pf_rd_r=7NW0HXR5A6SSJW1PH0B5&pf_rd_p=8694610d-b0f1-44fc-9100-33b28e57a8e7&ref_=Oct_Arh_mobile-browse-hero-5_4b7525a3-ab7d-45fa-ba66-38e702af9b48'
# URL='https://www.amazon.in/OnePlus-Glacial-Green-128GB-Storage/dp/B078BNQ318/ref=sr_1_1_sspa?dchild=1&fst=as%3Aoff&pf_rd_i=mobile&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=fc138b2b-c2a6-4c7d-a9d0-c12592b2d90d&pf_rd_r=ZHCVM9RMS6QJ4613AT1G&pf_rd_s=merchandised-search-8&pf_rd_t=Gateway&qid=1605265856&refinements=p_89%3AOnePlus&rnid=1389432031&s=electronics&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNFJPRVY1MDVSWUFKJmVuY3J5cHRlZElkPUEwNTYxNTc4MUlZUDlSNEVINkU1NCZlbmNyeXB0ZWRBZElkPUEwNDMxNjkwMjE0WjMyOUxNQ0tSWSZ3aWRnZXROYW1lPXNwX2F0Zl9icm93c2UmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'
products_to_track=[
    {
        "prod_url":"https://www.amazon.in/Redmi-Note-Pro-Interstellar-Snapdragon/dp/B08696XB3V/ref="
                   "sr_1_1?dchild=1&qid=1605714083&refinements=p_36%3A1500000-2000000&rnid=1318502031&s=electronics&sr=1-1",
        "name":"Redmi Note 9 Pro","target_price":16000

    },
    {
        "prod_url":"https://www.amazon.in/Samsung-Galaxy-Prime-Ocean-Storage/dp/B085J3GN6M/ref="
                   "sr_1_2?dchild=1&qid=1605714083&refinements=p_36%3A1500000-2000000&rnid=1318502031&s=electronics&sr=1-2",
        "name":"Samsung Galaxy M31","target_price":18000

    },
    {
        "prod_url":"https://www.amazon.in/Samsung-Galaxy-Electric-Blue-128GB-Storage/dp/B085J1J32G/ref="
                   "sr_1_1?dchild=1&qid=1605708064&refinements=p_36%3A2400000-2500000&rnid=1318502031&s=electronics&sr=1-1",
              "name":"Samsung Galaxy M51","target_price":24000
    },
    {
        "prod_url":"https://www.amazon.in/Stream-Storage-Additional-Exchange-Offers/dp/B086KCCPB7/ref="
                   "sr_1_19?dchild=1&qid=1605714083&refinements=p_36%3A1500000-2000000&rnid=1318502031&s=electronics&sr=1-19",
        "name":"Oppo A52","target_price":16000
    },
    {
        "prod_url":"https://www.amazon.in/Redmi-K20-Flame-128GB-Storage/dp/B082FMMD3B/ref=sr_1_19?dchild="
                   "1&qid=1605708064&refinements=p_36%3A2400000-2500000&rnid=1318502031&s=electronics&sr=1-19",
        "name":"Redmi K20","target_price":25000
    }
]
def give_prod_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36 Edg/86.0.622.69"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    prod_price = soup.find(id="priceblock_dealprice")
    if (prod_price == None):
        prod_price = soup.find(id="priceblock_ourprice")

    return prod_price.getText()

result_file=open('my_result_file.txt','w')
try:
    for every_prod in products_to_track:
        prod_price_returned = give_prod_price(every_prod.get("prod_url"))
        print(prod_price_returned + " " + every_prod.get("name"))

        my_prod_price = prod_price_returned[2:]
        my_prod_price = my_prod_price.replace(',', '')
        my_prod_price = int(float(my_prod_price))
        print(my_prod_price)

        if my_prod_price < every_prod.get("target_price"):
            print("Available at your required price")
            result_file.write(
                every_prod.get("name") + '- \t' + 'Available at target price' + '\tCurrent price=' + str(my_prod_price)+'\n')
        else:
            print("still at current price")
finally:
    result_file.close()









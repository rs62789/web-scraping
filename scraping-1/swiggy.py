from requests_html import HTMLSession
session=HTMLSession()
url="https://www.swiggy.com/restaurants/cafe-basilico-off-carter-road-bandra-west-mumbai-611121"
r=session.get(url)
r.html.render(sleep=1,keep_page=True,scrolldown=1)
divs=r.html.find(".RestaurantOffer_header__3FBtQ")
codes=r.html.find(".RestaurantOffer_offerCodeWrapper__2Cr4F")
#print(divs)
print("Coupon Names:")
for item in range(len(divs)):
    div={
        "Coupon Number": item,
        "Coupon Name": divs[item].text
    }
    print(div)
print("Coupon Codes:")
for item in range(len(codes)):
    code={
        "Coupon Number": item,
        "Coupon Code":codes[item].text
    }
    print(code)

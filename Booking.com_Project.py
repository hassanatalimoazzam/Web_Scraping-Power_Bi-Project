#                            Web Scraping By Hassanat Ibn Moazzam
#                            Booking.com (Rooms & Apartment Scraping)
#                            Targeted City (Capital Of Pakistan) 

import requests 
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.booking.com/searchresults.html?ss=Islamabad&ssne=Islamabad&ssne_untouched=Islamabad&efdco=1&label=gog235jc-1DCAIotQFCAnBrSDNYA2i1AYgBAZgBMbgBF8gBDNgBA-gBAfgBAogCAagCA7gCutXsvgbAAgHSAiQ1MjI3NGM4Ni1kYTZlLTQ2MGYtODYyMi0zYjc0Y2I5NWFkYzTYAgTgAgE&sid=029098095d906d51c5070871114aa1e4&aid=356980&lang=en-us&sb=1&src_elem=sb&src=index&dest_id=-2762812&dest_type=city&checkin=2025-04-25&checkout=2025-04-26&ltfd=5%3A1%3A3-2025%3A1%3A&group_adults=1&no_rooms=1&group_children=0"
r = requests.get(url)
print(r.status_code)

# Request Agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
r = requests.get(url, headers=headers)

name_list     = []
or_price_list = []
price_list    = []
discr_list    = []
room_ava_list = []
revie_list    = []
food_list     = []


soup = BeautifulSoup(r.text,"lxml")

# Hotels Names
name = (soup.find_all("div",class_ ="f6431b446c a15b38c233"))
for i in name:
    n = i.text
    name_list.append(n)
    print(n)

# Hotels original prices

original_price = (soup.find_all("span", class_ = "abf093bdfe c73ff05531 e84eb96b1f"))
for op in original_price:
    original = op.text
    or_price_list.append(original)
    print(original)

# Hotels Discounted prices
prices = (soup.find_all("span", class_ = "f6431b446c fbfd7c1165 e84eb96b1f"))
for c in prices:
    p = c.text
    price_list.append(p)
    print(p)

# Hotels Discriptions
discriptions = (soup.find_all("h4", class_ = "abf093bdfe e8f7c070a7"))
for d in discriptions:
    details = d.text
    discr_list.append(details)
    print(details)
    
# Hotels Rooms Availability
room_available = (soup.find_all("div", class_ = "d17181842f"))
for rd in room_available:
    available = rd.text
    room_ava_list.append(available)
    print(available)
    
# Hotels Reviews
reviews = (soup.find_all("div", {"class":"a3b8729ab1 e6208ee469 cb2cbb3ccb","class":"abf093bdfe f45d8e4c32 d935416c47"}))
for r in reviews:
    review = r.text
    revie_list.append(review)
    print(review)

Food = (soup.find_all("span", class_ ="a19404c4d7"))
for f in Food:
    foods = f.text
    food_list.append(foods)
    print(foods)
    



# Find the maximum length of all lists
max_length = max(len(name_list), len(or_price_list), len(price_list), 
                 len(discr_list), len(room_ava_list), len(revie_list), len(food_list))

# Pad lists with "N/A" if lengths are mismatched
name_list     += ["N/A"] * (max_length - len(name_list))
or_price_list += ["N/A"] * (max_length - len(or_price_list))
price_list    += ["N/A"] * (max_length - len(price_list))
discr_list    += ["N/A"] * (max_length - len(discr_list))
room_ava_list += ["N/A"] * (max_length - len(room_ava_list))
revie_list    += ["N/A"] * (max_length - len(revie_list))
food_list     += ["N/A"] * (max_length - len(food_list))

# Create DataFrame
df = pd.DataFrame({
    "Hotel Name": name_list,
    "Original Price": or_price_list,
    "Discounted Price": price_list,
    "Description": discr_list,
    "Room Availability": room_ava_list,
    "Reviews": revie_list,
    "Food Options": food_list
})

# Save DataFrame to an Excel file
df.to_excel("hotels_data.xlsx", index=False)

print("Data successfully saved to 'hotels_data.xlsx'!")


import requests
from bs4 import BeautifulSoup
import lxml
from time import sleep

headers = {"Accept": "text/html",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, как Gecko) Chrome/137.0.0.0 Safari/537.36" ,
           "X-Amzn-Trace-Id" : "Root=1-6852a93b-6bb46edc7636e03c1577601e" }

base_url = "https://7fon.org/%D0%9E%D0%B1%D0%BE%D0%B8/3840x2160/"

cnt = 1
image_number = 1
while True:
    if cnt == 1:
        url = base_url
    else:
        url = f"https://7fon.org/%D0%9E%D0%B1%D0%BE%D0%B8/3840x2160/{cnt}.html"

    response = requests.get(url, params = headers)
    soup = BeautifulSoup(response.text, "lxml")

    data = soup.find("div", id = "cbox")
    img_card = data.find_all("div", id = "tmbox")

    for img in img_card:
        try:
            img_card = img.find("a").find("img")
            img_url = "https:" + img_card.get("src")
            download_img = requests.get(img_url, params = headers).content
            sleep(3)
            with open(f"C:\\Users\\User\\Desktop\\Parser_images\\{image_number}.jpg", "wb") as file:
                file.write(download_img)
            image_number += 1

        except AttributeError:
            continue


    if cnt == 5:
        break

    sleep(5)
    cnt += 1

from bs4 import BeautifulSoup
import requests
import smtplib
import time

URL = "https://www.amazon.com/Sony-Mirrorless-Digital-Camera-28-70mm/dp/B00PX8CNCM/ref=sr_1_1?dchild=" \
       "1&keywords=Sony+a7&qid=1589658468&sr=8-1"

headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0',
           "Accept": '*/*',
           "Accept-Language": 'en-US,en;q=0.5',
           "Content-Type": 'application/x-www-form-urlencoded',
           }

def check_price():

       page = requests.get(URL, headers=headers)
       src = page.content
       soup = BeautifulSoup(src, "lxml")

       # title = soup.find(id="productTitle").get_text()
       price = soup.find(id="priceblock_saleprice").get_text()
       converted_price = float(price[1:7])

       if converted_price < 800:
              send_email()



def send_email():
       server = smtplib.SMTP('smtp.gmail.com', port=587)
       server.ehlo()
       server.starttls()
       server.ehlo()

       server.login('email_login', 'email_password')

       subject = 'Price fell down!'
       body = 'Check the Amazon link with your favourite product item:' \
              'https://www.amazon.com/Sony-Mirrorless-Digital-Camera-28-70mm/dp/B00PX8CNCM/ref=sr_1_1?dchild=" \
       "1&keywords=Sony+a7&qid=1589658468&sr=8-1'

       msg = f"Subject: {subject}\n\n{body}"

       server.sendmail(
              'email_login',
              'email_password',
              msg
       )

       print('Email has been sent successfully!')

       server.quit()

while(True):
       check_price()
       time.sleep(86400) #Once a day
#https://www.youtube.com/watch?v=1KHIFs8v7jY
#https://www.youtube.com/watch?v=QNLBBGWEQ3Q

#<meta property="og:price:amount" content="320.00">


# import libs
import requests
import json
from bs4 import BeautifulSoup
import smtplib

# def function for geting url and our data from url ( in this case price of deck)
def get_price(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    price = soup.find("meta", {"property": "og:price:amount"})["content"]
    return price

# def function for price which we wants to check
# if we want add more prices we just put into def main func another value p2,p3 
def add_price(p1):
    total = float(p1) # total = (float(p1) + float(p2) + float (p3)) etc
    return total

stinger_deck = get_price("https://zenitboards.com/collections/line-up-freeride-downhill/products/stinger")

total_price = add_price(stinger_deck)

# creat function to send mail notification when stinger lost price
# server.login = our email adress and passwords
# server.sendmail = from this email send to this mail
def send_mail():
    server = smtplib.SMTP(("smtp.gmail.com", 587)
    server.starttls()
    server.login("p0m3l0pack@gmail.com", "my password")
    subject = "Stinger Upgrade Price Today"
    body = f"The total price to upgrade to this day is: {total_price}"
    message = f"Subject:{subject}\n\n{body}"
    server.sendmail("p0m3l0pack@gmail.com", "santexD@seznam.cz", message)
    print("Email sent")
    server.quit()
    

send_mail()




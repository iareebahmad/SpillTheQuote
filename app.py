# Importing Required Libraries for Scrapping
import requests
from bs4 import BeautifulSoup
import streamlit as st

# Streamlit Setup
st.set_page_config(page_title="Spill The Quote", layout="centered")
st.image("logo.png", width=150)
st.title("Spill The Quote")
st.markdown("Quotes and Authors from [quotes.toscrape.com](http://quotes.toscrape.com)")


# Trigger Button for Scraping
if st.button("Scrap It!"):
    # Making request to the website
    url = "http://quotes.toscrape.com"
    response = requests.get(url)

    # Parsing the response using BeautifulSoup
    soup = BeautifulSoup(response.text,'html.parser')

    # Extraction of Quotes and Authors
    quotes = soup.find_all('div', class_='quote')

    # Success message
    st.success("Scraped the Quotes for you! Here are your quotes :")
    for quote in quotes:
        text = quote.find('span',class_='text').text
        author = quote.find('small',class_='author').text
        # Printing the streamlit output
        st.markdown(f"{text}\n \n *{author}*")

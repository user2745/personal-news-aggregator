import requests
import streamlit as st

# NEWSAPI 
API_KEY = ''

BASE_URL = 'https://newsapi.org/v2/everything'


def fetch_news(topic, page_size=10):
    params = {
        "q": topic,
        "apiKey": API_KEY,
        "pageSize": page_size,
        "sortBy": "relevancy",
        "language": "en"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        return articles
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []

    news = fetch_news("Artificial Intelligence", page_size=10)

    for idx, article in enumerate(news):
        print(f"{idx + 1}. {article['title']}\n{article['description']}\n{article['url']}\n")


# Streamlit visuals
# Input for the news topic

topic = st.text_input("Enter a topic to search for news:", "Artificial Intelligence & Economics")

if topic:
    st.write(f"Fetching news about: {topic}")
    articles = fetch_news(topic, page_size=10)

    for article in articles:
        st.subheader(article['title'])
        st.write(article['description'])
        st.markdown(f"[Read More]({article['url']})")
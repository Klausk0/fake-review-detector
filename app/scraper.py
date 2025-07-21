import requests
from bs4 import BeautifulSoup

def scrape_amazon_reviews(url, max_reviews=10):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Example selector (works on some pages)
    reviews = soup.select(".review-text-content span")
    extracted = [r.get_text(strip=True) for r in reviews]
    return extracted[:max_reviews]

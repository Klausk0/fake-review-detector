import streamlit as st
from model import predict_review_label
from scraper import scrape_amazon_reviews

st.set_page_config(page_title="Fake Review Detector")

st.title("🕵️ Amazon Fake Review Detector")

product_url = st.text_input("Paste Amazon product URL:")

if st.button("Check Reviews"):
    if not product_url.strip():
        st.warning("Please enter a valid URL.")
    else:
        with st.spinner("Scraping reviews..."):
            reviews = scrape_amazon_reviews(product_url)
        
        if not reviews:
            st.error("Could not extract any reviews.")
        else:
            st.success(f"Found {len(reviews)} reviews.")
            for i, review in enumerate(reviews, 1):
                label, confidence = predict_review_label(review)
                st.markdown(f"**Review #{i}:**")
                st.write(review)
                st.markdown(f"**Prediction:** `{label}` ({confidence}% confidence)")
                st.markdown("---")

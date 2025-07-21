FAKE REVIEW DETECTOR

One Simple Link to Detect If a Review is Real or Fake

This project was born out of a frustration that most of us silently share — how do you know if that glowing review on Amazon is real or just paid fluff? I set out to create a tool that could help users verify the authenticity of product reviews using nothing but a link.

What It Was Meant to Do:

Paste any Amazon product link

Automatically scrape the reviews

Classify each review as Real or Fake using an ML model

Give you an honest scorecard of the product

What I Built:

A Streamlit-powered frontend with a clean, user-friendly UI

A trained Naive Bayes classifier to detect fake vs real reviews

Custom preprocessing pipeline for cleaning and vectorizing text

Web scraping logic designed to pull reviews from Amazon automatically

Docker and deployment-ready structure (for the future)

Why It Didn’t Fully Work (Yet):
Amazon has strong anti-scraping protections in place (JavaScript-rendered reviews, bot detection, IP blocking, etc). Despite trying different methods, the scraper would often break or return empty results.

What I Learned:
Even though I hit a wall with scraping Amazon directly, this was a powerful learning experience for me:

Text preprocessing and natural language cleaning techniques

Training a real-world ML model for classification

Model evaluation using precision, recall, F1 score

Streamlit UI design and integration

How scraping works (and how it breaks!)

Dealing with real-life project blockers — and pushing through anyway

What’s Next:

Replace scraping with Amazon’s official API (if possible)

Extend the model to work on other e-commerce platforms like Flipkart or Walmart

Add user feedback loop to improve predictions over time

Possibly turn this into a Chrome extension for live review checking

Built By:
Nishant Acharya — AIML student, builder of weird & ambitious things.
You can find me on LinkedIn: https://www.linkedin.com/in/nishant-acharya-02751a28b
Or right here working on the next problem I probably won’t solve on the first try :)

How to Run:

git clone https://github.com/Klausk0/fake-review-detector

cd fake-review-detector

pip install -r requirements.txt

streamlit run app/ui.py

Disclaimer:
This tool is for educational purposes only. Scraping Amazon may violate their Terms of Service. Please use responsibly.

Star This Repo If You Like Projects That Try

Even if they don’t win — yet ;)


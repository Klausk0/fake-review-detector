def keyword_explain(text):
    keywords = ["free", "gift", "sponsored", "excellent product", "received"]
    reasons = [kw for kw in keywords if kw in text.lower()]
    return ", ".join(reasons) if reasons else "No suspicious keywords"

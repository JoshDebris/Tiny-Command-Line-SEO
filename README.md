
# Tiny Command-Line SEO Analyzer

A minimalistic Python script that quickly analyzes **Title, Meta Tags, and Headings (H1-H6)** of any website directly from the command line. Perfect for fast SEO sanity checks!

---

## ✨ Features
- URL Input & Validation (http/https)
- Extracts Website Title and its length
- Extracts Meta Description & Keywords (+ counts characters & keyword words)
- Lists all Headings (H1-H6) including content and length
- Shows total number of SEO-relevant characters
- Simple CLI output, no clutter

---

## 🗂️ Project Files
```
tclSEO_fixed.py
```

---

## 🚀 How to Use
1. Install required modules:
   ```bash
   pip install requests beautifulsoup4
   ```
2. Run the script:
   ```bash
   python tclSEO.py
   ```
3. Enter the website URL when prompted.

---

## 📖 Example Output
```
### Website Information ###
Title: Example Website (16 characters)

### Metadata ###
Description: This is an example description. (30 characters)
Keywords: example, SEO, script (23 characters, 3 words)

### Headings ###
h1: 1 Headings
- Welcome to Example (19 characters)

h2: 2 Headings
- Features (8 characters)
- Contact Us (10 characters)

### Total number of characters ###
106 characters in total
```

---

## 📖 License
MIT License – use it, modify it, break it, improve it. Just don’t sue me.

---

## 🧰 TODO (Optional)
- Export results as text/CSV file.
- Analyze additional SEO tags (OpenGraph, Twitter Cards).
- Add URL accessibility check (robots.txt, sitemap.xml).

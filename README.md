# 🇵🇰 Pakistan Laptop Price Scraper

A **web scraping tool built using Scrapy** to collect laptop prices and specifications from major Pakistani e-commerce websites such as Daraz, Shophive, Paklap, Galaxy.pk, and more.

---

## 🧠 Overview
This project automatically scrapes laptop listings (name, specs, model, and price) from multiple local marketplaces and saves them into a CSV file (`laptops.csv`).

Originally inspired by [tannu64/pakistan-laptop-scraper](https://github.com/tannu64/pakistan-laptop-scraper) under the MIT License — this version has been enhanced and extended by **Bilal Farooq Siddiqui**.

---

## 🚀 Features
✅ Scrapes from 25+ popular Pakistani e-commerce websites  
✅ Saves data into a clean, structured CSV file  
✅ Built-in pagination handling  
✅ Custom CSS selector support per domain  
✅ Error-handling and retry support  
✅ Runs standalone (no need for full Scrapy project)

---

## ⚙️ Requirements
Make sure you have **Python 3.8+** installed.

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate     # on Linux / macOS
venv\Scripts\activate        # on Windows
```

2. Install dependencies
```
pip install scrapy
```

▶️ Run the Scraper
Run directly using Python:
```
python laptop_scraper.py
```

After completion, check:
```
laptops.csv
```

It will contain columns:
| Laptop Name | Website | Main Specifications | Model Type | Price (PKR) | URL |

🧩 How It Works

List of URLs → predefined sites (Technox, Daraz, Paklap, etc.)

Custom selectors → CSS/XPath selectors for each website

Crawler → visits pages, extracts data, follows pagination

CSV output → stores all data neatly in one file

🧱 Extend / Customize

To add more websites → edit start_urls in laptop_scraper.py
To change how data is extracted → modify the selectors dictionary

# 🇵🇰 Pakistan Laptop Price Scraper
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Scrapy](https://img.shields.io/badge/Scrapy-2.11-green.svg)](https://scrapy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-success.svg)]()


---

## 🧠 Overview
**Pakistan Laptop Price Scraper** is a Python-based web scraping tool built with **Scrapy**.  

It collects **laptop prices, models, and specifications** from multiple popular **Pakistani e-commerce websites** — including **Daraz, Shophive, Paklap, Galaxy.pk, Mega.pk, MyShop.pk**, and more.
All extracted data is saved into a structured CSV file named **`laptops.csv`** for further analysis or price comparison.

> 🏷️ *This project is developed and maintained by **Bilal Farooq**, inspired by and extended from [tannu64/pakistan-laptop-scraper](https://github.com/tannu64/pakistan-laptop-scraper) under the MIT License.*

---

## 🚀 Features
✅ Scrapes from 25+ popular Pakistani e-commerce websites  
✅ Saves data into a clean, structured CSV file  
✅ Built-in pagination handling  
✅ Custom CSS selector support per domain  
✅ Error-handling and retry support  
✅ Runs standalone (no need for full Scrapy project)

---

## 🧩 Project Structure
📦 ML-Project/
┣ 📜 Laptop_Scraper.py # main scraper file
┣ 📜 laptops.csv # output file (auto-created)
┣ 📜 LICENSE # MIT License
┗ 📜 README.md # documentation (this file)

---
## ⚙️ Requirements
Make sure you have **Python 3.8+** installed.

### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate     # on Linux / macOS
venv\Scripts\activate        # on Windows
```

### 2. Install dependencies
```
pip install scrapy
```

▶️ Run the Scraper
Run directly using Python:
```
python Laptop_Scraper.py
```

After completion, check:
```
laptops.csv
```

It will contain columns:
Laptop Name	Website	Main Specifications	Model Type	Price (PKR)	URL

🧩 How It Works

List of URLs → predefined sites (Technox, Daraz, Paklap, etc.)

Custom selectors → CSS/XPath selectors for each website

Crawler → visits pages, extracts data, follows pagination

CSV output → stores all data neatly in one file

🧱 Extend / Customize

To add more websites → edit start_urls in laptop_scraper.py
To change how data is extracted → modify the selectors dictionary

---
🌐 Supported Websites

✅ technox.pk
✅ olx.com.pk
✅ paklap.pk
✅ shophive.com
✅ galaxy.pk
✅ daraz.pk
✅ fhlaptop.pk
✅ myshop.pk
✅ telemart.pk
✅ mega.pk
✅ vmart.pk
✅ tejar.pk
✅ and many others...

⚠️ Some domains may occasionally fail due to temporary DNS issues or blocking. The scraper will retry automatically.

---
🧪 Example Output (CSV Preview)
Laptop Name	Website	Specs Summary	Model	Price (PKR)	URL
HP Pavilion 15 Core i7 16GB 512GB	galaxy.pk	16GB RAM • 512GB SSD • 15.6" FHD	i7-1255U	192,000	https://www.galaxy.pk/laptops
Dell Inspiron 3511 Core i5	paklap.pk	8GB RAM • 256GB SSD • 11th Gen	i5-1135G7	162,999	https://paklap.pk/laptops-prices.html

--- 
🧑‍💻 Author
Bilal Farooq Siddiqui
🎓 FAST-NUCES | Student of Artificial Intelligence
💡 GitHub: @bilalfarooq056

---
🪪 Credits
Original project: tannu64/pakistan-laptop-scraper
Extended, improved, and refactored by Bilal Farooq Siddiqui (2025)

---
🧭 Future Enhancements

🚧 Add a machine learning model for price prediction
🚧 Introduce auto-scheduler for daily updates
🚧 Build dashboard (Flask + Chart.js) for visualization
🚧 Integrate with Google Sheets API





# Adapted from: https://github.com/tannu64/pakistan-laptop-scraper
# Original Author: tannu64
# License: MIT

import scrapy
import csv
import re
from urllib.parse import urlparse
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


class LaptopSpider(scrapy.Spider):
    name = "laptop_spider"

    # ✅ List of websites to scrape
    start_urls = [
        "https://technox.pk/product-category/laptops/laptops-under-60k/",
        "https://www.olx.com.pk/laptops-computers-accessories_c443/q-16gb",
        "https://www.mega.pk/product/laptop-specs-ram-16gb/",
        "https://mrlaptop.pk/product-category/shop-by-specs/dedicated-graphics-card-laptops/",
        "https://www.daraz.pk/laptops",
        "https://www.shophive.com/laptop-notebook",
        "https://www.paklap.pk/laptops-prices.html",
        "https://www.homeshopping.pk/computer-laptop",
        "https://www.galaxy.pk/laptops",
        "https://www.tejar.pk/category/laptops",
        "https://www.ishopping.pk/laptops",
        "https://www.symbios.pk/collections/laptop",
        "https://www.vmart.pk/laptops",
        "https://www.clicky.pk/computers/laptops",
        "https://www.laptab.com.pk/laptops",
        "https://www.megastore.pk/laptops",
        "https://www.shoprex.com/laptops",
        "https://www.shopon.pk/laptops",
        "https://www.telemart.pk/computer/laptops.html",
        "https://www.techcity.pk/laptops",
        "https://www.computerzone.com.pk/laptops",
        "https://www.czone.com.pk/laptops",
        "https://www.pakdukaan.com/laptops",
        "https://myshop.pk/laptops-desktops-computers/laptops",
        "https://hf-store.pk/laptops",
        "https://www.computronix.com.pk",
        "https://centurycomputerpk.com",
        "https://intaglaptops.com",
        "https://wajiz.pk",
        "https://fhlaptop.pk",
        "https://priceoye.pk/laptops"
    ]

    # ✅ Site-specific selectors
    selectors = {
        'technox.pk': {
            'laptop_item': '.product',
            'laptop_name': '.woocommerce-loop-product__title::text',
            'specs': '.product-short-description::text',
            'model': '.sku::text',
            'price': '.price bdi::text'
        },
        'olx.com.pk': {
            'laptop_item': '._7e3920c1',
            'laptop_name': '._4684f251::text',
            'specs': '._9c62ecdf::text',
            'model': '._93444fe0::text',
            'price': '._95eae7db::text'
        },
        'paklap.pk': {
            'laptop_item': '.product-item',
            'laptop_name': '.product-name::text',
            'specs': '.short-description::text',
            'model': '.sku::text',
            'price': '.price::text'
        },
        'shophive.com': {
            'laptop_item': '.product-item',
            'laptop_name': '.product-title::text',
            'specs': '.short-description::text',
            'model': '.model::text',
            'price': '.price bdi::text'
        },
        'galaxy.pk': {
            'laptop_item': '.product',
            'laptop_name': '.name::text',
            'specs': '.short-description::text',
            'model': '.sku::text',
            'price': '.price bdi::text'
        },
        'fhlaptop.pk': {
            'laptop_item': '.product',
            'laptop_name': '.woocommerce-loop-product__title::text',
            'specs': '.woocommerce-product-details__short-description::text',
            'model': '.sku::text',
            'price': '.price bdi::text'
        },
        # ✅ Default fallback selectors
        'default': {
            'laptop_item': '.product, .item, [class*="product"], [class*="item"]',
            'laptop_name': 'h2::text, h3::text, .name::text, .title::text, [class*="name"]::text, [class*="title"]::text',
            'specs': '.specs::text, .description::text, [class*="specs"]::text, [class*="description"]::text',
            'model': '.model::text, .sku::text, [class*="model"]::text, [class*="sku"]::text',
            'price': '.price::text, [class*="price"]::text'
        }
    }

    # ✅ CSV header fields
    fieldnames = ["Laptop Name", "Website", "Main Specifications", "Model Type", "Price (PKR)", "URL"]

    def __init__(self, *args, **kwargs):
        super(LaptopSpider, self).__init__(*args, **kwargs)
        self.file = None
        self.writer = None
        try:
            self.file = open("laptops.csv", "w", newline="", encoding="utf-8")
            self.writer = csv.DictWriter(self.file, fieldnames=self.fieldnames)
            self.writer.writeheader()
            self.logger.info("CSV file initialized successfully")
        except Exception as e:
            self.logger.error(f"Error initializing CSV file: {e}")

    def parse(self, response):
        domain = urlparse(response.url).netloc.replace('www.', '')
        selector_set = self.selectors.get(domain, self.selectors['default'])

        try:
            laptops = response.css(selector_set['laptop_item'])
            if not laptops:
                self.logger.warning(f"No laptops found on {response.url} using {selector_set['laptop_item']}")
                laptops = response.css(self.selectors['default']['laptop_item'])
            if not laptops:
                return

            self.logger.info(f"Found {len(laptops)} laptops on {response.url}")

            for laptop in laptops:
                name = self._extract_text(laptop, selector_set['laptop_name'])
                specs = self._extract_text(laptop, selector_set['specs'])
                model = self._extract_text(laptop, selector_set['model'])
                price = self._extract_text(laptop, selector_set['price'])
                price = self._clean_price(price)

                item = {
                    'Laptop Name': name,
                    'Website': domain,
                    'Main Specifications': specs,
                    'Model Type': model,
                    'Price (PKR)': price,
                    'URL': response.url
                }

                if item['Laptop Name'] and item['Price (PKR)']:
                    if self.writer:
                        self.writer.writerow(item)
                        self.logger.debug(f"Saved: {item['Laptop Name']} - {item['Price (PKR)']}")
                else:
                    self.logger.debug(f"Incomplete data on {response.url}: {item}")

            # ✅ Pagination support
            next_page = response.css('a.next::attr(href), li.next a::attr(href)').get()
            if next_page:
                yield response.follow(next_page, callback=self.parse)

        except Exception as e:
            self.logger.error(f"Error parsing {response.url}: {e}")

    def _extract_text(self, selector, css_path):
        for path in css_path.split(', '):
            result = selector.css(path).get()
            if result:
                return result.strip()
        fallback = selector.xpath('.//text()').getall()
        if fallback:
            return ' '.join(t.strip() for t in fallback if t.strip())[:150]
        return None

    def _clean_price(self, price):
        if not price:
            return None
        price = re.sub(r'[^\d.]', '', price)
        try:
            return float(price)
        except ValueError:
            return price

    def closed(self, reason):
        if self.file:
            try:
                self.file.close()
                self.logger.info(f"CSV file saved successfully. Reason: {reason}")
            except Exception as e:
                self.logger.error(f"Error closing CSV file: {e}")


# ✅ Settings (built-in for standalone run)
custom_settings = {
    'DOWNLOAD_DELAY': 2,
    'CONCURRENT_REQUESTS_PER_DOMAIN': 2,
    'RETRY_TIMES': 5,
    'DOWNLOAD_TIMEOUT': 30,
    'COOKIES_ENABLED': False,
    'REDIRECT_ENABLED': True,
    'RETRY_HTTP_CODES': [500, 502, 503, 504, 522, 524, 408],
    'HTTPERROR_ALLOW_ALL': True,
    'DEFAULT_REQUEST_HEADERS': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/120.0 Safari/537.36'
    },
    'LOG_LEVEL': 'INFO'
}


if __name__ == "__main__":
    process = CrawlerProcess({**get_project_settings(), **custom_settings})
    process.crawl(LaptopSpider)
    process.start()

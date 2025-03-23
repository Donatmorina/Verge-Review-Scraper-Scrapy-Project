# Verge-Review-Scraper-Scrapy-Project
This project is a web scraper built with Scrapy to collect article review metadata from The Verge, including titles, author names, and author profile URLs.

What it does:
Crawls the Reviews section on The Verge.
Follows internal article links using regex-based filtering.
Extracts and saves: Article URL, Article titlel, Author name, and Author profile URLs.
Stores the scraped data in a CSV file.

Project Structure
verge_spider.py: The main spider that handles crawling and parsing logic.
items.py: Defines the VergeReview data structure.
pipelines.py: Optional item processing (currently pass-through).
middlewares.py: Default spider and downloader middleware setup.
settings.py: Custom settings (CSV output, crawl limits, UTF-8 encoding).
verge_reviews.csv: Output file containing the scraped data.

Each row in the output CSV (verge_reviews.csv) includes: URLs to the article, Article title, Author names, and Author profile links.

Requirements: #pip install scrapy
Python 3.7+
Scrapy 2.11.0+

Disclaimer:
Intended for educational or personal use only.

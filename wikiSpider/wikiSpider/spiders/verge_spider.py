import scrapy
import re
from ..items import VergeReview

class VergeSpider(scrapy.Spider):
    name = "verge"
    allowed_domains = ["theverge.com"]
    start_urls = ["https://www.theverge.com/reviews"]

    # Regular Expression for Valid URLs
    pattern1 = re.compile(r"https://www.theverge.com/\d+/[\w\-]+$")
    pattern2 = re.compile(r"https://www.theverge.com/[a-z\-]+/\d+/[\w\-]+$")

    def parse(self, response):
        for article in response.css("a"):  # Extract all links
            link = article.attrib.get("href", "")
            absolute_url = response.urljoin(link)

            if self.pattern1.match(absolute_url) or self.pattern2.match(absolute_url):
                yield response.follow(absolute_url, self.parse_review)

    def parse_review(self, response):
        title = response.css("h1::text").get()
        
        # Extracting author name
        author = response.css('span[class*="114qu8c2"] a::text').get()
        
        # Extracting author profile link
        author_links = response.css('span[class*="114qu8c2"] a::attr(href)').getall()
        author_profile = ",".join([response.urljoin(link) for link in author_links]) if author_links else ""

        self.logger.info(f"Extracted: Title: {title}, Author: {author}, Author Links: {author_profile}")

        if title and author:
            item = VergeReview()
            item["url"] = response.url
            item["title"] = title.strip()
            item["author_name"] = author.strip()
            item["author_profile"] = author_profile.strip()
            yield item



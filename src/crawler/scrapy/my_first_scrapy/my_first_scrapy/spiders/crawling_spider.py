from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
    name = "mycrawler"
    allowed_domains = ["toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]  # "start_urls" is a predefined attribute name.

    rules = (
        # Rule(LinkExtractor(), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow="catalogue/category"), callback="parse_item"), # single element tuple you need to add an additional comma in the end. Otherwise, it's not going to be recognized as a tuple.a
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item"), # 這兩個Rule要一起是因為他要先經過catalogue/category 才能往下走，走完之後再用第二個rule回頭deny="category"(分頁)，因為不需要分頁，但是又需要透過分頁才能往下走
    )




    def parse_item(self, response):
        yield {
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get().strip(),
            "availability": response.css(".instock.availability::text").getall()[1],  # strip去空白換行用的
            'url': response.url,
        }

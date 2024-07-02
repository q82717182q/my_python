
import scrapy
import json

from scrapy import FormRequest


class LinkedInSpiderGpt(scrapy.Spider):
    name = 'linkedin_jobs'
    start_urls = ['https://www.linkedin.com/login']

    def parse(self, response):
        # 提取csrf token
        csrf = response.xpath('//input[@name="loginCsrfParam"]/@value').get()
        return FormRequest.from_response(response,
                                         formdata={
                                             'session_key': 'q82717182q@gmail.com',
                                             'session_password': 'eqbznna6984',
                                             'loginCsrfParam': csrf
                                         },
                                         callback=self.after_login)

    def after_login(self, response):
        # 确认登录成功
        if "feed" in response.url:
            self.logger.info("Logged in successfully")
            # 开始抓取工作页面
            yield scrapy.Request(url="https://www.linkedin.com/jobs/search/?keywords=python&location=United%20States", callback=self.parse_jobs)
        else:
            self.logger.error("Login failed")

    def parse_jobs(self, response):
        jobs = response.xpath('//ul[@class="jobs-search__results-list"]/li')
        for job in jobs:
            yield {
                'title': job.xpath('.//h3/text()').get(),
                'company': job.xpath('.//h4/a/text()').get(),
                'location': job.xpath('.//span[@class="job-result-card__location"]/text()').get(),
                'link': job.xpath('.//a/@href').get()
            }
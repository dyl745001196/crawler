import scrapy

class HouseSpider(scrapy.Spider):
    name = "house"
    start_urls=['http://bbs.whnet.edu.cn/cgi-bin/bbstdoc?board=House']

    def start_requests(self):
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        for url in self.start_urls:
            yield scrapy.Request(url, headers=headers)

    page = 0
    def parse(self, response):
        self.log("parse")
        for tr in response.css("tr"):
            td = tr.re(r'td>\d{4}')
            if len(td)>0:
                yield{
                        'index':tr.css('td')[0].css('::text').extract_first(),
                        'date':tr.css('td')[3].css('::text').extract_first(),
                        'detail':tr.css('td')[4].css('a::text').extract_first(),
                        'url':'http://bbs.whnet.edu.cn/cgi-bin/'+tr.css('td')[4].css('a::attr(href)').extract_first()
                        }
        next_page = response.css("a#lastpage::attr(href)").extract_first()
        if next_page is not None:
            next_page = "http://bbs.whnet.edu.cn/cgi-bin/"+next_page
            self.log(next_page)
            self.page = self.page +1
            if self.page < 3:
                yield scrapy.Request(next_page, callback=self.parse)

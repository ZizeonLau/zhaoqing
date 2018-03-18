# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.spiders import CrawlSpider
from scrapy import Selector
import urllib.parse as urlparse
import json
import regex


class Defaultcrawler1Spider(CrawlSpider):
#    name = 'DefaultCrawler1' .extract_first().extract_first()
#    allowed_domains = []
#    start_urls = ['http://www.bjjs.gov.cn/eportal/ui?pageId=39354h7&systemId=2&categoryId=1&salePermitId=5566894&buildingId=469223']
    name = 'ZhaoqingFang' 
    start_urls = ['http://www.zqjs.gov.cn/Housepresell/User_ItemList.aspx?lid={F96EA453-7C8F-488C-BEB4-A696849BBA06}']
#    def start_requests(self):
#        for url in self.start_urls:
#            req = Request(url=url, meta={'PageType': 'HouseInfo',
#                                            'BuildingName': 'hahahahah',
#                                            'ProjectName': 'lalalalallal'})
#            yield req
    def parse(self, response):
        metadict = response.meta
        sel = Selector(response)
        housetable = sel.xpath('//table[@id="listtable"]')
        for table in housetable:
            projectlist = table.xpath('./tr')
            for project in projectlist:
                href = project.xpath('./td[1]/a/@href').extract_first()
                url = 'http://www.zqjs.gov.cn/Housepresell/%s' % (href)
                projectname = project.xpath('./td[1]/a/text()').extract_first()
                projectaddress = project.xpath('./td[2]/text()').extract_first()
                city = project.xpath('./td[3]/text()').extract_first()
                info = {}
                info['url'] = url
                info['name'] = projectname
                info['address'] = projectaddress
                info['city'] = city
                #Sprint(info)
                yield Request(url= url, meta={'dict': info}, callback=self.parse_two)
        page = metadict.get('page')
        if page:
            page = page + 1
        else:
            page = 2
        pageurl = 'http://www.zqjs.gov.cn/Housepresell/user_itemlist.aspx?key=&kind=&LID={F96EA453-7C8F-488C-BEB4-A696849BBA06}&page=%s' % (page)
        yield Request(url= pageurl, meta={'page': page}, callback= self.parse)

    def parse_two(self, response):
        sel = Selector(response)
        metadict = response.meta
        tables = sel.xpath('/html/body/table/tr[2]/td/table/tr/td/table[2]')
        tableone = sel.xpath('//table[@id="kfsinfo"]')
        tabletwo = tables.xpath('./tr[@id="xiaosho uqingkuan"]/td/table')
        tablethree = sel.xpath('//table[@id="preselltable1"]')
        tablefour = sel.xpath('//table[@id="selltable1"]')
        projectinfo = {}
        infolist = []
        #headers = {'Host': 'www.zqjs.gov.cn',
        #                'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
        #                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #                'Accept-Language': 'en-US,en;q=0.5',
        #                'Accept-Encoding': 'gzip, deflate',
        #                'Cache-Control':'max-age=0',
        #                'Connection':'keep-alive',
        #                'Cookie':'safedog-flow-item=; yfx_c_g_u_id_10003289=_ck18031703542417427473416549606; yfx_f_l_v_t_10003289=f_t_1521273264744__r_t_1521273264744__v_t_1521273264744__r_c_0',
        #                'Referer':'http://www.zqjs.gov.cn/',
        #                'Upgrade-Insecure-Requests':'1',
        #} 
        for table in tableone:
            for tr in table.xpath('./tr'):
                for td in tr.xpath('./td'):
                    if td.xpath('./@id').extract_first() == 'kfsmctd':
                        infolist.append(td.xpath('./a/text()').extract_first())
                    else:
                        infolist.append(td.xpath('./text()').extract_first())
        for table in tabletwo:
            for tr in table.xpath('./tr'):
                for td in tr.xpath('./td'):
                    infolist.append(td.xpath('./text()').extract_first())
        a = 1
        for i in infolist:
            if a % 2 != 0:
                key = i
            if a % 2 == 0:
                projectinfo[key] = i
            a = a + 1
        for presell in tablethree:
            for td in presell.xpath('./tr[@bgcolor="white"]'):
                projectinfo['预售证号'] = td.xpath('./td[1]/a/text()').extract_first()
                projectinfo['座落'] = td.xpath('./td[2]/a/@title').extract_first()
                projectinfo['合同样本信息'] = td.xpath('./td[3]/a/font/text()').extract_first()
                href = td.xpath('./td[4]/a/@href').extract_first()
                url = 'http://www.zqjs.gov.cn/Housepresell/%s' % (href)
                yield Request(url= url, meta={'project': metadict, 'projectinfo': projectinfo}, callback=self.parse_six)
        for sell in tablefour:
            for td in sell.xpath('./tr[@bgcolor="white"]'):
                projectinfo['证明书号'] = td.xpath('./td[1]/text()').extract_first()
                projectinfo['座落'] = td.xpath('./td[2]/text()').extract_first()
                projectinfo['合同样本信息'] = td.xpath('./td[3]/text()').extract_first()
                href = td.xpath('./td[4]/a/@href').extract_first()
                url = 'http://www.zqjs.gov.cn/Housepresell/%s' % (href)
                #print(projectinfo)
                yield Request(url= url, meta= {'project': metadict, 'projectinfo':projectinfo}, callback=self.parse_three)

    def parse_three(self, response):
        metadict = response.meta
        sel = Selector(response)
        url = sel.xpath('//a/@href').extract_first()
        yield Request(url= url, meta= {'metadict': metadict}, callback=self.parse_four)

    def parse_four(self, response):
        metadict = response.meta
        sel = Selector(response)
        divs = sel.xpath('//div[@id="houseshow"]/table')
        floorinfo = {}
        for div in divs:
            tables = div.xpath('./tr')
            for table in tables:
                floor = table.xpath('./td[1]/text()').extract_first()
                lines = table.xpath('./td[2]/table/tr')
                floorinfo['楼层号'] = floor   
                for line in lines:
                    houses = line.xpath('./td')
                    for house in houses:
                        number = house.xpath('./a/font/text()').extract_first()
                        state = house.xpath('./table/tr/td/a/font/text()').extract_first()
                        href = house.xpath('./a/@href').extract_first()
                        floorinfo['房屋号'] = number
                        floorinfo['状态'] = state
                        url = 'http://www.zqjs.gov.cn/Housepresell/%s' % (href)
                        print(floorinfo)
                        yield Request(url= url, meta= {'metadict': metadict, 'floorinfo': floorinfo}, callback=self.parse_five)

    def parse_five(self, response):
        sel = Selector(response)
        metadict = response.meta
        lefts = sel.xpath('/html/body/table/tr/td[@bgcolor="#eff7ef"]')
        infolistone = []
        infolisttwo = []
        for left in lefts:
            info = left.xpath('./strong/text()').extract_first()
            if info:
                pass
            else:
                info = left.xpath('./text()').extract_first()
            infolistone.append(info.strip())
        rights = sel.xpath('/html/body/table/tr/td[@bgcolor="white"]')
        for right in rights:
            info = right.xpath('./strong/text()').extract_first()
            if info:
                pass
            else:
                info = right.xpath('./text()').extract_first()
            if info != '\r\n          ':
                infolisttwo.append(info)
        infodict = dict(zip(infolistone, infolisttwo))
        info = {}
        info.update(metadict)
        info.update(infodict)
        print(info)
    
    def parse_six(self, response):
        sel = Selector(response)
        metadict = response.meta
        lefts = sel.xpath('//table[@id="kfsinfo"]/tr/td[@bgcolor="#eeeeee"]')
        rights = sel.xpath('//table[@id="kfsinfo"]/tr/td[@bgcolor="#FFFFFF"]')
        users = sel.xpath('//table[@id="kfsinfo"]/tr/td[@id="bank"]/table[@id="banktable"]/tr[@bgcolor="#f5f5f5"]')
        listleft = []
        listright = []
        userdict = {}
        for left in lefts:
            info = left.xpath('./text()').extract_first()
            listleft.append(info.strip())
        for right in rights:
            info = right.xpath('./text()').extract_first()
            if info:
                pass
            else:
                info = right.xpath('./a/text()').extract_first()
            listright.append(info)
        for user in users:
            userdict['银行名称'] = user.xpath('./td[1]/text()').extract_first()
            userdict['银行账号'] = user.xpath('./td[2]/text()').extract_first()
            userdict['银行联系电话'] = user.xpath('./td[3]/text()').extract_first()
        infodict = dict(zip(listleft, listright))
        infodict['预售专用账户：'] = userdict
        prelist = sel.xpath('//table[@id="donglist"]')
        for pre in prelist:
            infodict['楼盘名称'] = pre.xpath('./tr/td[1]/text()').extract_first()
            infodict['楼盘坐落'] = pre.xpath('./tr/td[2]/text()').extract_first()
            infodict['栋号'] = pre.xpath('./tr/td[3]/text()').extract_first()
            infodict['层数'] = pre.xpath('./tr/td[4]/text()').extract_first()
            href = pre.xpath('./tr/td[5]/a/@href').extract_first()
            url = 'http://www.zqjs.gov.cn/Housepresell/%s' % (href)
            yield Request(url= url, meta= {'metadict': metadict, 'infodict': infodict}, callback= self.parse_three)


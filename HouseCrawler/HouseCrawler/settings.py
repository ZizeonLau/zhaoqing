# -*- coding: utf-8 -*-

# Scrapy settings for HouseCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import os
import sys

# PROXY_REDIS = dj_settings.SCRAPY_BASE_REDIS_CLIENT
# PROXYFLAG_REDIS = dj_settings.SCRAPY_BASE_REDIS_CLIENT
# BLOOMFILTER_REDIS = dj_settings.BLOOM_FILTER_REDIS_CLIENT

# BASE_MONGO_CLIENT = dj_settings.BASE_MONGO_CLIENT

BOT_NAME = 'HouseCrawler'

SPIDER_MODULES = ['HouseCrawler.Spiders']
NEWSPIDER_MODULE = 'HouseCrawler.Spiders'
COMMANDS_MODULE = 'HouseCrawler.Commands'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'HouseCrawler (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {'Host': 'www.zqjs.gov.cn',
                        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0',
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                        'Accept-Language': 'en-US,en;q=0.5',
                        'Accept-Encoding': 'gzip, deflate',
                        'Cache-Control':'max-age=0',
                        'Connection':'keep-alive',
                        'Cookie':'safedog-flow-item=; yfx_c_g_u_id_10003289=_ck18031703542417427473416549606; yfx_f_l_v_t_10003289=f_t_1521273264744__r_t_1521273264744__v_t_1521273264744__r_c_0',
                        'Referer':'http://www.zqjs.gov.cn/',
                        'Upgrade-Insecure-Requests':'1',
        } 

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 101
}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
}

RETRY_ENABLED = True
RETRY_TIMES = 5
RETRY_HTTP_CODES = []
REDIRECT_ENABLED = False


COOKIES_ENABLED = False
COOKIES_DEBUG = False

DOWNLOAD_DELAY = 0.5
DOWNLOAD_TIMEOUT = 15
RANDOMIZE_DOWNLOAD_DELAY = True
# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
EXTENSIONS = {
}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'HouseCrawler.Pipelines.Pipelines.Pipeline': 300,
}
HTTPERROR_ALLOWED_CODES = [302]

LOG_LEVEL = 'INFO'
# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


USER_AGENTS = ["Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0", ]

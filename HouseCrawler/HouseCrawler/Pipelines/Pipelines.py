# coding = utf-8
import sys
import os
import logging
import uuid
import datetime

logger = logging.getLogger(__name__)


class Pipeline(object):

    def __init__(self, settings):
        self.settings = settings

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings)

    def check_item_change(self, item):
        pass

    def process_item(self, item, spider):
        if item:
            pass
            return item

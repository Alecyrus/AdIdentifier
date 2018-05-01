# -*- coding: UTF-8 -*-

import os
import urlparse4 as urlparse
from tgrocery import Grocery
from fuzzywuzzy import process
import ConfigParser

TRAIN_SRC = "textsample.txt"
EASYLIST_SRC = "easylist.txt"

from adblockparser import AdblockRules

class AdIdentifier(object):
    def __init__(self):
        self.src = os.path.split(os.path.realpath(__file__))[0] 
        self.raw_rules = open("%s/%s" % (self.src, EASYLIST_SRC), "r").readlines()
        self.config = ConfigParser.RawConfigParser()
        self.f_kws = list()
        self._grocery = Grocery('model')
        if not os.path.exists("setting.conf"):
            self._generate_config()
        self._initialize_config()
        self._initialize_adfilters()
        self._initialize_detector()

    def _generate_config(self):
        self.config.add_section('CUSTOM')
        self.config.set('CUSTOM', 'uri_keywords', 'qian,dai,cf,wd,jin')
        self.config.set('CUSTOM', 'text_keywords', '网贷')
        self.config.set('CUSTOM', 'ad_filter', 'https://ss3.baidu.com/*,https://ss2.bdstatic.com/*')
        with open('setting.conf', 'wb') as configfile:
            self.config.write(configfile)


    def _initialize_config(self):
        self.config.read('setting.conf')
        uri_keywords = self.config.get("CUSTOM", 'uri_keywords').replace(" ", "").split(",")
        text_keywords = self.config.get("CUSTOM", 'text_keywords').replace(" ", "").split(",")
        ad_filter = self.config.get("CUSTOM", 'ad_filter').replace(" ", "").split(",")
        for u_k in uri_keywords:
            if u_k:
                self.f_kws.append(u_k)

        if  len(self.f_kws) == 0:
            raise AttributeError("Uri_keywords shouldn't be none, please check config file(setting.conf)")

        train_ssrc = list()
        for t_k in text_keywords:
            if t_k:
                train_ssrc.append(("finance", t_k))
        self._grocery.train(train_ssrc)

        for adf in ad_filter:
            if adf:
                self.raw_rules.append(adf)


    def _initialize_detector(self):
        try:
            self._grocery.train("%s/%s" %(self.src, TRAIN_SRC))
            self._grocery.save()
            self.grocery = Grocery('model')
            self.grocery.load()
        except Exception as e:
            print(e)
            raise AttributeError("Failed to initialize the Detector")

    def _initialize_adfilters(self):
        try:
            self.filter =  AdblockRules(self.raw_rules, 
                                        use_re2=True, 
                                        max_mem=512*1024*1024)
        except Exception as e:
            print(e)
            raise AttributeError("Failed to initialize the Adfilters")

    def get_domain_from_url(self, url):
        parsed_uri = urlparse.urlparse(url)
        return parsed_uri.netloc


    def is_ad(self, url, options=None):
        return self.filter.should_block(url, options)



    def is_finance(self, target):
        try:
            domain = self.get_domain_from_url(target)
            if not domain and self.grocery.predict(target).predicted_y == "finance":
                return True
            #print(self.get_domain_from_url(target))

            #print(process.extractOne(domain, self.f_kws))
            if process.extractOne(domain, self.f_kws)[1] >= 80:
                return True
            return False
        except Exception as e:
            print(e)
            return False

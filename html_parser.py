#coding:utf-8

from bs4 import BeautifulSoup

import re

import urllib.parse

class HtmlParser(object):

    #获取页面中所有的url
    def _get_new_urls(self,page_url,soup):
        new_urls = set()

        # <a target="_blank" href="/item/IEEE/150905" data-lemmaid="150905">IEEE</a>

        links = soup.find_all("a",href = re.compile(r"/item/"))

        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls






        #获取数据
    def _get_new_data(self,page_url,soup):
        res_data = {}

        res_data['url'] = page_url

        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node1 = soup.find("dd",class_="lemmaWgt-lemmaTitle-title")
        if  title_node1 is None:
            res_data['title'] = ''
        else:
            title_node2 = title_node1.find("h1")
            if title_node2 is None:
                res_data['title'] = ''
            else:
                res_data['title'] = title_node2.get_text()

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find("div",class_="lemma-summary")
        if  summary_node is None:
            res_data['summary'] = ''
        else:
            res_data['summary'] = summary_node.get_text()



        return res_data



    def parse(self,page_url,html_cont):

        if page_url is None or html_cont is None:
            return None

        soup = BeautifulSoup(html_cont,"html.parser")

        new_urls = self._get_new_urls(page_url,soup)

        new_data = self._get_new_data(page_url,soup)

        return new_urls,new_data

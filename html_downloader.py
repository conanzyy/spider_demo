#coding:utf-8

import urllib
import urllib.request

class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None

        response = urllib.request.urlopen(url)

        if response.getcode() != 200:
            return None
        print ("200")
        return response.read().decode('utf8')
# -*- coding: utf-8 -*-
"""
Utility function to scrape websites

Project page: https://github.com/inkjet/FBS_Power5

Author: Scott Rodkey, rodkeyscott@gmail.com

"""

def get_page(url):
    try:
        # Python 3.x method
        from urllib.request import urlopen
        page = urlopen(url)
    except:
        # Python 2.x method
        import urllib2
        page = urllib2.urlopen(url)
    return page

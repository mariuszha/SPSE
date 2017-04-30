#!/usr/bin/python2.7

#
# ex.exHTMLparser.py v1.0 by mariuszha
#

from bs4 import BeautifulSoup
import urllib


page = urllib.urlopen('http://www.securitytube.net/video/3000')


if page.code == 200:
        print 'The status code of the page is: ', page.code

        bt = BeautifulSoup(page.read(), 'lxml')

########### Print all URLs whitin the webpage #############
        print '############# All links in the www page ##############'

        for link in bt.find_all('a'):
                print link['href']


        print ''
        print ''
        print ''
########### Print juicy information ##############
        print '############ All juicy information from the webpage ################'
        print ''
        print '############### Title tag ###############'
        titleTag = bt.title.string
        print 'Title tag: ', titleTag
        print ''
        print '############# IMG tags #################'
        for IMG in bt.find_all('img'):
                print 'IMG tag: ', IMG['src']
        print ''

        allMetaTags = bt.find_all('meta')
        a = len(allMetaTags)
        a = a -1
        print ''
        print '############## Meta tags ################'
        while a > 0:
                print allMetaTags[a]
                a = a -1


else:
        print 'The requested page is unavailable'

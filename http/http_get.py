#! /usr/bin/python
# -*- coding: ISO-8859-1 -*-
# Creation d'une requete HTTP
# Created by: Aurelihein
#
import urllib, urllib2, cookielib, httplib2, time, socks, sys

theUrl = "http://www.hackbbs.org/miss/22/index.php?user=NIEHILERUA"
oldcookieValue="PHPSESSID=fphd55be9rtq4ea6ka02sofn31; __utma=28156965.79805353.1352201036.1352201036.1352204057.2; __utmc=28156965; __utmz=28156965.1352201036.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); name=NIEHILERUA; PHPSESSID=fphd55be9rtq4ea6ka02sofn31; __utmb=28156965.4.10.1352204057"
cookieValue="PHPSESSID=kpmapikfjo796jhrsvd2cosfn3; __utma=28156965.1434401342.1352204837.1352204837.1352204837.1; __utmc=28156965; __utmz=28156965.1352204837.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); name=NIEHILERUA; PHPSESSID=kpmapikfjo796jhrsvd2cosfn3"

proxyURL="164.77.196.78:80"
headers = {'Cookie':cookieValue}

def test() :
	print "Using test"

	proxy_handler = urllib2.ProxyHandler({'http':proxyURL})
	opener = urllib2.build_opener(proxy_handler)
	opener.addheaders = [('User-agent','Mozilla/5.0')]
	#opener.addheaders = [('Cookie',cookieValue)]
	urllib2.install_opener(opener)
        #req = urllib2.Request("http://www.google.com")
	req = urllib2.Request(theUrl)
	sock=urllib2.urlopen(req, timeout= 20)
	rs = sock.read(1000)
	print rs

def oldtest():
	print "Using old test"
	#http = httplib2.Http()
	http = httplib2.Http(proxy_info = httplib2.ProxyInfo(socks.PROXY_TYPE_HTTP, proxyURL, 80))

	# get cookie_value here
	try :
		response, content = http.request(theUrl, 'GET', headers=headers)
	except httplib2.ServerNotFoundError:
		print "Site is Down"
		sys.exit(0)

	print "response:"+str(response)
	print "content:\n"+content
	print"#########################################################################################################"
	#time.sleep(5)

	response, content = http.request(theUrl, 'GET', headers=headers)
	print "response:"+str(response)
	print "content:\n"+content
	print"#########################################################################################################"

test()

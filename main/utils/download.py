import urllib.request as urllib2
from get_proxy_ip import get_ip
__all__ = ['download_from_url', 'download_from_url_headers']

# send_headers = {
#     'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
#     'Referer':'http://www.sse.com.cn/assortment/stock/list/share/',
# }

proxies = {'http':''}

def download_from_url(url,file_name):
	global proxies	
	try:
		if proxies['http']!="":
			proxy_handler = urllib2.ProxyHandler(proxies)
			opener = urllib2.build_opener(proxy_handler)
			urllib2.install_opener(opener)
			# opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299')]
		f = urllib2.urlopen(url,timeout=6)
		data = f.read()
		with open(file_name, "wb") as code:
			code.write(data)
	except urllib2.HTTPError as e:
		print('HTTPError:%s'%url)
		print(e.code)
		if e.code == 404:
			print("访问的url不存在")
		elif e.code == 456:
			print("访问被拦截")
			proxies = get_ip()
			print(proxies)
			download_from_url(url,file_name)
		# print(e.read())
	except urllib2.URLError as e:
		print('URLError:%s'%url)
		print(e)
		download_from_url(url,file_name)
	except Exception as e:
		print('error')
		print(e)

def download_from_url_headers(url,send_headers,file_name):
	try:
	    req = urllib2.Request(url, headers=send_headers)
	    f = urllib2.urlopen(req)
	    data = f.read()
	    with open(file_name, "wb") as code:
	        code.write(data)
	except urllib2.HTTPError as e:
		print('HTTPError:%s'%url)
		if e.code == 404:
			print("访问的url不存在:%s"%url)
		elif e.code == 456:
			print("访问被拦截:%s"%url)
	except urllib2.URLError as e:
		print('URLError:%s'%url)



import urllib.request as urllib2

__all__ = ['download_from_url', 'download_from_url_headers']

# send_headers = {
#     'User-Agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299',
#     'Referer':'http://www.sse.com.cn/assortment/stock/list/share/',
# }

def download_from_url(url,file_name):
    f = urllib2.urlopen(url)
    data = f.read()
    with open(file_name, "wb") as code:
        code.write(data)

def download_from_url_headers(url,send_headers,file_name):
    req = urllib2.Request(url, headers=send_headers)
    f = urllib2.urlopen(req)
    data = f.read()
    with open(file_name, "wb") as code:
        code.write(data)


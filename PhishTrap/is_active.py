import urllib3
_ACTIVE_HTTP_Codes = [ 100, 101, 200, 201, 202, 203, 204, 205, 206]
_POTENTIALLY_ACTIVE_HTTP_Codes = [000, 300, 301, 302, 303, 304, 305, 307, 403, 405, 406, 407, 408, 411, 413, 417, 418, 500, 501, 502, 503, 504, 505]

def check_active_url( url, timeout=5 ):
    #url = url.replace('\n','')
    #return url, True
     try :
         http = urllib3.PoolManager()
         r = http.request('GET', url, timeout = timeout)
         return url, r.status in _ACTIVE_HTTP_Codes or r.status in _POTENTIALLY_ACTIVE_HTTP_Codes
     except :
         return None,False
if __name__ == '__main__':
   print(check_active_url('https://onlinebanking.bancogalicia.com.ar/login',1))

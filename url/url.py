
from __future__ import with_statement                                                         
  
import contextlib 
  
from urllib.parse import urlencode           
  
from urllib.request import urlopen 

import sys 
from urllib.parse import quote_plus


def make_tiny(url): 
    #request_url = ('http://tinyurl.com/api-create.php?' + urlencode({'url':url}))
    request_url = ('http://tinyurl.com/api-create.php?url=' + quote_plus(url))
    print(request_url)   
    with contextlib.closing(urlopen(request_url)) as response:                       
        return response.read().decode('utf-8 ')     

url = make_tiny('https://www.google.com/')
print(url)
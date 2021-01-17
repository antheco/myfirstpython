import re
import urllib3
import json
http = urllib3.PoolManager()
response = http.request('GET','http://example.webscraping.com/places/default/view/India-102')
html = response.read()
text = html.decode()
json.loads(response.data.decode('utf-8'))
print(re.findall('<td class="w2p_fw">(.*?)</td>',text))
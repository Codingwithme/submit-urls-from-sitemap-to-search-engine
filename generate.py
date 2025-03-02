import re
import json
import urllib
import urllib.request
import random

site = 'https://www.gwg365.cn'
sitemaps = ['https://www.gwg365.cn/web/sitemap1.xml','https://www.gwg365.cn/web/sitemap.xml']

result = []
bingData = {}
i=0

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}  

for sitemap in sitemaps:
    sitemap = site+sitemap
    req = urllib.request.Request(url=sitemap, headers=headers)
    html = urllib.request.urlopen(req).read().decode('utf-8')
    data = re.findall(re.compile(r'(?<=<loc>).*?(?=</loc>)'), html)
    result=result+data


del result[0]


bingUrllist=[]
googleUrllist=[]

for data in result:
    i=i+1
    result.remove(data)
    # bing 提交前500条
    if i <= 500:
        bingUrllist.append(data)
    # baidu google 提交前500条
    googleUrllist.append(data)
    if i == 500:
        break

# bing 提交随机500条
bingUrllist= bingUrllist + random.sample(result,500)
# baidu google 提交随机500条
googleUrllist=googleUrllist + random.sample(result,500)

with open('urls.txt', 'w') as file:
    for data in googleUrllist:
        print(data, file=file)


bingData["siteUrl"] = site
bingData["urlList"] = bingUrllist
with open("bing.json", "w") as f:
    json.dump(bingData,f)

# with open('all-urls.txt', 'w') as file:
#     for data in result:
#         print(data, file=file)

import os
import sys
import urllib.request
import json

ID = input("NAVER API client id를 입력하세요.")
KEY = input("NAVER API client secret을 입력하세요.")


def naver_api(where,what,how): # where은 news, cafearticle, blog ... what은 찾을 검색어
    encText = urllib.parse.quote(what)

    for i in range(1,1001,100):
        # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
        url = "https://openapi.naver.com/v1/search/" +where+ "?query=" + encText + "&display=100" + "&start=" + str(i)
        
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id",ID)
        request.add_header("X-Naver-Client-Secret",KEY)
        response = urllib.request.urlopen(request)
        rescode = response.getcode()
        if(rescode==200):
            response_body = response.read()
            result = response_body.decode('utf-8')
            items = json.loads(result)['items']
            for item in items:
                f = open(f"./data/{how}","a",encoding="utf8")
                title = item['title']
                description = item['description']

                title = title.replace('<b>','')
                title = title.replace('</b>','')
                description = description.replace('<b>','')
                description = description.replace('</b>','')
                description = description.replace('...','')



                f.write(title + '\n')
                f.write(description+ '\n')
                f.close()
                

# 사용예시 : naver_api("cafearticle","첼시","첼시.txt")
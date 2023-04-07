# coding:utf-8
from bs4 import BeautifulSoup
#웹서버에 요청(통신)
import urllib.request
#특정한 주제를 필터링
import re 

#웹봇으로 크롤링을 금지
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}

#파일에 저장(r: raw string notation)
f = open(r"c:\work\todayHumor", "wt", encoding="utf-8")
for n in range(1,11): 
        data ='http://www.todayhumor.co.kr/board/list.php?table=bestofbest&page=' + str(n)
        print(data)
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, headers = hdr)
        data = urllib.request.urlopen(req).read()
        #한글이 깨지는 경우는 유니코드로 다시 해석 
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')
        list = soup.find_all('td', attrs={'class':'list-title-text'})

        for item in list:
                try:
                        title = item.find('a').text.strip()
                        if (re.search('한국', title)):
                            print(title)
                            f.write(title.strip() + "\n")
                        #print(title.strip())
#                       if (re.search('아이패드', title)):
#                                print(title.strip())
#                                f.write(title.strip() + "\n")
                except:
                        pass
        
f.close() 
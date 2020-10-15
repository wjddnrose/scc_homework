import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
scores = soup.select('#regularTeamRecordList_table > tr')

# movies (tr들) 의 반복문을 돌리기
for score in scores:
    line = ""
    #순위
    rank_tag = score.select_one('th > strong')
    if rank_tag is not None:
        line += rank_tag.text
    #구단
    title_tag = score.select_one('td.tm > div > span')
    if title_tag is not None:
        line += ", "
        line += title_tag.text
    #평점
    point_tag = score.select_one('td > strong')
    if point_tag is not None:
        line += ", "
        line += point_tag.text

        # a의 text를 찍어본다.
        print(line)


        # regularTeamRecordList_table > tr:nth-child(1) > th > strong
        # regularTeamRecordList_table > tr:nth-child(1) > td.tm > div > img
        # #regularTeamRecordList_table > tr:nth-child(1) > td:nth-child(7) > strong

        ##dddd
        #####ddd
##asdf
##aaaaaa
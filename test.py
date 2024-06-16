# 구구단 출력 코드
pip install requests beautifulsoup4

for i in range(2, 10):  # 2단부터 9단까지
    print(f"{i}단:")
    for j in range(1, 10):  # 각 단의 1부터 9까지
        print(f"{i} x {j} = {i * j}")
    print()  # 각 단 사이에 빈 줄 추가

print ('구구단 출력 완료했습니다!')

import requests
from bs4 import BeautifulSoup

# 크롤링할 웹 페이지 URL
url = 'https://example.com'

# 웹 페이지 요청
response = requests.get(url)

# 요청이 성공했는지 확인
if response.status_code == 200:
    # 페이지 내용을 파싱
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 페이지 제목 가져오기
    title = soup.title.string
    print(f'페이지 제목: {title}')
else:
    print(f'요청 실패: {response.status_code}')

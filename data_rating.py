# 신용평가 3사(한국신용평가, 한국기업평가, 나이스신용평가)에서 신용등급 가져오기
# url_kis="https://www.kisrating.com/ratingsSearch/effective_ratingExcel.do"
# url_kr="http://www.rating.co.kr/disclosure/QDisclosure018ExcelAll.do"
# url_nice="https://www.nicerating.com/disclosure/validRatingListExcelPoi.do?cmpCd=&gubun=&searchType=&searchText="
# user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"

import requests
import pandas as pd
from io import BytesIO
import openpyxl

# user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
# headers={'user-agent':user_agent}
# url_kis="https://www.kisrating.com/ratingsSearch/effective_ratingExcel.do"
# res_kis=requests.get(url_kis, headers=headers)
# output_kis=BytesIO(res_kis.content)
# table_kis=pd.read_csv(output_kis)
# print(table_kis)

user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"
headers={'user-agent':user_agent}
url_kr="http://www.rating.co.kr/disclosure/QDisclosure018ExcelAll.do"
res_kr=requests.get(url_kr, headers=headers)
res_kr.raise_for_status()
output_kr=BytesIO(res_kr.content)
table_kr=pd.read_excel(output_kr, header=None)
print(table_kr)

# 엑셀 파일 불러와서 작업하는건 실패: pandas parser error

# import requests
# import re
# import pandas as pd
# from io import BytesIO
# from bs4 import BeautifulSoup

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

# url_kis="https://www.kisrating.com/ratingsSearch/effective_rating.do"
# res_kis=requests.get(url_kis, headers=headers)
# res_kis.raise_for_status()
# # html_kis=BytesIO(res_kis.content)
# # dataset_kis=pd.read_html(html_kis)
# # print(dataset_kis)
# # 깔끔하게 안 나와서 한번에 받을 수는 없음

# soup=BeautifulSoup(res_kis.text, "lxml")
# table_kis=soup.find("table", attrs={"id":"table1"})
# print(table_kis)

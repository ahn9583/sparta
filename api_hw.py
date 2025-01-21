import pandas as pd
import requests
from google.colab import userdata

api_key = userdata.get("Service_Key")

url = f"http://apis.data.go.kr/1741000/EarthquakeIndoors3/getEarthquakeIndoors3List?serviceKey={api_key}&pageNo=1&numOfRows=100&type=xml"

response = requests.get(url).content

df = pd.read_xml(response, xpath = "//row")

df.rename(columns = {"arcd" : "지역코드",
                     "acmdfclty_sn" : "시설일련번호",
                     "ctprvn_nm" : "시도명",
                     "sgg_nm" : "시군구명",
                     "vt_acmdfclty_nm" : "지진겸용 임시주거시설명",
                     "rdnmadr_cd" : "도로명주소코드",
                     "bdong_cd" : "법정동코드",
                     "hdong_cd" : "행정동코드",
                     "dtl_adres" : "지번주소",
                     "fclty_ar" : "시설면적",
                     "xcord" : "경도",
                     "ycord" : "위도",
                     "mngps_nm" : "관리부서",
                     "mngps_telno" : "관리기관전화번호",
                     "acmdfclty_dtl_cn" : "지진겸용 임시주거시설 상세시설명",
                     "rn_adres" : "도로명주소",
                     "mngdpt_nm" : "관리기관명",
                     "vt_acmd_psbl_nmpr" : "최대수용인원수"}, inplace = True)
df.head()

# 찾아야할 데이터 --> 상품명, 규격, 가격, 상품정보(속성)
import os
import requests
import json
from extraction_sheet_data.get_sheet_range.excel_parsing import sheet_extraction
from extraction_sheet_data.get_sheet_range.monkey_patch import monkey_patch_openpyxl
from extraction_sheet_data.extraction_sheet_data import valid_cell_extraction
from extraction_product_data.extraction_product_data import get_product_data

# 엑셀 파일들이 들어있는 디렉토리의 이름 / 경로
EXCELS_DIR_NAME = 'excel_files'

EXCELS_DIR_PATH = f"{os.getcwd()}/product_data/{EXCELS_DIR_NAME}/"

excel_files_list = os.listdir(EXCELS_DIR_PATH)

excel_files_list.remove('.DS_Store')

headers = {
        'Content-type': 'application/json',
        'Accept' : 'text/html',
        'charset': 'UTF-8'
}

url = 'http://127.0.0.1:8000/products/'

body = {
        'name': '',
        'attribute': '',
        'brand': '',
        'price': 0,
        'code_number': ''
        }


if __name__ == "__main__":

        monkey_patch_openpyxl()
        # 다운로드한 엑셀파일에 있는 데이터 접근 --> 각 시트들을 파싱한 객체와 해당 시트의 범위에 대한 정보, 메인 브랜드이름 리턴

        excels_data = sheet_extraction(excel_files_list, EXCELS_DIR_PATH)

        # 각 시트마다 데이터 추출을 시작할 셀 위치와 해당 시트의 특성을 담은(브랜드, 마지막행숫자) 리스트 반환
        sheets_data = valid_cell_extraction(excels_data)
        for i in sheets_data:
                print(i)
        # parse_sheets_data를 기반으로 공산품 데이터 파싱
        products_data = get_product_data(sheets_data)
        for i in products_data:
                for j in i:
                        for key, value in j.items():
                                body[key] = value
                        response = requests.post(url, data=json.dumps(body), headers=headers)
                        print(response.status_code)
                        body["code_number"] = ''


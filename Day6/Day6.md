# 1. OCR(Optical Character Recognition)
* 광학 문자 인식
* 이미지나 문서에서 텍스트를 자동으로 인식하고 컴퓨터가 이해할 수 있는 텍스트 데이터로 변환하는 프로세스

# 2. 테서렉트(Tesseract)
* 오픈 소스 OCR 라이브러리로 구글에서 개발하고 현재는 여러 커뮤니티에 의해 유지보수
* https://github.com/UB-Mannheim/tesseract/wiki 에서 tesseract-ocr-w64-setup-5.3.1.20230401.exe 를 다운로드(2023.07.31 기준)
* 설치중 - Choose Components에서 additional scriptdata(download) 트리를 내려 Hangul script와 Hangul vertical script를 체크. Additional language data(download)에서 koran을 체크
* C:\Program Files\Tesseract-OCR 에 설치
* 환경 설정
    * 탐색기 -> "내 PC"에서 마우스 오른쪽 버튼 클릭 "속성"을 선택 -> 창을 최대화한 후 우특 메뉴 "고급 시스템 설정"을 클릭 -> "환경 변수" 버튼 클릭 -> 시스템 변수에서 "path"를 선택하고 "편집" 버튼을 클릭 -> "새로 만들기" 버튼을 클릭 -> 테서렉트 설치 경로를 추가(C:\Program Files\Tesseract-OCR)


### 금요일 오전 발표 과제
- EasyOCR
- PaddleOCR
- 등등..
- 3개 이상의 라이브러리 또는 API를 이용해서 OCR 프로젝트를 개발
- (차량번호인식, 간판, 주민등록증, 운전면허증 ...)
- 각 라이브러리 또는 API의 장단점 비교 분석
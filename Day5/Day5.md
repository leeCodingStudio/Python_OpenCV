# 1. 필터링
- 커널(filter)이라고 하는 행렬을 정의하고, 이 커널을 이미지 위에서 이동시켜가면서 커널과 겹쳐진 이미지 영역과 연산을 한 후, 그 결과값을 연산을 진행한 이미지 픽셀을 대신하여 새로운 이미지를 만드는 연산
  - filter2D(영상, 이미지깊이, 커널, 중심점 좌표, 추가될 값, 가장자리 화소 처리)
    - 이미지깊이: -1(입력과 동일)
    - 커널 행렬: 3*3, 5*5 ...
    - 가장자리 화소 처리
      - BORDER_CONSTANT: 000픽셀픽셀픽셀픽셀000
      - BORDER_REPLICATE: aaaabcdefgggg
      - ...

# 2. 블러링(BLurring)
- 초점이 맞지 않은듯 영상을 흐릿하게 하는 작업
- 평균 블러링
  - 가장 일반적인 블러링 방법으로 균일한 값을 정규화 된 커널을 이용한 이미지 필터링 방법
  - 커널 영역 내에서 평균 값으로 해당 픽셀을 대체함
  - 주변 픽셀들의 평균값을 적용하면 픽셀 간 차이가 적어져 선명도가 떨어져 전체적으로 흐려짐
  - 필터의 크기가 클수록 평균 블러링을 적용했을 때 선명도가 떨어짐
    - cv2.blur(영상, 커널)
- 가우시안 블러링
  - 가우시안 분포를 갖는 커널로 블러링 하는 것(정규 분포, 평균 근처에 몰려 있는 값들의 개수가 많고 평균에서 멀어질수록 그 개수가 적어지는 분포)
  - 대상 픽셀에 가까울수록 많은 영향을 주고, 멀어질수록 적은 영향을 주기 때문에 원래의 영상과 비슷하면서도 노이즈를 제거하는 효과가 있음
    - cv2.GaussianBlur(영상, 출력영상, 커널)
      - 출력영상: (0, 0)이면 입력 영상과 같음
      - 커널: 예) 3, 3*3
- 미디언 블러링
  - 커널의 픽셀 값 중 중앙값을 선택
  - 소금-후추 잡음을 제거하는 효과
    - cv2.medianBlur(영상, 커널)

- 바이레터럴 필터(Bilateral Filter)
  - 기존 블러리의 문제점(잡음을 제거하는 효과는 뛰어났지만, 경계도 흐릿하게 만드는 문제)을 개선하기 위해 나온 필터링 기법
  - 경계도 뚜렷하고 노이즈도 제거되는 효과가 있지만 속도가 느리다는 단점이 존재
  - cv2.bilateralFIlter(영상, 픽셀의 거리, 시그마컬러, 시그마스페이스)
    - 픽셀의 거리: -1을 입력하면 자동 결정됨
    - sigmaColor: 색공간의 시그마 값
    - sigmaSpace: 좌표공간의 시그마 값(값이 그면 멀리 떨어져 있는 픽셀들이 서로 영향을 미침)

# 3. 에지(edge) 검출
- 영상에서 화소의 밝기가 급격하게 변하는 부분
- 물체의 윤곽선(경계선)이 해당
- 예지를 검출할 수 있으면 물체의 윤곽선을 알 수 있음
- "캐니 에지 검출" 상당한 수준으로 에지를 신뢰성 있게 검출하는 방법
  - 노이즈 제거: 5*5 가우시안 블러링 필터
  - 경계 그레디언트 방향 계산: 소벨 필터로 경계 및 그레디언트 방향 검출
  - 비최대치 억제: 그레디언트 방향에서 검출된 경계 중 가장 큰 값만 선택하고 나머지는 제거
  - 이력 스레시 홀딩: 두 개의 경계 값(Max, Min)을 지정해서 경계 영역에 있는 픽셀들 중 큰 경계 값(Max) 밖의 픽셀과 연결성이 없는 픽셀 제거
    - cv2.Canny(영상, 최소 임계값, 최대임계값, 커널)

### 문제
- 웹캠 영상에서 스페이스바를 누를 때마다 "일반영상", "가우시안 필터영상", "케니 필터영상"으로 변환되는 프로그램을 작성

# 4. 모폴로지 처리
- 영상의 밝은 영역이나 어두운 영역을 축소, 확대하는 기법
- 모폴리 구조 요소를 생성
  - cv2.getStructuringElement(구조 요소의 모양, 사이즈)
    - 구조 요소의 모양
      - cv2.MORPH_RECT: 사각형
      - cv2.MORPH_ELLIPSE: 타원형
      - cv2.MORPH_CROSS: 십자형

### 4-1. 침식(erosion) 연산
- 이미지를 깎아 내는 연산
- 객체 크기는 감소하고 배경은 확대
- 작은 크기의 객체(잡음)제거 효과가 있음
  - cv2.erode(영상, 구조 요소, 출력 영상, 고정점 위치)

### 4-2. 팽창(dilation) 연산
- 물체의 주변을 확장하는 연산
- 팽창 연산은 객체 외곽을 확대시키는 연산
- 객체 크기는 증가되고 배경은 감소
- 객체 내부의 홀이 있다면 홀이 채워지는 효과
  - cv2.dilate(영상, 구조요소, 출력영상, 조정점 위치)


> 침식은 어두운 부분의 노이즈를 제거하는 효과
> 
> 팽창은 밝은 부분의 노이즈를 제거하는 효과
> 
> 노이즈 제거 효과는 좋으나, 원래 모양이 홀쭉해지거나 뚱뚱해지는 변형이 일어남

### 4-3. 열림(Opening) 연산
- 팽창 연산과 침식 연산의 조합
- 침식 연산을 적용한 다름, 팽창 연산을 적용
- 침식 연산으로 인해 밝은 영역이 줄어들고, 어두운 영역이 늘어남
- 객게의 크기 감소를 원래대로 복구 할 수 있음

### 4-4. 닫힘(Closing) 연산
- 팽창 연산과 침식 연산의 조합
- 팽창 연산을 적용한 다음, 침식 연산을 적용
- 어두운 영역이 줄어들고 밝은 영역이 늘어남
- 늘어남 영역을 다시 복구하기 위해 핌식 연산을 적용하면 밝은 영역이 줄어들고 어두운 영역이 늘어남
- 객체 내부의 홀이 사라지면서 발생한 크기 즐가를 복구할 수 있음

### 4-5. 그레디언트(Gradient) 연산
- 팽창 연산과 침식 연산의 조합
- 열림 연산이나 닫힘 연산과 달리 입력 이미지에 각각 팽창 연산과 침식 연산을 적용하고 감산을 진행
  - cv2.morphologyEx(영상, 연산 방법, 구조 요소)
    - 연산 방법
      - cv2.MORPH_DILATE: 팽창 연산
      - cv2.MORPH_ERODE: 침식 연산
      - cv2.MORPH_CLOSE: 닫힘 연산
      - cv2.MORPH_GRADIENT: 그레디언트 연산

# 5. 레이블링
- 이진화, 모폴로지를 수행하면 객체와 배경 영역을 구분할 수 있게됨
- 객체 단위 분석을 통해 각 객체를 분할하여 특징을 분석하고 객체의 위치, 크기 정보, 모양 분석, ROI 추출등이 가능함
- 서로 연결되어 있는 객체 픽셀에 고유번호를 할당하여 영역 기반 모양 분석, 레이블맵, 바운딩 박스, 픽셀 개수, 무게 중심, 좌표 등을 반환할 수 있게 함
  - cv2.connectedComponents(영상, 레이블맵)
    - 레이블 맵: 픽셀 연결 관계(4방향 연결, 방향 연결)
    - return: 객체 갯수, 레이블 맵 행렬
  - cv2.connectedComponentsWithStats(영상, 레이블맵)
    - return: 객체 갯수, 레이블 맵 행렬, (객체 위치, 가로세로길이, 면적등 행렬), 무게중심 정보

# 6. 객체의 외곽선 검출
- 레이블링과 함께 영상에서 객체의 정보를 검출하는 방법 중 하나
- 이진화된 영상에서 검출되며 배경 영역과 닿아 있는 픽셀을 찾아 외곽선으로 인식
- 외곽선은 객체 외부 뿐 아니라 내부에도 생길 수 있음
  - cv2.findContours(영상, 검출모들, 외각선 좌표 근사화 방법)
    - 검출모드
      - RETR_EXTERNAL: 객체 외부 외곽선만 검출
      - RETR_LIST:객체 외부, 내부 외곽선 모두 검충
      - RETR_CCOMP: 모든 외곽선 검출, 2단계 계층 구조를 구성
      - RETR_TREE: 모든 외곽선 검충, 전체 계층 구조 구성
    - 외각선 좌표 근사화 방법
      - CHAIN_APPROX_NONE: 모든 외곽선 좌표를 저장
      - CHAIN_APPROX_SIMPLE: 외곽선 중에서 수평, 수직, 대각선 성분은 끝 점만 저장
  - cv2.drawContours(영상, 외곽선 좌표 정보, 외곽선 인덱스, 색상, 두께): 외곽선 그리기
    - 외곽선 인덱스: -1을 지정하면 모든 외곽선을 그림
  - cv2.arclength(외곽선 좌표, 폐곡선 여부): 외곽선 길이 구하기
  - cv2.contourArea(외곽선 좌표, False): 면적 구하기
  - cv2.boundungRect(외곽선 좌표): 바운딩 박스 구하기

- 외곽선 근사화
  - 검출한 윤곽선 정보를 분석하여 정점수가 적은 윤곽선 또는 다각형으로 표현할 수 있게 만드는 것
    - cv2.approxPolyDP(외곽선 좌표, 근사화 정밀도 조절, 폐곡선 여부)
      - 근사화 정밀도 조절: 입력 컨투어와 근사화된 건투어 사이의 최대 거리. 값이 작을수록 다각형이 정확해지고, 꼭지점의 수가 늘어남
    - cv2.isCoutourConvex()
      - contour에 오목한 부분이 있는지 체크(있으면 True, 없으면 False)
    - cv2.convexHull()
      - contour에 있는 오목한 부분을 제거


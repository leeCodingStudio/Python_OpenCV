import cv2
import numpy as np
points = np.array([(100, 100), (300, 100), (300, 400), (100, 400)], np.int32)
num_points = len(points)
selected_point_idx = None
selected_image = None


def draw_points(img, points):
    for i, point in enumerate(points):
        cv2.circle(img, tuple(point), 5, (0, 0, 255), -1)
        cv2.putText(img, str(i+1), tuple(point), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    for i in range(num_points):
        start_point = tuple(points[i])
        end_point = tuple(points[(i + 1) % num_points])
        cv2.line(img, start_point, end_point, (0, 255, 0), 2)


def select_point(event, x, y, flags, param):
    global points, selected_point_idx, selected_image
    if event == cv2.EVENT_LBUTTONDOWN:
        for i, point in enumerate(points):
            if abs(point[0] - x) < 10 and abs(point[1] - y) < 10:
                selected_point_idx = i
                break
    elif event == cv2.EVENT_LBUTTONUP:
        selected_point_idx = None
    elif event == cv2.EVENT_MOUSEMOVE:
        if selected_point_idx is not None:
            points[selected_point_idx] = (x, y)


def get_transformed_image():
    global selected_image
    width, height = 600, 300  # 변환된 이미지의 크기
    pts1 = [points[0], points[1], points[2], points[3]]
    pts2 = [(0, 0), (width, 0), (width, height), (0, height)]
    matrix = cv2.getPerspectiveTransform(
        src=np.float32(pts1), dst=np.float32(pts2)
    )
    result = cv2.warpPerspective(selected_image, matrix, (width, height))
    return result


def show_selected_area(image, points):
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, [points], (255, 255, 255))
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


img_path = 'namecard.jpg'  # 분석하고자 하는 이미지 경로로 바꿔주세요
img = cv2.imread(img_path)
selected_image = img.copy()
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', select_point)
while True:
    img_copy = img.copy()
    draw_points(img_copy, points)
    cv2.imshow('Image', img_copy)
    key = cv2.waitKey(1)
    if key == 13 and selected_image is not None:  # Enter 키를 누르면 선택한 영역의 이미지를 따로 표시
        transformed_img = get_transformed_image()
        cv2.imshow('Transformed Image', transformed_img)
    if key == 27 or key == ord('q'):  # 'ESC' 또는 'q'를 누르면 종료
        break
cv2.destroyAllWindows()
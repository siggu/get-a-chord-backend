'''
major / minor / 7 / 5 / dim
dim7 / aug / sus2 / sus4 / maj7
m7 / 7sus4 / maj9 / maj11 / maj13
maj9#11 / maj13#11
'''
from PIL import Image

# 이미지 불러오기
image = Image.open('images\c.png')  # 'image.jpg'를 원하는 이미지 경로로 변경하세요.

# 이미지 크기 확인
w, h = image.size

# 섹션 너비/높이 계산
section_w = w // 10
section_h = h // 10

# 섹션 이미지 저장
for i in range(10):
    # 가로 섹션
    y = 0
    for j in range(10):
        x = j * section_w
        section = image.crop((x, y, x+section_w, y+section_h))
        section.save(f'section_{i}_{j}.png')  # 파일 이름 변경 가능
        y += section_h

    # 세로 섹션 (선택 사항)
    x = 0
    for j in range(10):
        y = j * section_h
        section = image.crop((x, y, x+section_w, y+section_h))
        section.save(f'section_{i}_{j}.png')  # 파일 이름 변경 가능
        x += section_w

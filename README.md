# 집현전 카테고리 생성 프로그램

필요 외부 라이브러리: `Pillow`

## 실행

`python3 create.py`

결과물 (카테고리 + 콜라주)은 `dist/`에

## 설정

```py
config = Config(
    # PPCM = Pixel Per CeniMeter, cm당 픽셀 수 (300dpi 기준)
    canvas_size=(PPCM * 16, PPCM * 6), # 16cm x 6cm
    image_per=50, # 카테고리 아이콘 배율 (=50%)
    font_ko_per=10, # 가로 길이에 대한 한글 폰트 크기 (이미지 가로의 10%),
    font_en_per=5 # ,
    font_symbol_per=20,
    # location: (0, 0)가 좌측 위, (100, 100)가 우측 아래라고 했을때 위치
    image_location=(1, 16),
    font_ko_location=(28, 26),
    font_en_location=(29, 60),
    font_symbol_location=(85, 50),
    # (기본값) 추가 선택 인자
    (선택) font_ko = "neodgm_pro.ttf",
    (선택) font_en = "Ubuntu_MonoUbuntuMono-Regular.ttf",
    (선택) font_bound_mult = 0.8 # 글자 길이가 경계를 넘을때 줄일 크기 (80%)
    (선택) font_ko_len_bound = 8 # 한글 글꼴 크기를 줄일 글자 길이의 경계
    (선택) font_en_len_bound = 28 # 영어 글꼴 크기를 줄일 글자 길이의 경계
)
```

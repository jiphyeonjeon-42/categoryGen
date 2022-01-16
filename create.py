from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from PIL.Image import Image as Img

from utils import get_info, resized_img, show_image

Size = tuple[int, int]

PPCM = PIXEL_PER_CM = int(118.11023622)  # 300ppi
WHITE = (255, 255, 255)
CANVAS_COLOR = (174, 218, 232)
CANVAS_SIZE = (PPCM * 12, PPCM * 6)

font_ko = ImageFont.truetype("fonts/neodgm_pro.ttf", PPCM)
font_en = ImageFont.truetype(
    "fonts/Ubuntu_Mono/UbuntuMono-Regular.ttf", int(PPCM / 1.8)
)


def create_category(path: Path) -> Img:
    # 빈 캔버스 생성
    rgb, ko, en = get_info(path)
    print(rgb)
    canvas = Image.new("RGBA", CANVAS_SIZE, rgb)

    img = Image.open(path)
    img = resized_img(img, 60)

    canvas.paste(img, (0, PPCM // 2), img)

    draw = ImageDraw.Draw(canvas)
    draw.text((int(PPCM * 4), PPCM // 2), ko, font=font_ko, fill=WHITE)
    draw.text(
        (CANVAS_SIZE[0] // 2, CANVAS_SIZE[1] - PPCM), en, WHITE, font=font_en
    )

    return canvas


canvas = create_category(
    Path("category/집현전_카테고리_아이콘-300ppi-백색/01.프로그래밍 언어.png")
)

show_image(canvas, 30)

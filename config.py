from dataclasses import dataclass

from PIL import ImageFont

from utils import RGB, WHITE, Per, Size

font_ko, font_en = (
    "fonts/neodgm_pro.ttf",
    "fonts/Ubuntu_Mono/UbuntuMono-Regular.ttf",
)


@dataclass
class Config:

    image_per: int
    image_location: Per

    canvas_size: Size

    font_ko_per: float
    font_ko_location: Per

    font_en_per: float
    font_en_location: Per

    font_symbol_per: float
    font_symbol_location: Per

    font_color: RGB = WHITE

    def __post_init__(self):
        self.font_ko_ttf = ImageFont.truetype(
            font_ko, self.perw(self.font_ko_per)
        )
        self.font_ko_ttf_small = ImageFont.truetype(
            font_ko, self.perw(self.font_ko_per * 0.8)
        )
        self.font_en_ttf = ImageFont.truetype(
            font_en,
            self.perw(self.font_en_per),
        )
        self.font_en_ttf_small = ImageFont.truetype(
            font_en,
            self.perw(self.font_en_per * 0.8),
        )
        self.font_symbol_ttf = ImageFont.truetype(
            font_ko,
            self.perw(self.font_symbol_per),
        )

    def perw(self, percent: float) -> int:
        return int(self.canvas_size[0] * percent / 100)

    def per(self, percent: Per) -> Size:
        return tuple(
            [int(self.canvas_size[i] * percent[i] / 100) for i in range(2)]
        )

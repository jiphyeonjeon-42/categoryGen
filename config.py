from dataclasses import dataclass

from PIL import ImageFont

from utils import RGB, WHITE, Size, Per


@dataclass
class Config:

    image_per: int
    image_location: Per

    canvas_size: Size

    font_ko_per: float
    font_ko_location: Per

    font_en_per: float
    font_en_location: Per

    font_color: RGB = WHITE

    def __post_init__(self):
        self.font_ko_ttf = ImageFont.truetype(
            "fonts/neodgm_pro.ttf", self.perw(self.font_ko_per)
        )
        self.font_ko_ttf_small = ImageFont.truetype(
            "fonts/neodgm_pro.ttf", self.perw(self.font_ko_per * 0.8)
        )
        self.font_en_ttf = ImageFont.truetype(
            "fonts/Ubuntu_Mono/UbuntuMono-Regular.ttf",
            self.perw(self.font_en_per),
        )
        self.font_en_ttf_small = ImageFont.truetype(
            "fonts/Ubuntu_Mono/UbuntuMono-Regular.ttf",
            self.perw(self.font_en_per * 0.8),
        )

    def perw(self, percent: float) -> int:
        return int(self.canvas_size[0] * percent / 100)

    def per(self, percent: Per) -> Size:
        return tuple(
            [int(self.canvas_size[i] * percent[i] / 100) for i in range(2)]
        )

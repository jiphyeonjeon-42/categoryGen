from dataclasses import dataclass
from pathlib import Path

from PIL import ImageFont

from utils import RGB, WHITE, Per, Size

_fontpath = Path("fonts")


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

    font_color = WHITE

    font_ko = "fonts/neodgm_pro.ttf"
    font_en = "fonts/Ubuntu_Mono/UbuntuMono-Regular.ttf"
    font_ko_len_bound = 8
    font_en_len_bound = 28
    font_bound_mult: float = 0.8

    def __post_init__(self):
        ko = str(_fontpath / self.font_ko)
        en = str(_fontpath / self.font_en)
        self.font_ko_ttf = ImageFont.truetype(ko, self.perw(self.font_ko_per))
        self.font_ko_ttf_small = ImageFont.truetype(
            ko, self.perw(self.font_ko_per * self.font_bound_mult)
        )
        self.font_en_ttf = ImageFont.truetype(
            en,
            self.perw(self.font_en_per),
        )
        self.font_en_ttf_small = ImageFont.truetype(
            en,
            self.perw(self.font_en_per * self.font_bound_mult),
        )
        self.font_symbol_ttf = ImageFont.truetype(
            ko,
            self.perw(self.font_symbol_per),
        )

    def perw(self, percent: float) -> int:
        return int(self.canvas_size[0] * percent / 100)

    def per(self, percent: Per) -> Size:
        return tuple(
            [int(self.canvas_size[i] * percent[i] / 100) for i in range(2)]
        )

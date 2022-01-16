from pathlib import Path

from PIL import Image, ImageDraw
from PIL.Image import Image as Img

from config import Config
from utils import BLACK, get_info, resized_img


class Category:
    def __init__(self, path: Path, config: Config) -> None:
        self.path = path
        self.name = path.name
        self.rgb, self.ko, self.en = get_info(path)
        self.conf = config
        self.img = Image.open(path)

        self.canvas = self.render()

    def render(self) -> Img:
        canvas = Image.new("RGBA", self.conf.canvas_size, self.rgb)
        img = resized_img(self.img, 60)

        canvas.paste(img, self.conf.per(self.conf.image_location), img)

        draw = ImageDraw.Draw(canvas)

        draw.text(
            xy=self.conf.per(self.conf.font_ko_location),
            text=self.ko,
            font=self.conf.font_ko_ttf
            if len(self.en) < 8
            else self.conf.font_ko_ttf_small,
            fill=self.fontcolor,
        )
        draw.text(
            xy=self.conf.per(self.conf.font_en_location),
            text=self.en,
            font=self.conf.font_en_ttf
            if len(self.en) < 28
            else self.conf.font_en_ttf_small,
            fill=self.fontcolor,
        )

        return canvas

    def save(self):
        self.canvas.save(f"dist/{self.name}")

    @property
    def fontcolor(self):
        if all([br > 200 for br in self.rgb]):
            return BLACK
        return self.conf.font_color

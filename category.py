from pathlib import Path

from PIL import Image, ImageDraw
from PIL.Image import Image as Img

from config import Config
from utils import BLACK, get_info, resized_img
from aiopath import AsyncPath
from io import BytesIO
class Category:
    def __init__(self, path: Path, config: Config) -> None:
        self.path = path
        self.name = path.name
        self.rgb, self.ko, self.en, self.symbol = get_info(path)
        self.conf = config
        self.img = Image.open(path)

        self.canvas = self.render()

    def render(self) -> Img:
        canvas = Image.new("RGBA", self.conf.canvas_size, self.rgb)
        txt = Image.new("RGBA", self.conf.canvas_size, self.rgb)

        img = resized_img(self.img, 60)

        draw = ImageDraw.Draw(txt)
        draw.text(
            xy=self.conf.per(self.conf.font_symbol_location),
            text=self.symbol,
            font=self.conf.font_symbol_ttf,
            fill=(*self.fontcolor, 64),
        )
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

        result = Image.alpha_composite(canvas, txt)
        result.paste(img, self.conf.per(self.conf.image_location), img)
        return result

    async def save(self):
        buffer = BytesIO()
        self.canvas.save(buffer, format="PNG")
        async with AsyncPath(f"dist/{self.name}").open("wb") as f:
            await f.write(buffer.getbuffer())


    @property
    def fontcolor(self):
        if all([br > 200 for br in self.rgb]):
            return BLACK
        return self.conf.font_color

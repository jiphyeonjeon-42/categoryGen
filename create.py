from asyncio import gather, run
from pathlib import Path

from aiopath import AsyncPath

from category import Category
from collage import create_collage
from config import Config

PPCM = PIXEL_PER_CM = int(118.11023622)  # 300ppi

config = Config(
    canvas_size=(PPCM * 16, PPCM * 6),
    image_per=50,
    font_ko_per=10,
    font_en_per=5,
    font_symbol_per=20,
    image_location=(1, 16),
    font_ko_location=(28, 26),
    font_en_location=(29, 60),
    font_symbol_location=(85, 50),
)

from time import time


async def save_img(path: Path):
    category = Category(path=path, config=config)
    await category.save()


async def main():
    await gather(*[save_img(path) for path in Path("icons").glob("**/*.png")])

if __name__ == "__main__":
    start = time()
    run(main())
    print(f"{(time() - start):.2f}s")

    # create_collage().save(Path("dist/collage.png"))

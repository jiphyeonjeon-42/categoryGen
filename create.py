from asyncio import gather, run
from pathlib import Path
from time import time

from category import Category
from collage import create_collage
from config import Config
from utils import PPCM


async def save_img(path: Path):
    Category(path=path, config=config).save()


async def main():
    Path('dist').mkdir(exist_ok=True)
    res = await gather(
        *[save_img(path) for path in Path("icons").glob("**/*.png")]
    )
    print(f"이미지 {len(res)}개 처리됨")
    create_collage()
    print("콜라주 생성 완료")


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

if __name__ == "__main__":
    start = time()
    run(main())
    end = time()
    print(f"took {end - start:.2f}s")

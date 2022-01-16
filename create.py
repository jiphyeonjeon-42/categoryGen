import asyncio
from pathlib import Path

# from aio
from category import Category
from config import Config
from collage import create_collage

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


def main():
    category_path = Path("category/집현전_카테고리_아이콘")
    for path in category_path.glob("**/*.png"):
        Category(path=path, config=config).save()

    create_collage().save(Path("dist/collage.png"))


if __name__ == "__main__":
    main()

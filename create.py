from pathlib import Path

from category import Category
from config import Config

PPCM = PIXEL_PER_CM = int(118.11023622)  # 300ppi

config = Config(
    canvas_size=(PPCM * 16, PPCM * 6),
    image_per=50,
    font_ko_per=10,
    font_en_per=5,
    image_location=(3, 16),
    font_ko_location=(30, 26),
    font_en_location=(31, 60),
)


def main():
    category_path = Path("category/집현전_카테고리_아이콘")
    for path in category_path.glob("**/*.png"):
        Category(path=path, config=config).save()


if __name__ == "__main__":
    main()

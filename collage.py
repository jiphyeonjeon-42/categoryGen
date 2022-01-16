from pathlib import Path

from PIL import Image
from PIL.Image import Image as Img

from utils import WHITE, show_image

dist = Path("dist")
savepath = dist / "collage.png"
wh = (400, 150)
canvas_wh = (wh[0] * 4, wh[1] * 4)

def create_collage(path: Path = dist):
    imgs = [Image.open(f) for f in path.glob("*.png") if f != dist / "collage.png"]
    thumbnails = [img.resize(wh) for img in imgs]

    canvas = Image.new("RGBA", canvas_wh, WHITE)

    for i, img in enumerate(thumbnails):
        canvas.paste(img, (i % 4 * wh[0], i // 4 * wh[1]))

    return canvas

if __name__ == "__main__":
    canvas = create_collage()
    canvas.save(savepath)
    show_image(canvas)

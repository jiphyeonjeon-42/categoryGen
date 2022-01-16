import json
import tkinter
from tkinter import Tk
from pathlib import Path

from PIL import Image, ImageFont, ImageTk
from PIL.Image import Image as Img

RGB = tuple[int, int , int]

with Path("data.json").open("r") as f:
    data = json.load(f)


def resized_img(img, per):
    new_size = (img.width * per // 100, img.height * per // 100)
    if new_size == img.size:
        return img
    return img.resize(new_size, Image.HAMMING)


def show_image(img: Img, per: int = 100):
    root = Tk()
    render = ImageTk.PhotoImage(resized_img(img, per))
    label = tkinter.Label(root, image=render)
    label.pack()
    root.mainloop()

def get_info(path: Path) -> tuple[RGB, str, str]:
    res = data.get(path.name)
    return tuple(res["rgb"]), res["ko"], res["en"]

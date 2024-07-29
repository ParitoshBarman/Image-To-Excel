# pip install image-to-excel
from image_to_excel import BaseClass
from pathlib import Path

img = "Picsart_24-07-28_11-06-51-776.jpg"

app = BaseClass("config.yml")

app.image_to_excel(
    Path(img), 100, Path("output.xlsx")
)
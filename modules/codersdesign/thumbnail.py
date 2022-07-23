import os
import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageFont


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def thumb(thumbnail, title, userid):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open(f"resource/thumb{userid}.png", mode="wb")
                await f.write(await resp.read())
                await f.close()
    image1 = Image.open(f"resource/thumb{userid}.png")
    image2 = Image.open("resource/telugucodersvplay.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save(f"resource/temp{userid}.png")
    img = Image.open(f"resource/temp{userid}.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("resource/Roboto-Regular.ttf", 50)
    font2 = ImageFont.truetype("resource/Roboto-Medium.ttf", 72)
    draw.text(
        (25, 615),
        f"{title[:20]}...",
        fill="white",
        font=font2,
    )
    draw.text(
        (27, 543),
        f"Now Playing",
        fill="red",
        font=font,
    )
    img.save(f"resource/final{userid}.png")
    os.remove(f"resource/temp{userid}.png")
    os.remove(f"resource/thumb{userid}.png")
    final = f"resource/final{userid}.png"
    return final

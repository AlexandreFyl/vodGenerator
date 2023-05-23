from PIL import Image, ImageDraw, ImageFont

REGULAR_FONT = 'assets/fonts/Roboto-Regular.ttf'
BOLD_FONT = 'assets/fonts/Roboto-Bold.ttf'
FONT_COLOR = "#969892"


def generateFirstImage(champName, patchVersion):
    # Look to be the best dimensions for full screen phone content in portrait mode nowadays
    # We use a white background for the moment
    firstImg = Image.new("RGBA", (1080, 1920), "white")

    # We load the champion loading screen img, resize it and place it ideally on the generated img
    champLoadingScreenImg = Image.open(
        "assets/temp/champ/champion-loading-screen-picture.jpg")
    champLoadingScreenImg = champLoadingScreenImg.resize((604, 1096))
    firstImg.paste(champLoadingScreenImg, (238, 108))

    # We generate needed texts
    # We remove the unsused part returned by API
    troncatedPatchVersion = patchVersion.rsplit(".", 1)[0]

    # We format our txt and font sizes / weights
    text1 = champName
    text2 = "Build"
    text3 = "Patch " + troncatedPatchVersion

    font1 = ImageFont.truetype(BOLD_FONT, 140)  # for champ name
    font2 = ImageFont.truetype(REGULAR_FONT, 60)  # for the rest

    # We create a draw linked to our img
    draw = ImageDraw.Draw(firstImg)

    # We place our txts
    width, height = firstImg.size
    textwidth, textheight = draw.textsize(text1, font1)
    x1 = width/2-textwidth/2
    textwidth, textheight = draw.textsize(text2, font2)
    x2 = width/2-textwidth/2
    textwidth, textheight = draw.textsize(text3, font2)
    x3 = width/2-textwidth/2

    draw.text((x1, 1350), text1, font=font1, fill='black')
    draw.text((x2, 1510), text2, font=font2, fill='black')
    draw.text((x3, 1680), text3, font=font2, fill='black')

    firstImg.show()

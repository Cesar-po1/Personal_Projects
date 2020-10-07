from PIL import Image, ImageDraw, ImageFont
# get an image
foto= input('nombre de la foto? ')

color_image = Image.open(foto+'.jpeg')

bw_image = color_image.convert('L')
    
base = bw_image.convert('RGBA')

# make a blank image for the text, initialized to transparent text color
txt = Image.new('RGBA', base.size, (255,255,255,0))
print(color_image.size)
# get a font
fnt = ImageFont.truetype('waltographUI.ttf', 30)
# get a drawing context
d = ImageDraw.Draw(txt)

# draw text, half opacity
d.text((170,300),"message", font=fnt, fill=(200,140,0,105))
# draw text, full opacity
d.text((190,350), "text", font=fnt, fill=(0,250,150,105))
# draw text, full opacity
d.text((350,400), "-Cesar", font=fnt, fill=(105,80,100,100))

out = Image.alpha_composite(base, txt)
out.save('imageNewName.png')
out.show('imageNewName.png')
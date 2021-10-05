from captcha.image import ImageCaptcha  #pip install captcha
from random import randrange

image=ImageCaptcha(width=280, height=90)

captcha_text=str(randrange(9999,99999))

data=image.generate(captcha_text)

image.write(captcha_text,"Captcha.png")

print("Captcha generado correctamente")

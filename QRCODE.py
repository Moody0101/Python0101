import qrcode

img = qrcode.make("Love is good")
img.save('qr.png', 'PNG')
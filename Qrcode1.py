import qrcode as qr
img= qr.make("Enter link or any text that you want to scan .. ")
img.save("image.jpg")
import qrcode
#qr=qrcode.make("www.adityabakare.cf")
#qr.save('myQR.png')
qr=qrcode.QRCode(
    version=1,
    box_size=15,
    border=5

)
data='www.adityabakare.cf'
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black', back_color='white')
img.save('abc.jpg')


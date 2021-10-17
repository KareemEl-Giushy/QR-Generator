from os import mkdir, path
from json import dumps
import qrcode
import csv
from PIL import Image

tdir = __file__.split('\\')
tdir.pop(-1)
tdir = '\\'.join(tdir)
qrFile = tdir + '\\qrcodes'

logo = Image.open(tdir + '\\logo.png')

with open(tdir + '\\data.csv', newline='') as d:
    reader = csv.reader(d)
    reader
    for i, row in enumerate(reader):
        if i == 0:
            continue
        qr = qrcode.QRCode(
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=4,
            border=1
        )
        row.append('GDG Damanhour')
        qr.add_data(dumps({
            "firstname": row[0],
            "lastname":row[1],
            "email": row[2],
            "phone": row[3],
            "gdg": "GDG Damanhour"
        }))
        # qr.add_data('FirstName: ' + row[0]) #To Make It Look Better (not efficient when retrieving data)
        img = qr.make_image(fill_color='black', back_color='white')
        img = img.convert('RGBA')
        w, h = img.size
        logo_size = 100
        xmin = ymin = int(w / 2) - int(logo_size / 2)
        xmax = ymax = int(w / 2) + int(logo_size / 2)
        logo = logo.resize((xmax - xmin, ymax - ymin))
        img.paste(logo, (xmin, ymin, xmax, ymax), logo)
        
        if not path.isdir(qrFile):
            mkdir(qrFile)
        pa = qrFile + '\\qr_' + row[0].lower() + '_' + row[3] + '.png'
        img.save(pa)

print('Completed ...')
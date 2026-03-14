import qrcode

from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.Error_handle_H,
                   box_size=10,
                   border=4,)
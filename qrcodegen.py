import qrcode
from PIL import Image

def create_qr_with_logo(url, logo_path, output_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color='black', back_color='white').convert('RGBA')
    logo = Image.open(logo_path).convert("RGBA")

    white_bg = Image.new("RGBA", logo.size, "WHITE")
    white_bg.paste(logo, (0, 0), logo)
    logo = white_bg

    logo_size = min(qr_img.size[0] // 3, qr_img.size[1] // 3)  # try not to go below 3 as only 30% reduncancyt in qr code
    logo.thumbnail((logo_size, logo_size), Image.LANCZOS)
    logo_position = ((qr_img.size[0] - logo_size) // 2, (qr_img.size[1] - logo_size) // 2)
    qr_img.paste(logo, logo_position, logo)
    qr_img.save(output_path)



create_qr_with_logo('https://diamondi23.anvil.app', '/Users/vwg85559/Downloads/P12M.png', './P12MQR.png')
create_qr_with_logo('https://www.diamond.ac.uk/Instruments/Mx/I23', 'dls.png', 'dlsqr.png')
create_qr_with_logo('https://www.nature.com/articles/s42004-023-01014-0', '/Users/vwg85559/Downloads/pub.png', 'pubqr.png')


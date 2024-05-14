import qrcode

def generate_qr_code(link, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)

# Exemplo de uso
link = input("Link: ")
output_file = "qr_code.png"
generate_qr_code(link, output_file)
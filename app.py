import qrcode
# from qrcode.image.styledpill import StyledPilImage
# from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
# from qrcode.image.styles.colormasks import RadialGradiantColorMask


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Djemeleza')
qr.make(fit=True)

img = qr.make_image(back_color="red", fill_color="green")
img.save('qrcode001.png')

# img_1 = qr.make_image(image_factory=StyledPilImage,
#                       module_drawer=RoundedModuleDrawer())
# img_2 = qr.make_image(image_factory=StyledPilImage,
#                       color_mask=RadialGradiantColorMask())
# img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="/path/to/image.png")

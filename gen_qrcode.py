import qrcode


def generate_qr_code(data, file_name, pixel_size=240):
    """
    Generate a QR code from the given data and save it to a file.

    Parameters:
        data (str): The data to encode into the QR code.
        file_name (str): The name of the file to save the QR code image to.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=pixel_size,
        # box_size=10,
        # border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code instance
    qr_img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    qr_img.save(file_name)

# Example usage:
data_to_encode = "https://example.com"
output_file = "example_qr_code.png"
generate_qr_code(data_to_encode, output_file)

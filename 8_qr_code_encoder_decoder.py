import qrcode
from pyzbar.pyzbar import decode
from PIL import Image

# Generate QR Code
def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrcode.png")
    print("QR code generated and saved as 'qrcode.png'.")
    return img

# Decode QR Code
def decode_qr_code(image_path):
    img = Image.open(image_path)
    decoded_object = decode(img)
    for obj in decoded_object:
        print(f"Decoded Data: {obj.data.decode('utf-8')}")


while True:
    choice = input("Do you want to generate a QR code (g) or decode an existing QR code (d)? (g/d): ").lower()
    if choice == 'g':
        data = input("Enter the data to encode in the QR code: ")
        print(f"Data to encode: {data}")
        print("Generating QR code...")
        generate_qr_code(data)
        break
    elif choice == 'd':
        image_path = input("Enter the path to the QR code image: ")
        decode_qr_code(image_path)
        break
    else:
        print("Invalid choice. Please enter 'g' to generate or 'd' to decode.")
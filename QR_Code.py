#pip install qrcode[pil]

import qrcode
print("---- QR Code Generator ----")
data = input("Enter Text or URL: ")
img = qrcode.make(data)
file_name = input("Enter File Name(without .png): ")
img.save(file_name + ".png")
print("\n QR Code Generated Successfully!")
print(f"Saved as: {file_name}.png")
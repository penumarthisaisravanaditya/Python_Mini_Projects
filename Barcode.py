# pip install python-barcode pillow

import barcode
from barcode.writer import ImageWriter

data = input("Enter the data to generate barcode: ")
barcode_format = input(
    "Enter the barcode format (e.g., 'code128', 'ean13', 'upc'): "
).lower()

barcode_file = input(
    "Enter the filename to save the barcode (without extension): "
)

if barcode_format not in ["code128", "ean13", "upc"]:
    print("Unsupported barcode format.")
else:
    try:
        # EAN-13 requires numbers only
        if barcode_format == "ean13":
            if not data.isdigit():
                print("Error: EAN-13 can contain numbers only.")
            elif len(data) not in [12, 13]:
                print("Error: EAN-13 requires 12 or 13 digits.")
            else:
                barcode.get(
                    barcode_format,
                    data,
                    writer=ImageWriter()
                ).save(barcode_file)

                print(f"Barcode generated and saved as '{barcode_file}.png'.")

        # UPC requires numbers only
        elif barcode_format == "upc":
            if not data.isdigit():
                print("Error: UPC can contain numbers only.")
            else:
                barcode.get(
                    barcode_format,
                    data,
                    writer=ImageWriter()
                ).save(barcode_file)

                print(f"Barcode generated and saved as '{barcode_file}.png'.")

        # Code 128 supports text
        elif barcode_format == "code128":
            barcode.get(
                barcode_format,
                data,
                writer=ImageWriter()
            ).save(barcode_file)

            print(f"Barcode generated and saved as '{barcode_file}.png'.")

    except Exception as e:
        print(f"Error: {e}")
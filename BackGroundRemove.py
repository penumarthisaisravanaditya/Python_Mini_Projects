#pip install "rembg[cpu]" pillow
from PIL import Image
from rembg import remove

# Load the image
name_input = input("Enter the name of the input image (with extension): ")
image = Image.open(name_input)
# Remove the background
output_image = remove(image)
# Save the output image
name_output = input("Enter the name of the output image (without extension): ")
output_image.save(f"{name_output}.png")
print(f"Background removed and saved as {name_output}.png")
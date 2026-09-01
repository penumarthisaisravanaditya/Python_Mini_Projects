from PIL import Image
image = Image.open("input2.jpeg")
image = image.convert("L")  # Convert to grayscale
width, height = image.size
new_width = 100
new_height = int((height / width) * new_width/2)
image = image.resize((new_width, new_height))
characters = "@%#*+=-:. "
pixels = image.getdata()

for y in range(new_height):
    for x in range(new_width):
        pixel_value = pixels[y * new_width + x]
        character = characters[pixel_value * len(characters) // 256]
        print(character, end="")
    print()
    
# Image
#   ↓
# Grayscale
#   ↓
# Resize
#   ↓
# Get pixel brightness
#   ↓
# Map brightness to characters
#   ↓
# Print ASCII art
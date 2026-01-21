from pdf2image import convert_from_path
from PIL import Image
import sys

pdf_path = sys.argv[1] if len(sys.argv) > 1 else 'poster.pdf'
output_path = sys.argv[2] if len(sys.argv) > 2 else 'poster_9pages.pdf'

# Convert PDF to image at 300 DPI
print("Converting PDF to image...")
img = convert_from_path(pdf_path, dpi=300)[0]
w, h = img.size
print(f"Image size: {w} x {h}")

# A4 at 300 DPI
a4_w, a4_h = 2480, 3508
tile_w, tile_h = w // 3, h // 3

tiles = []
for row in range(3):
    for col in range(3):
        tile = img.crop((col * tile_w, row * tile_h, 
                         (col + 1) * tile_w, (row + 1) * tile_h))
        
        # Fit to A4
        ratio = min(a4_w / tile_w, a4_h / tile_h)
        new_size = (int(tile_w * ratio), int(tile_h * ratio))
        tile_resized = tile.resize(new_size, Image.LANCZOS)
        
        # Center on A4
        page = Image.new('RGB', (a4_w, a4_h), 'white')
        page.paste(tile_resized, ((a4_w - new_size[0]) // 2, 
                                   (a4_h - new_size[1]) // 2))
        tiles.append(page)
        print(f"Tile {row*3 + col + 1}/9")

tiles[0].save(output_path, save_all=True, append_images=tiles[1:], resolution=300)
print(f"Saved {output_path}")

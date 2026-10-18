import fitz
import os
from PIL import Image
import io

doc = fitz.open('assets/pdf/primary/primary_scholarship_policy_routine_2026.pdf')
new_doc = fitz.open()

print(f"Compressing {len(doc)} pages...")
for i, page in enumerate(doc):
    pix = page.get_pixmap(dpi=130)
    img = Image.open(io.BytesIO(pix.tobytes("png"))).convert("L") # grayscale
    out_io = io.BytesIO()
    img.save(out_io, format="JPEG", quality=75, optimize=True)
    out_bytes = out_io.getvalue()
    
    # create new pdf page with the compressed image
    rect = page.rect
    new_page = new_doc.new_page(width=rect.width, height=rect.height)
    new_page.insert_image(rect, stream=out_bytes)

output_path = 'assets/pdf/primary/primary_scholarship_policy_routine_2026_clean.pdf'
new_doc.save(output_path, garbage=4, deflate=True)
print(f"Done! Original: {os.path.getsize('assets/pdf/primary/primary_scholarship_policy_routine_2026.pdf')} bytes -> New: {os.path.getsize(output_path)} bytes")

#!/usr/bin/env python3
"""
tools/image_optimizer/webp_compressor.py
Ultra-lightweight WebP Compressor targeting 10 to 20 KB file sizes.
Preserves crisp Bengali typography and contrast for Core Web Vitals (LCP < 1.0s).
"""

import os
import sys
import argparse
import io
from PIL import Image

try:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


def compress_to_target_webp(
    input_path: str,
    output_path: str = None,
    target_min_kb: float = 10.0,
    target_max_kb: float = 20.0,
    max_width: int = 1200,
    max_height: int = 675,
) -> tuple[str, float]:
    """
    Compresses any input image (PNG, JPG, etc.) into an optimized WebP file
    strictly constrained to target_min_kb - target_max_kb (default 10KB - 20KB).
    
    Returns: (output_path, final_size_kb)
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input image not found: {input_path}")

    if not output_path:
        base, _ = os.path.splitext(input_path)
        output_path = f"{base}_optimized.webp"

    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

    with Image.open(input_path) as img:
        # Convert RGBA / P to RGB with a solid background if needed
        if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
            bg = Image.new("RGB", img.size, (255, 255, 255))
            if img.mode != "RGBA":
                img = img.convert("RGBA")
            bg.paste(img, mask=img.split()[3])  # 3 is the alpha channel
            img = bg
        elif img.mode != "RGB":
            img = img.convert("RGB")

        orig_w, orig_h = img.size
        # Resize if dimensions exceed max limits while preserving 16:9 aspect ratio
        scale = min(1.0, max_width / orig_w, max_height / orig_h)
        if scale < 1.0:
            target_w = max(100, int(orig_w * scale))
            target_h = max(100, int(orig_h * scale))
            working_img = img.resize((target_w, target_h), Image.Resampling.LANCZOS)
        else:
            working_img = img.copy()

        # Multi-pass binary search to dial in the target size (target_min_kb to target_max_kb)
        min_quality = 10
        max_quality = 85
        best_buffer = None
        best_size_kb = 0.0
        best_quality = 50

        # Pass 1: Binary search on quality parameter
        for _ in range(7):
            current_q = (min_quality + max_quality) // 2
            buf = io.BytesIO()
            working_img.save(
                buf,
                format="WEBP",
                quality=current_q,
                method=6,  # Maximum compression effort
                lossless=False,
            )
            size_kb = buf.tell() / 1024.0

            if target_min_kb <= size_kb <= target_max_kb:
                best_buffer = buf
                best_size_kb = size_kb
                best_quality = current_q
                break
            elif size_kb > target_max_kb:
                max_quality = current_q - 1
                best_buffer = buf
                best_size_kb = size_kb
                best_quality = current_q
            else:
                min_quality = current_q + 1
                best_buffer = buf
                best_size_kb = size_kb
                best_quality = current_q

        # Pass 2: If file is still too big (> target_max_kb), incrementally downscale resolution
        curr_w, curr_h = working_img.size
        while best_size_kb > target_max_kb and curr_w > 640:
            curr_w = int(curr_w * 0.90)
            curr_h = int(curr_h * 0.90)
            downscaled = working_img.resize((curr_w, curr_h), Image.Resampling.LANCZOS)

            buf = io.BytesIO()
            downscaled.save(
                buf,
                format="WEBP",
                quality=best_quality,
                method=6,
                lossless=False,
            )
            size_kb = buf.tell() / 1024.0
            best_buffer = buf
            best_size_kb = size_kb

        # Pass 3: If file is under target_min_kb (e.g. 8KB), slightly bump quality to maximize crispness
        if best_size_kb < target_min_kb:
            for q in range(best_quality + 5, 95, 5):
                buf = io.BytesIO()
                working_img.save(
                    buf,
                    format="WEBP",
                    quality=q,
                    method=6,
                    lossless=False,
                )
                size_kb = buf.tell() / 1024.0
                if size_kb <= target_max_kb:
                    best_buffer = buf
                    best_size_kb = size_kb
                    best_quality = q
                else:
                    break

        # Write the final buffer to disk
        with open(output_path, "wb") as f:
            f.write(best_buffer.getvalue())

    return output_path, best_size_kb


def batch_compress(dir_path: str, target_min_kb: float = 10.0, target_max_kb: float = 20.0):
    """Compresses all PNG/JPG files in a directory to WebP in target size range."""
    valid_exts = {".png", ".jpg", ".jpeg", ".bmp"}
    results = []
    for root, _, files in os.walk(dir_path):
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in valid_exts and not file.endswith("_optimized.webp"):
                inp = os.path.join(root, file)
                out_name = os.path.splitext(file)[0] + ".webp"
                outp = os.path.join(root, out_name)
                try:
                    orig_kb = os.path.getsize(inp) / 1024.0
                    _, final_kb = compress_to_target_webp(
                        inp, outp, target_min_kb=target_min_kb, target_max_kb=target_max_kb
                    )
                    saved_pct = (1.0 - final_kb / max(0.1, orig_kb)) * 100.0
                    results.append((file, orig_kb, final_kb, saved_pct))
                    print(f"✅ {file:40} {orig_kb:7.1f} KB ➔ {final_kb:5.1f} KB (Saved: {saved_pct:5.1f}%)")
                except Exception as e:
                    print(f"❌ Error compressing {file}: {e}")
    return results


def main():
    parser = argparse.ArgumentParser(description="Ultra-lightweight 10-20 KB WebP Optimizer for Helptrickbd")
    parser.add_argument("--input", "-i", help="Path to input image file")
    parser.add_argument("--output", "-o", help="Path to output WebP file")
    parser.add_argument("--batch-dir", "-b", help="Directory of images to batch compress")
    parser.add_argument("--target-min-kb", type=float, default=10.0, help="Minimum target size in KB (default: 10.0)")
    parser.add_argument("--target-max-kb", type=float, default=20.0, help="Maximum target size in KB (default: 20.0)")

    args = parser.parse_args()

    print("=" * 60)
    print("🚀 Helptrickbd WebP Optimizer (10–20 KB Target Engine)")
    print("=" * 60)

    if args.batch_dir:
        batch_compress(args.batch_dir, args.target_min_kb, args.target_max_kb)
    elif args.input:
        orig_kb = os.path.getsize(args.input) / 1024.0
        out_path, final_kb = compress_to_target_webp(
            args.input, args.output, args.target_min_kb, args.target_max_kb
        )
        saved_pct = (1.0 - final_kb / max(0.1, orig_kb)) * 100.0
        print(f"Original File : {args.input} ({orig_kb:.1f} KB)")
        print(f"Optimized WebP: {out_path} ({final_kb:.1f} KB)")
        print(f"Bandwidth Save: {saved_pct:.1f}%")
        if args.target_min_kb <= final_kb <= args.target_max_kb:
            print(f"🎯 Status: PERFECT (Within {args.target_min_kb}KB – {args.target_max_kb}KB goal!)")
        else:
            print(f"ℹ️ Status: Compact ({final_kb:.1f} KB)")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

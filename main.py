from PIL import Image
import os
import subprocess

total_mbs_saved = 0

def print_mbs_saved(input_path, before_mbs, img_extension):
    after_mbs = os.path.getsize(input_path) / 1_000_000
    mbs_saved = (before_mbs - after_mbs)
    print(f"✅ Compressed {img_extension} saved to {input_path} ({before_mbs:.2f} MB -> {after_mbs:.2f} MB), saved {mbs_saved:.2f} MB")
    return mbs_saved

def compress_jpg(input_path):
    global total_mbs_saved
    before_mbs = os.path.getsize(input_path) / 1_000_000
    try:
        img = Image.open(input_path)
        img.save(input_path, "JPEG", quality=80, optimize=True)
        total_mbs_saved += print_mbs_saved(input_path, before_mbs, "JPEG")
    except Exception as e:
        print(f"❌ Error: {e}")

def compress_png(input_path):
    global total_mbs_saved
    before_mbs = os.path.getsize(input_path) / 1_000_000
    try:
        subprocess.run([
            "pngquant", "--force", "--speed", "1",
            "--output", input_path, input_path
        ], shell=True, check=True)
        total_mbs_saved += print_mbs_saved(input_path, before_mbs, "PNG")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")

def compress_images_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file.lower().endswith(".jpg") or file.lower().endswith(".jpeg"):
                compress_jpg(file_path)
            elif file.lower().endswith(".png"):
                compress_png(file_path)

repo_path = "project"
compress_images_in_directory(repo_path)

print(f"Total saved: {total_mbs_saved:.2f} MB")

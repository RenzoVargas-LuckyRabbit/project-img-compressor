## Description

A Python script for compressing images (**JPEGs and PNGs**) within a project (folder structure), using **pngquant** and **Pillow**.

## Features

- ✅ Compresses **JPEG** and **PNG** images recursively within a folder structure.
- ✅ Uses **Pillow** for JPEG compression.
- ✅ Uses **pngquant** for PNG compression.
- ✅ Outputs a folder with compressed images without modifying the original files.

---

## Installation & Setup

### 1️⃣ Install Dependencies

Create a virtual environment and install required Python libraries:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2️⃣ Install `pngquant`

#### Windows

1. Download `pngquant.exe` from [pngquant.org](https://pngquant.org).
2. Add the executable to your system `PATH`.

#### Linux/macOS

Install using a package manager:

```bash
# Ubuntu / Debian
sudo apt install pngquant

# macOS
brew install pngquant
```

---

## Usage

1. Place your project inside the `project_pre` and `project` folders (both initially empty).
2. Fill both folders with the project you want to compress the images within.
3. Run the script:
   ```bash
   python main.py
   ```
4. The images in the `project` folder will be compressed, while the `project_pre` folder remains unchanged as a reference.

---

## Requirements

- Python 3.x
- Pillow
- pngquant (for PNG compression)

---

## License

MIT License

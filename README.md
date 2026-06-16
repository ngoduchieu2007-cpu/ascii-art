# ASCII Art Generator

A little weekend project that turns any image into ASCII art — mostly built to actually understand how Pillow, numpy, and pixels work under the hood, not because the world needed another one of these.

## What it does

Takes an image, grayscales it, and maps every pixel's brightness onto a "ramp" of characters ordered by how dense they look (`" .:-=+*#%@"`, light to dark). Then it spits out two things:

- A small preview, printed straight to your terminal
- A full-resolution version, saved to `output/output.txt`

Two sizes because terminals are cramped little boxes and decent ASCII art needs way more room to breathe.

## How it works (short version)

Every pixel is just a number, 0 (black) to 255 (white). Slot that number into a list of characters sorted by visual density, and you've got ASCII art — no magic, just brightness-to-character mapping. The mapping itself is vectorized with numpy instead of looping pixel-by-pixel, because nobody's got time for 200,000 iterations of a Python `for` loop.

## Setup

```bash
pip install pillow numpy
```

## Usage

No CLI flags yet — refreshingly low-tech. To convert your own image:

1. Drop the image file into the `images/` folder
2. Open `ascii.py` and edit the config block at the top of `main()`:

   ```python
   img_path = 'images/your_image.png'   # point this at your image
   output_width = 700                    # width of the saved file
   terminal_width = 60                   # width of the terminal preview
   ```
3. Run it:

   ```bash
   python ascii.py
   ```

You'll get a (probably rough, low-res) preview in the terminal, and a much better version waiting in `output/output.txt`. Open it, zoom out, and admire your pixels reborn as `@`s and `.`s.

<img width="425" height="323" alt="image" src="https://github.com/user-attachments/assets/08b1bc0f-e488-49ae-919c-6f66732809f3" />


## Project structure

```
ascii-art/
├── ascii.py
├── images/      # drop source images here
└── output/      # generated .txt files land here
```

---

Built one pixel-to-character mapping at a time.

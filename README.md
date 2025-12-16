# Photo Tools

A powerful Command Line Interface (CLI) for processing photos and videos. Built with Python and OpenCV.

## Features

- **Timelapse Creation**: Convert a sequence of images into a high-quality video.
- **Customizable Output**: Control frame rate, output format, and resolution.
- **Smart Resizing**: Automatically handles images of different sizes or scales them to your desired resolution.

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/6ickomod3/photo_tools.git
    cd photo_tools
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Creating a Timelapse

Use the `timelapse` command to generate a video from a directory of images.

```bash
python main.py timelapse -i /path/to/images -o output.mp4
```

#### Options

| Option | Short | Description | Default |
| :--- | :--- | :--- | :--- |
| `--input-dir` | `-i` | **Required.** Directory containing source images. | - |
| `--output` | `-o` | Output video filename. | `output.mp4` |
| `--fps` | `-f` | Frames per second. | `30` |
| `--ext` | `-e` | Image file pattern (matches glob). | `*.jpg` |
| `--resolution` | `-r` | Target size (WxH) or scale factor (float). | Original Size |

#### Examples

**Basic Usage:**
```bash
python main.py timelapse -i ./vacation_photos
```

**Custom Resolution (1920x1080):**
```bash
python main.py timelapse -i ./photos --resolution 1920x1080
```

**Half Resolution (50% scale):**
```bash
python main.py timelapse -i ./photos -r 0.5
```

**Double Resolution:**
```bash
python main.py timelapse -i ./photos -r 2.0
```

## Requirements

- Python 3.6+
- OpenCV (`opencv-python`)
- Click
- Pillow

## License

MIT

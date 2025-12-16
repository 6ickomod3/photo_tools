import cv2
import os
import glob
from pathlib import Path
from typing import List, Tuple

def create_timelapse(input_dir: str, output_file: str, fps: int = 30, extension: str = "*.jpg"):
    """
    Creates a time-lapse video from images in a directory.

    Args:
        input_dir: Path to the directory containing images.
        output_file: Path to the output video file (e.g., output.mp4).
        fps: Frames per second for the video.
        extension: Glob pattern for image files (default: *.jpg).
    """
    input_path = Path(input_dir)
    images = sorted(list(input_path.glob(extension)))

    if not images:
        print(f"No images found in {input_dir} with pattern {extension}")
        return

    # Read the first image to determine frame size
    frame = cv2.imread(str(images[0]))
    if frame is None:
        print(f"Failed to read the first image: {images[0]}")
        return
    
    height, width, layers = frame.shape
    size = (width, height)

    # Define the codec and create VideoWriter object
    # mp4v is a safe codec for .mp4 files
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(output_file, fourcc, fps, size)

    print(f"Found {len(images)} images. creating video...")
    
    count = 0
    for image_path in images:
        img = cv2.imread(str(image_path))
        if img is not None:
            # Resize if dimensions don't match (optional, but good for safety)
            if (img.shape[1], img.shape[0]) != size:
                 img = cv2.resize(img, size)
            out.write(img)
            count += 1
            if count % 50 == 0:
                print(f"Processed {count}/{len(images)} frames")
        else:
            print(f"Warning: Could not read image {image_path}")

    out.release()
    print(f"Video saved to {output_file}")

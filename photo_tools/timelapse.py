import cv2
import os
import glob
from pathlib import Path
from typing import List, Tuple

def create_timelapse(input_dir: str, output_file: str, fps: int = 30, extension: str = "*.jpg", resolution: str = None):
    """
    Creates a time-lapse video from images in a directory.

    Args:
        input_dir: Path to the directory containing images.
        output_file: Path to the output video file (e.g., output.mp4).
        fps: Frames per second for the video.
        extension: Glob pattern for image files (default: *.jpg).
        resolution: Target resolution (e.g., "1920x1080") or scale factor (e.g., "0.5", "2").
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
    
    # Determine target size based on resolution param
    target_width, target_height = width, height
    
    if resolution:
        try:
            if 'x' in resolution.lower():
                w_str, h_str = resolution.lower().split('x')
                target_width = int(w_str)
                target_height = int(h_str)
            else:
                scale = float(resolution)
                target_width = int(width * scale)
                target_height = int(height * scale)
            
            print(f"Target resolution: {target_width}x{target_height} (Original: {width}x{height})")
        except ValueError:
            print(f"Error parsing resolution/scale '{resolution}'. Using original size.")
            target_width, target_height = width, height

    size = (target_width, target_height)

    # Define the codec and create VideoWriter object
    # mp4v is a safe codec for .mp4 files
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
    out = cv2.VideoWriter(output_file, fourcc, fps, size)

    print(f"Found {len(images)} images. creating video...")
    
    count = 0
    for image_path in images:
        img = cv2.imread(str(image_path))
        if img is not None:
            # Resize if dimensions don't match target size
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

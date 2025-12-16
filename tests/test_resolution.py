import cv2
import numpy as np
import os
import shutil
from photo_tools.timelapse import create_timelapse

def create_dummy_images(dirname, count=3, width=100, height=100):
    if os.path.exists(dirname):
        shutil.rmtree(dirname)
    os.makedirs(dirname)
    
    for i in range(count):
        # Create a random image
        img = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)
        cv2.imwrite(os.path.join(dirname, f"img_{i:03d}.jpg"), img)

def verify_video_size(video_path, expected_width, expected_height):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"FAILED: Could not open video {video_path}")
        return False
    
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    cap.release()
    
    if width == expected_width and height == expected_height:
        print(f"PASSED: {video_path} is {width}x{height}")
        return True
    else:
        print(f"FAILED: {video_path} is {width}x{height}, expected {expected_width}x{expected_height}")
        return False

def test_resolution():
    input_dir = "test_images"
    create_dummy_images(input_dir, width=100, height=100)
    
    # Test 1: Explicit Resolution
    output_res = "test_res.mp4"
    if os.path.exists(output_res): os.remove(output_res)
    create_timelapse(input_dir, output_res, fps=10, resolution="50x50")
    if not verify_video_size(output_res, 50, 50):
        return

    # Test 2: Scale Factor (0.5)
    output_scale = "test_scale.mp4"
    if os.path.exists(output_scale): os.remove(output_scale)
    create_timelapse(input_dir, output_scale, fps=10, resolution="0.5")
    if not verify_video_size(output_scale, 50, 50):
        return

    # Test 3: Scale Factor (2.0)
    output_scale_up = "test_scale_up.mp4"
    if os.path.exists(output_scale_up): os.remove(output_scale_up)
    create_timelapse(input_dir, output_scale_up, fps=10, resolution="2")
    if not verify_video_size(output_scale_up, 200, 200):
        return

    # Cleanup
    shutil.rmtree(input_dir)
    if os.path.exists(output_res): os.remove(output_res)
    if os.path.exists(output_scale): os.remove(output_scale)
    if os.path.exists(output_scale_up): os.remove(output_scale_up)
    
    print("All resolution tests passed!")

if __name__ == "__main__":
    test_resolution()

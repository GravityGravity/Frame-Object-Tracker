<p align="center">
  <img src="Screenshots/Banner.png" alt="Frame Track Banner">
</p>


# 🎯 Frame-Object-Tracker

**Frame-Object-Tracker** is a lightweight computer vision project that detects and tracks a single object across **30 consecutive video frames** using **OpenCV** and **NumPy**.  

It demonstrates essential skills in video frame processing, bounding box tracking, and step-by-step frame visualization in Python.

> ⚠️ This project **does not detect or identify** objects — it only **tracks** a given object whose **initial bounding box** is provided.

## Quick Overview

- Tracks one visible object across a short 30-frame video clip.  
- Uses **OpenCV** for frame analysis and **NumPy** for matrix operations.  
- Displays each frame interactively with a bounding box update.  
- Saves output frames for later review in the `output/` folder.  

## 📸 Example Output
<p align="center">
  <img src="Screenshots/frame1.png" alt="Frame 1 Track example" width="33%">
  <img src="Screenshots/frame2.png" alt="Frame 2 Track example" width="33%">
  <img src="Screenshots/frame3.png" alt="Frame 3 Track example" width="33%">
</p>

Each processed frame shows a bounding box around the tracked object, maintaining smooth positional updates across all 30 frames.


## How It Works

1. Loads 30 sequential frames from an input folder.  
2. Initializes a bounding box around the target object.  
3. Updates the bounding box per frame using OpenCV operations.  
4. Displays each frame step-by-step or runs continuously.  
5. Saves processed frames with bounding boxes to `output/`.

---
## ⚙️ Input Details

All test cases follow these constraints:
- **Video length:** 30 frames  
- **Frame size:** `1280×720` or `640×360`  
- **Object:** always visible (no occlusion)  
- **Bounding boxes:** overlap between consecutive frames  



## 💻 Run the Project

Example command:
```bash
python main.py C:\_repos\CompVision\Frame-Object-Tracker\tests\0

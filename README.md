# UAV Image Optimizer (EXIF/GPS Preserver)

## Overview
A Python utility script designed to batch-resize drone imagery for cloud-based photogrammetry processing (e.g., WebODM, Agisoft Metashape, Pix4D). 

When processing large datasets from UAV flights, high-resolution images can significantly increase cloud computing costs, transfer times, and RAM usage. Standard image resizing tools strip the essential EXIF metadata (Latitude, Longitude, Altitude), ruining the dataset for photogrammetry. 

This script solves that problem by drastically reducing image weight while securely preserving the critical spatial data required for 3D modeling and orthomosaic generation.

## Key Features
* **Batch Processing:** Automatically scans and processes all `.jpg` and `.jpeg` files in a targeted directory.
* **EXIF Preservation:** Utilizes the `piexif` library to extract and re-embed original GPS metadata into the downscaled images.
* **Lanczos Resampling:** Uses `Image.Resampling.LANCZOS` via the `Pillow` library to ensure the highest possible detail retention, which is crucial for tie-point generation in photogrammetry algorithms.
* **Error Handling:** Built-in safeguards to skip corrupted files without breaking the processing loop.

## Tech Stack
* Python 3
* Pillow (PIL)
* Piexif

import os
from PIL import Image
import piexif

def resize_drone_images(input_folder, output_folder, scale_percent=50):
    # Create output dir if needed
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    print(f"Starting batch resize from: {input_folder}")

    processed_count = 0
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.jpg', '.jpeg')):
            img_path = os.path.join(input_folder, filename)
            out_path = os.path.join(output_folder, filename)

            try:
                with Image.open(img_path) as img:
                    # Keep EXIF data for photogrammetry (GPS, altitude, camera model)
                    exif_data = img.info.get('exif')
                    
                    # Calculate new dimensions
                    width, height = img.size
                    new_size = (int(width * scale_percent / 100), int(height * scale_percent / 100))
                    
                    # Resize with Lanczos filter for better detail retention
                    img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
                    
                    # Save while preserving original EXIF metadata
                    if exif_data:
                        img_resized.save(out_path, "JPEG", exif=exif_data, quality=85)
                    else:
                        img_resized.save(out_path, "JPEG", quality=85)
                        
                    print(f"Processed: {filename}")
                    processed_count += 1
            except Exception as e:
                print(f"Skipped {filename} due to error: {e}")
                
    print(f"\nDone. Processed {processed_count} images.")

if __name__ == "__main__":
    # Local paths
    input_path = r'C:\Users\igorh\OneDrive\Dokumenty\zdjecia dom UK\RAW_ALL'
    output_path = r'C:\Users\igorh\OneDrive\Dokumenty\zdjecia dom UK\RESIZED_ALL'
    
    # Run optimizer
    resize_drone_images(input_path, output_path, scale_percent=50)
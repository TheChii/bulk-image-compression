from PIL import Image
import os
import concurrent.futures


def compress_images_parallel(input_folder, output_folder, quality=85):
    global size_difference
    size_difference = 0

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []

        for filename in os.listdir(input_folder):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)

                future = executor.submit(compress_single_image, input_path, output_path, quality)
                futures.append(future)

        concurrent.futures.wait(futures)

        size_difference = sum(f.result() for f in futures)

def compress_single_image(input_path, output_path, quality=85):
    original_image = Image.open(input_path)
    original_size = os.path.getsize(input_path)
    compressed_image = Image.frombytes('RGB', original_image.size, original_image.tobytes(), 'raw', 'RGB')
    compressed_image.save(output_path, 'JPEG', quality=quality)
    compressed_size = os.path.getsize(output_path)

    return original_size - compressed_size

if __name__ == "__main__":


    input_folder = input("Input folder path:")
    output_folder = input("Output folder path:")
    quality = int(input("Quality (1-100):"))

    compress_images_parallel(input_folder, output_folder, quality)

    print("Compression done. Total Size Difference:", round(size_difference / 1048576, 2), "MB")

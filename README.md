# Bulk Image Compression

**Description:**

This Python script provides a convenient solution for bulk image compression, allowing users to compress multiple images concurrently using multithreading. The script utilizes the Python Imaging Library (PIL) to open, compress, and save images in the JPEG format. The compression quality is adjustable, providing flexibility to balance image size reduction with visual quality.

**Features:**

- **Multithreaded Compression:** The script leverages `concurrent.futures` to compress multiple images simultaneously, improving overall performance.

- **Adjustable Compression Quality:** Users can specify the compression quality (1-100) to achieve the desired balance between image size reduction and visual quality.

- **Simple Usage:** The script prompts users for input and output folder paths, as well as the desired compression quality, making it user-friendly.

**Usage:**

1. Clone the repository.
2. Run the script using `py main.py`.
3. Enter the relevant input and output paths along with the desired compression quality.

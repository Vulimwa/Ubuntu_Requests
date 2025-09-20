# PLP Academy Python Assignment — Week 6

## Overview
This assignment is designed to help practice Python file handling, HTTP requests, error management, and safe downloading practices. The main script allows users to fetch images from the web by providing one or more image URLs. It demonstrates best practices for working with external resources and handling potential risks.

## Project Structure
- `file.py` — Main Python script for downloading images.
- `text.txt` — Assignment instructions and evaluation criteria.
- `Fetched_Images/` — Folder where downloaded images are stored.

## Features
- **Multiple URL Support:** Enter several image URLs (comma-separated) to download them in one run.
- **Duplicate Prevention:** The script checks for existing filenames in `Fetched_Images/` and skips downloads to avoid duplicates.
- **Error Handling:** Network errors and other exceptions are caught and reported with clear messages.
- **Directory Management:** Automatically creates the `Fetched_Images/` folder if it does not exist.
- **Filename Extraction:** Uses the URL path to name files, with a fallback if the URL does not contain a filename.

## Usage Instructions
1. Ensure you have Python 3.7+ installed.
2. Install the required package:
   ```powershell
   pip install requests
   ```
3. Run the script:
   ```powershell
   python file.py
   ```
4. When prompted, enter one or more image URLs separated by commas:
   ```
   https://example.com/image1.jpg, https://example.com/image2.png
   ```
5. Downloaded images will appear in the `Fetched_Images/` folder.

## Safety Precautions
When downloading files from unknown sources:
- **Check Content-Type:** Only save files if the response header indicates an image (e.g., `image/jpeg`, `image/png`).
- **Limit File Size:** Avoid saving files that are too large or empty by checking the `Content-Length` header.
- **Use HTTPS:** Prefer secure URLs to protect data integrity.
- **Scan Files:** Use antivirus software to scan downloaded files before opening.
- **Avoid Execution:** Never automatically execute or open downloaded files.

## Important HTTP Headers to Check
- `Content-Type`: Should start with `image/`.
- `Content-Length`: Should be reasonable (not zero, not excessively large).
- `Content-Disposition`: May suggest a filename; use with caution.
- `ETag` and `Last-Modified`: Useful for deduplication and caching.

## Assignment Requirements (from `text.txt`)
- Handle multiple URLs at once.
- Take precautions when downloading files from unknown sources.
- Prevent downloading duplicate images.
- Check important HTTP headers before saving content.
- Use the `requests` library properly.
- Implement effective error handling.
- Manage files and directories appropriately.
- Write clean, readable code with comments.
- Demonstrate Ubuntu principles of community and respect.

## Example Output
```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web
Successfully fetched: image1.jpg
Image saved to Fetched_Images/image1.jpg
Skipped duplicate: image2.png
Connection strengthened. Community enriched.
```
## Author & License
This assignment is for PLP Academy, Week 6. Feel free to use and adapt for educational purposes.

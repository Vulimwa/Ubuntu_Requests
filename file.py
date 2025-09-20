import requests
import os
from urllib.parse import urlparse

def fetch_image(url, folder="Fetched_Images"):
    """Download and save a single image from a given URL."""

    try:
        # 1. Create directory if it doesn't exist
        os.makedirs(folder, exist_ok=True)

        # 2. Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # 3. Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # if URL doesn't have a filename
            filename = "downloaded_image.jpg"

        filepath = os.path.join(folder, filename)

        # 4. Prevent duplicates
        if os.path.exists(filepath):
            print(f"Skipped duplicate: {filename}")
            return

        # 5. Save the image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"Successfully fetched: {filename}")
        print(f"Image saved to {filepath}")

    except requests.exceptions.RequestException as e:
        print(f"Connection error for {url}: {e}")
    except Exception as e:
        print(f"An error occurred with {url}: {e}")


def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Get multiple URLs from user
    urls = input("Enter image URLs (comma-separated): ").split(",")

    # Process each URL
    for url in urls:
        fetch_image(url.strip())

    print("\nConnection strengthened. Community enriched.")


if __name__ == "__main__":
    main()

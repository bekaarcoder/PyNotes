import time
import requests
import concurrent.futures
from PIL import Image, ImageFilter

t1 = time.perf_counter()

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235'
]

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1532009324734-20a7a5813719.jpg'
]

size = (1200, 1200)


def process_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f"{img_name}.jpg"
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded.")
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f"processed/{img_name}")
    print(f"{img_name} was processed")


if __name__ == "__main__":
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(process_image, img_urls)
    # process_image(img_names[0])

    t2 = time.perf_counter()

    print(f"Finished in {t2-t1} seconds")
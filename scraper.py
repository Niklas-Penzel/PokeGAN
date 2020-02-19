import requests
import os
import urllib.request
from tqdm import tqdm

def scrape_pokewiki_images(out_path="pokemon"):
    if not os.path.isdir(out_path):
        os.makedirs(out_path)

    url = "https://www.pokewiki.de/Datei:Sugimori_"

    for i in tqdm(range(1,891)):
        page = requests.get(f"{url}{i:03d}.png")
        page_cont = str(page.content)

        if "property=\"og:image\" content=\"" in page_cont:
            img_url = page_cont.split("property=\"og:image\" content=\"")[1].split("\"/>")[0]
            urllib.request.urlretrieve(img_url, os.path.join(out_path, f"{i:03d}.png"))


if __name__ == "__main__":
    scrape_pokewiki_images()
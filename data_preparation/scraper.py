import requests
import os
import urllib.request
from tqdm import tqdm


def read_names(path=os.path.join("..","pkm_list")):
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()

    names = [str(l.replace(":", "-").replace("\t", "").replace("\n", "").replace(",", "").replace("\"", "")) for l in lines]
    return names

def scrape_pokewiki_images(out_path=os.path.join("..","pokemon")):
    if not os.path.isdir(out_path):
        os.makedirs(out_path)

    names = read_names()

    url = "https://www.pokewiki.de/Datei:Sugimori_"
    url_anime = "https://www.pokewiki.de/Datei:Anime-Artwork_"
    url_pgl = "https://www.pokewiki.de/Datei:PGL-Artwork_"

    for i in tqdm(range(1,891)):
        # main image
        page = requests.get(f"{url}{i:03d}.png")
        page_cont = str(page.content)

        if "property=\"og:image\" content=\"" in page_cont:
            img_url = page_cont.split("property=\"og:image\" content=\"")[1].split("\"/>")[0]
            urllib.request.urlretrieve(img_url, os.path.join(out_path, f"{i}.png"))

        # anime art
        page = requests.get(f"{url_anime}{i:03d}.png")
        page_cont = str(page.content)

        if "property=\"og:image\" content=\"" in page_cont:
            img_url = page_cont.split("property=\"og:image\" content=\"")[1].split("\"/>")[0]
            urllib.request.urlretrieve(img_url, os.path.join(out_path, f"{i}_aa.png"))

        if i-1 < len(names):
            # pgl art
            page = requests.get(f"{url_pgl}{names[i-1]}.png")
            page_cont = str(page.content)

            if "property=\"og:image\" content=\"" in page_cont:
                img_url = page_cont.split("property=\"og:image\" content=\"")[1].split("\"/>")[0]
                urllib.request.urlretrieve(img_url, os.path.join(out_path, f"{i}_pgl.png"))



if __name__ == "__main__":
    scrape_pokewiki_images()
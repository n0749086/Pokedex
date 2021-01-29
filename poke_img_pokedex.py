from poke_img import PokeImg
import requests
from bs4 import BeautifulSoup
import json


class PokeImgPokedex(PokeImg):
    def __init__(self):
        self.base_path = 'https://zukan.pokemon.co.jp/zukan-api/up/images/index/'
        self.img_size = 100

    def get_poke_img_path_from_hp(self, pokedex_no):
        base_uri = 'https://zukan.pokemon.co.jp/detail/'

        if pokedex_no.isdecimal():
            target_uri = "{}{:03d}".format(base_uri, int(pokedex_no))
        else:
            target_uri = "{}{}".format(base_uri, pokedex_no)
        r = requests.get(target_uri)
        soup = BeautifulSoup(r.text, 'lxml')

        data = "fuga"
        for a in soup.find_all('script', attrs={"id": "json-data"}):
            data = json.loads(a.string)
            img_path = data["pokemon"]["image_s"]
        return img_path

    def get_poke_img_path(self, pokedex_no, poke_name):
        url = self.get_poke_img_path_from_hp(pokedex_no)

        return url, self.img_size

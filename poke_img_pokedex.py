from poke_img import PokeImg
import requests
from bs4 import BeautifulSoup
import json


class PokeImgPokedex(PokeImg):
    def __init__(self):
        self.base_path = 'https://zukan.pokemon.co.jp/zukan-api/up/images/index/'
        self.img_size = 100

    def get_poke_img_path_from_hp(self, pokedex_no) -> str:
        """
        ポケモンの画像パスを返す
        :param pokedex_no: ポケモン番号
        :return: 画像パス
        """
        base_uri = 'https://zukan.pokemon.co.jp/detail/'

        if pokedex_no.isdecimal():
            target_uri = "{}{:03d}".format(base_uri, int(pokedex_no))
        else:
            target_uri = "{}{}".format(base_uri, pokedex_no)
        r = requests.get(target_uri)
        soup = BeautifulSoup(r.text, 'lxml')

        data = json.loads(soup.find('script', attrs={"id": "json-data"}).string)
        img_path = data["pokemon"]["image_s"]

        return img_path

    def get_poke_img_path(self, pokedex_no, poke_name) -> str:
        """
        ポケモン名、図鑑番号からポケモンの画像パスを検索する
        :param pokedex_no: 図鑑番号
        :param poke_name: ポケモン名
        :return: ポケモンの画像
        """
        url = self.get_poke_img_path_from_hp(pokedex_no)

        return url, self.img_size

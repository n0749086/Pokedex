import pickle
import csv
from poke_img_pokedex import PokeImgPokedex


class Pokedex(object):
    poke_list = {}
    poke_name_list = []

    def load_poke_data_pkl(self):
        self.poke_name_list, self.poke_list = pickle.load(open("poke.pkl", "rb"))
        self.poke_name_list = self.replace_poke_name(self.poke_name_list, True)

    #図鑑番号,ポケモン名,タイプ１,タイプ２,通常特性１,通常特性２,夢特性,HP,こうげき,ぼうぎょ,とくこう,とくぼう,すばやさ,合計
    def load_poke_data_csv(self):
        self.poke_list = {}
        self.poke_name_list = []
        with open("pokemon_status.csv") as f:
            reader = csv.reader(f)
            next(reader)
            data = {}
            for row in reader:
                data["no"] = row[0]
                name = row[1].replace("\r", "").replace("\n", "")
                data["type1"] = row[2]
                data["type2"] = row[3]
                data["abi1"] = row[4]
                data["abi2"] = row[5]
                data["abiD"] = row[6]
                data["HP"] = int(row[7])
                data["ATK"] = int(row[8])
                data["DEF"] = int(row[9])
                data["S_ATK"] = int(row[10])
                data["S_DEF"] = int(row[11])
                data["SPD"] = int(row[12])

                self.poke_list[name] = data.copy()
                self.poke_name_list.append(name)
        with open("poke.pkl", "wb") as f:
            l = [self.poke_name_list, self.poke_list]
            pickle.dump(l, f)

    def __init__(self):
        self.replace_lists = (
            (":A", "<ア>", "(アローラ)"),
        )
        self.load_poke_data_pkl()
        #self.load_poke_data_csv()

    def get_poke_name_list(self):
        return self.poke_name_list

    def replace_poke_name(self, names, shorten):
        result = []

        for i in names:
            for j in self.replace_lists:
                if j[0] in i:
                    if shorten:
                        result.append(i.replace(j[0], j[1]))
                    else:
                        result.append(i.replace(j[0], j[2]))
                else:
                    result.append(i)

        return result

    def rebase_poke_name(self, name):
        result = name

        for j in self.replace_lists:
            if j[1] in name:
                result = name.replace(j[1], j[0])
        return result

    def get_poke_info(self, name):
        result = []
        img_data = PokeImgPokedex()
        name_rebased = self.rebase_poke_name(name)
        for k, v in self.poke_list.items():
            if name_rebased in k:
                data = v.copy()
                data["name"] = self.replace_poke_name((k, ), False)[0]
                data["img_path"], data["img_size"] = img_data.get_poke_img_path(data["no"], data["name"])
                result.append(data)
        return result


if __name__ == "__main__":
    poke = Pokedex()

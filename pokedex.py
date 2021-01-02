import pickle
import csv


class Pokedex:
    poke_list = {}
    poke_name_list = []

    def load_poke_data_pkl(self):
        self.poke_name_list, self.poke_list = pickle.load(open("poke.pkl", "rb"))

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
        self.load_poke_data_pkl()
        #self.load_poke_data_csv()

    def get_poke_name_list(self):
        return self.poke_name_list

    def get_poke_info(self, name):
        result = []
        for k, v in self.poke_list.items():
            if name in k:
                data = v.copy()
                data["name"] = k
                result.append(data)
        return result


if __name__ == "__main__":
    poke = Pokedex()

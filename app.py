from flask import Flask, render_template
import os
from pokedex import Pokedex

app = Flask(__name__)

@app.route('/')
def get_poke_info():
    pokedex = Pokedex()
    poke_name = pokedex.get_poke_name_list()
    title = "{}のステータス"
    return render_template('poke_info.html', title=title, name=poke_name[0], name_list=poke_name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

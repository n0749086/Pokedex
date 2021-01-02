from flask import Flask, render_template, request
import os
from pokedex import Pokedex

app = Flask(__name__)

@app.route('/')
def get_poke_info():
    pokedex = Pokedex()
    poke_name = pokedex.get_poke_name_list()
    name = request.args.get('name')
    if name != None:
        tgt_name = name
    else:
        tgt_name = poke_name[0]

    title = "{}の種族値".format(tgt_name)
    poke_status = pokedex.get_poke_info(tgt_name)

    return render_template('poke_info.html', title=title, info=poke_status, name_list=poke_name)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

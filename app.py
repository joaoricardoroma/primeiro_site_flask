from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html", messages=False)


@app.route('/contato')
def contact():
    return 'contato'


@app.route('/pokemons')
def pokemons():
    return render_template("pokemons.html", data=[])


@app.route('/pokemon/<int:id>')
def pokemon(id):
    data = {
        "name": "bulbasaur"
    }
    return render_template("pokemon.html", data=data)

from ..app import app
from flask import render_template
import requests


@app.route("/")
def accueil():
    return render_template("pages/index.html")

# Ajout d'une gestion des mauvaises url avec une redirection vers "oops.html"
@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/oops.html'), 404

@app.route("/retrive_wikidata/<string:id>")
def retrieve_wikidata(id:str):
    r = requests.get(f'https://www.wikidata.org/wiki/Special:EntityData/{id}.json')
    response = r.status_code
    r_type = r.headers['content-type']
    if(response == 200):
        r_json = r.json()
    else :
        r_json = ""
    return render_template('pages/wikidata.html', response=response, id=id, r_type=r_type, r_json=r_json)

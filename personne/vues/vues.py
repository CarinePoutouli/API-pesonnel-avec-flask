from flask import Blueprint, request
from flask_jwt_extended import jwt_required


from personne.controller.controller import Controller

personne = Blueprint('personne', __name__)

utilisateur_controller = Controller()


@personne.route('personne', methods=['POST'])
def person():
    nom = request.json.get('nom', None)
    prenom = request.json.get('prenom', None)
    age = request.json.get('age', None)

    return utilisateur_controller.personne(nom, prenom, age)




@personne.route('personne', methods=['GET'])
def read():
    return utilisateur_controller.get_utilisateur()



@personne.route('personne/<int:id>', methods=['DELETE'])
def dele(id):

    return utilisateur_controller.delete(id)






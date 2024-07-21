from flask import jsonify

from personne.model.model import Utilisateur
from extensions import db


class Controller:
    def __init__(self):
        self.model = Utilisateur

    def Utilisateur(self, nom, prenom, age):
    #    print(f"controller{image}")
        Utilisateur = self.model(nom=nom, prenom=prenom, age=age)
       # Article.save_File(image)
        db.session.add(Utilisateur)

        db.session.commit()

        return jsonify(
            {"msg": " successfully"}), 201


    def get_utilisateur(self):
        utilisateur = self.model.query.all()

        return jsonify({
            "nom": utilisateur.nom,
            "prenom": utilisateur.prenom,
            "age": utilisateur.age
        }), 200


    def delete(self, id):
        utilisateur = self.model.query.filter_by(id=id).first()
        db.session.delete(utilisateur)
        db.session.commit()
        return jsonify(
            {"msg": "good"}), 201

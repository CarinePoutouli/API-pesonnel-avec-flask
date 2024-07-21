from extensions import db, STATIC_FOLDER

import os
import uuid
from werkzeug.utils import secure_filename


upload_folder = os.path.join(STATIC_FOLDER, 'uploads')
os.makedirs(upload_folder, exist_ok=True)

class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(256), nullable=True)
    prenom = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)




    def __init__(self, nom, prenom, age):

        self.nom = nom
        self.prenom = prenom
        self.age = age



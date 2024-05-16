from flask import Flask
from flask import request
from flask import send_from_directory
import mysql.connector


app = Flask(__name__)

def create_connection():
    cnx = mysql.connector.connect(
        host='localhost',  # L'adresse du serveur, localhost pour une machine locale
        user='root',  # Remplacez par votre nom d'utilisateur MySQL
        password='',  # Remplacez par votre mot de passe MySQL
        database='amandzique'  # Remplacez par le nom de votre base de données
    )
@app.route("/", methods=['POST', 'GET'])
def send_musique():
    msg = request.values.get('message', 'Marche pas')
    print(msg)
    return send_from_directory("musiques/", "musique.mp4", as_attachment=True)









if __name__ == '__main__':
    app.run(debug=True)
from __future__ import unicode_literals
import yt_dlp
import mysql.connector
import os

def create_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='amandzique'
    )

def download_video(url):
    download_folder = '/musiques/'
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': download_folder + '%(title)s/%(title)s.%(ext)s',
        'writethumbnail': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        infos_vid = ydl.extract_info(url, download=True)
        # Générer le chemin exact du fichier après téléchargement
        filename = ydl.prepare_filename(infos_vid)
        titre = infos_vid.get('title', None)
        print("Titre de la vidéo :", titre)
    send_data(titre, filename, url)

def send_data(titre, lienfichier, url):
    data_vid = (titre, lienfichier, url)
    addMusique = "INSERT INTO musiques (nom, lienfichier, url) VALUES (%s, %s, %s)"
    cnx = create_connection()
    cursor = cnx.cursor()
    cursor.execute(addMusique, data_vid)
    cnx.commit()
    cursor.close()
    cnx.close()



if __name__ == "__main__":
    video_url = 'https://www.youtube.com/watch?v=mnIVGG3ny5w'
    download_video(video_url)

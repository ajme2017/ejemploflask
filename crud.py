from flask import Flask, jsonify, request
from flask_cors import CORS
import psycopg2
import os


app = Flask(__name__)

# CORS implemented so that we don't get errors when trying to access the server from a different server location
CORS(app)

DB_HOST = "localhost"
DB_NAME = "prueba"
DB_USER = "postgres"
DB_PASS = "123456789"
try:
    con = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST)
    
    cur = con.cursor()
    
    print(con.status)
    # GET: Fetch all movies from the database

    @app.route("/")
    def hello():
      return "<h1 style='color:blue'>ESTAMOS EN EL LABORATORIO DE ARCHIVOS !</h1>"

    @app.route('/toda', methods=['GET'])
    def fetch_all_movies():
        cur.execute('SELECT * FROM movies')
        rows = cur.fetchall()
        print(rows)

        return jsonify(rows)
    
  
    
    if __name__ == "__main__":
     app.run(host='0.0.0.0')        

except:
    print('Error')
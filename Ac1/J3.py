#cHupa meu pau :D
import sqlite3
from contextlib import closing
from flask import Flask, jsonify, Response, request,render_template

app = Flask(__name__)

sql = """
    CREATE TABLE IF NOT EXISTS atividades(id_atividade integer primary key autoincrement,
    titulo_atividade varchar (30) not null,
    descricao_atividade text not null
    );
    """
def con():
    return sqlite3.connect('atividades.db')

def banco():
        with closing(con()) as connection, closing(connection.cursor()) as cursor:
            cursor.executescript(sql)
            connection.commit()   
@app.route("/", methods=["GET"])
def inicio():
    print("\n")
    return render_template("bemvindo.html", mensagem="")

@app.route("/", methods=["GET"])
def ver():
    with closing(con()) as connection, closing(connection.cursor()) as cursor:
        cursor.execute("SELECT * FROM atividades")
        a=cursor.fetchall()
        for n in a:
            b=((list(n))[::])
            b[0]= str(b[0])
            lita=str(('-'.join(b[0:2])))
            print(lita)
    return render_template("vista.html", mensagem=lita)
    
@app.route("/criar", methods=["GET"])
def criacao():
    print("\n")
    return render_template("indocriar.html")

@app.route("/criar", methods=["POST"])
def criar():
        titulo_atividade = request.form["titulo"]
        descricao_atividade = request.form["descricao"]
        with closing(con()) as connection, closing(connection.cursor()) as cursor:
            id_atividade =cursor.lastrowid
            cursor.execute( cursor.execute("INSERT INTO atividades VALUES(?,?)",(titulo_atividade,descricao_atividade)))
            connection.commit()            
        return render_template("bemvindo.html", mensagem="Atividade criada com sucesso, você tem algo a mais pra fazer....")
        
if __name__ == '__main__':
    banco()
    app.run(host='localhost', port=5000, debug=True)

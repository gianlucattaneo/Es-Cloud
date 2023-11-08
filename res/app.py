from flask import Flask, request, jsonify
import psycopg2
import time

app = Flask(__name__)

def connect(host):
    return psycopg2.connect(
        dbname='mydatabase',
        user='myuser',
        password='mypassword',
        host=host,
        port= 5432
    )

def retry(times, wait_time, host):
    i = 0

    # X Test in locale
    try:
        conn = connect('localhost')
    except:
        conn = None

    while i <= times: 
        try:
            conn = connect(host)
        except:
            i += 1
            time.sleep(wait_time)
        else:
            break

    return conn

conn = retry(times=5, wait_time=1, host='db')
cur = conn.cursor()

cur.execute(''' 
CREATE TABLE IF NOT EXISTS Persona (
    id serial PRIMARY KEY,
    Nome text,
    Cognome text
);
''')

@app.route('/data', methods=['GET'])
def get_data():
    cur.execute("SELECT * FROM Persona")
    data = cur.fetchall()
    return jsonify(data)

@app.route('/data/<int:id>', methods=['GET'])
def get_single_data(id):
    cur.execute("SELECT * FROM Persona WHERE id = %s", (id,))
    data = cur.fetchone()
    return jsonify(data)

@app.route('/data', methods=['POST'])
def create_data():
    # Assumi che i dati siano inviati come JSON
    new_data = request.get_json()
    cur.execute("INSERT INTO Persona (Nome, Cognome) VALUES (%s, %s)", (new_data['value1'], new_data['value2']))
    conn.commit()
    return jsonify({'message': 'Data created'})

@app.route('/data/<int:id>', methods=['PUT'])
def update_data(id):
    updated_data = request.get_json()
    cur.execute("UPDATE Persona SET Nome = %s, Cognome = %s WHERE id = %s",
                (updated_data['value1'], updated_data['value2'], id))
    conn.commit()
    return jsonify({'message': 'Data updated'})

@app.route('/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    cur.execute("DELETE FROM Persona WHERE id = %s", (id,))
    conn.commit()
    return jsonify({'message': 'Data deleted'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
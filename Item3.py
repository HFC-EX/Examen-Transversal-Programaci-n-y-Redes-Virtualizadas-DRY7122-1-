import pyotp    # generates one-time passwords
import sqlite3  # database for username/passwords
import hashlib  # secure hashes and message digests
import uuid     # for creating universally unique identifiers
from flask import Flask, request

app = Flask(__name__)  # Be sure to use two underscores before and after "name"

db_name = 'test.db'

######################################### Password Hashing #########################################################

def create_database():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USER_HASH
           (USERNAME  TEXT    PRIMARY KEY NOT NULL,
            HASH      TEXT    NOT NULL);''')
    conn.commit()
    conn.close()

@app.route('/signup/v2', methods=['GET', 'POST'])
def signup_v2():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    try:
        hash_value = hashlib.sha256(request.form['password'].encode()).hexdigest()
        c.execute("INSERT INTO USER_HASH (USERNAME, HASH) "
                  "VALUES (?, ?)", (request.form['username'], hash_value))
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return "username has been registered."
    conn.close()
    return "signup success"

def verify_hash(username, password):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    query = "SELECT HASH FROM USER_HASH WHERE USERNAME = ?"
    c.execute(query, (username,))
    records = c.fetchone()
    conn.close()
    if not records:
        return False
    return records[0] == hashlib.sha256(password.encode()).hexdigest()

@app.route('/login/v2', methods=['GET', 'POST'])
def login_v2():
    if request.method == 'POST':
        if verify_hash(request.form['username'], request.form['password']):
            return 'login success'
        else:
            return 'Invalid username/password'
    else:
        return 'Invalid Method'

if __name__ == '__main__':
    create_database()
    app.run(host='0.0.0.0', port=9500, ssl_context='adhoc')

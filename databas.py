import sqlite3
DB_FIL = "bibliotek.db"
def skapa_databas():
    try:
        conn = sqlite3.connect(DB_FIL)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bocker (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titel TEXT NOT NULL,
                forfattare TEXT NOT NULL
                year INTEGER NOT NULL
            )
        """)
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return e
def lagg_till_bok(titel, forfattare, year):
    try:
        conn = sqlite3.connect(DB_FIL)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bocker (titel, forfattare, year) VALUES (?, ?, ?)", (titel, forfattare, year))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        return e
def sok_bok(nyckelord):
    try:
        conn = sqlite3.connect(DB_FIL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bocker WHERE titel LIKE ? OR forfattare LIKE ? OR year LIKE ?", 
                       ('%' + nyckelord + '%', '%' + nyckelord + '%', '%' + nyckelord + '%'))
        resultat = cursor.fetchall()
        conn.close()
        for bok in resultat:
            # Returnera bokinformationen i ett läsbart format
            return bok
        if not resultat:
            return None
    except Exception as e:
        return e

def hämta_alla_bocker():
    try:
        conn = sqlite3.connect(DB_FIL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bocker")
        resultat = cursor.fetchall()
        conn.close()
        return resultat
    except Exception as e:
        return e

def visa_alla_bocker():
    try:
        conn = sqlite3.connect(DB_FIL)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM bocker")
        resultat = cursor.fetchall()
        conn.close()

        böcker = []
        for bok in resultat:
            böcker.append(bok)
        if not böcker:
            return None
        return böcker
    except Exception as e:
        return e
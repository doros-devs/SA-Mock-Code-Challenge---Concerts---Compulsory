import sqlite3

class Venue:
    def __init__(self, id, title, city):
        self.id = id
        self.title = title
        self.city = city

    @staticmethod
    def create(title, city):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO venues (title, city) VALUES (?, ?)", (title, city))
        conn.commit()
        conn.close()

    def concerts(self):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM concerts WHERE venue_id = ?", (self.id,))
        concerts = cur.fetchall()
        conn.close()
        return concerts

    def bands(self):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute("""
            SELECT DISTINCT bands.*
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            WHERE concerts.venue_id = ?
        """, (self.id,))
        bands = cur.fetchall()
        conn.close()
        return bands


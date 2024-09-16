import sqlite3

from concert import Concert


class Band:
    def __init__(self, id, name, hometown):
        self.id = id
        self.name = name
        self.hometown = hometown

    @staticmethod
    def create(name, hometown):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO bands (name, hometown) VALUES (?, ?)", (name, hometown))
        conn.commit()
        conn.close()


    def concerts(self):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM concerts WHERE band_id = ?", (self.id,))
        concerts = cur.fetchall()
        conn.close()
        return concerts

    def venues(self):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute("""
            SELECT DISTINCT venues.*
            FROM concerts
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.band_id = ?
        """, (self.id,))
        venues = cur.fetchall()
        conn.close()
        return venues

    def play_in_venue(self, venue, date):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)",
            (self.id, venue.id, date)
        )
        conn.commit()
        conn.close()

    def all_introductions(self):
        concerts = self.concerts()
        introductions = []
        for concert in concerts:
            c = Concert(concert[0], concert[1], concert[2], concert[3])
            introductions.append(c.introduction())
        return introductions

    @staticmethod
    def most_performances():
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute("""
            SELECT bands.*, COUNT(concerts.id) as concert_count
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            GROUP BY bands.id
            ORDER BY concert_count DESC
            LIMIT 1
        """)
        band = cur.fetchone()
        conn.close()
        return band
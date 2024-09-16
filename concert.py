import sqlite3

class Concert:
    def __init__(self, id, band_id, venue_id, date):
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date

    @staticmethod
    def create(band_id, venue_id, date):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?)",
            (band_id, venue_id, date)
        )
        conn.commit()
        conn.close()

    def band(self):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM bands WHERE id = ?", self.band_id)
        band = cur.fetchone()
        conn.close()
        return band

    def venue(self):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM venues WHERE id = ?", self.venue_id)
        venue = cur.fetchone()
        conn.close()
        return venue

    def hometown_show(self):
        conn = sqlite3.connect('concerts.db')
        cur = conn.cursor()
        cur.execute('''
            SELECT concerts.id
            FROM concerts
            JOIN bands ON concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE bands.id = ? AND venues.city = bands.hometown
        ''', self.band_id)
        result = cur.fetchone()
        conn.close()
        return result

    def introduction(self):
        band = self.band()
        venue = self.venue()
        return f"Hello {venue[2]}!!!!! We are {band[1]} and we're from {band[2]}"


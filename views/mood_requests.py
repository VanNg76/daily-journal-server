import json
import sqlite3
from models import Mood

def get_all_moods():
    """Get all moods"""
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
            SELECT
                m.id,
                m.label
            FROM moods m
        """)

        # Initialize an empty list to hold all moods representations
        moods = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a mood instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Entry class above.
            mood = Mood(row['id'], row['label'])

            moods.append(mood.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(moods)

def get_single_mood(id):
    """get single mood"""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                m.id,
                m.label
            FROM moods m
            WHERE id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        mood = Mood(data['id'], data['label'])
        mood = mood.__dict__

    return json.dumps(mood)

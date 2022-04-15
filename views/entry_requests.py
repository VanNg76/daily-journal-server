import json
import sqlite3
from models import Entry, Mood

def get_all_entries():
    """Get all entries"""
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
            SELECT
                e.id,
                e.concept,
                e.entry,
                e.mood_id,
                e.date,
                m.label mood_label
            FROM entries e
            JOIN moods m
                ON m.id = e.mood_id
        """)

        # Initialize an empty list to hold all entries representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an entry instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Entry class above.
            entry = Entry(row['id'], row['concept'], row['entry'], row['mood_id'], row['date'])
            mood = Mood(row['mood_id'], row['mood_label'])

            entry.mood = mood.__dict__

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)


def get_single_entry(id):
    """get single entry"""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                e.id,
                e.concept,
                e.entry,
                e.mood_id,
                e.date,
                m.label mood_label
            FROM entries e
            JOIN moods m
                ON m.id = e.mood_id
            WHERE e.id = ?
        """, (id, ))

        data = db_cursor.fetchone()

        entry = Entry(data['id'], data['concept'], data['entry'], data['mood_id'], data['date'])
        mood = Mood(data['mood_id'], data['mood_label'])

        entry.mood = mood.__dict__

        entry = entry.__dict__

    return json.dumps(entry)


def delete_entry(id):
    """delete an entry"""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM entries
            WHERE id = ?
        """, (id, ))


def update_entry(id, new_entry):
    """update single entry"""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE entries
        SET
            concept = ?,
            entry = ?,
            mood_id = ?,
            date = ?
        WHERE id = ?
        """, (new_entry['concept'], new_entry['entry'],
              new_entry['mood_id'], new_entry['date'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


def create_entry(new_entry):
    """create new entry"""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO entries
            ( concept, entry, mood_id, date )
        VALUES
            ( ?, ?, ?, ? )
        """, (new_entry['concept'], new_entry['entry'],
              new_entry['moodId'], new_entry['date'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id


    return json.dumps(new_entry)


def search_entries(searched_term):
    """search entries"""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
            SELECT
                e.id,
                e.concept,
                e.entry,
                e.mood_id,
                e.date,
                m.label mood_label
            FROM entries e
            JOIN moods m
                ON m.id == e.mood_id
            WHERE e.entry LIKE ?
        """, (f"%{searched_term}%", ))

        matching_entries = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            entry = Entry(row['id'], row['concept'], row['entry'], row['mood_id'], row['date'])
            mood = Mood(row['mood_id'], row['mood_label'])
            entry.mood = mood.__dict__
            matching_entries.append(entry.__dict__)

        return json.dumps(matching_entries)

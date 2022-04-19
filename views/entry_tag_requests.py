import json
import sqlite3
from models import Entry_Tag

def get_all_entries_tags():
    """Get all entries_tags"""
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
            SELECT
                et.id,
                et.entry_id
                et.tag_id
            FROM entries_tags et
        """)

        # Initialize an empty list to hold all moods representations
        entries_tags = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create a mood instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Entry class above.
            entry_tag = Entry_Tag(row['id'], row['entry_id'], row['tag_id'])

            entries_tags.append(entry_tag.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries_tags)


def create_entry_tag(new_entry_tag):
    """create new entry_tag"""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()
        conn.row_factory = sqlite3.Row

        db_cursor.execute("""
        INSERT INTO entries_tags ( entry_id, tag_id )
        VALUES ( ?, ? )
        """, (new_entry_tag['entry_id'], new_entry_tag['tag_id'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry_tag['id'] = id

    return json.dumps(new_entry_tag)

def delete_entry_tag(id):
    """delete an entry_tag"""
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
            DELETE FROM entries_tags
            WHERE id = ?
        """, (id, ))

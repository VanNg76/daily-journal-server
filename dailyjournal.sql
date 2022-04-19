CREATE TABLE entries (
id INTEGER PRIMARY KEY AUTOINCREMENT,
concept TEXT,
entry TEXT,
mood_id INT,
date TEXT,
FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);

DROP TABLE entries;

CREATE TABLE moods (
id INTEGER PRIMARY KEY AUTOINCREMENT,
label TEXT
);

CREATE TABLE tags (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT
);

CREATE TABLE entries_tags (
id INTEGER PRIMARY KEY AUTOINCREMENT,
entry_id INT,
tag_id INT,
FOREIGN KEY(`entry_id`) REFERENCES `entries`(`id`),
FOREIGN KEY(`tag_id`) REFERENCES `tags`(`id`)
);

INSERT INTO entries VALUES (null, "Javascript", "I learned about loops today.", 1, "Wed Sep 15 2021 10:10:47");
INSERT INTO entries VALUES (null, "Python", "Python is named after the Monty Python comedy group from the UK.", 2, "Wed Sep 15 2021 10:11:33");
INSERT INTO entries VALUES (null, "Python", "Why did it take so long for python to have a switch statement?", 3, "Wed Sep 15 2021 10:13:11");
INSERT INTO entries VALUES (null, "Javascript", "Dealing with Date is terrible", 4, "Wed Sep 16 2021 10:10:47 ");

INSERT INTO moods VALUES (NULL, "Sad");
INSERT INTO moods VALUES (NULL, "Happy");
INSERT INTO moods VALUES (NULL, "Angry");
INSERT INTO moods VALUES (NULL, "OK");

INSERT INTO tags VALUES (NULL, "SQL");
INSERT INTO tags VALUES (NULL, "Python");
INSERT INTO tags VALUES (NULL, "Javascript");

INSERT INTO entries_tags VALUES (NULL, 1, 2);
INSERT INTO entries_tags VALUES (NULL, 1, 3);
INSERT INTO entries_tags VALUES (NULL, 3, 1);
INSERT INTO entries_tags VALUES (NULL, 3, 3);
INSERT INTO entries_tags VALUES (NULL, 4, 1);
INSERT INTO entries_tags VALUES (NULL, 4, 2);
INSERT INTO entries_tags VALUES (NULL, 4, 3);

delete from entries_tags
where id =4;

SELECT
    et.id,
    et.entry_id,
    et.tag_id,
    e.concept entry_concept,
    t.name tag_name
FROM entries_tags et, entries e
JOIN tags t
    ON t.id = et.tag_id
WHERE et.entry_id = e.id AND et.tag_id = t.id;

SELECT *
FROM entries_tags et
WHERE et.entry_id = ?

SELECT
    et.id,
    et.entry_id,
    et.tag_id,
    en.id entry_entry_id
FROM entries_tags et
JOIN entries en
    ON et.entry_id = en.id
WHERE et.entry_id = 1;

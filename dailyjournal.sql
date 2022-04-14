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

INSERT INTO entries VALUES (null, "Javascript", "I learned about loops today.", 1, "Wed Sep 15 2021 10:10:47");
INSERT INTO entries VALUES (null, "Python", "Python is named after the Monty Python comedy group from the UK.", 2, "Wed Sep 15 2021 10:11:33");
INSERT INTO entries VALUES (null, "Python", "Why did it take so long for python to have a switch statement?", 3, "Wed Sep 15 2021 10:13:11");
INSERT INTO entries VALUES (null, "Javascript", "Dealing with Date is terrible", 4, "Wed Sep 16 2021 10:10:47 ");

INSERT INTO moods VALUES (NULL, "Sad");
INSERT INTO moods VALUES (NULL, "Happy");
INSERT INTO moods VALUES (NULL, "Angry");
INSERT INTO moods VALUES (NULL, "OK");


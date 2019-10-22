import sqlite3


dbfile = "../holding.db"

db = sqlite3.connect(dbfile)
c = db.cursor()


def update(table, edit):
    current = "SELECT story_text FROM stories WHERE story_id = {}"
    command = current.format()


def insert(table, param1, param2):
    outline = "INSERT INTO {} VALUES({}, {})"
    command = outline.format(table, param1, param2)
    c.execute(command)

def insert(table, param1, param2, param3):
    outline = "INSERT INTO {} VALUES({}, {}, {})"
    command = outline.format(table, param1, param2, param3)
    c.execute(command)

def insert(table, param1, param2, param3, param4):
    outline = "INSERT INTO {} VALUES({}, {}, {}, {})"
    command = outline.format(table, param1, param2, param3, param4)
    c.execute(command)


db.commit()
db.close()

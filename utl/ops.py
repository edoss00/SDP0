import sqlite3


dbfile = "../holding.db"

db = sqlite3.connect(dbfile)
c = db.cursor()


def update(story, edit):
    current = ""
    outline = "SELECT story_text FROM stories WHERE story_id = {};"
    command = outline.format(story)
    q = c.execute(command)
    for bar in q:
      current = bar[0] + edit
    outline = "UPDATE stories SET story_text = {}, last_edit = {} WHERE story_id = {};"
    command = outline.format(current, edit, story)
 
    
    


def insert(table, param1, param2):
    outline = "INSERT INTO {} VALUES({}, {});"
    command = outline.format(table, param1, param2)
    c.execute(command)

def insert(table, param1, param2, param3):
    outline = "INSERT INTO {} VALUES({}, {}, {});"
    command = outline.format(table, param1, param2, param3)
    c.execute(command)

def insert(table, param1, param2, param3, param4):
    outline = "INSERT INTO {} VALUES({}, {}, {}, {});"
    command = outline.format(table, param1, param2, param3, param4)
    c.execute(command)


db.commit()
db.close()

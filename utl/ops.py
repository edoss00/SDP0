import sqlite3


dbfile = "../holding.db"

db = sqlite3.connect(dbfile)
c = db.cursor()


def update(user, story, edit):
    current = ""
    outline = "SELECT story_text FROM stories WHERE story_id = {};"
    command = outline.format(story)
    q = c.execute(command)
    for bar in q:
      current = bar[0] + edit
    outline = "UPDATE stories SET story_text = {}, last_edit = {} WHERE story_id = {};"
    command = outline.format(current, edit, story)
 
    outline = "INSERT INTO edits VALUES ({}, {}, {});"
    command = outline.format(user, story, edit)
    c.execute(command)
    


def insert(table, *params):
    begin = "INSERT INTO {} VALUES ({}"
    start = begin.format(table, params[0])
    end = ");"
    middle = ""
    for x in params[1:]:
      in = ", {}"
      put = in.format(x)
      middle += put
    command = start + middle + end
    c.execute(command)




def has_edited(user, story):
    outline = "SELECT * FROM edits WHERE user_id = {} AND story_id = {};"
    command = outline.format(user, story)
    q = c.execute(command)
    for bar in q:
      return True
    return False


db.commit()
db.close()

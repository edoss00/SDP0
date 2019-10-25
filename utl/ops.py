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
    return command

def insert(table, *params):
    begin = "INSERT INTO {} VALUES ({}"
    start = begin.format(table, params[0])
    end = ");"
    middle = ""
    for x in params[1:]:
      if table == 'edits':
        d = ", {}"
      else:
        d = ", \"{}\""
      put = d.format(x)
      middle += put
    command = start + middle + end
    return command


db.commit()
db.close()

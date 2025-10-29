import sqlite3

conn = sqlite3.connect('newsEvents.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS questionsMain")
conn.commit()

cursor.execute("CREATE TABLE IF NOT EXISTS questionsMain (ID INTEGER PRIMARY KEY AUTOINCREMENT,question TEXT, questionGroup INT)")
conn.commit()
#Ob es verkehrliche Einschränkungen gibt?

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wo sind die verkehrlichen Einschränkungen?",1))
conn.commit()

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wann sind die verkehrlichen Einschränkungen?",1))
conn.commit()

'''
cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wo sind die verkehrlichen Einschränkungen?",1))
conn.commit()

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wann sind verkehrliche Einschränkungen?",1))
conn.commit()

#####
cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wann war die Autobahn für den Verkehr freigegeben??",2))
conn.commit()

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wann wird die Autobahn für den Verkehr freigegeben?",2))
conn.commit()

###
cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wann war die Autobahn für den Verkehr gesperrt?",2))
conn.commit()

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wie lange war die Autobahn gesperrt?",2))
conn.commit()

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wann wird die Autobahn für den Verkehr gesperrt?",2))
conn.commit()

###

###3
cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Welche Autobahn war für den Verkehr freigegeben?",2))
conn.commit()

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Welche Autobahn wird für den Verkehr freigegeben?",2))
conn.commit()

###4
cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Welche Autobahn war für den Verkehr gesperrt?",2))
conn.commit()

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Welche Autobahn wird für den Verkehr gesperrt?",2))
conn.commit()
###

###5
cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wann war die Autobahnstrecke für den Verkehr freigegeben?",2))
conn.commit()

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wie lange war die Autobahnstrecke freigegeben?",2))
conn.commit()

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wann wird die Autobahnstrecke für den Verkehr freigegeben?",2))
conn.commit()
###

###6
cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wann war die Autobahnstrecke für den Verkehr gesperrt?",2))
conn.commit()

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wie lange war die Autobahnstrecke gesperrt?",2))
conn.commit()

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Wann wird die Autobahnstrecke für den Verkehr gesperrt?",2))
conn.commit()
###

###7
cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Welche Autobahnstrecke war für den Verkehr freigegeben?	",2))
conn.commit()

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Welche Autobahnstrecke wird für den Verkehr freigegeben?",2))
conn.commit()

###8
cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Welche Autobahnstrecke war für den Verkehr gesperrt?",2))
conn.commit()

cursor.execute("INSERT INTO questionsMain (question,questionGroup) VALUES(?,?)",("Welche Autobahnstrecke wird für den Verkehr gesperrt?",2))
conn.commit()




cursor.execute(" INSERT INTO articlesMain (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
        conn.commit()
'''
conn.close()
import sqlite3

conn = sqlite3.connect('newsEvents.db')
cursor = conn.cursor()    

createstr = '''DROP TABLE IF EXISTS  answersTEST '''
cursor.execute(createstr)
conn.commit()

#createDB statement
createstr = '''CREATE TABLE answersTEST (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  id_article INTEGER, id_question INTEGER, answer TEXT)'''
cursor.execute(createstr)
conn.commit()

for i in range(1,11,1):
    cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(i,1,""))
    conn.commit()
    cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(i,2,""))
    conn.commit()
#----------------------------------------
answer='''A5, Fahrtrichtung Kassel: Montag, 21. April bis Freitag, 26. September 2025, Sperrung der inneren Hauptfahrbahn; Lkw-Umleitung über die Parallelspur.
    Im Rahmen der eingerichteten Baustellenverkehrsführung steht auch der nach rechts verschwenkte Fahrstreifen dem Verkehr in Fahrtrichtung Kassel zur Verfügung. Der Verkehr, der diesen Fahrstreifen nutzt, wird nicht ausgeleitet, sondern an dessen Ende wieder auf die Hauptfahrbahn der A5 geführt, siehe Skizze oben.
    '''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(11,1,answer))
conn.commit()

answer='''A5, Fahrtrichtung Basel: Montag, 28. April bis Freitag, 3. Oktober 2025, Sperrung der inneren Hauptfahrbahn;
          Lkw-Umleitung über die Parallelspur.'''

cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(11,1,answer))
conn.commit()
    
answer = '''Während der gesamten Bauzeit ist die Sperrung der Ausfahrt von der A5 in Fahrtrichtung Basel zur A66 in Fahrtrichtung Frankfurt-Miquelallee notwendig.
    Umleitung: Die Umleitung erfolgt über die A5, das Westkreuz Frankfurt, die A648 und das Autobahndreieck Eschborn.'''

cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(11,1,answer))
conn.commit()

answer='''Montag, 21. April bis Freitag, 26. September 2025'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(11,2,answer))
conn.commit()
   
answer='''Montag, 28. April bis Freitag, 3. Oktober 2025'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(11,2,answer))
conn.commit()
#-------------------------------------------------------------

answer='''Die Autobahn Westfalen bricht an diesem Wochenende (21.-24.2.) unter Vollsperrung der A1 an der Anschlussstelle 
Osnabrück-Nord bei Wallenhorst eine Brücke ab. 
In dieser Zeit fließt der Verkehr mit einer Spur je Richtung auf dem westlichen Bauwerk. 
Steht der Neubau, wird der komplette Verkehr darauf umgelegt und das westliche Bauwerk wird abgebrochen und neu errichtet.
 '''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(12,1,answer))
conn.commit()

answer=''' an diesem Wochenende (21.-24.2.)
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(12,2,answer))
conn.commit()
#--------------------------------------------------------------

answer='''Am Freitag, 19 Uhr, wurde die A1 pünktlich gesperrt, die umfangreichen Arbeiten zum Abbruch der Brücke begannen. 
Am Montagmorgen um 6 Uhr der Verkehr auf der A1 zwischen Lübeck und Hamburg wieder fließen konnte.
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(13,1,answer))
conn.commit()

answer='''Am Freitag, 19 Uhr'''

cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(13,2,answer))
conn.commit()

answer='''Am Montagmorgen um 6 Uhr'''

cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(13,2,answer))
conn.commit()


#-------------------------------------------------------------

answer='''Die Autobahnmeisterei Hagen der Autobahnniederlassung Westfalen hat seit dem frühen Samstagabend (30.11.) die Polizei bei der Absicherung der Unfallstelle auf der A1 und Sperrung der Strecke zwischen Volmarstein und Hagen-West unterstützt.
Fünf Lkw, sieben Sicherungstafeln und vier Vorwarner wurden auf der A1 aufgebaut, um den Verkehr an den Anschlussstellen Gevelsberg und Hagen-West von der A1 abzuleiten.
Noch in der Nacht hat die Autobahnmeisterei zudem Teile der mobilen Gleitwände zwischen den Anschlussstellen abgebaut, damit die Polizei nach der Unfallaufnahme den Stau dort auflösen und die Verkehrsteilnehmenden von der Autobahn leiten konnte. 
Die Autobahnmeisterei Remscheid der Niederlassung Rheinland hat am Samstagabend im Zusammenhang mit der Unfallfahrt des Lkw zudem einen Streckenabschnitt der A46 gesperrt, der aber kurze Zeit später wieder freigegeben werden konnte. 
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(14,1,answer))
conn.commit()

answer='''seit dem frühen Samstagabend (30.11.)'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(14,2,answer))
conn.commit()

answer='''am Samstagabend'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(14,2,answer))
conn.commit()


#-----------------------------------------------------------

answer='''Der Tunnel Rudower Höhe auf der A113 war für die Dauer der Übung in der Nacht vom 30.09. auf den 01.10.2024 ab 21 Uhr bis 05:00 Uhr voll gesperrt.  
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(15,1,answer))
conn.commit()

answer='''in der Nacht vom 30.09. auf den 01.10.2024 ab 21 Uhr bis 05:00 Uhr.  
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(15,2,answer))
conn.commit()

#-------------------------------------------------------------
answer='''Regionalniederlassung Ruhr sperrt am Freitagabend (26.9.) erneut die L736 (Ostenhellweg) zwischen Schachtstraße und Hellweg in Bergkamen. Grund sind Arbeiten an der Brücke, welche die L736 in Bergkamen-Rünthe über den Datteln-Hamm-Kanal führt. Der Abschnitt steht dem Verkehr ab Montagmorgen wieder zur Verfügung. Eine Umleitung führt über die Industriestraße und die B233 (Werner Straße).
Nach dem Wochenende steht dem Verkehr in diesem Bereich der L736 noch für etwa eine Woche nur ein Fahrstreifen zu Verfügung. In dieser Zeit wird der Korrosionsschutz auf das neue Querkraftgelenk aufgetragen. Der Verkehr wird mit einer Baustellenampel geregelt
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(16,1,answer))
conn.commit()

answer='''am Freitagabend (26.9.)'''

cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(16,2,answer))
conn.commit()

answer='''Nach dem Wochenende'''

cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(16,2,answer))
conn.commit()

answer='''etwa eine Woche nur'''

cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(16,2,answer))
conn.commit()


#-------------------------------------------------------------



answer='''Erster Bauabschnitt: ab Montag (29.9.)
In diesem Abschnitt wird die B57 „Kalkarer Straße“ zwischen der L18 „Berk’sche Straße“ und der „Stefan-Paeßens-Straße“ voll gesperrt. Auch der Geh- und Radweg entlang der L18 zwischen der B57 und der K5 „Sommerlandstraße“ ist in dieser Zeit nicht nutzbar. Der Verkehr wird in beide Richtungen über den „Johann-van-Aken-Ring“, die K27 „Alte Bahn / Römerstraße“ und die B67 „Gocher Straße“ umgeleitet. An der Kreuzung „Johann-van-Aken-Ring“ / „Alte Bahn“ kommt eine mobile LSA zum Einsatz. Der Fuß- und Radverkehr wird über den „Schafweg“ und die Straße „Tillerfeld“ umgeleitet.
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(17,1,answer))
conn.commit()

answer='''Zweiter Bauabschnitt: ab Montag (13.10.)
Im zweiten Schritt wird die L18 „Berk’sche Straße“ in beiden Richtungen voll gesperrt. Die Bauzeit beträgt voraussichtlich acht Wochen. 
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(17,1,answer))
conn.commit()

answer=''' ab Montag (29.9.)'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(17,2,answer))
conn.commit()

answer=''' ab Montag (13.10.)'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(17,2,answer))
conn.commit()

#-----------------------------------------------------------


answer='''Der Landesbetrieb Straßenbau Nordrhein-Westfalen saniert ab Freitag, 26.9., den B51-Abzweig im Bereich Dahlem in Richtung Hellenthal und Udenbreth zwischen der B51 und der L110.
Die rund 600 Meter lange Verbindung zwischen B51 und L110 wird bis voraussichtlich Montag, 6.10., unter Vollsperrung erneuert.
Der Verkehr in Richtung Hellenthal, Udenbreth und Dahlemer Binz wird ab der B51 (Abzweig in Fahrtrichtung Dahlem) über die Schmidtheimer Straße (L110) umgeleitet.
'''

cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(18,1,answer))
conn.commit()

answer= '''ab Freitag, 26.9.'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(18,2,answer))
conn.commit()
#-----------------------------------------------------------


answer='''Die Straßen.NRW-Regionalniederlassung Ruhr beseitigt Straßenschäden auf der B227 (Halterner Straße) in Essen. Ab Montag (29.9.) ist die B227 deshalb zwischen Krayer Straße und A40 in Fahrtrichtung Süden gesperrt. Damit ist zwei Wochen lang auch die Auffahrt zur A40 an der Anschlussstelle Gelsenkirchen-Süd gesperrt. Die Abfahrt von der A40 in Richtung Gelsenkirchen-Innenstadt steht dem Verkehr während der Arbeiten zur Verfügung. Zudem ist die Kemnastraße in Bochum-Wattenscheid nicht von der B227 aus erreichbar, auch die Zufahrt zur B227 ist nicht möglich. Lokale Umleitungen zu den A40-Anschlussstellen Bochum-Wattenscheid-West und Essen-Kray sind ausgeschildert. Auf den Umleitungsstrecken gelten zum Teil zusätzliche Halteverbote.
'''

cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(19,1,answer))
conn.commit()

answer='''Ab Montag (29.9.)'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(19,2,answer))
conn.commit()

#-----------------------------------------------------------
answer='''Dafür wird ab dem morgigen Freitag, 26. September, der Kreuzungsbereich der Bundesstraße mit dem Stadtring Kattenstroth/Kiebitzstraße bis zur Einmündung Auf’m Kampe gesperrt.
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(20,1,answer))
conn.commit()

answer='''Anpassung der Umleitung
Der Verkehr in Richtung Gütersloh wird von der Brockstraße rechts in den Stadtring Kattenstroth und dann weiter auf die Neuenkirchener Straße (L782) geführt.
Die Umleitung in Richtung Rheda-Wiedenbrück ändert sich nicht.
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(20,1,answer))
conn.commit()

answer='''Freitag, 26. September'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(20,2,answer))
conn.commit()

#-----------------------------------------------------------

answer='''Die Stützwand im Zuge der Waterloostraße (B238) im Kalletal bekommt ein neues Geländer: Zwischen Montag und Donnerstag, 29. September bis 2. Oktober, wird deshalb der Geh-/Radweg gesperrt sowie die Geschwindigkeit für den motorisierten Verkehr auf Tempo 50 reduziert.
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(21,1,answer))
conn.commit()

answer=''' Zwischen Montag und Donnerstag, 29. September bis 2. Oktober'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(21,2,answer))
conn.commit()


#-----------------------------------------------------------

answer='''Für diesen wird die Sperrung im Bereich der Autobahnbrücke weiter ausgeweitet. Eine Auffahrt auf die A43 Münster und eine Abfahrt aus Wuppertal kommend ist bereits morgen früh vor dem Berufsverkehr nicht mehr möglich. Auch die Zufahrt zum Grenzweg wird gesperrt. Die Sanierungsarbeiten der Fahrbahn der L611 sind bereits weitgehend realisiert. Voraussichtlich ab Ende der kommenden Woche kann der Streckenabschnitt von der Autobahnbrücke in Richtung Coesfeld bis zur Anschlussstelle der B474 wieder freigegeben werden. Für die Brückenarbeiten und die Umgestaltung der Strecke im Bereich des Grenzweges ist eine Sperrung noch bis Ende November geplant. Auch der hier liegende Mitfahrerparkplatz bleibt gesperrt. Eine Umleitung über Dülmen-Nord ist ausgeschildert.
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(22,1,answer))
conn.commit()

answer='''ab Ende der kommenden Woche'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(22,2,answer))
conn.commit()

answer='''bis Ende November '''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(22,2,answer))
conn.commit()

#-----------------------------------------------------------
answer='''Aus diesem Grund muss die L914 in dem Bereich voll gesperrt werden. Nach Aufhebung der Elektrifizierung sind die vorhandenen Platten nicht mehr notwendig und müssen fachgerecht abgebrochen werden, um die Verkehrssicherheit des Bauwerks langfristig zu gewährleisten.
Eine Umleitung wird über die L743 Meschede-Enste, L840 -Calle nach -Wennemen und umgekehrt eingerichtet. 
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(23,1,answer))
conn.commit()


#----------------------------------------------------------



#-----------------------------------------------------------
answer='''Für die Entfernung von sogenannten Elektroschutzplatten, die mit Ihrer isolierenden Wirkung vor unter Spannung stehenden Teilen schützen und nach Aufhebung der Elektrifizierung der Bahnstrecke nicht mehr benötigt werden, wird die Antoniusbrücke im Zuge der B55 verkehrlich eingeschränkt. Zwischen dem 29. September und dem 4. Oktober wird in beiden Richtungen jeweils ein Fahrstreifen gesperrt.
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(24,1,answer))
conn.commit()

answer="Zwischen dem 29. September und dem 4. Oktober"
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(24,2,answer))
conn.commit()
#-----------------------------------------------------------
answer='''Aus diesem Grund steht Verkehrsteilnehmenden am Mittwoch (24.9.) in Fahrtrichtung Lünen zwischen 9 und 15 Uhr nur ein Fahrstreifen zur Verfügung. Am Donnerstag (25.9.) ist einer von zwei Fahrstreifen in Fahrtrichtung Schwerte gesperrt. Zudem ist am Mittwoch die Verbindung von der B1 in Richtung Dortmund-Zentrum auf die B236 in Richtung Lünen gesperrt. Eine Umleitung ist eingerichtet.
'''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(25,1,answer))
conn.commit()

answer=''' am Mittwoch (24.9.) '''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(25,2,answer))
conn.commit()

answer='''  Am Donnerstag (25.9.)  '''
cursor.execute(" INSERT INTO answersTEST (id_article, id_question, answer) VALUES (?,?,?)",(25,2,answer))
conn.commit()
#-----------------------------------------------------------

conn.close()
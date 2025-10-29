import sqlite3

conn = sqlite3.connect('newsEvents.db')
cursor = conn.cursor()

#cursor.execute("DROP TABLE articlesTESTSET")
cursor.execute('''CREATE TABLE articlesTESTSET (ID INTEGER PRIMARY KEY AUTOINCREMENT,
articleDate TEXT, articleText TEXT)''')#conn.commit()

cursor.execute(''' INSERT INTO articlesTESTSET(articleDate,articleText)
                SELECT articleDate,articleText FROM articlesMAIN WHERE ID >= 1 AND ID <= 10''') 
conn.commit()

#----------------------

articleText ='''Im Zuge der ersten Bauphase bleiben auf der Hauptfahrbahn der A5 jeweils zwei Fahrstreifen pro Fahrtrichtung für den Verkehr geöffnet. Folgende verkehrliche Einschränkungen sind notwendig:
    A5, Fahrtrichtung Kassel: Montag, 21. April bis Freitag, 26. September 2025, Sperrung der inneren Hauptfahrbahn; Lkw-Umleitung über die Parallelspur.
    Im Rahmen der eingerichteten Baustellenverkehrsführung steht auch der nach rechts verschwenkte Fahrstreifen dem Verkehr in Fahrtrichtung Kassel zur Verfügung. Der Verkehr, der diesen Fahrstreifen nutzt, wird nicht ausgeleitet, sondern an dessen Ende wieder auf die Hauptfahrbahn der A5 geführt, siehe Skizze oben.
    A5, Fahrtrichtung Basel: Montag, 28. April bis Freitag, 3. Oktober 2025, Sperrung der inneren Hauptfahrbahn; Lkw-Umleitung über die Parallelspur.
    Die Baustelleneinrichtung in beide Fahrtrichtungen beginnt am Montag, 7. April 2025.
    Während der gesamten Bauzeit ist die Sperrung der Ausfahrt von der A5 in Fahrtrichtung Basel zur A66 in Fahrtrichtung Frankfurt-Miquelallee notwendig.
    Umleitung: Die Umleitung erfolgt über die A5, das Westkreuz Frankfurt, die A648 und das Autobahndreieck Eschborn.
Die Verkehrseinschränkungen bestehen auf einer Länge von etwa 1,6 Kilometern. Über die weiteren Bauphasen wird gesondert informiert.
In die Gesamtmaßnahme investiert die Autobahn GmbH ca. 3,8 Millionen Euro.
Es wird empfohlen, auf die Verkehrsmeldungen im Rundfunk zu achten, etwaige Störungen bei der Routenplanung zu berücksichtigen und angemessene Fahrzeit für die Umleitungsstrecke einzuplanen.
Die Autobahn GmbH bittet die Verkehrsteilnehmenden um eine umsichtige Fahrweise im Baustellenbereich und Verständnis für die aufgrund der notwendigen Arbeiten unvermeidbaren Verkehrsbeeinträchtigungen.
'''
datetime_value="2025-09-19"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()

#------------------

articleText ='''Wallenhorst. Der Startschuss ist gefallen. Die Autobahn Westfalen bricht an diesem Wochenende (21.-24.2.) unter Vollsperrung der A1 an der Anschlussstelle Osnabrück-Nord bei Wallenhorst eine Brücke ab. Das Bauwerk stammt aus dem Jahr 1967 und führt die B68 über die Autobahn. Sieben Bagger zerlegen aktuell das erste von zwei Teilbauwerken, damit an gleicher Stelle ein neues entstehen kann. „Die Brücke muss ersetzt werden, da ihre Tragfähigkeit nicht mehr ausreicht, um den gestiegenen Belastungen standzuhalten“, erklärt Philip Overbeck, Geschäftsbereichsleiter Bau und Erhaltung bei der Autobahn Westfalen in der Außenstelle Osnabrück. 
Doch bevor die mit Stemmhämmern und Abbruchscheren ausgerüsteten Bagger in der Nacht zu Samstag (22.2.) mit dem Rückbau der rund 86 Meter langen Brücke starten konnten, mussten noch einige Vorarbeiten geleistet werden: Auf der Brücke wurden auf rund 1.350 Quadratmetern der Belag abgefräst, die Schutzplanken zurückgebaut, Geländer und Schilder demontiert sowie die Widerlager freigelegt. Auf dem vorerst verbleibenden westlichen Teilbauwerk wurde ein Sichtschutz montiert, damit der Verkehr dort künftig sicher fließen kann, ohne durch die daneben stattfindenden Brückenarbeiten während der Bauzeit abgelenkt zu werden. 
2000 Tonnen Betonabbruch müssen zerkleinert werden
„Die beiden Bauwerke stehen in einem Abstand von nur wenigen Zentimetern nebeneinander. Beim Abbruch müssen wir auch darauf achten, dass das westliche Bauwerk unbeschadet bleibt, denn darauf fließt ja künftig der gesamte Verkehr der B68“, erklärt Aylin Pohl, Projektleiterin bei der Autobahn Westfalen in der Außenstelle Osnabrück. 
Auch unter der Brücke musste alles vorbereitet werden, bevor der erste Bagger den Stemmhammer ansetzen konnte. Es wurden insgesamt 400 Meter Betonschutzwände aufgenommen, ein Arbeitsbereich für die Baufahrzeuge errichtet sowie ein Fallbett aufgeschüttet. 1.000 Kubikmeter Sand sorgen unter der Brücke dafür, dass die herabfallenden Teile die darunterliegende Fahrbahn nicht beschädigen.   
Sind Brücke und Mittelpfeiler „gefallen“, geht es unter Hochdruck weiter: Rund 2.000 Tonnen Betonbruch müssen zerkleinert, aufgeladen und mit etwa 100 Lkw-Ladungen abtransportiert werden. Danach wird die Fahrbahn mit einer Kehrmaschine gereinigt, es werden Schutzeinrichtungen montiert und eine Baustellenverkehrsführung auf der A1 eingerichtet. Die Arbeiten laufen unter dem Einsatz von Flutlicht Tag und Nacht. Über 30 Mitarbeitende sind dafür am gesamten Wochenende im Einsatz.
Nach Freigabe der Autobahn am Montagmorgen (24.2.) um 4 Uhr wird der Verkehr auf Höhe der Anschlussstelle Osnabrück-Nord in einer Baustellenverkehrsführung fließen. Dabei werden alle Fahrspuren aufrechterhalten. Nach Ausführung von Restarbeiten, wie dem vollständigen Rückbau der Widerlager, kann der Neubau in einigen Wochen an Fahrt aufnehmen. 
Hintergrund zur Baumaßnahme
Täglich fahren 27.000 Fahrzeuge über das B68 Bauwerk, darunter 1.400 Lkw. Die Bundesstraße ist ein wichtiger Verbindungsweg aus Wallenhorst und Bramsche sowie anderen Orten im Nordkreis nach Osnabrück. Zuletzt wurden bereits Maßnahmen wie Reduzierung von Fahrsteifen und Abstandsgebote ergriffen, um das Bauwerk unter Verkehr halten zu können. 
Ersetzt wird es in den kommenden Monaten durch einen Neubau nach modernstem technischen Standard, der von allen im Straßenverkehr zugelassenen Fahrzeugen befahren werden kann.  Die Brücke besteht aus zwei Teilbauwerken, eines für jede Fahrtrichtung. 
An diesem Wochenende wird das östliche Bauwerk abgebrochen und in den kommenden Monaten erneuert. In dieser Zeit fließt der Verkehr mit einer Spur je Richtung auf dem westlichen Bauwerk. Steht der Neubau, wird der komplette Verkehr darauf umgelegt und das westliche Bauwerk wird abgebrochen und neu errichtet. '''
datetime_value="2025-09-20"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()


#--------------------

articleText ='''Um die Verkehrsbeziehungen im Autobahnkreuz dennoch aufrecht zu erhalten, wurde bereits im November letzten Jahres während einer Wochenend-Vollsperrung eine Behelfsbrücke errichtet.
Am Freitag, 19 Uhr, wurde die A1 pünktlich gesperrt, die umfangreichen Arbeiten zum Abbruch der Brücke begannen. Zuerst mussten die Schutzeinrichtungen für den fließenden Verkehr abgebaut, Schutzflies auf der Fahrbahn ausgebreitet und ein Sandbett zum Schutz der Fahrbahn einen halben Meter hoch aufgeschüttet. Erst danach durften die neun Baumaschinen mit den unterschiedlichsten Aufsetzen wie Abbruchhammer und -schere, Tieflöffel, Sieb sowie Sortengreifer und Magnet in Position gebracht werden, um das alte Bauwerk zu zerlegen – immerhin galt es eine Brücke inklusive Widerlager und Mittelstütze von einer Gesamtlänge von knapp 67 Metern und einer Breite knapp 18 Metern „klein“ zu kriegen.  
Die Brückenfläche von 1173 m² mit ca. 2.000 Tonnen Abbruchmaterial mussten zerkleinert, nach Materialart sortiert und auf die bereitstehenden Lastwagen verladen werden, damit am Montagmorgen um 6 Uhr der Verkehr auf der A1 zwischen Lübeck und Hamburg wieder fließen konnte.
Insgesamt waren 40 Personen im Schichtsystem während der 59 Stunden beschäftigt, die ihr Handwerk bestens verstanden. Alle Arbeiten wurden unter dem wachsamen Auge unserer örtlichen Bauüberwachung durchgeführt.
Das Umleitungssystem? Ausgeklügelt! Sowohl die Verkehrsüberwachung der Polizei, die keine nennenswerten Staulagen verzeichnen konnten, als auch die örtliche Bauüberwachung konnten zufrieden am Montag von einem erfolgreichen Wochenende berichten!
'''
datetime_value="2025-09-21"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()


#----------------------
articleText ='''Hagen. Die Autobahnmeisterei Hagen der Autobahnniederlassung Westfalen hat seit dem frühen Samstagabend (30.11.) die Polizei bei der Absicherung der Unfallstelle auf der A1 und Sperrung der Strecke zwischen Volmarstein und Hagen-West unterstützt. Seit dem Morgen sind die Straßenwärterinnen und Straßenwärter mit Aufräum- und Reparaturarbeiten beschäftigt. Ein Lkw hatte auf der Strecke zwischen Neuss (A46) und Hagen (A1) eine Serie von Unfällen verursacht. Kurz vor Hagen-West kam das Fahrzeug schließlich quer zur Fahrbahn in einer Baustelle zum Stehen.
„Bei dem Unfall ist beinahe die komplette Baustellenverkehrsführung für den Ersatzneubau der Brücke Nöhstraße zerstört worden“, sagt der Leiter der Autobahnmeisterei Hagen, Christoph Heer. „Hier ist unser Verkehrssicherer nun seit sieben Uhr mit zwei Sattelzügen und zwei Kränen angerückt, um die zerstörten Teile ab und neue Gleitwände wieder aufzubauen.“ Heer hofft, dass diese Arbeiten bis zum späten Vormittag erledigt sind und zumindest eine Fahrtrichtung wieder freigegeben werden kann.
Die Benachrichtigung durch die Polizei erfolgte in der Autobahnmeisterei kurz vor Schichtwechsel. „Das war ein Glück, weil wir so mit der Tagschicht die Absperrungen in Hagen-West und Volmarstein noch einrichten konnten und die Nachtschicht dann übernehmen konnte. Fünf Lkw, sieben Sicherungstafeln und vier Vorwarner wurden auf der A1 aufgebaut, um den Verkehr an den Anschlussstellen Gevelsberg und Hagen-West von der A1 abzuleiten. Noch in der Nacht hat die Autobahnmeisterei zudem Teile der mobilen Gleitwände zwischen den Anschlussstellen abgebaut, damit die Polizei nach der Unfallaufnahme den Stau dort auflösen und die Verkehrsteilnehmenden von der Autobahn leiten konnte. 
Da der Lkw, der quer über der Fahrbahn zum Stillstand kam, sich bei dem Unfall den Tank aufgerissen hatte, musste die Entwässerung der Strecke von einem Fachunternehmen gespült werden. „An der Regenwasserbehandlungsanlage Vorhalle, in die die Entwässerung an diesem Punkt führt, haben wir noch in der Nacht Ölsperren aufgebaut“, so Heer. Eine erste Streckenkontrolle zwischen Wuppertal-Nord und Volmarstein ist zudem noch in der Nacht durchgeführt worden, da es auch in diesem Abschnitt Unfälle gegeben hatte. „Hier werden wir nun bei Tageslicht noch einmal genau hinschauen, ob noch etwas abzusichern ist“, sagt der Meistereileiter. 
Die Autobahnmeisterei Remscheid der Niederlassung Rheinland hat am Samstagabend im Zusammenhang mit der Unfallfahrt des Lkw zudem einen Streckenabschnitt der A46 gesperrt, der aber kurze Zeit später wieder freigegeben werden konnte. 
Update: Die Fahrtrichtung Bremen ist um 11 Uhr wieder freigegeben worden. Die Fahrtrichtung Köln folgt gegen 12 Uhr. 

'''
datetime_value="2025-09-22"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()

#------------------------

articleText ='''Solch eine Übung rettet im tatsächlichen Notfall Leben, denn im Tunnel zählt jede Sekunde. Brände stellen in Tunnelanlagen für alle Beteiligten die größte Herausforderung dar – sowohl für Verkehrsteilnehmende als auch für die Rettungskräfte. Dunkelheit, Enge, Panik – wenn es brennt, kann dies schnell in eine Katastrophe führen.
Ein ausbrechendes Feuer führt im Tunnel zu einer massiven Hitze- und extremen Rauchentwicklung, welche zu einer starken Einschränkung der Sicht und letztlich zu schwerwiegenden Rauchgasvergiftungen führen kann. Deshalb sind Übungen wie diese unverzichtbar, um sicherzustellen, dass sowohl die Tunnelleitzentrale der Niederlassung Nordost der Autobahn GmbH des Bundes als auch die Rettungskräfte im Ernstfall schnell, koordiniert und effektiv handeln.
Einmal pro Jahr findet in zwei von den insgesamt elf Berliner Autobahntunneln eine Großübung statt. Damit ist sichergestellt, dass in jedem der elf Tunnel nach spätestens vier Jahren eine Simulation des Ernstfalls stattgefunden hat. Neben der Großübung werden alle weiteren Tunnel jährlich in einer Simulationsübung auf funktionierende Kommunikationswege zwischen der Tunnelleitzentrale und den Leitstellen der Einsatzkräfte überprüft.
„Wir freuen uns über den reibungslosen Ablauf der Übung“, berichtet Ronald Normann, Direktor der Niederlassung Nordost der Autobahn GmbH . „Sowohl die Technik als auch der starke personelle Einsatz haben gezeigt, dass wir auf solche Vorfälle in unseren Tunneln vorbereitet sind.“
Erst im August wurde das Herzstück der Sicherheitsüberwachung aller Berliner Autobahntunnel auf den neuesten Stand gebracht. Dabei wurde nicht nur die Hard-, sondern auch die Software unter einer kontrollierten stundenweisen Abschaltung ausgetauscht. Seitdem ist die Tunnelleitzentrale wieder 24 Stunden und 365 Tage im Jahr von einem Dutzend Monitoren und mit Hunderten Bildern aus den Tunneln hell erleuchtet, an dem am Montagabend die Übung gut zu sehen war. Ohne echte Opfer, dafür mit sieben Komparsen des DRK Berlin, die den Ernstfall nachstellten.
Diese Art der realistisch dargestellten Übungen ist unerlässlich, um Abläufe zu perfektionieren und sicherzustellen, dass im Ernstfall jeder Handgriff sitzt.
Übungen der einsatztaktischen Vorgehensweise sind für die Berliner Feuerwehr enorm wichtig und fester Bestandteil der Einsatzvorbereitung. Seit 2022 hat die Berliner Feuerwehr das Einsatzkonzept Tunnelbrandbekämpfung eingeführt, welches sich an der Einsatzlehre der International Fire Academy in der Schweiz orientiert. Diese hat sich als europaweiter Stand der Technik etabliert.
Der Tunnel Rudower Höhe auf der A113 war für die Dauer der Übung in der Nacht vom 30.09. auf den 01.10.2024 ab 21 Uhr bis 05:00 Uhr voll gesperrt.  
'''
datetime_value="2025-09-23"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()

#------------------------


#################
articleText ='''Regionalniederlassung Ruhr sperrt am Freitagabend (26.9.) erneut die L736 (Ostenhellweg) zwischen Schachtstraße und Hellweg in Bergkamen. Grund sind Arbeiten an der Brücke, welche die L736 in Bergkamen-Rünthe über den Datteln-Hamm-Kanal führt. Der Abschnitt steht dem Verkehr ab Montagmorgen wieder zur Verfügung. Eine Umleitung führt über die Industriestraße und die B233 (Werner Straße).
Nach dem Wochenende steht dem Verkehr in diesem Bereich der L736 noch für etwa eine Woche nur ein Fahrstreifen zu Verfügung. In dieser Zeit wird der Korrosionsschutz auf das neue Querkraftgelenk aufgetragen. Der Verkehr wird mit einer Baustellenampel geregelt.
'''
datetime_value="2025-09-24"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()

#------------------------

articleText ='''Bedburg-Hau (straßen.nrw). Am Montag (29.9.) beginnt die Straßen.NRW-Regionalniederlassung Niederrhein mit dem Umbau der Kreuzung B57 „Kalkarer Straße“ / L18 „Berk’sche Straße“. Ziel ist es, diese Unfallhäufungsstelle nachhaltig zu entschärfen. Im Rahmen der Maßnahme wird die Kreuzung baulich umgestaltet und mit einer neuen Ampelanlage (LSA) ausgestattet. Die Arbeiten sind in zwei Bauabschnitte unterteilt.
Erster Bauabschnitt: ab Montag (29.9.)
In diesem Abschnitt wird die B57 „Kalkarer Straße“ zwischen der L18 „Berk’sche Straße“ und der „Stefan-Paeßens-Straße“ voll gesperrt. Auch der Geh- und Radweg entlang der L18 zwischen der B57 und der K5 „Sommerlandstraße“ ist in dieser Zeit nicht nutzbar. Der Verkehr wird in beide Richtungen über den „Johann-van-Aken-Ring“, die K27 „Alte Bahn / Römerstraße“ und die B67 „Gocher Straße“ umgeleitet. An der Kreuzung „Johann-van-Aken-Ring“ / „Alte Bahn“ kommt eine mobile LSA zum Einsatz. Der Fuß- und Radverkehr wird über den „Schafweg“ und die Straße „Tillerfeld“ umgeleitet.
Zweiter Bauabschnitt: ab Montag (13.10.)
Im zweiten Schritt wird die L18 „Berk’sche Straße“ in beiden Richtungen voll gesperrt. Die Bauzeit beträgt voraussichtlich acht Wochen. In diesem Zeitraum erneuert und verbreitert Straßen.NRW rund 135 Meter der Fahrbahn der L18, führt die Geh- und Radwege im Kreuzungsbereich neu und führt umfangreiche Tiefbauarbeiten zur Vorbereitung der Ampelanlage durch. Die Umleitung erfolgt über die K12 „Zum Wisseler See“, L41 „Rheinstraße“, B57 „Bahnhofstraße“, B67 „Gocher Straße“ und die K27 „Römerstraße“. Eine mobile Ampelanlage wird an der Kreuzung K12 / L41 installiert. Der Fuß- und Radverkehr wird in beiden Richtungen über die Straße „Tillerfeld“, den „Alleenradweg“, die B67 und die K27 umgeleitet.

'''
datetime_value="2025-09-24"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()

#------------------------

articleText ='''Dahlem (straßen.nrw). Der Landesbetrieb Straßenbau Nordrhein-Westfalen saniert ab Freitag, 26.9., den B51-Abzweig im Bereich Dahlem in Richtung Hellenthal und Udenbreth zwischen der B51 und der L110.
Die rund 600 Meter lange Verbindung zwischen B51 und L110 wird bis voraussichtlich Montag, 6.10., unter Vollsperrung erneuert.
Der Verkehr in Richtung Hellenthal, Udenbreth und Dahlemer Binz wird ab der B51 (Abzweig in Fahrtrichtung Dahlem) über die Schmidtheimer Straße (L110) umgeleitet.
'''
datetime_value="2025-09-24"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()

#------------------------

articleText ='''Gelsenkirchen (straßen.nrw). Die Straßen.NRW-Regionalniederlassung Ruhr beseitigt Straßenschäden auf der B227 (Halterner Straße) in Essen. Ab Montag (29.9.) ist die B227 deshalb zwischen Krayer Straße und A40 in Fahrtrichtung Süden gesperrt. Damit ist zwei Wochen lang auch die Auffahrt zur A40 an der Anschlussstelle Gelsenkirchen-Süd gesperrt. Die Abfahrt von der A40 in Richtung Gelsenkirchen-Innenstadt steht dem Verkehr während der Arbeiten zur Verfügung. Zudem ist die Kemnastraße in Bochum-Wattenscheid nicht von der B227 aus erreichbar, auch die Zufahrt zur B227 ist nicht möglich. Lokale Umleitungen zu den A40-Anschlussstellen Bochum-Wattenscheid-West und Essen-Kray sind ausgeschildert. Auf den Umleitungsstrecken gelten zum Teil zusätzliche Halteverbote.
'''
datetime_value="2025-07-24"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()

#------------------------
################################
articleText ='''Gütersloh/Rheda-Wiedenbrück (straßen.nrw). Im Rahmen der Sanierung der B61 wird das Baufeld erweitert: Dafür wird ab dem morgigen Freitag, 26. September, der Kreuzungsbereich der Bundesstraße mit dem Stadtring Kattenstroth/Kiebitzstraße bis zur Einmündung Auf’m Kampe gesperrt. Der Knotenpunkt soll bis Donnerstag, 2. Oktober, fertig saniert sein.
Bislang endete der erste Bauabschnitt kurz vor der Kreuzung. Um diesen stark frequentierten Bereich zeitnah fertigstellen zu können, wird die Baufirma über das Wochenende und auch nachts tätig sein. Sobald die Sanierung der Kreuzung abgeschlossen ist, wird sie wieder freigegeben. Dann endet die Sperrung wie vorher kurz vor dem Knotenpunkt.
Verkehrsteilnehmende können während der zusätzlichen Sperrung aus Gütersloh kommend links in Auf’m Kampe abbiegen, sodass die anliegenden Unternehmen erreichbar bleiben. Auf der Kiebitzstraße beginnt die Sperrung kurz hinter der Einfahrt zum Baumarkt, sodass auch dort der Lieferverkehr gewährleistet ist.
Anpassung der Umleitung
Der Verkehr in Richtung Gütersloh wird von der Brockstraße rechts in den Stadtring Kattenstroth und dann weiter auf die Neuenkirchener Straße (L782) geführt.
Die Umleitung in Richtung Rheda-Wiedenbrück ändert sich nicht.
Fortschritt 1. Bauabschnitt
Die Sanierung des am 15. September begonnen Abschnitts geht gut voran: Nächste Woche werden unter anderem die Gräben hergestellt, Bankette eingebaut und Leitpfosten gesetzt.
'''
datetime_value="2025-07-24"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()

#------------------------

articleText ='''Kalletal (straßen.nrw). Die Stützwand im Zuge der Waterloostraße (B238) im Kalletal bekommt ein neues Geländer: Zwischen Montag und Donnerstag, 29. September bis 2. Oktober, wird deshalb der Geh-/Radweg gesperrt sowie die Geschwindigkeit für den motorisierten Verkehr auf Tempo 50 reduziert.
Das Geländer ist notwendig, weil es die Straßenwärter*innen beim Grünschnitt vor Abstürzen schützt. Bislang gab es entlang der Stützwand ein provisorisches Geländer.
'''
datetime_value="2025-07-24"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()

#------------------------

articleText ='''Dülmen (straßen.nrw) Die Straßen.NRW Regionalniederlassung Münsterland saniert aktuell die L611 von Dülmen Richtung Coesfeld. Die Arbeiten liegen gut im Zeitplan. Ab Mittwoch (24.9.) beginnt der zweite Bauabschnitt. Für diesen wird die Sperrung im Bereich der Autobahnbrücke weiter ausgeweitet. Eine Auffahrt auf die A43 Münster und eine Abfahrt aus Wuppertal kommend ist bereits morgen früh vor dem Berufsverkehr nicht mehr möglich. Auch die Zufahrt zum Grenzweg wird gesperrt. Die Sanierungsarbeiten der Fahrbahn der L611 sind bereits weitgehend realisiert. Voraussichtlich ab Ende der kommenden Woche kann der Streckenabschnitt von der Autobahnbrücke in Richtung Coesfeld bis zur Anschlussstelle der B474 wieder freigegeben werden. Für die Brückenarbeiten und die Umgestaltung der Strecke im Bereich des Grenzweges ist eine Sperrung noch bis Ende November geplant. Auch der hier liegende Mitfahrerparkplatz bleibt gesperrt. Eine Umleitung über Dülmen-Nord ist ausgeschildert.
Zum Hintergrund der Maßnahme :
Die Fahrbahn der L611 (alte B474) zwischen Dülmen und Coesfeld wird auf einer Länge von rund 2,5 Kilometer erneuert. Im Zuge der Sanierung wird auch der vorhandene Rad- und Gehweg saniert und die Radwegeführung vom Grenzweg bis zum Mitfahrerparkplatz optimiert. Der Radweg wird auf der Ostseite der Fahrbahn errichtet. Für die sichere Querung der Radfahrer und Fußgänger wird in Höhe des Grenzweges eine Querungshilfe gebaut. Saniert wird im Rahmen der Maßnahme auch die Autobahnbrücke. Es ist vorgesehen, den vorhandenen Fahrbahnbelag auf der Brückenplatte und die Abdichtung zu erneuern. Die sogenannten Brückenkappen werde mit saniert und die Schutzeinrichtungen im Bereich der Autobahnanschlussstelle Dülmen und auf der Brücke werden den neuen Anforderungen angepasst. Weiterhin wird die Ampelanlage erneuert.
'''
datetime_value="2025-07-24"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()

#------------------------

articleText ='''Meschede (straßen.nrw). Ab Montag (29.9.) starten in Meschede Wennemen im Bereich des Brückenbauwerks über den Bahnübergang die Arbeiten zum Abbau der Elektroschutzplatten, die ursprünglich als isolierende Elemente zum Schutz vor unter Spannung stehenden Teilen eingebaut wurden. Aus diesem Grund muss die L914 in dem Bereich voll gesperrt werden. Nach Aufhebung der Elektrifizierung sind die vorhandenen Platten nicht mehr notwendig und müssen fachgerecht abgebrochen werden, um die Verkehrssicherheit des Bauwerks langfristig zu gewährleisten.
Eine Umleitung wird über die L743 Meschede-Enste, L840 -Calle nach -Wennemen und umgekehrt eingerichtet. Innerhalb von etwa einer Woche sollen die Arbeiten abgeschlossen sein.
'''
datetime_value="2025-07-24"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()

#------------------------

articleText ='''Meschede (straßen.nrw). Für die Entfernung von sogenannten Elektroschutzplatten, die mit Ihrer isolierenden Wirkung vor unter Spannung stehenden Teilen schützen und nach Aufhebung der Elektrifizierung der Bahnstrecke nicht mehr benötigt werden, wird die Antoniusbrücke im Zuge der B55 verkehrlich eingeschränkt. Zwischen dem 29. September und dem 4. Oktober wird in beiden Richtungen jeweils ein Fahrstreifen gesperrt. Zudem werden zur Sicherheit einige Parkflächen unterhalb des Bauwerks für die Dauer der Entfernungs-Tätigkeit nicht nutzbar sein. Die Bahnsteige sind zeitweise von kurzfristigen Sperrungen betroffen. Der Bahnbetrieb wird in dieser Zeit eingestellt und ein Schienenersatzverkehr über die Deutsche Bahn eingerichtet.
'''
datetime_value="2025-07-24"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()

#------------------------

articleText ='''Dortmund (straßen.nrw). Die Straßen.NRW-Regionalniederlassung Ruhr führt zusätzliche Wartungsarbeiten im B236-Tunnel Wambel in Dortmund durch. Aus diesem Grund steht Verkehrsteilnehmenden am Mittwoch (24.9.) in Fahrtrichtung Lünen zwischen 9 und 15 Uhr nur ein Fahrstreifen zur Verfügung. Am Donnerstag (25.9.) ist einer von zwei Fahrstreifen in Fahrtrichtung Schwerte gesperrt. Zudem ist am Mittwoch die Verbindung von der B1 in Richtung Dortmund-Zentrum auf die B236 in Richtung Lünen gesperrt. Eine Umleitung ist eingerichtet.
'''
datetime_value="2025-07-24"
cursor.execute(" INSERT INTO articlesTESTSET (articleDate, articleText) VALUES (?,?)",(datetime_value,articleText))
conn.commit()

#------------------------


conn.close()
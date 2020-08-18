import sys
import sqlite3

class Data(): 
    nom="journal.db"

    def __init__(self):
        self.conn= sqlite3.connect(self.nom)
        self.c= self.conn.cursor()

    def modify(self, commande):
        self.c.execute(commande)
        self.conn.commit()

    def labels(self, label):
        self.tabGauche= []
        self.tabCentrale= []
        res= self.c.execute("SELECT * FROM journal WHERE note_label LIKE '%"+label+"%' order by id")
        for ligne in res:
            self.tabGauche.append([ligne[1], ligne[2], ligne[3]])
        return self.tabGauche

    def insert(self, date, note, labels):
        #2020-08-18T22:10:00
        self.c.execute("insert into journal (note_date, note_text, note_label) values ('"+date+"','"+note+"','"+labels+"');")
        self.conn.commit()

    def delete(self, lieu):
        self.c.execute("DELETE FROM journal WHERE lieu= '"+lieu+"'")
        self.conn.commit()

d= Data()

sys.argv.pop(0)

if len(sys.argv) == 0:
    tout=""
elif len(sys.argv) == 1:
    tout= sys.argv[0]
else:
    tout= ",".join(sorted(sys.argv))


tab= d.labels(tout)

for ligne in tab:
    print(ligne[0]+"\n"+ligne[1]+"\n labels:"+ligne[2]+"\n \n")


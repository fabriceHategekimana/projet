import xlsxwriter
import openpyxl
from pathlib import Path
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QTableWidget, QTableWidgetItem, QApplication, QGridLayout, QAction, QMainWindow, qApp, QPushButton, QDialog, QVBoxLayout, QTextEdit, QHeaderView, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QCalendarWidget, QRadioButton, QListWidget
)
from PyQt5.QtGui import QIcon, QPainter, QColor, QPen
from PyQt5.QtCore import pyqtSlot, Qt, QDate
import sqlite3
from datetime import timedelta, datetime, tzinfo, timezone
from PyQt5 import QtCore, QtGui, QtWidgets


class Data(): 
    nom="espacePlus.db"
    tabGauche= []
    tabCentrale= []

    def __init__(self):
        self.conn= sqlite3.connect(self.nom)
        self.c= self.conn.cursor()

    def getTab(self, commande, header):
        tab= []
        res= self.c.execute(commande)
        if header:
            headers= []
            for des in res.description:
                headers.append(des[0])
            tab.append(headers)
        for ligne in res:
            tab.append(list(ligne))
        return tab

    def modify(self, commande):
        self.c.execute(commande)
        self.conn.commit()

    def importMilitaire(self, lieu):
        self.tabGauche= []
        self.tabCentrale= []
        res= self.c.execute("SELECT * FROM militaire WHERE lieu LIKE '"+lieu+"' order by id")
        for ligne in res:
            self.tabGauche.append([ligne[1], ligne[2], ligne[3]])
            self.tabGauche.append([" ", " ", ""])
            self.tabCentrale.append(ligne[4].split(","))
            self.tabCentrale.append(ligne[5].split(",")) 
        self.tabGauchePlanningsBlocs=[self.tabGauche, self.tabCentrale]
        return self.tabGauchePlanningsBlocs

    def insert(self, chaine, lieu):
        self.c.execute("INSERT INTO militaire (id, grade, nom, prenom, planning, bloc, lieu) VALUES ("+chaine+",'"+lieu+"')")
        self.c.execute("DELETE FROM militaire WHERE rowid NOT IN (SELECT min(rowid) FROM militaire GROUP BY grade, nom, prenom, lieu)")
        self.conn.commit()

    def resetID(self, ntabGauche, lieu):
        for i in range(len(ntabGauche)):
            if i%2 == 0:
                self.c.execute("UPDATE militaire SET id="+str(int(i/2))+" WHERE (nom= '"+ntabGauche[i][1]+"' AND prenom= '"+ntabGauche[i][2]+"' AND lieu= '"+lieu+"')")
        self.conn.commit()
    def viderToutLesMilitairesDUnLieu(self, lieu):
        self.c.execute("DELETE FROM militaire WHERE lieu= '"+lieu+"'")
        self.conn.commit()


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.bleu= QColor(116, 185, 255)
        self.annee= "2014"
        self.date_livraison= ["date", "07/07/2014"]
        self.initUI()

    #fonction d'initialisation
    def initUI(self):
        self.data= Data()
        self.layoutMain = QGridLayout()
        self.dashboard()

    def dashboard(self):
        self.load("tout")
        self.display()

    def load(self, valeur):
        self.colonne_chantiers= self.get_colonne_chantiers(200, 400)
        self.planning= self.get_planning(1000, 400)
        self.date_haut= self.get_date_haut(1000, 100)
        self.livraisons= self.get_livraisons(1000, 200)
        if valeur != "tables":
            self.calendrier= self.get_calendar(200, 200)
            self.rienB= self.initButton(" ", self.rien)
            self.tll= self.initButton("Toutes les livraisons", self.toutes_les_livraisons)
            self.combo_annee= self.get_combobox(["2014", "2015", "2016", "2017", "2018", "2019", "2020"])

    def display(self):
        self.layoutMain.addWidget(self.date_haut, 0, 1) 
        self.layoutMain.addWidget(self.colonne_chantiers, 1, 0) 
        self.layoutMain.addWidget(self.planning, 1, 1) 
        self.layoutMain.addWidget(self.rienB, 2, 0) 
        self.layoutMain.addWidget(self.tll, 2, 1) 
        self.layoutMain.addWidget(self.livraisons, 3, 1) 
        self.layoutMain.addWidget(self.calendrier, 3, 0) 
        self.layoutMain.addWidget(self.combo_annee, 0, 0) 
        #Début add_chantier et delete_chantier
        self.colonne_chantiers.itemDoubleClicked.connect(self.mini_menu_chantier)
        self.livraisons.itemDoubleClicked.connect(self.mini_menu_livraison)
        self.calendrier.clicked.connect(self.jours_livraisons)
        self.combo_annee.currentTextChanged.connect(self.changer_annee)
        self.setLayout(self.layoutMain) 
        self.synchronisation()
        self.show()

    def synchronisation(self):
        #première synchro table widget à table bas
        self.date_haut.horizontalScrollBar().valueChanged.connect(self.planning.horizontalScrollBar().setValue)
        self.planning.horizontalScrollBar().valueChanged.connect(self.date_haut.horizontalScrollBar().setValue)

    def clear(self):
        for i in reversed(range(self.layoutMain.count())): 
                self.layoutMain.itemAt(i).widget().setParent(None)

    def edit_livraison(self):
        self.fermer_fenetre()
        item= self.Item
        if item.row() > 0:
            self.colonne_a_modifier= self.livraisons.item(0, item.column()).text()
            if item.column() in [2, 4, 6]:
                self.editText(self.editText3)
            elif item.column() == 0:
                self.edit_liste_table("chantiers", "where DATE_DEBUT like '%/"+self.annee+"'", self.edit_liste_chantier)
            elif item.column() == 1:
                self.editCalendar(self.editCalendar3)
            elif item.column() == 3:
                self.edit_liste_table("flottes", "", self.edit_flottes)
            elif item.column() == 5:
                self.edit_liste_table("fournisseurs", "", self.edit_fournisseurs)

    def edit_flottes(self, item):
        self.fermer_fenetre()
        nouveau= self.liste_table.item(item.row(), 0).text()
        self.data.modify("update livraisons set "+self.colonne_a_modifier+"='"+nouveau+"' where ID_LIVRAISON='"+self.ID+"'")
        self.load("tables")
        self.display()

    def edit_liste_chantier(self, item):
        self.fermer_fenetre()
        nouveau= self.liste_table.item(item.row(), 0).text()
        self.data.modify("update livraisons set "+self.colonne_a_modifier+"='"+nouveau+"' where ID_LIVRAISON='"+self.ID+"'")
        self.load("tables")
        self.display()

    def edit_fournisseurs(self, item):
        self.fermer_fenetre()
        nouveau= self.liste_table.item(item.row(), 1).text()
        self.data.modify("update livraisons set "+self.colonne_a_modifier+"='"+nouveau+"' where ID_LIVRAISON='"+self.ID+"'")
        self.load("tables")
        self.display()
        

    def edit_liste_table(self, table, where, callback):
        tab= self.data.getTab("select * from "+table+" "+where, True) 
        self.liste_table= self.table(tab, 1000, 400)
        self.liste_table.itemDoubleClicked.connect(callback)
        layout= QGridLayout()
        layout.addWidget(self.liste_table)
        self.fenetre(layout, 1050, 450)

    def editCalendar3(self):
        self.fermer_fenetre()
        self.data.modify("update livraisons set "+self.colonne_a_modifier+"='"+self.date_retenue+"' where ID_LIVRAISON='"+self.ID+"'")
        self.load("tables")
        self.display()

    def editText3(self):
        self.fermer_fenetre()
        nouveau= str(self.et.toPlainText())
        self.data.modify("update livraisons set "+self.colonne_a_modifier+"='"+nouveau+"' where ID_LIVRAISON='"+self.ID+"'")
        self.load("tables")
        self.display()

    def edit_chantier(self, item):
        self.fermer_fenetre()
        if item.row() > 0:
            self.colonne_a_modifier= self.table_detail_chantier.item(0, item.column()).text()
            if item.column() in [1, 2, 3, 5]:
                self.editText(self.editText2)
            elif item.column() == 4:
                self.editCalendar(self.editCalendar2)
            elif item.column() in [6, 7, 8]:
                self.binarySwitch(item.text())
            elif item.column() == 9:
                self.check_employes(item.text())

    def check_employes(self, text):
        vbox= QVBoxLayout()
        self.tabSelected= []
        if text not in [" ", "-"]:
            self.tabSelected= text.split(",")
        tabAll= self.data.getTab("select ID_EMPLOYES from employes", False)
        tab= []
        layout= QGridLayout()
        i=0
        self.liste = QListWidget()
        self.liste.setSortingEnabled(True)
        self.liste.setMaximumWidth(50)
        self.liste.setMaximumHeight(400)
        for employe in self.tabSelected:
            self.liste.insertItem(0, employe)
        tab= self.data.getTab("select * from employes", True)
        self.table_employe= self.table(tab, 1000, 400)
        self.table_employe.itemDoubleClicked.connect(self.update_liste_employes)
        self.Valider= self.initButton("valider", self.save_liste_employes)
        layout.addWidget(self.liste, 0, 0)
        layout.addWidget(self.table_employe, 0, 1)
        layout.addWidget(self.Valider, 1, 1)
        self.fenetre(layout, 1100, 500)
         
    def update_liste_employes(self, item):
        self.fermer_fenetre()
        nouveauID= self.table_employe.item(item.row(), 0).text()
        print("nouveauID: ",nouveauID)
        if nouveauID in self.tabSelected:
            self.tabSelected.pop(self.tabSelected.index(nouveauID))
        else:
            self.tabSelected.append(nouveauID)
        self.liste = QListWidget()
        self.liste.setSortingEnabled(True)
        self.liste.setMaximumWidth(50)
        self.liste.setMaximumHeight(400)
        for employe in self.tabSelected:
            self.liste.insertItem(0, employe)
        self.Valider= self.initButton("valider", self.save_liste_employes)
        layout= QGridLayout()
        layout.addWidget(self.liste, 0, 0)
        layout.addWidget(self.table_employe, 0, 1)
        layout.addWidget(self.Valider, 1, 1)
        self.fenetre(layout, 1100, 500)

    def save_liste_employes(self):
        self.fermer_fenetre()
        nouveau= ",".join(self.tabSelected)
        self.data.modify("update chantiers set "+self.colonne_a_modifier+"='"+nouveau+"' where NUM_CHANTIER='"+self.ID+"'")
        self.load("tables")
        self.display()
        self.detail_chantier()
          
    def binarySwitch(self, text):
        if text == "oui":
            text= "non"
        else:
            text= "oui"
        self.data.modify("update chantiers set "+self.colonne_a_modifier+"='"+text+"' where NUM_CHANTIER='"+self.ID+"'")
        self.load("tables")
        self.display()
        self.detail_chantier()

    def editCalendar2(self):
        self.fermer_fenetre()
        self.data.modify("update chantiers set "+self.colonne_a_modifier+"='"+self.date_retenue+"' where NUM_CHANTIER='"+self.ID+"'")
        self.load("tables")
        self.display()
        self.detail_chantier()

    def set_date_retenue(self, date):
        self.date_retenue= self.date(date)

    def editCalendar(self, callback):
        cal= self.get_calendar(200, 200)
        cal.clicked.connect(self.set_date_retenue)
        valider= self.initButton("valider", callback)
        layout= QGridLayout()
        layout.addWidget(cal, 0, 0)
        layout.addWidget(valider, 1, 0)
        self.fenetre(layout, 200, 200)

    def editText2(self):
        self.fermer_fenetre()
        nouveau= str(self.et.toPlainText())
        self.data.modify("update chantiers set "+self.colonne_a_modifier+"='"+nouveau+"' where NUM_CHANTIER='"+self.ID+"'")
        self.load("tables")
        self.display()
        self.detail_chantier()

    def editText(self, callback):
        layout= self.get_editText(callback)
        self.fenetre(layout, 200, 200)

    def mini_menu_livraison(self, item):
        self.ID= self.livraisons.item(item.row(), 7).text()
        self.Item= item
        addB= self.initButton("add", self.add_livraison)
        deleteB= self.initButton("delete", self.delete_livraison)
        editB= self.initButton("edit", self.edit_livraison)
        layout= QGridLayout()
        layout.addWidget(addB, 0, 0)
        layout.addWidget(deleteB, 1, 0)
        layout.addWidget(editB, 2, 0)
        self.fenetre(layout, 100, 100)

    def add_livraison(self):
        self.fermer_fenetre()
        dic={"A":"B","B":"C","C":"A"}
        #je fais un double pop car la liste est de la forme [[content]]
        lastID= self.data.getTab("select ID_LIVRAISON from livraisons", False).pop().pop()
        tab= lastID.split("_")
        gauche= tab[0]
        droite= tab[1]
        #on commence
        droite= dic[droite]
        if droite == "A":
            gauche= str(int(gauche)+1)
        identifiant= gauche+"_"+droite
        chaine= "'-','"+self.date_livraison[1]+"','08h00','-','-','-','-','"+identifiant+"'"
        header= self.data.getTab("select * from livraisons where HEURE='rien'", True)
        self.data.modify("insert into livraisons ("+",".join(header[0])+") values ("+chaine+")")
        self.load("table")
        self.display()

    def delete_livraison(self):
        self.fermer_fenetre()
        self.data.modify("delete from livraisons where ID_LIVRAISON='"+self.ID+"'")
        self.load("table")
        self.display()

    def mini_menu_chantier(self, item):
        self.ID= item.text()
        addB= self.initButton("add", self.add_chantier)
        deleteB= self.initButton("delete", self.delete_chantier)
        detailB= self.initButton("detail", self.detail_chantier)
        layout= QGridLayout()
        layout.addWidget(addB, 0, 0)
        layout.addWidget(deleteB, 1, 0)
        layout.addWidget(detailB, 2, 0)
        self.fenetre(layout, 100, 100)

    def add_chantier(self):
        self.fermer_fenetre()
        tabAnnee=["A", "B", "C", "D", "E", "F", "G"]
        lettre= tabAnnee[int(self.annee)-2014]
        #je fais un double pop car la liste est de la forme [[content]]
        num= len(self.data.getTab("select NUM_CHANTIER from chantiers where DATE_DEBUT like '%/"+self.annee+"'", False))+1
        identifiant= lettre+str(num)
        chaine= "'"+identifiant+"','-','-','-','01/01/"+self.annee+"','1 semaine','non','non','non','-'"
        header= self.data.getTab("select * from chantiers where ADRESSE='rien'", True)
        self.data.modify("insert into chantiers ("+",".join(header[0])+") values ("+chaine+")")
        self.load("tables")
        self.display()

    def delete_chantier(self):
        self.fermer_fenetre()
        self.data.modify("delete from chantiers where NUM_CHANTIER='"+self.ID+"'")
        self.load("table")
        self.display()

    def detail_chantier(self):
        self.fermer_fenetre()
        tab= self.data.getTab("select * from chantiers where NUM_CHANTIER='"+self.ID+"'", True)
        self.table_detail_chantier= self.table(tab, 1000, 100)
        layout= QGridLayout()
        layout.addWidget(self.table_detail_chantier, 0, 0)
        self.table_detail_chantier.itemDoubleClicked.connect(self.edit_chantier)
        self.fenetre(layout, 1050, 150)

    def changer_annee(self):
        self.clear()
        self.annee= str(self.combo_annee.currentText())
        self.calendrier.setMaximumDate(QDate(int(self.annee), 12, 30))
        self.calendrier.setMinimumDate(QDate(int(self.annee), 1, 1))
        self.load("tables")
        self.display() 

    def jours_livraisons(self, date):
        self.calendrier.disconnect()
        self.clear()
        self.date_livraison= ["jour", self.date(date)]
        self.livraisons= self.get_livraisons(1000, 200)
        self.display()

    def toutes_les_livraisons(self):
        self.clear()
        tab= self.data.getTab("select * from livraisons where DATE_LIVRAISON like '%/"+self.annee+"'", True)
        self.date_livraison= ["all", "01/01/"+self.annee]
        self.livraisons= self.table(tab, 1000, 200)
        self.display()

    def get_livraisons(self, largeur, hauteur):
        #if self.date_livraison[0] == "jour":
        tab= self.data.getTab("select * from livraisons where DATE_LIVRAISON='"+self.date_livraison[1]+"'", True)
        table= self.table(tab, largeur, hauteur)
        return table

    def get_date_haut(self, largeur, hauteur):
        #obtention de la table
        date= self.date("01/01/"+self.annee)
        tabMois=["janvier", "févirer", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
        tab= ["janvier"]
        tab2=[1]
        dernier= tab[0]
        for i in range(51):
            date= date.addDays(7)
            mois= tabMois[date.month()-1]
            if mois != dernier:
                dernier= mois
                tab.append(mois)
            else:
                tab.append(" ")
            tab2.append(i+2)
        tabFinal= [tab, tab2]
        table= self.table(tabFinal, largeur, hauteur)
        return table
          
    def get_planning(self, largeur, hauteur):
        tab= self.data.getTab("select DATE_DEBUT,DUREE from chantiers where DATE_DEBUT like '%/"+self.annee+"'", False)
        table= self.creerTable(largeur, hauteur, len(tab), 52)
        marquages= self.get_marquages(tab)
        self.colorier(marquages, table, self.bleu)
        return table

    def get_marquages(self, dateDuree):
        tab= []
        i= 0
        for dd in dateDuree:
            date= self.date(dd[0])
            duree= int(dd[1].split(" ")[0])
            semaineDebut= date.weekNumber()[0]-1
            semaineFin=date.addDays(duree*7).weekNumber()[0]-1
            for j in range(semaineDebut, semaineFin):
                if j < 52:
                    tab.append([i, j])
            i= i+1
        return tab

    def date(self, date):
        if type(date) == str:
            tab= date.split("/")
            date= QDate(int(tab[2]), int(tab[1]),int(tab[0]))
        else:
            date= self.monStr(date.day())+"/"+self.monStr(date.month())+"/"+self.monStr(date.year())
        return date

    def monStr(self, num):
        texte= ""
        if num < 10:
            texte= "0"+str(num)
        else:
            texte= str(num)
        return texte

    def get_colonne_chantiers(self, largeur, hauteur):
        tab= self.data.getTab("select NUM_CHANTIER from chantiers where DATE_DEBUT like '%/"+self.annee+"'", False)
        table= self.table(tab, largeur, hauteur)
        return table

    def table(self, tab, largeur, hauteur):
        table= self.creerTable(largeur, hauteur, 1, 1)
        #dimensions (nb cellules) de la table
        if tab != []:
            ligneTab= len(tab)
            colonneTab= len(tab[0])
            ligneTable= table.rowCount()
            colonneTable= table.columnCount()

            #on arrange les lignes
            #si on a moins de ligne que la table
            if ligneTab < ligneTable:
                nbLigneEnMoins= ligneTable-ligneTab
                for i in range(nbLigneEnMoins, 0, -1):
                    table.removeRow(table.rowCount()-1)
            elif ligneTab > ligneTable:
                nbLigneEnPlus= ligneTab-ligneTable
                for i in range(0, nbLigneEnPlus, 1):
                    table.insertRow(table.rowCount())
            #on arrange les colonnes
            #si on a moins de colonne que la table
            if colonneTab < colonneTable:
                nbColonneEnMoins= colonneTable-colonneTab
                for i in range(nbColonneEnMoins, 0, -1):
                    table.removeColumn(table.columnCount()-1)
            elif colonneTab > colonneTable:
                nbColonneEnPlus= colonneTab-colonneTable
                for i in range(0, nbColonneEnPlus, 1):
                    table.insertColumn(table.columnCount())
        
            #remplissage de la table
            for i in range(ligneTab):
                for j in range(colonneTab):
                    table.setItem(i, j, QTableWidgetItem(str(tab[i][j])))
                    table.item(i, j).setFlags(Qt.ItemIsEnabled)
        return table

    def creerTable(self, largeur, hauteur, ligne, colonne):
       # creer la table
        tableWidget = QTableWidget()
        #dimensions (nb cellules) de la table
        tableWidget.setMaximumWidth(largeur)
        tableWidget.setMaximumHeight(hauteur)
        tableWidget.setRowCount(ligne)
        tableWidget.setColumnCount(colonne)
        #on cache les headers
        tableWidget.verticalHeader().hide()
        tableWidget.horizontalHeader().hide()
        #remplissage de la table
        for i in range(ligne):
            for j in range(colonne):
                tableWidget.setItem(i, j, QTableWidgetItem(" "))
                tableWidget.item(i, j).setFlags(Qt.ItemIsEnabled)
        return tableWidget

    def colorier(self, positions, table, couleur):
        for position in positions:
            table.item(position[0], position[1]).setBackground(couleur)

    def verouiller(self, positions, table):
        for position in positions:
            table.item(position[0], position[1]).setFlags(Qt.ItemIsEnabled)

    def get_calendar(self, largeur, hauteur):
        calendar = QCalendarWidget(self)
        calendar.setGridVisible(True)
        #calendar.clicked.connect(self.show_date)
        calendar.setMaximumDate(QDate(int(self.annee), 12, 30))
        calendar.setMinimumDate(QDate(int(self.annee), 1, 1))
        calendar.setMaximumWidth(largeur)
        calendar.setMaximumHeight(hauteur)
        return calendar

    def initButton(self, texte, callback):
        button = QPushButton(texte)
        button.clicked.connect(callback)
        return button

    def rien(self):
        print("rien")

    def get_combobox(self, tab):
        combobox= QComboBox()
        combobox.addItems(tab)
        return combobox
        #combobox.currentTextChanged.connect(self.comboSemaine)

    def fenetre(self, layoutContenu, largeur, longueur):
        self.fen = QDialog(self)
        self.fen.setAttribute(Qt.WA_DeleteOnClose)
        self.fen.setLayout(layoutContenu)
        self.fen.setGeometry(100, 100, largeur, longueur)
        self.fen.setWindowTitle('window')
        self.fen.exec() 

    def fermer_fenetre(self):
        self.fen.done(0)

    def get_editText(self, callback):
        self.et= QTextEdit() 
        valider= self.initButton("valider", callback)
        box= QGridLayout()
        box.addWidget(self.et, 0, 0)
        box.addWidget(valider, 1, 0)
        return box

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 



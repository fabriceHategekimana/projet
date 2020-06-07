import xlsxwriter
import openpyxl
from pathlib import Path
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QComboBox, QTableWidget, QTableWidgetItem, QApplication, QGridLayout, QAction, QMainWindow, qApp, QPushButton, QDialog, QVBoxLayout, QTextEdit, QHeaderView, QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QCalendarWidget
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
        #Début
        self.calendrier.clicked.connect(self.jours_livraisons)
        self.combo_annee.currentTextChanged.connect(self.changer_annee)
        self.setLayout(self.layoutMain) 
        self.show()

    def clear(self):
        for i in reversed(range(self.layoutMain.count())): 
                self.layoutMain.itemAt(i).widget().setParent(None)

    def changer_annee(self):
        self.clear()
        #editText juste en bas
        #self.annee= str(self.combo_annee.toPlainText())
        self.annee= str(self.combo_annee.currentText())
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 



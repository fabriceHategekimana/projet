from pyvis.network import Network
import random

def getRandomColor():
    random_number = random.randint(0,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    return hex_number

def getColumn(num, mylist):
    return [x[num] for x in mylist]

def unique(mylist):
    return list(set(mylist))

def addNodes(net, facts):
    nodeList= unique(getColumn(0,facts)+getColumn(2,facts))
    net.add_nodes(nodeList)

def addEdges(net, facts):
    d= {} #on crée un dictionnaire qui assignera à chaque type de noeud une couleur
    uniqueLinks= unique(getColumn(1, facts))
    for u in uniqueLinks:
        d[u]= getRandomColor()
    for f in facts:
        net.add_edge(f[0], f[2], label=f[1], color=d[f[1]])

def displayNetwork(tab):
    net = Network(bgcolor='#333333', font_color='white', height='100%', width='70%', directed=True)
    addNodes(net, tab)
    addEdges(net, tab)

    net.barnes_hut(gravity=-20000, central_gravity=0.0, spring_length=73, spring_strength=0.01, damping=0.09, overlap=0)
    net.show_buttons(filter_=["layout", "edges", "physics"])
    #net.show_buttons() interaction, manipulation
    net.show("network.html")

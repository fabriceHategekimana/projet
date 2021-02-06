import bpy

#rappel mathématiques pour bpy
#1)les angles s'écrivent en radian
#2)pour convertire des degrés en radian, il suffit de fair (x/360)*2*3.14


#supprimer l'objet sélectionné
#bpy.ops.object.delete(use_global=False)

#faire apparaître une caméra à une position et une vue donné
#bpy.ops.object.camera_add(location=(0.0, -15.0, 5.0), rotation=(1.42, 0.0, 0.0))

#faire apparaître un cube à une position donnée
#bpy.ops.mesh.primitive_cube_add(location=(0.0, 0.0, 0.0))

#faire apparaître une sphère à une position donnée et à un rayon donné
#bpy.ops.mesh.primitive_uv_sphere_add(size=1, location=(0.0, 0.0, 0.0))

#faire apparaître une lampe à une position donnée (2e ligne: définit sa puissance)
#bpy.ops.object.lamp_add(type='POINT', location=(0.0, 0.0, 0.0))
#bpy.context.object.data.energy= 20

#remettre la localisation d'un objet vers 0 0 0
#bpy.ops.object.location_clear(clear_delta=False)


#changer la couleur d'un objet (en rgb)
#bpy.context.object.active_material.diffuse_color= (0.0, 0.0, 0.0) #couleur noir en rgb

#retirer les contrastes d'un objet ou le mettre en couleur métallique
#bpy.context.object.active_material.use_shadeless= True #retire les contrastes
#bpy.context.object.active_material.use_tangent_shadign= True #fait une ligne de lumière

#mettre la texture d'un objet en transparent et choisir la transparence
#bpy.context.object.active_material.use_transparency= True
#bpy.context.object.active_material.alpha= 0.5

#la liste des objets actuellement présent sur la session de Blender
#bpy.data.objects

#changer les frames de début et de fin
#	bpy.context.scene.frame_start= 1
#bpy.context.scene.frame_end= 30

#changer le rendu vidéo en ffmpeg
#bpy.context.scene.render.image_settings.file_format= 'FFMPEG'

#mettre la destination du rendu sur le bureau
#bpy.context.scene.render.filepath= '/home/fabrice/Bureau/'

#prendre l'objet actif dans une variable et changer sa matière
#mat= bpy.data.materials["Material"]
#objet= bpy.context.object.data
#objet.materials.append(mat)

#choisir le numéro d'une frame
#bpy.context.scene.frame_set(num)

#choisir un objet selon sont nom
#objet= bpy.data.objects["Cube"]
#objet.location #position de l'objet
#objet.keyframe_insert(data_path="location", index= -1)
import bpy

#Mettre le rendu en ffmpeg
bpy.context.scene.render.image_settings.file_format= 'FFMPEG'
#Mettre la destination du rendu dans le bureau
bpy.context.scene.render.filepath= '/home/fabrice/Bureau/'
#changer le start et le end frame
bpy.context.scene.frame_start= 1
bpy.context.scene.frame_end= 30

#Supprimer tout les objets
bpy.ops.object.select_all(action='TOGGLE')
bpy.ops.object.select_all(action='TOGGLE')

bpy.ops.object.delete(use_global=False)

#Créer une caméra placée au bon endroit
bpy.ops.object.camera_add(location=(0.0, -15.0, 5.0), rotation=(1.42, 0.0, 0.0))

#Créer une sphère placée au bon endroit
bpy.ops.mesh.primitive_uv_sphere_add(size=1, location=(0.0, 0.0, 0.0))


import bpy
import math

def rotationx(r, teta, t):
    teta= toRadian(teta)
    return r*math.cos(teta*t)


def rotationy(r, teta, t):
    teta= toRadian(teta)
    return r*math.sin(teta*t)

def toRadian(teta):
    return (teta/360)*2*3.14

#on récupère l'objet point
point= bpy.data.objects["point"]
x= 0
y= 0
z= 0
r= 5
teta= 32
i= 1
while i<6:
    bpy.context.scene.frame_set(10+i)
    x= rotationx(r, teta, i)
    z= rotationy(r, teta, i)
    point.location= (x, y, z) #position de l'objet
    point.keyframe_insert(data_path="location", index= -1)
    i= i+1





import math


def rotationx(r, teta, t):
    teta= toRadian(teta)
    return r*math.cos(teta*t)


def rotationy(r, teta, t):
    teta= toRadian(teta)
    return r*math.sin(teta*t)

def toRadian(teta):
    return (teta/360)*2*3.14

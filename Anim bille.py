from tkinter import *
import math

largeur = 300
hauteur = 300
rayon = 15 # rayon de la balle
dt=0.5 # homogène à un temps (en secondes) 

# position et vitesse initiale
x1, y1 = 40., 100.
vx1, vy1 = 0, 0

x2, y2 = 150., 150.
vx2, vy2 = 0, 0

# Création de la fenêtre principale
Mafenetre = Tk()
Mafenetre.title("Animation Balle")

# Création d'un widget Canvas
Canevas = Canvas(Mafenetre,height=hauteur,width=largeur,bg='green')
Canevas.pack(padx=5,pady=5)

# Création des objets graphiques
Bille1=Canevas.create_oval(x1-rayon, y1-rayon, x1+rayon, y1+rayon ,width=1,fill='black')
Bille2=Canevas.create_oval(x2-rayon, y2-rayon, x2+rayon, y2+rayon ,width=1,fill='White')

print("Choisir une puissance sur une échelle de 1 à 10")

def coup(event):
    x,y = event.x,event.y
    if x in range(int(x1-rayon),int(x1+rayon)) and y in range(int(y1-rayon),int(y1+rayon)) :
            
            deplacement()
    
def deplacement():
    """ Déplacement de la balle """
    global x1, y1, x2, y2, vx1, vy1, vx2, vy2
    
    
    
    if vx1==0 and vy1 == 0:
        vx1= puissance
        vy1= puissance+3
    
    # rebond à droite
    if x1 + rayon > largeur:
        x1, y1 = largeur-rayon, y1
        vx1, vy1 = -vx1, vy1

    if x2 + rayon > largeur:
        x2, y2 = largeur-rayon, y2
        vx2, vy2 = -vx2, vy2 

    # rebond à gauche
    if x1 - rayon < 0:
        x1, y1 = rayon, y1
        vx1, vy1 = -vx1, vy1

    if x2 - rayon < 0:
        x2, y2 = rayon, y2
        vx2, vy2 = -vx2, vy2
        
    # rebond en bas
    if y1 + rayon > hauteur:
        x1, y1 = x1, hauteur-rayon
        vx1, vy1 = vx1, -vy1
        
    if y2 + rayon > hauteur:
        x2, y2 = x2, hauteur-rayon
        vx2, vy2 = vx2, -vy2

    # rebond en haut
    if y1 - rayon < 0:
        x1, y1 = x1, rayon
        vx1, vy1 = vx1, -vy1
        
    if y2 - rayon < 0:
        x2, y2 = x2, rayon
        vx2, vy2 = vx2, -vy2
            
    # detection collision
    dcarre= (x1-x2)**2 + (y1-y2)**2
    if (dcarre <= (2.* rayon)**2):
        print("collision")
        # calcul du vecteur unitaire reliant les deux centres
        ux, uy = x2 - x1, y2 - y1
        norme = math.sqrt(ux**2+uy**2)
        ux, uy = ux/norme, uy/norme
        # a = (v2-v1).u, voir les formules 
        a = (vx2-vx1)*ux + (vy2-vy1)*uy
        vxp1, vyp1 = vx1 + a*ux, vy1 + a*uy
        vxp2, vyp2 = vx2 - a*ux, vy2 - a*uy

        vx1 , vy1 = vxp1, vyp1
        vx2 , vy2 = vxp2, vyp2
                    
    # calcul nvelle position
    x1, y1 = x1 + vx1 * dt, y1 + vy1 * dt
    x2, y2 = x2 + vx2 * dt, y2 + vy2 * dt
                
    # affichage des billes dans nvelle position
    Canevas.coords(Bille1, x1-rayon, y1-rayon, x1+rayon, y1+rayon)
    Canevas.coords(Bille2, x2-rayon, y2-rayon, x2+rayon, y2+rayon)
    # mise à jour
    Mafenetre.after(int(10*dt),deplacement)


   

Mafenetre.bind('<ButtonPress-1>',coup)
puissance = float(input("puissance du coup ? :"))       
# ----------------------------------------------------------------

Mafenetre.mainloop()

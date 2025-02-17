import tkinter 
import tkinter.font as tkFont
import os

#=============== ici c'est le mot de passe ================

player1 = ""
player2 = ""

while str(input("Shazam existe et te demande un mot de passe\n----> ")) != "StackOverflow": 
    print("Shazam te refuse l'entrée")

print("félicitations tu a correctement saisie [insérer longueur du mot de passe]")

while len(player1)>10 or len(player1)==0:
    if len(player1)>10:
        print("Je ne crois pas que ton nom soit un roman...")
    player1 = str(input("Joueur 1 comment t'appelle tu ? ~> "))

while len(player2)>10 or len(player2)==0:
    if len(player2)>10:
        print("Je ne crois pas que ton nom soit un roman...")
    elif player1==player2:
        print("Par souci de budget on doit vraiment avoir deux noms différents sinon c'est la mer2")

    player2 = str(input("toi Joueur 2, dit moi ton nom ? ~> "))

#=============================================================

#=========================== FONCTIONS =============================

def board(x1, y1, x2, y2):
    # Cette fonction définie les rectangles du tableau de jeu
    pas = x2 - x1
    for i in range(4):
        for j in range(4):
            can.create_rectangle(x1 + j*pas, y1 + i*pas, x2 +j*pas, y2 + i*pas)         

def pturn(powner):
    # Permet de changer l'appartanence du tour pour chaque joueur
    if powner == "p1":
        ControlNode.owner = "p1"
    elif powner == "p2":
        ControlNode.owner = "p2"
    
    allowinteraction()
    playertobegin.place_forget()
    ichoosedone.place_forget()
    ichoosedtwo.place_forget()

    button_giveup.place(x = 140, y = 400) 
    button_exitprocess.place(x = 310, y = 400)
    score.configure(background="white", foreground = "red",
                         text = player1+"'s turn")
    
def init_cases():
    #On reinitialise les conteurs avec les jetons de chacun
    ControlNode.Tokencb = 0
    ControlNode.Tokenmp1 = 8
    ControlNode.Tokenmp2 = 8
    ControlNode.round_type = "type1"

    playertobegin.place(x = 165, y = 370)
    ichoosedone.place(x = 220, y = 405)
    ichoosedtwo.place(x = 220, y = 465)

    #On enleve les jetons des cases
    for case in liste_cases:
        case.remove_token()
    
    labelnamep1.configure(text = "j1's token: " + str(ControlNode.Tokenmp1))
    labelnamep2.configure(text = "j2's token: " + str(ControlNode.Tokenmp2))
    #for i in range(ControlNode.Tokenmp1):
    #    if i % 2 == 0:
    #         blue_remaining[i] = can.create_image(40, 150 + 26 * i, anchor = "nw", image = img_light_red)
    #    else:
    #         blue_remaining[i] = can.create_image(110, 150 + 26 * (i - 1), anchor = "nw", image = img_light_red)
    #
    # on replace les pions bleu
    #for i in range(ControlNode.Tokenmp2):
    #     if i % 2 == 0:
    #         red_remaining[i] = can.create_image(440, 150 + 26 * i, anchor = "nw", image = img_light_blue)
    #     else:
    #         red_remaining[i] = can.create_image(510, 150 + 26 * (i - 1), anchor = "nw", image = img_light_blue)
        
    score.configure(background="white", text = "")
    
    start_button.place_forget()
    button_exitprocess.place_forget()
    
def allowinteraction():
    for case in liste_cases:
        case.canvas.bind("<Button-1>", case.PionObjectCoreInter)
        case.frame.configure(cursor = "hand2")
    
def blockinteraction():
    for case in liste_cases:
        case.canvas.unbind("<Button-1>")
        case.frame.configure(cursor = "")  
    
def winningifloop(val):
    #gracieusement récuperée sur Github
    if (caseA1.intcolor == val and caseB1.intcolor == val and caseC1.intcolor == val or
        caseB1.intcolor == val and caseC1.intcolor == val and caseD1.intcolor == val or
        caseA2.intcolor == val and caseB2.intcolor == val and caseC2.intcolor == val or
        caseB2.intcolor == val and caseC2.intcolor == val and caseD2.intcolor == val or
        caseA3.intcolor == val and caseB3.intcolor == val and caseC3.intcolor == val or
        caseB3.intcolor == val and caseC3.intcolor == val and caseD3.intcolor == val or
        caseA4.intcolor == val and caseB4.intcolor == val and caseC4.intcolor == val or
        caseB4.intcolor == val and caseC4.intcolor == val and caseD4.intcolor == val or
        caseA1.intcolor == val and caseA2.intcolor == val and caseA3.intcolor == val or
        caseA2.intcolor == val and caseA3.intcolor == val and caseA4.intcolor == val or
        caseB1.intcolor == val and caseB2.intcolor == val and caseB3.intcolor == val or
        caseB2.intcolor == val and caseB3.intcolor == val and caseB4.intcolor == val or
        caseC1.intcolor == val and caseC2.intcolor == val and caseC3.intcolor == val or
        caseC2.intcolor == val and caseC3.intcolor == val and caseC4.intcolor == val or
        caseD1.intcolor == val and caseD2.intcolor == val and caseD3.intcolor == val or
        caseD2.intcolor == val and caseD3.intcolor == val and caseD4.intcolor == val or
        caseA1.intcolor == val and caseB2.intcolor == val and caseC3.intcolor == val or
        caseB1.intcolor == val and caseC2.intcolor == val and caseD3.intcolor == val or
        caseA2.intcolor == val and caseB3.intcolor == val and caseC4.intcolor == val or
        caseB2.intcolor == val and caseC3.intcolor == val and caseD4.intcolor == val or
        caseC1.intcolor == val and caseB2.intcolor == val and caseA3.intcolor == val or
        caseD1.intcolor == val and caseC2.intcolor == val and caseB3.intcolor == val or
        caseC2.intcolor == val and caseB3.intcolor == val and caseA4.intcolor == val or
        caseD2.intcolor == val and caseC3.intcolor == val and caseB4.intcolor == val):
        return True
    return False 
    
def winnerbool():
    if (winningifloop(light_red) or winningifloop(dark_red) or winningifloop(light_blue) or winningifloop(dark_blue)):
        score.configure(background="white", text = "WIN!!!")
        button_giveup.place_forget()
        reboot_button.place(x = 140, y = 400) 
        cancel_button.place_forget()
        blockinteraction()
        return True 
    return False

def useful_updat_token():
    #Actualise le decompte des jetons restants
    labelnamep1.configure(text = "j1's token: " + str(ControlNode.Tokenmp1))
    labelnamep2.configure(text = "j2's token: " + str(ControlNode.Tokenmp2))
    
def relaunchgame():
    #pour relancer le jeu
    reboot_button.place_forget()
    for element in blue_remaining:
        can.delete(element)
        
    init_cases()

def giveup():
    #Pour capituler
    blockinteraction()
    button_giveup.place_forget()
    reboot_button.place(x = 140, y = 400) 
    cancel_button.place_forget()


#=========================== OBJETS =============================

class ControlNode:
    # Simple agregateur de coordination du jeu
    owner = "p1" 
    round_type = "type1"
    Tokencb = 0
    Tokenmp1 = 8
    Tokenmp2 = 8

class Pions:
    #Les cases sont les pions, elles peuvent intéragir
    def __init__(self, pos, index):
        # Inititialisation
        self.frame = tkinter.Frame(background = "white", height = 49, width = 49)
        self.canvas = tkinter.Canvas(self.frame, width = 50, height = 50, background = "white")
        self.index = index
        self.coord = pos
        self.intcolor = 0 
        self.token = ""

        self.canvas.place(x = -1, y = -1)
    
    #----------- Mouvements de jetons ------------
    
    def movetoken(self, direction):
        #transfert vers la direction indiquée
        if direction == "up":
            case_du_haut = liste_cases[self.index - 4]
            self.ultimove(case_du_haut)
        elif direction == "left":
            case_de_gauche = liste_cases[self.index - 1]
            self.ultimove(case_de_gauche)
        elif direction == "right":
            case_de_droite = liste_cases[self.index + 1]
            self.ultimove(case_de_droite)
        elif direction == "down":
            case_du_bas = liste_cases[self.index + 4]
            self.ultimove(case_du_bas)
        
        if winnerbool():
            return
        allowinteraction()
        cancel_button.place_forget()
        ControlNode.round_type = "type1"
        
    #----------- Placements de Jetons ------------

    def playredlight_token(self):
        self.token = self.canvas.create_image(1, 1, anchor = "nw", image = img_light_red)
        self.intcolor = light_red
        ControlNode.Tokenmp1 -= 1
        ControlNode.Tokencb += 1        
        self.board_round()
    
    
    def payreddark_token(self):
        self.token = self.canvas.create_image(1, 1, anchor = "nw", image = img_dark_red)
        self.intcolor = dark_red
        ControlNode.Tokenmp1 -= 1
        ControlNode.Tokencb += 1
        self.board_round()
    

    def playbluelight_token(self):
        self.token = self.canvas.create_image(1, 1, anchor = "nw", image = img_light_blue)
        self.intcolor = light_blue
        ControlNode.Tokenmp2 -= 1
        ControlNode.Tokencb += 1
        self.board_round()
    
        
    def playbluedark_token(self):
        self.token = self.canvas.create_image(1, 1, anchor = "nw", image = img_dark_blue)
        self.intcolor = dark_blue
        ControlNode.Tokenmp2 -= 1
        ControlNode.Tokencb += 1
        self.board_round()
        
    #----------- Fonctions très importantes ------------

    def check_empty(self):
        # Si il y a une couleur sur la case c'est qu'il y a un pion tout simplement
        if self.intcolor != 0:
            return True
        else:
            return False
    
    def remove_token(self):
        # On supprime le canvas correspondant et reboot le token
        self.canvas.delete(self.token)
        self.token = ""
        self.intcolor = 0

    def board_round(self):
        # On retourne le owner au tableau de jeu
        choicetokenwindow.place_forget()
        lightchoosed.place_forget()
        darkchoosed.place_forget()
        cancel_button.place_forget()
        if ControlNode.Tokencb == 16:
            if winnerbool():
                cancel_button.place_forget() #enleve le boutton annuler
                return
            score.configure(background="white", text = "")
            button_giveup.place_forget()
            reboot_button.place(x = 140, y = 400)
            cancel_button.place_forget()
            blockinteraction()
            return
        else:
            allowinteraction()
            useful_updat_token()
            if ControlNode.owner == "p1":
                ControlNode.owner = "p2"
                score.configure(background="white", text =  player2 + "'s turn")
            else:
                ControlNode.owner = "p1"
                score.configure(background="white", text = player1 + "'s turn")
            ControlNode.round_type = "type2"

    def ultimove(self, destination):      
        # l'opération de ultimove ce fait ici
        if self.intcolor == light_red:
            destination.token = destination.canvas.create_image(1, 1, anchor = "nw", image = img_dark_red)
            destination.intcolor = dark_red
        elif self.intcolor == dark_red:
            destination.token = destination.canvas.create_image(1, 1, anchor = "nw", image = img_light_red)
            destination.intcolor = light_red
        elif self.intcolor == light_blue:
            destination.token = destination.canvas.create_image(1, 1, anchor = "nw", image = img_dark_blue)
            destination.intcolor = dark_blue
        elif self.intcolor == dark_blue:
            destination.token = destination.canvas.create_image(1, 1, anchor = "nw", image = img_light_blue)
            destination.intcolor = light_blue
        
        self.canvas.delete(self.token)
        self.token = ""
        self.intcolor = 0
        return
    
    def movecancel(self):
        #Permet de deselectionner
        choicetokenwindow.place_forget()
        lightchoosed.place_forget()
        darkchoosed.place_forget()
        cancel_button.place_forget()
        allowinteraction()
        
    def ennemycancel(self):
        cancel_button.place_forget()
        allowinteraction()        
    
    def PionObjectCoreInter(self, event):
        # Verifie la prochaine action à accomplir pour chaque cases
        if ControlNode.round_type == "type1": #Si il s'agit simplement d'installer un pion
            if self.check_empty():
                return
            blockinteraction()
            choicetokenwindow.place(x = 105, y = 370)
            lightchoosed.place(x = 140, y = 400)
            darkchoosed.place(x = 310, y = 400)
            cancel_button.place(x = 225, y = 450)
            #On installe la bonne couleur en fonction du joueur
            if ControlNode.owner == "p1":
                lightchoosed.configure(command = self.playredlight_token)
                darkchoosed.configure(command = self.payreddark_token)
            else:
                lightchoosed.configure(command = self.playbluelight_token)
                darkchoosed.configure(command = self.playbluedark_token)
            cancel_button.configure(command = self.movecancel)
            return

        elif ControlNode.owner == "p1":
            checkemptypions = 0
            blockinteraction() 

            if (self.index - 4 >= 0 and self.index - 4 <= 15 and not liste_cases[self.index - 4].check_empty()):
                checkemptypions += 1
                liste_cases[self.index - 4].canvas.bind("<Button-1>", lambda event, arg="up": self.movetoken(arg))
                liste_cases[self.index - 4].frame.configure(cursor = "hand2")
               
            if (self.index - 1 != 3 and self.index - 1 != 7 and self.index - 1 != 11 and self.index - 1 >= 0 and self.index - 1 <= 15 and not liste_cases[self.index - 1].check_empty()):
                checkemptypions += 1
                liste_cases[self.index - 1].canvas.bind("<Button-1>", lambda event, arg="left": self.movetoken(arg))
                liste_cases[self.index - 1].frame.configure(cursor = "hand2")

            if (self.index + 1 != 4 and self.index + 1 != 8 and self.index + 1 != 12 and self.index + 1 >= 0 and self.index + 1 <= 15 and not liste_cases[self.index + 1].check_empty()):
                checkemptypions += 1
                liste_cases[self.index + 1].canvas.bind("<Button-1>", lambda event, arg="right": self.movetoken(arg))
                liste_cases[self.index + 1].frame.configure(cursor = "hand2")

            if (self.index + 4 >= 0 and self.index + 4 <= 15 and not liste_cases[self.index + 4].check_empty()):
                checkemptypions += 1
                liste_cases[self.index + 4].canvas.bind("<Button-1>", lambda event, arg="down": self.movetoken(arg))
                liste_cases[self.index + 4].frame.configure(cursor = "hand2")
               
            if checkemptypions == 0:
                allowinteraction()
                return
                
            cancel_button.place(x = 225, y = 450)
            cancel_button.configure(command = self.ennemycancel)
            return
        
        else:
            checkemptypions = 0
            blockinteraction()       
            if (self.index - 4 >= 0 and self.index - 4 <= 15 and not liste_cases[self.index - 4].check_empty()):
                checkemptypions += 1
                liste_cases[self.index - 4].canvas.bind("<Button-1>", lambda event, arg="up": self.movetoken(arg))
                liste_cases[self.index - 4].frame.configure(cursor = "hand2")
                
            if (self.index - 1 != 3 and self.index - 1 != 7 and self.index - 1 != 11 and self.index - 1 >= 0 and self.index - 1 <= 15 and not liste_cases[self.index - 1].check_empty()):
                checkemptypions += 1
                liste_cases[self.index - 1].canvas.bind("<Button-1>", lambda event, arg="left": self.movetoken(arg))
                liste_cases[self.index - 1].frame.configure(cursor = "hand2")
                
            if (self.index + 1 != 4 and self.index + 1 != 8 and self.index + 1 != 12 and self.index + 1 >= 0 and self.index + 1 <= 15 and not liste_cases[self.index + 1].check_empty()):
                checkemptypions += 1
                liste_cases[self.index + 1].canvas.bind("<Button-1>", lambda event, arg="right": self.movetoken(arg))
                liste_cases[self.index + 1].frame.configure(cursor = "hand2")
                    
            if (self.index + 4 >= 0 and self.index + 4 <= 15 and not liste_cases[self.index + 4].check_empty()):
                checkemptypions += 1
                liste_cases[self.index + 4].canvas.bind("<Button-1>", lambda event, arg="down": self.movetoken(arg))
                liste_cases[self.index + 4].frame.configure(cursor = "hand2")
                
            if checkemptypions == 0:
                allowinteraction()
                return
            
            cancel_button.place(x = 225, y = 450)
            cancel_button.configure(command = self.ennemycancel)
            return


#=========================== GRAPHISME =============================

fen = tkinter.Tk()
fen.option_add('*Font', '19')
fen.geometry("600x600") #Dimensions de la fenetre
fen.title("Hearthsone Pre-Alpha Edition") #Nom de la fenetre. Reference à un jeu de plateau similaire
fen.resizable(False, False) #On empeche de redimensionner la fenetre

#Canvas création
can = tkinter.Canvas(fen, width = 600, height = 600, background = "white")
can.place(x = 0, y = 0)
x1, y1, x2, y2 = 200, 150, 250, 200
board(x1, y1, x2, y2)

# place name
labelnamep1 = tkinter.Label(background = "white", foreground = "red", font = ("Courier", 15), width = 19, text = ("j1 : " + player1))
labelnamep1.place(x = -10, y = 70)
labelnamep2 = tkinter.Label(background = "white", foreground = "blue", font = ("Courier", 15), width = 19, text = ("j2 : " + player2))
labelnamep2.place(x = -10, y = 100)

#mini-frame
score = tkinter.Label(can, background ="white", width = 32, font = ("Arial", 25))
score.place(x = 0, y = 32)
playertobegin = tkinter.LabelFrame(background = "white", relief = "ridge", border = 5, height = 150, width = 280, labelanchor = "n", text = "Qui commence ?", font = ("Arial", 15))
ichoosedone = tkinter.Button(background = "white", bd = 5, relief  = "ridge", width = 13, text = player1, font = 40, cursor = "hand2", command = lambda:pturn("p1"))
ichoosedtwo = tkinter.Button(background = "white", bd = 5, relief  = "ridge", width = 13, text = player2, font = 40, cursor = "hand2", command = lambda:pturn("p2"))

#------ Les boutons ------
start_button = tkinter.Button(background = "white", bd = 5, relief  = "ridge", width = 13, text = "Start", font = 40, cursor = "hand2", command = init_cases)

reboot_button = tkinter.Button(background = "white", bd = 5, relief  = "ridge", width = 13, text = "Reboot", font = 40, cursor = "hand2", command = relaunchgame)

button_giveup = tkinter.Button(background = "white", bd = 5, relief  = "ridge", width = 13, text = "Capituler", font = 40, cursor = "hand2", command = giveup)

button_exitprocess = tkinter.Button(background = "white", bd = 5, relief  = "ridge", width = 13, text = "exit", font = 40, cursor = "hand2", command = fen.destroy)

choicetokenwindow = tkinter.LabelFrame(background = "white", relief = "ridge", border = 5, height = 100, width = 400, labelanchor = "n", text = "Quelle couleur veut tu ?", font = ("Arial", 15))

lightchoosed = tkinter.Button(background = "white", bd = 5, relief  = "ridge", width = 13, text = "Light Token", font = 40, cursor = "hand2", command = "")

darkchoosed = tkinter.Button(background = "white", bd = 5, relief  = "ridge", width = 13, text = "Dark Token", font = 40, cursor = "hand2", command = "")

cancel_button = tkinter.Button(background = 'white', bd = 5, relief = "ridge", width = 13, text = "Annuler", font = 40, cursor = "hand2", command = "")
start_button.place(x = 220, y = 400)
button_exitprocess.place(x = 220, y = 450)

# ========================================
# vvvvvv SECTION VARIABLES vvvvvv
# ========================================

# int définissant la couleur
light_red = 1
dark_red = 2
light_blue = 3
dark_blue = 4

#icon paths
img_light_red = tkinter.PhotoImage(file="redshibalight.png")  
img_dark_red = tkinter.PhotoImage(file="redshibadark.png")
img_light_blue = tkinter.PhotoImage(file="blueshibalight.png")  
img_dark_blue = tkinter.PhotoImage(file="blueshibadark.png") 

caseA1 = Pions(pos = "A1", index = 0) #ligne 1
caseB1 = Pions(pos = "B1", index = 1)   
caseC1 = Pions(pos = "C1", index = 2)
caseD1 = Pions(pos = "D1", index = 3)
caseA2 = Pions(pos = "A2", index = 4) #ligne 2
caseB2 = Pions(pos = "B2", index = 5)
caseC2 = Pions(pos = "C2", index = 6)
caseD2 = Pions(pos = "D2", index = 7)
caseA3 = Pions(pos = "A3", index = 8) #ligne 3
caseB3 = Pions(pos = "B3", index = 9)
caseC3 = Pions(pos = "C3", index = 10)
caseD3 = Pions(pos = "D3", index = 11)
caseA4 = Pions(pos = "A4", index = 12) #lign 4
caseB4 = Pions(pos = "B4", index = 13)
caseC4 = Pions(pos = "C4", index = 14)
caseD4 = Pions(pos = "D4", index = 15)


#On range ces cases dans une liste pour pouvoir iterer des actions pour chaque case
liste_cases = [caseA1, caseB1, caseC1, caseD1, 
               caseA2, caseB2, caseC2, caseD2, 
               caseA3, caseB3, caseC3, caseD3, 
               caseA4, caseB4, caseC4, caseD4]


#On crée des listes vides à 8 places pour contenir les jetons rouges et bleus restants
blue_remaining = ["", "",
                           "", "",
                           "", "",
                           "", ""]

red_remaining = ["", "",
                           "", "",
                           "", "",
                           "", ""]

#On place les cadres sur leurs cases
caseA1.frame.place(x = 201, y = 151)
caseB1.frame.place(x = 251, y = 151)
caseC1.frame.place(x = 301, y = 151)
caseD1.frame.place(x = 351, y = 151)
caseA2.frame.place(x = 201, y = 201)
caseB2.frame.place(x = 251, y = 201)
caseC2.frame.place(x = 301, y = 201)
caseD2.frame.place(x = 351, y = 201)
caseA3.frame.place(x = 201, y = 251)
caseB3.frame.place(x = 251, y = 251)
caseC3.frame.place(x = 301, y = 251)
caseD3.frame.place(x = 351, y = 251)
caseA4.frame.place(x = 201, y = 301)
caseB4.frame.place(x = 251, y = 301)
caseC4.frame.place(x = 301, y = 301)
caseD4.frame.place(x = 351, y = 301)

fen.mainloop()
from tkinter import* 
import pygame 

pygame.init() 
son1=pygame.mixer.Sound("Alan Walker - Sing Me To Sleep.wav") 
son2=pygame.mixer.Sound("twenty one pilots Ride.wav") 
son3=pygame.mixer.Sound("Castle in the Sky - DJ Satomi.wav") 

#def 
#jouer 
def jouer1():
    son1.play() 

def jouer2():
    son2.play() 

def jouer3():
    son3.play() 

#pause 
def pause():
    pygame.mixer.pause() 

#continue 
def continu():
    pygame.mixer.unpause() 

#stop 
def arret1():
    son1.stop() 

def arret2():
    son2.stop() 

def arret3():
    son3.stop() 


fen=Tk() 

#graphique 
fen.title("Jukebox / mélange son") 
canevas=Canvas(fen,bg="grey26",heigh=400,width=400) 
canevas.grid(rowspan=4,columnspan=3) 

#boutonS 
#b1 play (lecture) 
#b1.1 AW 
bout11=Button(fen,text="Alan Walker play",command=jouer1) 
bout11.grid(row=4,column=1,padx=10,pady=10) 

#b1.2 21 pilots 
bout12=Button(fen,text="21 pilots play",command=jouer2) 
bout12.grid(row=5,column=1,padx=10,pady=10) 

#b1.3 Castle sky 
bout13=Button(fen,text="Castle sky play",command=jouer3) 
bout13.grid(row=6,column=1,padx=10,pady=10) 

#b2 pause (temporaire) 
bout2=Button(fen,text="pause",command=pause) 
bout2.grid(row=0,column=3,padx=10,pady=10) 

#b3 continue (a mettre en position 3 plus tard) 
bout3=Button(fen,text="continue" ,command=continu) 
bout3.grid(row=3,column=3,padx=10,pady=10) 

#b4 rewind (reprend depuis début) 
#b4.1 stop AW 
bout41=Button(fen,text="Alan Walker stop",command=arret1) 
bout41.grid(row=4,column=2,padx=10,pady=10) 

#b4.2 stop 21 pilots 
bout42=Button(fen,text="21 pilots stop",command=arret2) 
bout42.grid(row=5,column=2,padx=10,pady=10) 

#b4.3 
bout43=Button(fen,text="Castle sky stop",command=arret3) 
bout43.grid(row=6,column=2,padx=10,pady=10) 


#b5 quit 
bout5=Button(fen,text="Fermer fenêtre" ,command=fen.destroy) 
bout5.grid(row=7,column=3,padx=10,pady=10) 

fen.mainloop()

add_library('minim')
import os
path=os.getcwd()
player = Minim(this)

class Creature:
    def __init__(self,x,y,r,g,img,w,h,F):
        self.x=x # X position
        self.y=y # Y position
        self.r=r # Radius
        self.g=g # Ground level
        self.vx=0 # Change of x
        self.vy=0 # Change of y
        self.w=w # Width of image
        self.h=h # Height of image
        self.F=F # Frame count
        self.f=0 # Cycles through frames
        self.img = loadImage(path+"/images/"+img)
        self.dir = 1 # Direction of image
    
    def gravity(self):
        if self.y+self.r < self.g:
            self.vy += 0.3
            if self.vy > self.g - (self.y+self.r):
                self.vy = self.g - (self.y+self.r)
        else:
            self.vy = 0 #-10
    
    def update(self):
        self.gravity()
        self.x += self.vx
        self.y += self.vy
        
    def display(self):
        self.update()
        
        # if self.vy != 0:
        #     self.f = 4
        if self.vx != 0:
            self.f = (self.f+0.3)%self.F
        else:
            self.f = 3
            
        if self.dir > 0:
            image(self.img,self.x-self.w//2,self.y-self.h//2,self.w,self.h,int(self.f)*self.w,0,int(self.f+1)*self.w,self.h)
        elif self.dir < 0:
            image(self.img,self.x-self.w//2,self.y-self.h//2,self.w,self.h,int(self.f+1)*self.w,0,int(self.f)*self.w,self.h)
            
        strokeWeight(5)
        stroke(255)
        noFill()
        ellipse(self.x,self.y,2*self.r,2*self.r)
    
class Quote(Creature):
    def __init__(self,x,y,r,g,img,w,h,F):
        Creature.__init__(self,x,y,r,g,img,w,h,F)
        self.keyHandler={LEFT:False, RIGHT:False, UP:False}
    def update(self):
        self.gravity()
        
        if self.keyHandler[LEFT]:
            self.vx = -5
            self.dir = 1
        elif self.keyHandler[RIGHT]:
            self.vx = 5
            self.dir = -1
        else:
            self.vx = 0
        
        if self.keyHandler[UP] and self.y+self.r == self.g:
            self.vy = -10
        
        self.x += self.vx
        self.y += self.vy
        
        for e in game.enemies:
            if self.distance(e) <= self.r + e.r:
                # there is a collision
                # if self.vy > 0 and self.y < e.y:
                game.enemies.remove(e)
                del e
                # self.vy = -8
                
        for g in game.guns:
            if self.distance(g) <= self.r + g.r:
                game.guns.remove(g)
                del g
                game.gunAcquired = True
                    
    def distance(self,e):
        return ((self.x-e.x)**2+(self.y-e.y)**2)**0.5
        
class Bat(Creature):
    def __init__(self,x,y,r,g,img,w,h,F,y1,y2):
        Creature.__init__(self,x,y,r,g,img,w,h,F)
        self.y1=y1
        self.y2=y2
        self.dir = -1
        
    def update(self):
        
        if self.y < self.y1:
            self.vy = 3
        elif self.y > self.y2:
            self.vy = -3
            
        self.y += self.vy

class Gun(Creature):
    def __init__(self,x,y,r,g,img,w,h,F):
        Creature.__init__(self,x,y,r,g,img,w,h, F)
        

class Bullet(Creature):
    def __init__(self,x,y,r,g,img,w,h,F,vx):
        Creature.__init__(self,x,y,r,g,img,w,h,F)
        self.vx = vx
        self.dir = vx
        self.ttl = 60
        
    def update(self):
        self.x += self.vx
        self.ttl -= 1
        if self.ttl == 0:
            game.bullets.remove(self)
            del self
            return
        
        for e in game.enemies:
            if self.distance(e) <= self.r + e.r:
                game.enemies.remove(e)
                game.bullets.remove(self)
                del self
                del e
                return
        
    def distance(self,e):
        return ((self.x-e.x)**2+(self.y-e.y)**2)**0.5
        
class Game:
    def __init__ (self,w,h,g):
        self.w=w
        self.h=h
        self.g=g
        self.gunAcquired = False
        self.quote = Quote(50,50,75,self.g,"quote.png",130,130,6)
        self.enemies = []
        self.enemies.append(Bat(300,50,35,self.g,"quote.png",70,70,8,200,500))
        self.guns = []
        self.guns.append(Gun(300,50,35,self.g,"guns.png",70,70, 0))
        
        self.bullets = []
        
    def display(self):
        stroke(255)
        line(0,self.g,self.w,self.g)
            
        self.quote.display()
        
        for g in self.guns:
            g.display()

        for e in self.enemies:
            e.display()
            
        for b in self.bullets:
            b.display()
        
game = Game(1024,768,600)

def setup():
    size(game.w, game.h)
    background(0)
    
def draw():
    background(0)
    game.display()
    
def keyPressed():
    # if game.quote.y+game.quote.r == game.quote.g: # Disallows movement when mid-air. WIP.
    if keyCode == LEFT:
        game.quote.keyHandler[LEFT]=True
    elif keyCode == RIGHT:
        game.quote.keyHandler[RIGHT]=True
    elif keyCode == UP:
        game.quote.keyHandler[UP]=True
    elif keyCode == 32 and game.gunAcquired == True:
        game.bullets.append(Bullet(game.quote.x+game.quote.dir*game.quote.r,game.quote.y,25,0,"quote.png",50,50,10,game.quote.dir*(-8))) # Needs to be edited to fit the inverted Quote sprites.
        
def keyReleased():
    if keyCode == LEFT:
        game.quote.keyHandler[LEFT]=False
    elif keyCode == RIGHT:
        game.quote.keyHandler[RIGHT]=False   
    elif keyCode == UP:
        game.quote.keyHandler[UP]=False

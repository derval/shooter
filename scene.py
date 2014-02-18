#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
from parameters import *
import entity, projectiles

class Player() :
    """class for player settings, controls, ships"""
    def __init__(self, scene):
        self.scene = scene
        self.keys = {'up':False, 'down':False, 'right':False, 'left':False,
        'shoot':False}
        self.go_right = False
        self.go_left = False
        self.go_up = False
        self.go_down = False
        self.ship = self.scene.ship
        self.alive = True
        self.score = 0

    def update(self, interval) :
        #where is going the ship ?
        if self.keys['right'] and not self.go_right and not self.keys['left'] :
            self.go_right = True
        elif not self.keys['right'] and self.go_right :
            self.go_right = False
        if self.keys['left'] and not self.go_left and not self.keys['right'] :
            self.go_left = True
        elif not self.keys['left'] and self.go_left :
            self.go_left = False

        if self.keys['up'] and not self.go_up and not self.keys['down'] :
            self.go_up = True
        elif not self.keys['up'] and self.go_up :
            self.go_up = False
        if self.keys['down'] and not self.go_down and not self.keys['up'] :
            self.go_down = True
        elif not self.keys['down'] and self.go_down :
            self.go_down = False
        
        #command ship !!
        if self.go_right :
            self.ship.fly('right', interval)
        elif self.go_left :
            self.ship.fly('left', interval)
        if self.go_up :
            self.ship.fly('up', interval)
        elif self.go_down :
            self.ship.fly('down', interval)
        #is the ship charging ?
        if self.keys['shoot'] :
            offset = CHARGE_RATE * interval
            if self.ship.charge + offset > 1 :
                self.ship.charge = 1.
            else :
                self.ship.charge += offset
        else :
            #charged shot
            if self.ship.charge > 0.5 :
                self.ship.shoot('projectiles.Blasts', self.ship.charge)
            self.ship.charge = 0.


class Scene():
    def __init__(self, game) :
        self.game = game
        self.limits = game.limits
        self.font = game.font
        self.content = []
        self.load_content()
        for item in self.content :
            if isinstance(item, entity.Ship) :
                self.ship = item
                break
        self.player = Player(self)
        self.lst_sprites = []
        #textual info
        self.last_txt_flip = 0
        self.fps_surf = self.game.font.render('', False, txt_color)
        self.update()

    
    def load_fighter(self, identity, targ_bullets) :
        coord = random.randint(0, self.limits[0]), self.limits[1]/6
        fighter = entity.Fighter(self, coord, identity)
        #link fighters to projectile maps
        fighter.new_weapon(targ_bullets)

    def load_ship(self, identity, ship_bullets, ship_blasts) :
        ship = entity.Ship(self, (0,self.limits[1]-2*txt_inter), identity)
        ship.new_weapon(ship_bullets)
        ship.new_weapon(ship_blasts)
        
    def load_content(self) :
        #projectile maps
        self.ship_blasts = projectiles.Blasts(self, 'up', 'OOO')
        self.ship_bullets = projectiles.Bullets(self, 'up', 'o')
        self.targ_bullets = projectiles.Bullets(self, 'down', 'H')

        self.load_ship('ship', self.ship_bullets, self.ship_blasts)


    def collide(self, proj_map, target_map, time) :
        """repercute collisions projectiles and alpha maps of sprites"""
        for xP, yP, xPe, yPe, pixel, itemP, index in proj_map :
            #one pixel projectile
            if pixel :
                for xT, yT, xTe, yTe, itemT in target_map :
                    #is in range ?
                    if xP < xTe and xP > xT and yP < yTe and yP > yT :
                        #per pixel collision
                        if itemT.array[xP - xT, yP - yT] :
                            #remove or not, colliding projectile
                            #hurt or not, entity
                            itemT.collided(itemP, index, time)
                            itemP.collided(index)
            #rectangular projectile
            else :
                for xT, yT, xTe, yTe, itemT in target_map :
                    if xP < xTe and xPe > xT and yP < yTe and yPe > yT :
                        if True in itemT.array[xP-xT:xPe-xT, yP-yT:yPe-yT] :
                            print yP, yPe - yP,yT, yTe - yT
                            itemT.collided(itemP, index, time)
                            itemP.collided(index)

    def update(self, interval = 0, time = 0) :
        #collision maps
        ship_map = []
        target_map = []
        ship_proj_map = []
        target_proj_map = []
        #sprite list for drawing
        self.lst_sprites = []
        self.nb_fighters = 0
        #show fps but not every frame
        if time > self.last_txt_flip + 500 :
            fps = str(int(self.game.fps))
            self.fps_surf = self.game.font.render(fps, False, txt_color)
            self.lst_sprites.append(((0, 0), self.fps_surf))
            self.last_txt_flip = time
        else :
            self.lst_sprites.append(((0, 0), self.fps_surf))
        #explore scene
        for item in self.content :
            if isinstance(item, entity.Mobile_sprite) :
                x, y = item.pos
                #prepare sprite list for drawing
                self.lst_sprites.append(((x, y), item.surface))
                #populate collision maps
                #precompute for faster detection
                width, height = item.array.shape
                identifier = (x, y, x+width, y+height, item)
                if item.ally :
                    ship_map.append(identifier)
                else :
                    if isinstance(item, entity.Fighter) :
                        self.nb_fighters += 1
                    target_map.append(identifier)
            elif isinstance(item, projectiles.Projectile) :
                for i in range(len(item.positions)) :
                    x, y = item.draw_position(i)
                    self.lst_sprites.append(((x, y), item.surface))
                    #blasts have wide damage zone other are on a pixel only
                    if isinstance(item, projectiles.Blasts) :
                        identifier = (x, y, x+item.width, y+item.height, False, item, i)
                    else :
                        x, y = item.position(i)
                        identifier = (x, y, 1, 1, True, item, i)
                    if item.ally :
                        ship_proj_map.append(identifier)
                    else :
                        target_proj_map.append(identifier)
        #detect collisions and update accordingly
        #~ print len(ship_proj_map), len(target_map), len(target_proj_map), len(ship_map)
        self.collide(ship_proj_map, target_map, time)
        #~ self.collide(target_proj_map, ship_map)
        #evolution of scenery
        if self.nb_fighters < NBENEMIES :
            self.load_fighter('target', self.targ_bullets)
        #update individuals
        for item in self.content :
            #shoot and stuff
            item.update(interval)
        #update player status
        if self.player.alive :
            self.player.update(interval)
    

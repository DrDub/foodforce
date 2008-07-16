#! /usr/bin/env python##   Author : Mohit Taneja (mohitgenii@gmail.com)#   Date : 9/06/2008 ##   This program is free software; you can redistribute it and/or modify#   it under the terms of the GNU General Public License as published by#   the Free Software Foundation; either version 2 of the License, or#   (at your option) any later version.##   This program is distributed in the hope that it will be useful,#   but WITHOUT ANY WARRANTY; without even the implied warranty of#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the#   GNU General Public License for more details.##   You should have received a copy of the GNU General Public License#   along with this program; if not, write to the Free Software#   Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.#import pygameimport osfrom pygame.locals import *class Spritesheet:    def __init__(self, filename):        self.sheet = pygame.image.load(os.path.join('data', filename)).convert_alpha()            def imgat(self, rect, colorkey = None):        rect = Rect(rect)        image = pygame.Surface(rect.size).convert()        image.blit(self.sheet, (0, 0), rect)        if colorkey is not None:            if colorkey is -1:                colorkey = image.get_at((0, 0))            image.set_colorkey(colorkey, RLEACCEL)        return image                def imgsat(self, rects, colorkey = None):        imgs = []        for rect in rects:            imgs.append(self.imgat(rect, colorkey))        return imgs        House_tiles_list = []Hospital_tiles_list = []Farm_tiles = [] Workshop_tiles_list = []School_tiles_list = [] Fountain_tiles = []def load_images():        global House_tiles_list    global Hospital_tiles_list    global Farm_tiles    global Workshop_tiles_list    global School_tiles_list    global Fountain_tiles        # Loading images of School    ss = Spritesheet('school_upgrade0.png')    tiles = ss.imgsat([( 0, 0, 410, 450),( 410, 0, 440, 450),( 850, 0, 440, 450),( 1290, 0, 440, 450)], -1)    School_tiles_list.append(tiles)                ss = Spritesheet('school_upgrade1.png')    tiles = ss.imgsat([( 0, 0, 420, 450),( 420, 0, 420, 450),( 840, 0, 420, 450)], -1)    School_tiles_list.append(tiles)      ss = Spritesheet('school_upgrade2.png')    tiles = ss.imgsat([( 0, 0, 420, 450),( 420, 0, 420, 450),( 840, 0, 420, 450)], -1)    School_tiles_list.append(tiles)      ss = Spritesheet('school_upgrade3.png')    tiles = ss.imgsat([( 0, 0, 420, 450),( 420, 0, 420, 450),( 840, 0, 420, 450)], -1)    School_tiles_list.append(tiles)                # Loading images of Workshop    ss = Spritesheet('workshop_upgrade0.png')    tiles = ss.imgsat([(   0, 0, 480, 500),( 480, 0,520, 500),( 1000, 0, 520, 500)], -1)    Workshop_tiles_list.append(tiles)                ss = Spritesheet('workshop_upgrade1.png')    tiles = ss.imgsat([( 0, 0, 520, 500),( 520, 0, 520, 500),( 1040, 0, 520, 500)], -1)    Workshop_tiles_list.append(tiles)     ss = Spritesheet('workshop_upgrade2.png')    tiles = ss.imgsat([(   0, 0, 515, 500),( 515, 0, 515, 500),( 1030, 0, 515, 500)], -1)    Workshop_tiles_list.append(tiles)        ss = Spritesheet('workshop_upgrade3.png')    tiles = ss.imgsat([(   0, 0, 520, 520),( 520, 0, 520, 520),( 1040, 0, 760, 520)], -1)    Workshop_tiles_list.append(tiles)            # Loading images of House    ss = Spritesheet('house_upgrade0.png')    tiles = ss.imgsat([(   0, 0, 250, 300),( 250, 0, 280, 300),( 530, 0, 280, 300),( 810, 0, 280, 300)], -1)    House_tiles_list.append(tiles)                ss = Spritesheet('house_upgrade1.png')    tiles = ss.imgsat([(   0, 0, 260, 300),( 260, 0, 260, 300),( 520, 0, 260, 300)], -1)    House_tiles_list.append(tiles)     ss = Spritesheet('house_upgrade2.png')    tiles = ss.imgsat([(   0, 0, 260, 300),( 260, 0, 260, 300),( 520, 0, 260, 300)], -1)    House_tiles_list.append(tiles)        ss = Spritesheet('house_upgrade3.png')    tiles = ss.imgsat([(   0, 0, 260, 300),( 260, 0, 260, 300),( 520, 0, 260, 300)], -1)    House_tiles_list.append(tiles)            # Loading images of Hospital        ss = Spritesheet('hospital_upgrade0.png')    tiles = ss.imgsat([(   0, 0, 340, 500),( 340, 0, 370, 500),( 710, 0, 370, 500),( 1080, 0, 363, 500)], -1)    Hospital_tiles_list.append(tiles)                ss = Spritesheet('hospital_upgrade1.png')    tiles = ss.imgsat([(   0, 0, 370, 500),( 370, 0, 370, 500),( 740, 0, 370, 500)], -1)    Hospital_tiles_list.append(tiles)        ss = Spritesheet('hospital_upgrade2.png')    tiles = ss.imgsat([(   0, 0, 370, 500),( 370, 0, 370, 500),( 740, 0, 370, 500)], -1)    Hospital_tiles_list.append(tiles)        ss = Spritesheet('hospital_upgrade3.png')    tiles = ss.imgsat([(   0, 0, 370, 500),( 370, 0, 370, 500),( 740, 0, 370, 500)], -1)    Hospital_tiles_list.append(tiles)        # Loading of images of Farm        ss = Spritesheet('farm.png')    tiles = ss.imgsat([(   0, 0, 500, 500),( 516, 0, 480, 500),( 1000, 0, 516, 500)], -1)    Farm_tiles.append(tiles)        # Loading images of Fountain        ss = Spritesheet('fountain.png')    tiles = ss.imgsat([( 0, 0, 140, 192),( 150, 0, 115, 192),( 285, 0, 130, 192),( 435, 0, 197, 192)], -1)    Fountain_tiles.append(tiles)
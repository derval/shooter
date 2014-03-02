#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame.locals as p_l

GAMESIZE = (320, 240) #~neo geo
#~ GAMESIZE = (1024, 500)
COLORDEPTH = 16 #set to 8 for speedier game with low color resolution !
RESCALE = '2x' #set to 2x or mame

#control settings
KEYMAP1 = {p_l.K_f : 'fullscreen',
p_l.K_m : 'mute',
p_l.K_p : 'pause',
p_l.K_RIGHT : 'right',
p_l.K_LEFT : 'left',
p_l.K_UP : 'up',
p_l.K_DOWN : 'down',
p_l.K_SPACE : 'shoot'
}

KEYMAP2 = {p_l.K_d : 'right',
p_l.K_q : 'left',
p_l.K_z : 'up',
p_l.K_s : 'down',
p_l.K_LSHIFT : 'shoot'
}

KEYMAPS = [KEYMAP1, KEYMAP2]


DEFAULTPLAY = {'name':'default',
'flash_pulse': 16,     #ms
'hit_pulse' : 50,
'blast_hit_pulse' : 100,
'game_speed' : 1,
'speed' : 0.2,     #px/ms
'bullet_speed': 0.25
}

GAMEPLAY = DEFAULTPLAY

#Theme packs
DEFAULTTHEME = {'name' : None,
'explosion_pulse' : 100,
'bg_color' : (50, 50, 50),
'txt_color' : (100, 100, 100),
'font' : "./fonts/FIXED_BO.TTF",
'monospace_font' : "./fonts/FIXED_BO.TTF",
'small_font' : "./fonts/MiniPower.ttf",
'txt_size' : 8,
'txt_inter' : 8,
'small_size' : 16
}

DEFAULTSNDPACK = {'name' : None,
'music_volume' : 0.3,
'effect_volume' : 0.2
}

MCPACK = {'name' : 'mc'
}

DERVAL = {'name':'derval'
}

IRONBRAIN = {'name':'ironbrain',
'bg_color' : (100, 110, 100),
'font' : "./fonts/AtariSmall.ttf",
'txt_size' : 16,
'txt_inter' : 16
}

#projectiles
BULLET = {'name':'A',
'type' : 'Bullet',
'direction' : 'up',
'speed' : GAMEPLAY['bullet_speed'],
'cooldown' : 100,
'damage' : 1
}

BULLET2 = {'name':'o',
'type' : 'Bullet',
'direction' : 'down',
'speed' : GAMEPLAY['bullet_speed'],
'cooldown' : BULLET['cooldown'] * 6,
'damage' : 1,
}

BLAST = {'name' : 'oOOo',
'type' : 'Blast',
'direction' : 'up',
'speed' : GAMEPLAY['bullet_speed'],
'cooldown' : BULLET['cooldown'] * 6,
'power': 1,
}

#entities
SHIP = {'name' : 'ship',
'type' : 'Ship',
'ally' : True,
'speed' : GAMEPLAY['speed'],
'charge_rate' : 0.001,
'life' : 100,
'weapons' : [BULLET, BLAST]
}

INVINCIBLE = {'name' : 'ship',
'type' : 'Ship',
'ally' : True,
'speed' : GAMEPLAY['speed'],
'charge_rate' : 0.001,
'life' : 100,
'weapons' : [BULLET, BLAST]
}

TARGET = {'name':'target',
'type' : 'Fighter',
'speed':GAMEPLAY['speed'] / 4,
'life': 5,
'weapons' : [BULLET2],
'trajectory' : 'Circular'
}

TARGETOLD = {'name':'target',
'type' : 'Fighter',
'speed':GAMEPLAY['speed'] / 2,
'life': 5,
'weapons' : [BULLET2],
'trajectory' : 'AlignV'
}

#The reference playable level used to complete others
DEFAULTLEVEL = {'name':'default',
'theme' : DEFAULTTHEME,
'sound_pack' : DEFAULTSNDPACK,
'gameplay' : DEFAULTPLAY,
'nb_enemies' : 3
}

STRESSLEVEL = {'name':'stress',
'theme' : DERVAL,
'sound_pack' : MCPACK,
'nb_enemies' : 10
}

LEVEL = STRESSLEVEL

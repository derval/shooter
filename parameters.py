# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame.locals as p_l
import param_gen

GAMESIZE = (320, 240)  # ~neo geo
# GAMESIZE = (1024, 500)
COLORDEPTH = 16  # set to 8 for speedier game with low color resolution !
RESCALE = '2x'  # set to 2x or mame or None

DEFAULTPLAY = {
    'name': 'default',
    'flip_rate': 70,  # fps cap
    'hit_pulse': 50,  # ms between two hits on ship
    'blast_hit_pulse': 20,  # ms between two blast hits
    'game_speed': 1,
    'ratio_life_upgrade': 0.1
}

# control settings
KEYMAP1 = {
    p_l.K_f: 'fullscreen',
    p_l.K_m: 'mute',
    p_l.K_p: 'pause',
    p_l.K_RIGHT: 'right',
    p_l.K_LEFT: 'left',
    p_l.K_UP: 'up',
    p_l.K_DOWN: 'down',
    p_l.K_SPACE: 'shoot'
}

KEYMAP2 = {
    p_l.K_d: 'right',
    p_l.K_q: 'left',
    p_l.K_z: 'up',
    p_l.K_s: 'down',
    p_l.K_LSHIFT: 'shoot'
}

KEYMAPS = [KEYMAP1, KEYMAP2]


# Theme packs
DEFAULTTHEME = {
    'name': None,
    'bg_color': (65, 65, 65),
    'txt_color': (100, 100, 100),
    'font': "FIXED_BO.TTF",
    'monospace_font': "FIXED_BO.TTF",
    'small_font': "MiniPower.ttf",
    'txt_size': 8,
    'txt_inter': 8,
    'small_size': 16
}

DEFAULTSNDPACK = {
    'name': None,
    'music_volume': 0.3,
    'effect_volume': 0.2
}

MCPACK = {
    'name': 'mc'
}

DERVALTHEME = {
    'name': 'derval',
    'bg_color': (200, 0, 0)
}

CLEBARD = {
    'name': 'clebard',
    'txt_color': (255, 200, 150)
}

CLEB2 = {'name':'cleb2',
'txt_color' : (255, 200, 150)
}

IRONBRAIN = {'name':'ironbrain',
'bg_color' : (100, 110, 100),
'font' : "AtariSmall.ttf",
'txt_size' : 16,
'txt_inter' : 16
}

# Various....
COLLISIONDAMAGE = -1

#itempriorities
ANIMPRIOR = 1
BASEPRIOR = 2
FOLLOWPRIOR = 10
BLANKPRIOR = 20

# set layers of sprites
MENULAY = 35
MENUSHADOWLAY = 34
MENUBGLAY = 32
MESSAGELAY = 30
INTERFACELAY = 25
FRONTLAY = 20
OVERLAY = 18
SHIPLAY = 15
ACTORLAY = 10
BELOWSHIPLAY = 8
SHADOWLAY = 5
CLOUDLAY = 4
BGLAY = 1

#
# Animations
#

TARGETBLINK = {
    'type': 'Loop',
    'sprites': ['target_red', 'target'],
    'durations': [1000, 1000]
}

BULLETBLINK = {
    'type': 'SyncLoop',
    'sprites': ['o', 'x'],
    'durations': [300, 200]
}

HITBLINK = {
    'type': 'Blank',
    'duration': 50     # ms for white flash when collision
}

SHIPORIENTATION = {
    'type': 'Roll',
    'sprites': ['FighterB 1a', 'FighterB 1b', 'FighterB 1c'],
    'delay': 100
}

EXPLOSIONANIM = {
    'type': 'Film',
    # 'sprites' : ['ExplA1', 'ExplA2', 'ExplA3', 'ExplA4', 'ExplA5', 'ExplA6', 'ExplA7', 'ExplA8', 'ExplA9', 'ExplA10', 'ExplA11'],
    # 'pulse': 50,
    'sprites' : ['ExplB1', 'ExplB2', 'ExplB3'],
    'pulse': 110,
    'to_nothing': True
}

CHARGEANIM = {
    'type': 'Film',
    'sprites': ['B', 'BB', 'BBB']
}

ROTORANIM = {
    'type': 'SyncLoop',
    'sprites': ['CopterA rotor1', 'CopterA rotorb'],
    'durations': [50, 50]
}

# Special Effects
#

EXPLOSION = {
    'type': 'OnParent',
    'animations': [EXPLOSIONANIM],
    'layer': OVERLAY
}

SHADOW = {
    'type': 'Follower',
    'layer': SHADOWLAY,
    'opacity': 100,
    'offset': (10, 15)
}
SHADOWSCALE = 0.8

CHARGE = {
    'type': 'Follower',
    'animations': [CHARGEANIM],
    'layer': BELOWSHIPLAY
}

ROTOR = {
    'type': 'Follower',
    'animations': [ROTORANIM],
    'layer': OVERLAY,
    'opacity': 100
}

#projectiles
########################################

SPREADER0_0 = {
    'name': 'spreader_0',
    'type': 'Bullet',
    'trajectory': 'Up',
    'speed': 0.3,
    'cooldown': 100,
    'effect': {'add_life': -1},
    'layer': BELOWSHIPLAY
}

SPREADER0_22_5 = {
    'name': 'spreader_0_22.5',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': 22.5},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER0_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER0_MINUS22_5 = {
    'name': 'spreader_0_22.5:Vsym',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': -22.5},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER0_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER0_45 = {
    'name': 'spreader_0_45',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': 45},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER0_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER0_MINUS45 = {
    'name': 'spreader_0_45:Vsym',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': -45},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER0_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER1_0 = {
    'name': 'spreader_1',
    'type': 'Bullet',
    'trajectory': 'Up',
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': {'add_life': -2},
    'layer': BELOWSHIPLAY
}

SPREADER1_22_5 = {
    'name': 'spreader_1_22.5',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': 22.5},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER1_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER1_MINUS22_5 = {
    'name': 'spreader_1_22.5:Vsym',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': -22.5},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER1_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER1_45 = {
    'name': 'spreader_1_45',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': 45},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER1_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER1_MINUS45 = {
    'name': 'spreader_1_45:Vsym',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': -45},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER1_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER2_0 = {
    'name': 'spreader_2',
    'type': 'Bullet',
    'trajectory': 'Up',
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': {'add_life': -3},
    'layer': BELOWSHIPLAY
}

SPREADER2_22_5 = {
    'name': 'spreader_2_22.5',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': 22.5},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER2_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER2_MINUS22_5 = {
    'name': 'spreader_2_22.5:Vsym',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': -22.5},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER2_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER2_45 = {
    'name': 'spreader_2_45',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': 45},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER2_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER2_MINUS45 = {
    'name': 'spreader_2_45:Vsym',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': -45},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER2_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER3_0 = {
    'name': 'spreader_3',
    'type': 'Bullet',
    'trajectory': 'Up',
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': {'add_life': -5},
    'layer': BELOWSHIPLAY
}

SPREADER3_22_5 = {
    'name': 'spreader_3_22.5',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': 22.5},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER3_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER3_MINUS22_5 = {
    'name': 'spreader_3_22.5:Vsym',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': -22.5},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER3_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER3_45 = {
    'name': 'spreader_3_45',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': 45},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER3_0['effect'],
    'layer': BELOWSHIPLAY
}

SPREADER3_MINUS45 = {
    'name': 'spreader_3_45:Vsym',
    'type': 'Bullet',
    'trajectory': 'Line',
    'trajectory_params': {'angle': -45},
    'speed': SPREADER0_0['speed'],
    'cooldown': SPREADER0_0['cooldown'],
    'effect': SPREADER3_0['effect'],
    'layer': BELOWSHIPLAY
}


BULLET = {
    'name': 'o',
    'type': 'Bullet',
    'trajectory': 'Down',
    'animations': [BULLETBLINK],
    'damage': 1,
    'layer': BELOWSHIPLAY,
    'speed': 0.15,
    'cooldown': SPREADER0_0['cooldown'] * 6,
    'collision_type': 'pixel'
}

LINEBULLET = {
    'name': 'o',
    'type': 'LineBullet',
    'trajectory': 'Line',
    'animations': [BULLETBLINK],
    'damage': 1,
    'layer': BELOWSHIPLAY,
    'speed': 0.1,
    'cooldown': SPREADER0_0['cooldown'] * 6,
    'collision_type': 'pixel'
}

BLAST = {
    'name': 'blast',
    'type': 'Blast',
    'trajectory': 'Up',
    'layer': BELOWSHIPLAY,
    'speed': 0.15,
    'cooldown': SPREADER0_0['cooldown'] * 6,
    'power': -1,
    'collision_type': 'rectangle'
}

MISSILESIXTTDIR = {
    'type': 'AlignWithDirection',
    'animations': param_gen.make_16_films([
        ['Rocket A 1a', 'Rocket A 1b'],
        ['Rocket A 2a', 'Rocket A 2b'],
        ['Rocket A 3a', 'Rocket A 3b']], 50)
}

MISSILE = {
    'name': 'A',
    'type': 'Missile',
    'trajectory': 'Targeted',
    'animations': [MISSILESIXTTDIR],
    'effect': {'add_life': -5},
    'layer': BELOWSHIPLAY,
    'speed': 0.15,
    'cooldown': 800,
}

#weapons
#################################

BLASTER = {
    'name': 'blaster',
    'levels': [[BLAST]]
}

CANON = {
    'name': 'canon',
    'levels': [[BULLET]]
}

ANGLECANON = {
    'name': 'angular_canon',
    'levels': [[LINEBULLET]]
}

MISSILE_WEAPON = {'name': 'missile',
                  'levels': [[MISSILE]]
}

SPREADER = {'name': 'spreader0',
            'levels': [[SPREADER0_0],
                        [SPREADER1_0],
                        [SPREADER0_MINUS22_5, SPREADER1_0, SPREADER0_22_5],
                        [SPREADER1_MINUS22_5, SPREADER1_0, SPREADER1_22_5],
                        [SPREADER0_MINUS45, SPREADER1_MINUS22_5, SPREADER1_0, SPREADER1_22_5, SPREADER0_45],
                        [SPREADER0_MINUS45, SPREADER1_MINUS22_5, SPREADER2_0, SPREADER1_22_5, SPREADER0_45],
                        [SPREADER1_MINUS45, SPREADER1_MINUS22_5, SPREADER2_0, SPREADER1_22_5, SPREADER1_45],
                        [SPREADER1_MINUS45, SPREADER2_MINUS22_5, SPREADER2_0, SPREADER2_22_5, SPREADER1_45],
                        [SPREADER1_MINUS45, SPREADER2_MINUS22_5, SPREADER3_0, SPREADER2_22_5, SPREADER1_45],
                        [SPREADER2_MINUS45, SPREADER2_MINUS22_5, SPREADER3_0, SPREADER2_22_5, SPREADER2_45],
                        [SPREADER2_MINUS45, SPREADER3_MINUS22_5, SPREADER3_0, SPREADER3_22_5, SPREADER2_45],
                        [SPREADER3_MINUS45, SPREADER3_MINUS22_5, SPREADER3_0, SPREADER3_22_5, SPREADER3_45]]
}


# entities
#################################
SHIP = {
    'name': 'ship',
    'type': 'Ship',
    'has_shadow': True,
    'ally': True,
    'speed': 0.2,
    'charge_rate': 0.001,
    'life': 10,
    'weapons': [SPREADER, MISSILE_WEAPON]
}

STALKER = {
    'name': 'ship',
    'type': 'Ship',
    'has_shadow': True,
    'ally': True,
    'speed': 0.2,
    'charge_rate': 0.001,
    'life': 20,
    'weapons': [MISSILE_WEAPON, BLASTER]
}

INVINCIBLE = SHIP.copy()

INVINCIBLE.update({'life': 10000})

SAUCER = {
    'name': 'target',
    'type': 'Fighter',
    'has_shadow': True,
    'speed': 0.05,
    'life': 5,
    'weapons': [CANON],
    'trajectory': 'Circular',
    'animations': [TARGETBLINK],
    'reward': 1,
    'bonus_rate': 0.2
}


COPTEREIGHTDIR = {
    'type': 'FaceTarget',
    'animations': [
        {
        'type': 'SyncLoop',
        'sprites': ['CopterA 1a', 'CopterA 1b'],
        'durations': [50, 50]
        },
        {
        'type': 'SyncLoop',
        'sprites': ['CopterA 2a', 'CopterA 2b'],
        'durations': [50, 50]
        },
        {
        'type': 'SyncLoop',
        'sprites': ['CopterA 3a', 'CopterA 3b'],
        'durations': [50, 50]
        },
        {
        'type': 'SyncLoop',
        'sprites': ['CopterA 4a', 'CopterA 4b'],
        'durations': [50, 50]
        },
        {
        'type': 'SyncLoop',
        'sprites': ['CopterA 5a', 'CopterA 5b'],
        'durations': [50, 50]
        },
        {
        'type': 'SyncLoop',
        'sprites': ['CopterA 6a', 'CopterA 6b'],
        'durations': [50, 50]
        },
        {
        'type': 'SyncLoop',
        'sprites': ['CopterA 7a', 'CopterA 7b'],
        'durations': [50, 50]
        },
        {
        'type': 'SyncLoop',
        'sprites': ['CopterA 8a', 'CopterA 8b'],
        'durations': [50, 50]
        }
    ]
}

COPTER = {
    'name': 'copter',
    'type': 'Fighter',
    'has_shadow': True,
    'speed': 0.03,
    'life': 9,
    'weapons': [ANGLECANON],
    'trajectory': 'GoFront',
    #~ 'trajectory_params': {'init_pos': (100, 110)},
    'animations': [COPTEREIGHTDIR],
    'followers': [ROTOR],
    'reward': 1,
    'bonus_rate': 0.2
}

TANK = {
    'name': 'tank',
    'type': 'Fighter',
    'has_shadow': True,
    'speed': 0.03,
    'life': 9,
    'weapons': [ANGLECANON],
    'trajectory': 'Down',
    'trajectory_params': {'init_pos': (100, 110)},
    'animations': [COPTEREIGHTDIR],
    'followers': [ROTOR],
    'reward': 1,
    'bonus_rate': 0.2
}

DESERT = {
    'name': 'desert',
    'type': 'Landscape',
    'has_alpha': False,
    'speed': 0.04,
    'layer': BGLAY,
    }

CLOUD = {
    'name': 'clouds',
    'type': 'Landscape',
    'speed': 0.1,
    'layer': CLOUDLAY,
    'opacity': 200,
    }

DEFAULTBACKGROUND = {
    'name': 'background',
    'type': 'Landscape',
    'has_alpha': False,
    'layer': BGLAY,
    'speed': 0.04,
    }

BONUSLIFE = {
    'name': 'bonusL',
    'type': 'Mobile',
    'speed': 0.1,
    'trajectory': 'OscillationDown',
    'trajectory_params': {'amplitude': 30},
    'collision_type': 'pixel_perfect',
    'effect': {'add_life': 1}
}

BONUSWEAPON = {
    'name': 'bonusW',
    'type': 'Mobile',
    'speed': 0.1,
    'trajectory': 'OscillationDown',
    'trajectory_params': {'amplitude': 30},
    'collision_type': 'pixel_perfect',
    'effect': {'upgrade_weapon': 1},
    }

# Player settings
# "
PLAYER = {
    'name': 'player1',
    'ship': SHIP
}

ALTPLAYER = {
    'name': 'Bloody Barron',
    'ship': INVINCIBLE
}

DERVAL = {
    'name': 'derval',
    'ship': STALKER
}

# The reference playable level used to complete others
#
DEFAULTLEVEL = {
    'name': 'default',
    'theme': DEFAULTTHEME,
    'sound_pack': DEFAULTSNDPACK,
    'gameplay': DEFAULTPLAY,
    'background': DEFAULTBACKGROUND,
    'music': 'background',
    'nb_enemies': 6,
    'player': PLAYER,
    'enemy': SAUCER
}

STRESSLEVEL = {
    'name': 'stress',
    'theme': CLEBARD,
    'background': DESERT,
    'sound_pack': DEFAULTSNDPACK,
    'nb_enemies': 200,
    'player': ALTPLAYER
}

CLEBLEVEL = {
    'name': 'clebard',
    'theme': CLEBARD,
    'sound_pack': MCPACK,
    'background': DESERT,
    'nb_enemies': 7,
    'player': DERVAL
}

THEME = DEFAULTTHEME
LEVEL = CLEBLEVEL

import pygame


default_image_file = pygame.image.load('images/grass.png')
empty_image_file_1 = pygame.image.load('images/empty-1.png')
empty_image_file_2 = pygame.image.load('images/empty-2.png')
empty_image_file_3 = pygame.image.load('images/empty-3.png')
empty_image_file_4 = pygame.image.load('images/empty-4.png')
arrow_1d_image_file = pygame.image.load('images/arrow-1d.png')
arrow_1s_image_file = pygame.image.load('images/arrow-1s.png')
arrow_2d_image_file = pygame.image.load('images/arrow-2d.png')
arrow_2s_image_file = pygame.image.load('images/arrow-2s.png')
arrow_3_image_file = pygame.image.load('images/arrow-3.png')
arrow_4d_image_file = pygame.image.load('images/arrow-4d.png')
arrow_4s_image_file = pygame.image.load('images/arrow-4s.png')
horse_image_file = pygame.image.load('images/horse.png')
rotate_2_image_file = pygame.image.load('images/rotate-2.png')
rotate_3_image_file = pygame.image.load('images/rotate-3.png')
rotate_4_image_file = pygame.image.load('images/rotate-4.png')
rotate_5_image_file = pygame.image.load('images/rotate-5.png')
ice_image_file = pygame.image.load('images/ice.png')
pitfall_image_file = pygame.image.load('images/pitfall.png')
crocodile_image_file = pygame.image.load('images/crocodile.png')
cannibal_image_file = pygame.image.load('images/cannibal.png')
fort_image_file = pygame.image.load('images/fort.png')
fort_live_image_file = pygame.image.load('images/fort-live.png')
coins_1_image_file = pygame.image.load('images/coins-1.png')
coins_2_image_file = pygame.image.load('images/coins-2.png')
coins_3_image_file = pygame.image.load('images/coins-3.png')
coins_4_image_file = pygame.image.load('images/coins-4.png')
coins_5_image_file = pygame.image.load('images/coins-5.png')
plane_image_file = pygame.image.load('images/plane.png')
balloon_image_file = pygame.image.load('images/balloon.png')
keg_image_file = pygame.image.load('images/keg.png')
gun_image_file = pygame.image.load('images/gun.png')


card_types = {
    'EMPTY': {
        'value': 1,
        'quantity': 40,
        'image': empty_image_file_1
    },
    'ARROW_1D' : {
        'value': 2,
        'quantity': 3,
        'image': arrow_1d_image_file,
        'rotate_available': True
    },
    'ARROW_1S' : {
        'value': 3,
        'quantity': 3,
        'image': arrow_1s_image_file,
        'rotate_available': True
    },
    'ARROW_2D' : {
        'value': 4,
        'quantity': 3,
        'image': arrow_2d_image_file,
        'rotate_available': True
    },
    'ARROW_2S' : {
        'value': 5,
        'quantity': 3,
        'image': arrow_2s_image_file,
        'rotate_available': True
    },
    'ARROW_3' : {
        'value': 6,
        'quantity': 3,
        'image': arrow_3_image_file,
        'rotate_available': True
    },
    'ARROW_4D' : {
        'value': 7,
        'quantity': 3,
        'image': arrow_4d_image_file
    },
    'ARROW_4S' : {
        'value': 8,
        'quantity': 3,
        'image': arrow_4s_image_file
    },
    'HORSE' : {
        'value': 9,
        'quantity': 2,
        'image': horse_image_file
    },
    'ROTATE_2' : {
        'value': 10,
        'quantity': 5,
        'image': rotate_2_image_file
    },
    'ROTATE_3' : {
        'value': 11,
        'quantity': 4,
        'image': rotate_3_image_file
    },
    'ROTATE_4' : {
        'value': 12,
        'quantity': 2,
        'image': rotate_4_image_file
    },
    'ROTATE_5' : {
        'value': 13,
        'quantity': 1,
        'image': rotate_5_image_file
    },
    'ICE' : {
        'value': 14,
        'quantity': 6,
        'image': ice_image_file
    },
    'PITFALL' : {
        'value': 15,
        'quantity': 3,
        'image': pitfall_image_file
    },
    'CROCODILE' : {
        'value': 16,
        'quantity': 4,
        'image': crocodile_image_file
    },
    'CANNIBAL' : {
        'value': 17,
        'quantity': 1,
        'image': cannibal_image_file
    },
    'FORT' : {
        'value': 18,
        'quantity': 2,
        'image': fort_image_file
    },
    'FORT_LIVE' : {
        'value': 19,
        'quantity': 1,
        'image': fort_live_image_file
    },
    'COINS_1' : {
        'value': 20,
        'quantity': 5,
        'image': coins_1_image_file
    },
    'COINS_2' : {
        'value': 21,
        'quantity': 5,
        'image': coins_2_image_file
    },
    'COINS_3' : {
        'value': 22,
        'quantity': 3,
        'image': coins_3_image_file
    },
    'COINS_4' : {
        'value': 23,
        'quantity': 2,
        'image': coins_4_image_file
    },
    'COINS_5' : {
        'value': 24,
        'quantity': 1,
        'image': coins_5_image_file
    },
    'PLANE' : {
        'value': 25,
        'quantity': 1,
        'image': plane_image_file
    },
    'BALLOON' : {
        'value': 26,
        'quantity': 2,
        'image': balloon_image_file
    },
    'GUN' : {
        'value': 27,
        'quantity': 2,
        'image': gun_image_file
    },
    'KEG' : {
        'value': 28,
        'quantity': 4,
        'image': keg_image_file
    }}
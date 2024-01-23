import pygame

from audio import audio

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
gun_top_image_file = pygame.image.load('images/gun_top.png')
gun_left_image_file = pygame.image.load('images/gun_left.png')
gun_right_image_file = pygame.image.load('images/gun_right.png')
gun_bottom_image_file = pygame.image.load('images/gun_bottom.png')

coin_disallowed_card_types = ['FORT', 'FORT_LIVE', 'CANNIBAL', 'GUN_TOP',
                              'GUN_BOTTOM', 'GUN_RIGHT', 'GUN_LEFT']

def check_ship_in_cell(cell, player=None):
    if not player:
        return False
    return cell.column == player.ship.column and cell.row == player.ship.row

def check_can_move_with_coin(cell, player=None):
    active_pirate = player.get_active_pirate()

    return ((active_pirate.with_coin and cell.card_type and cell.card.opened and not(cell.card_type in coin_disallowed_card_types))
            or not active_pirate.with_coin or cell.type == 'water')

def horse_available_cells(cell, column, row, player=None):
    return (((abs(cell.column - column) == 1 and abs(cell.row - row) == 2)
             or (abs(cell.column - column) == 2 and abs(cell.row - row) == 1))
            and (cell.type == 'ground' or check_ship_in_cell(cell, player))
            and check_can_move_with_coin(cell, player))


def balloon_available_cells(cell, column, row, player=None):
    if not player:
        return False
    else:
        return cell.column == player.ship.column and cell.row == player.ship.row


def plane_available_cells(cell, column, row, player=None):
    if not player:
        return False

    if player.plane_available:
        return ((column != cell.column or row != cell.row)
                and (cell.type == 'ground' or check_ship_in_cell(cell, player))
            and check_can_move_with_coin(cell, player))
    else:
        return column == cell.column and row == cell.row


def ice_available_cells(cell, column, row, player=None):
    if not player:
        return False

    prev_column, prev_row = player.get_active_pirate_prev_pos()
    next_column = column + (column - prev_column)
    next_row = row + (row - prev_row)

    return (cell.column == next_column and cell.row == next_row) and check_can_move_with_coin(cell, player)


def crocodile_available_cells(cell, column, row, player=None):
    if not player:
        return False

    prev_column, prev_row = player.get_active_pirate_prev_pos()
    return cell.column == prev_column and cell.row == prev_row


def gun_top_available_cells(cell, column, row, player=None):
    if column == 1 or column == 11:
        return cell.column == column and cell.row == 1
    return cell.column == column and cell.row == 0


def gun_bottom_available_cells(cell, column, row, player=None):
    if column == 1 or column == 11:
        return cell.column == column and cell.row == 11
    return cell.column == column and cell.row == 12


def gun_left_available_cells(cell, column, row, player=None):
    if row == 1 or row == 11:
        return cell.column == 1 and cell.row == row
    return cell.column == 0 and cell.row == row


def gun_right_available_cells(cell, column, row, player=None):
    if row == 1 or row == 11:
        return cell.column == 11 and cell.row == row
    return cell.column == 12 and cell.row == row


def arrow_1s_available_cells(cell, column, row, player=None):
    return cell.row == row and cell.column - column == 1 and check_can_move_with_coin(cell, player)


def arrow_2s_available_cells(cell, column, row, player=None):
    return ((cell.row == row and abs(cell.column - column) == 1) and (cell.type == 'ground' or check_ship_in_cell(cell, player))
            and check_can_move_with_coin(cell, player))


def arrow_1d_available_cells(cell, column, row, player=None):
    return cell.row == row - 1 and cell.column == column + 1 and check_can_move_with_coin(cell, player)


def arrow_2d_available_cells(cell, column, row, player=None):
    return ((cell.row == row - 1 and cell.column == column + 1 or cell.row == row + 1 and cell.column == column - 1)
            and (cell.type == 'ground') or check_ship_in_cell(cell, player)
            and check_can_move_with_coin(cell, player))


def arrow_3_available_cells(cell, column, row, player=None):
    return (((cell.row == row - 1 and cell.column == column - 1) or (cell.row == row and cell.column - column == 1) or
            (cell.column == column and cell.row - row == 1)) and (cell.type == 'ground') or check_ship_in_cell(cell, player)
            and check_can_move_with_coin(cell, player))


def arrow_4d_available_cells(cell, column, row, player=None):
    return ((abs(cell.column - column) == 1 and abs(cell.row - row) == 1) and (cell.type == 'ground' or check_ship_in_cell(cell, player))
            and check_can_move_with_coin(cell, player))


def arrow_4s_available_cell(cell, column, row, player=None):
    return (((abs(cell.column - column) == 1 and cell.row == row) or (abs(cell.row - row) == 1 and cell.column == column))
            and (cell.type == 'ground' or check_ship_in_cell(cell, player))
            and check_can_move_with_coin(cell, player))


card_types = {
    'EMPTY': {
        'quantity': 44,
        'image': empty_image_file_1
    },
    'ARROW_1D': {
        'quantity': 3,
        'image': arrow_1d_image_file,
        'rotate_available': True,
        'available cells': arrow_1d_available_cells
    },
    'ARROW_1S': {
        'quantity': 3,
        'image': arrow_1s_image_file,
        'rotate_available': True,
        'available cells': arrow_1s_available_cells
    },
    'ARROW_2D': {
        'quantity': 3,
        'image': arrow_2d_image_file,
        'rotate_available': True,
        'available cells': arrow_2d_available_cells
    },
    'ARROW_2S': {
        'quantity': 3,
        'image': arrow_2s_image_file,
        'rotate_available': True,
        'available cells': arrow_2s_available_cells
    },
    'ARROW_3': {
        'quantity': 3,
        'image': arrow_3_image_file,
        'rotate_available': True,
        'available cells': arrow_3_available_cells
    },
    'ARROW_4D': {
        'quantity': 4,
        'image': arrow_4d_image_file,
        'available cells': arrow_4d_available_cells
    },
    'ARROW_4S': {
        'quantity': 4,
        'image': arrow_4s_image_file,
        'available cells': arrow_4s_available_cell
    },
    'HORSE': {
        'quantity': 4,
        'image': horse_image_file,
        'available cells': horse_available_cells
    },
    # 'ROTATE_2': {
    #     'quantity': 5,
    #     'image': rotate_2_image_file
    # },
    # 'ROTATE_3': {
    #     'quantity': 4,
    #     'image': rotate_3_image_file
    # },
    # 'ROTATE_4': {
    #     'quantity': 2,
    #     'image': rotate_4_image_file
    # },
    # 'ROTATE_5': {
    #     'quantity': 1,
    #     'image': rotate_5_image_file
    # },
    'ICE': {
        'quantity': 6,
        'image': ice_image_file,
        'available cells': ice_available_cells
    },
    'PITFALL': {
        'quantity': 3,
        'image': pitfall_image_file
    },
    'CROCODILE': {
        'quantity': 4,
        'image': crocodile_image_file,
        'sound': audio.crocodile_sound,
        'available cells': crocodile_available_cells
    },
    'CANNIBAL': {
        'quantity': 2,
        'image': cannibal_image_file
    },
    'FORT': {
        'quantity': 2,
        'image': fort_image_file
    },
    'FORT_LIVE': {
        'quantity': 1,
        'image': fort_live_image_file
    },
    'COINS_1': {
        'quantity': 5,
        'image': coins_1_image_file
    },
    'COINS_2': {
        'quantity': 5,
        'image': coins_2_image_file
    },
    'COINS_3': {
        'quantity': 3,
        'image': coins_3_image_file
    },
    'COINS_4': {
        'quantity': 2,
        'image': coins_4_image_file
    },
    'COINS_5': {
        'quantity': 1,
        'image': coins_5_image_file
    },
    'PLANE': {
        'quantity': 1,
        'image': plane_image_file,
        'available cells': plane_available_cells
    },
    'BALLOON': {
        'quantity': 3,
        'image': balloon_image_file,
        'available cells': balloon_available_cells
    },
    'GUN_TOP': {
        'quantity': 1,
        'image': gun_top_image_file,
        'available cells': gun_top_available_cells
    },
    'GUN_BOTTOM': {
        'quantity': 1,
        'image': gun_bottom_image_file,
        'available cells': gun_bottom_available_cells
    },
    'GUN_RIGHT': {
        'quantity': 1,
        'image': gun_right_image_file,
        'available cells': gun_right_available_cells
    },
    'GUN_LEFT': {
        'quantity': 1,
        'image': gun_left_image_file,
        'available cells': gun_left_available_cells
    },
    'KEG': {
        'quantity': 4,
        'image': keg_image_file
    }}

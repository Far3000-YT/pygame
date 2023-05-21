#Game setup
fps = 60
width = 1280
height = 720
tile_size = 64

#ui
BAR_HEIGH = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = 'font/font.ttf'
UI_FONT_SIZE = 18

#general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

#ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'yellow'
UI_BORDER_COLOR_ACTIVE = 'gold'

#Weapon setup
weapon_data = {
	'sword': {'cooldown': 100, 'damage': 15,'graphic':'images/weapon/sword/full.png'},
	'lance': {'cooldown': 400, 'damage': 30,'graphic':'images/weapon/lance/full.png'},
	'axe': {'cooldown': 300, 'damage': 20, 'graphic':'images/weapon/axe/full.png'},
	'rapier':{'cooldown': 50, 'damage': 8, 'graphic':'images/weapon/rapier/full.png'},
	'sai':{'cooldown': 80, 'damage': 10, 'graphic':'images/weapon/sai/full.png'}
}

#Magic
magic_data = {
	'flame': {'strength': 5,'cost': 20,'graphic':'images/particles/flame/fire.png'},
	'heal' : {'strength': 20,'cost': 10,'graphic':'images/particles/heal/heal.png'}
}

#Enemy
monster_data = {
	'dragon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw', 'speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
	'troll': {'health': 70,'exp':50,'damage':6,'attack_type': 'leaf_attack', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius': 300}
}

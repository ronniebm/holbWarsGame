# Developed by:
# Jose Vallejo / Ronnie Barrios.
# Use it for educational purpose only.
import sys
import pygame
import random
import math
from assets import  *



# ******* GLOBAL VAR *****
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
WHITE = (255, 255, 255)
BLUE = (59, 131, 189)
NEGRO = (0, 0, 0)
PATH_ELFO = "assets/Personajes_png/elfo_animated_move.png"
PATH_WARRIOR = "assets/Personajes_png/warrior_animated_move.png"
PATH_MAGO_WOMAN = "assets/Personajes_png/woman_animated_move.png"
PATH_TROLL = "assets/Personajes_png/troll_animated_move.png"
PATH_JOSE = "assets/Personajes_png/jose_animated_move.png"
FONDOS = [
	pygame.image.load("assets/Background/fondo.png"),
	pygame.image.load("assets/Background/fondo1.png"),
	pygame.image.load("assets/Background/fondo2.png"),
	pygame.image.load("assets/Background/fondo3.png")
]
PATH_BOTTONS = {
	'elfo':[
		"assets/buttons/elf_player.png",
		"assets/buttons/elf_player2.png"
	],
	'maga':[
		"assets/buttons/woman_player.png",
		"assets/buttons/woman_player2.png"
	],
	'warrior':[
		"assets/buttons/warrior_player.png",
		"assets/buttons/warrior_player2.png"
	],
}

IMG_NUMBER = 10
FPS = 30
POS_X_HERO = 20
POS_X_BAD_HERO = (SCREEN_WIDTH - 320)
POS_Y_CHMP = (SCREEN_HEIGHT - 300)

CHARACTER_DATA = {
	'elfo' : {
		'info_level1': {
			'name':"Itharos",
			'race': "Elfo",
			'gender': "M",
			'level': 1,
			'exp_to_next_lv': 10,
			'current_exp': 0,
			'exp_total': 0,
			'stat_point': 0,
			'stats': {
				'health': 100, 
				'attack': 30, 
				'defense': 5,
				'magic': 0,
				'speed': 2
			},
		},
		'path_image' : PATH_ELFO
	},

	'maga' : {
		'info_level1' : {
			'name':"Chost",
			'race': "Maga",
			'gender': "F",
			'level': 1,
			'exp_to_next_lv': 10,
			'current_exp': 0,
			'exp_total': 0,
			'stat_point': 0,
			'stats': {
				'health': 100, 
				'attack': 10, 
				'defense': 15,
				'magic': 10,
				'speed': 3
			},
		},
		'path_image' : PATH_MAGO_WOMAN,

	},

	'warrior' : {
		'info_level1' : {
			'name':"Heaghan",
			'race': "Warrior",
			'gender': "M",
			'level': 1,
			'exp_to_next_lv': 10,
			'current_exp': 0,
			'exp_total': 0,
			'stat_point': 0,
			'stats': {
				'health': 100, 
				'attack': 20, 
				'defense': 20,
				'magic': 0,
				'speed': 3
			},
		},
		'path_image' : PATH_WARRIOR,

	},

	'troll' : {
		'info_level1' : {
			'name':"Ordum",
			'race': "Troll",
			'gender': "M",
			'level': 1,
			'exp_to_next_lv': 10,
			'current_exp': 0,
			'exp_total': 0,
			'stat_point': 0,
			'stats': {
				'health': 100, 
				'attack': 35, 
				'defense': 15,
				'magic': 0,
				'speed': 1
			},
		},
		'path_image' : PATH_TROLL,

	},

	'jose' : {
		'info_level1' : {
			'name':"JosElfo",
			'race': "Humano",
			'gender': "M",
			'level': 1,
			'exp_to_next_lv': 10,
			'current_exp': 0,
			'exp_total': 0,
			'stat_point': 0,
			'stats': {
				'health': 100, 
				'attack': 20, 
				'defense': 10,
				'magic': 0,
				'speed': 1
			},
		},
		'path_image' : PATH_JOSE
	}
}

# ****** FUNTIONS **********

def draw_Menu(screen, cursor):
	"""Draw menu in screen.

	Args:
		screen (screen): screen of game.
		cursor (cursor): cursor position mouse.

	Returns:
		list: list character type sprite.
	"""

	x, y = 150, 350
	idx_bottons = 0
	fondo_menu = pygame.image.load("assets/Background/wall_intro.png")
	list_bottons_selection = list(PATH_BOTTONS.keys())
	list_bottons = []
	for botton in list_bottons_selection:
		list_bottons.append(Botton(x, y, PATH_BOTTONS.get(botton), botton))
		x += 200

	while True:
		screen.fill(WHITE)
		screen.blit(fondo_menu, (0, 0))
		
		cursor.update()
		for idx_bottons in range(len(list_bottons)):
			list_bottons[idx_bottons].draw_botton(screen)
			list_bottons[idx_bottons].update(screen, cursor)
			if list_bottons[idx_bottons].exit:
				return list_bottons[idx_bottons].list_champion
				

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		# ****** update screen *********
		pygame.display.flip()

def load_Champion(hero_name=""):
	"""Load champions for game play

	Args:
		hero_name (str): hero for user paly. Defaults to "".

	Returns:
		list: It's two objet first heroe, second is a list of enemy
	"""
	list_characters = []
	if hero_name is not None:
		idx_enemy = 0
		hero_select = CHARACTER_DATA.get(hero_name)	
		list_enemy_name = list(CHARACTER_DATA.keys())
		x,y = POS_X_BAD_HERO, POS_Y_CHMP
		# load Champion
		heroe = Champion(hero_select.get('path_image'), POS_X_HERO, POS_Y_CHMP)
		heroe.update_base(hero_select.get('info_level1'))
		list_characters.append(heroe)
		list_characters.append([])

		#load bad_champion
		for enemy_name in list_enemy_name:
			idx_enemy = len(list_characters[1])
			if enemy_name != hero_name:
				enemy_data = CHARACTER_DATA.get(enemy_name)
				list_characters[1].append(Champion(enemy_data.get('path_image'), x, y))
				list_characters[1][idx_enemy].update_base(enemy_data.get('info_level1'))
	
	return list_characters

def evaluate_Demage(data, dest=True):
	"""Evaluate demage get hero or enemy

	Args:
		data (tuple): first element is hero secon enemy
		dest (bool, defaul true): false sub point health enemy to hero, else invert
	"""
	if type(data) is list and data is not None:

		at_hero = data[0].stats.get('attack')
		#def_hero = data[0].stats.get('defense')
		at_villan = data[1][0].stats.get('attack')
		#def_villan = data[1][0].stats.get('defense')
		#magic_villan = data[1][0].stats.get('magic')
		health_hero = data[0].stats.get('health')
		health_villan = data[1][0].stats.get('health')


		
		if dest is True:
			sub_to_villan = (health_villan -  at_hero)
			print(sub_to_villan)
			data[1][0].Increase_Stats({'health': sub_to_villan})

		else:
			sub_to_hero = (health_hero - at_villan)
			data[0].Increase_Stats({'health': sub_to_hero})



# ******** GAME *********
def HolbWars_Game():
	""" app for game """

	pygame.init()

	Reloj = pygame.time.Clock()

	# ***********DEFINED SCREEN TO PLAY ********
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
	pygame.display.set_caption(':::  Holb-Wars v1.0  :::')
	pygame.display.set_icon(pygame.image.load("assets/Background/ico2.png"))
	fondo_intro = pygame.image.load("assets/Background/intro.png")
	#fondo_menu = pygame.image.load("assets/Background/wall_intro.png")
	menu1 = pygame.image.load("assets/Background/info_menu.png")
	menu2 = pygame.image.load("assets/Background/info_menu2.png")


	# ******* BOTTON FOR CONTROL FLOW PROGRAM ******
	boton_home = Botton(350, 10, ["assets/buttons/button_return_off.png", "assets/buttons/button_return_on.png"], "menu")
	cursor = Cursor()

	# ****** INTRO ******
	pause = pygame.time.get_ticks()
	while True:
		screen.blit(fondo_intro, (0,0))
		if pause + 3000 < pygame.time.get_ticks():
			break
		pygame.display.flip()

	# ****** VAR FOR FLOW CONTROL *****
	reload_bad_champion = True
	delay = 0
	idx_fondo = 0
	menu = True
	
	# ****** LOOP GAME CONTROL ******
	while True:

		# *** START MENU ****
		if menu:
			list_champion = draw_Menu(screen, cursor)
		if len(list_champion) > 0:
			menu = False
			boton_home.menu = False
		else:
			menu = True


		screen.fill(WHITE)
		screen.blit(FONDOS[idx_fondo], (0, 0))
		screen.blit(menu1, (20, 10))
		screen.blit(menu2, (670, 10))
		screen.blit(boton_home.image, boton_home.rect)

		
		if list_champion[0]:
			hero = list_champion[0]
			hero.draw_heroe(screen)
			hero.draw_Inf(screen)

		# *********ATTACK BHAIVOR**********# 
		if len(list_champion[1]) > 0 and reload_bad_champion is True:

			enemy = list_champion[1][0]
			enemy.draw_heroe(screen, False)
			enemy.draw_Inf(screen, 50, 30, False)

			# ACTION ATTACK ENEMY ON CICLE
			if enemy.attack_sel is True:
				enemy.attack(False)

				# CALL ACTION DIE HERO
				if hero.stats.get('health') <= 0:
					hero.die_sel = True
					hero.reverse_life = True

			# ACTION DIE HERO
			if hero.die_sel is True:
				hero.die()

			# HERO RELOAD HEALTH POINT
			if hero.life is False:
				hero.draw_heroe(screen)
				hero.reverse()
				hero.Increase_Stats({'health': 100})
				hero.current_exp = int(hero.current_exp * 0.5)

		
			# ACTION ATTACK HERO ON CICLE
			if hero.attack_sel is True:
				hero.attack()

				# CALL ACTION DIE VIELLAN
				if enemy.stats.get('health') <= 0:
					enemy.die_sel = True

			# ACTION DIE VILLANE
			if enemy.die_sel:
				enemy.die()

				if enemy.life == False and reload_bad_champion == True:
					del list_champion[1][0]
					reload_bad_champion = False
					delay = pygame.time.get_ticks()
					idx_fondo += 1
					if idx_fondo >= len(FONDOS) - 1:
						idx_fondo = 0
			

		# ****GET EVENT******
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					if len(list_champion[1]) > 0:
						hero.attack_sel = True
						hero.gain_Exp()
						evaluate_Demage(list_champion)


				elif event.key == pygame.K_k:
					if len(list_champion[1]) > 0:
						enemy.attack_sel = True
						evaluate_Demage(list_champion, False)


		# *** UPDATE SCREEEN ****
		boton_home.update(screen, cursor)
		cursor.update()



		if delay + 600 < pygame.time.get_ticks():
			reload_bad_champion = True
			if boton_home.menu == True:
				menu = True
				list_champion.pop()
				list_champion.pop()

		pygame.display.flip()
		Reloj.tick(30)



# **** Class ************
class Base_Champions(object):
	"""clas main for champions

	Args:
		object (object): base champions
	"""
	
	def __init__(self):
		self.name = ""
		self.race = ""
		self.gender = ""
		self.level = 0
		self.exp_to_next_lv = 0
		self.current_exp = 0
		self.exp_total = 0
		self.stats = {}
		self.stat_point = 0

	def update_base(self, kwarg):
		"""update data

		Args:
			kwarg (dict): get new value and set in variable
		"""
		if kwarg is not None:
			self.name = kwarg.get("name")
			self.race = kwarg.get("race")
			self.gender = kwarg.get("gender")
			self.level = kwarg.get("level")
			self.exp_to_next_lv = kwarg.get("exp_to_next_lv")
			self.current_exp = kwarg.get("current_exp")
			self.exp_total = kwarg.get("exp_total")
			self.stats.update(kwarg.get("stats"))
			self.stat_point = kwarg.get("stat_point")

	def draw_Inf(self, place, x=70, y=10, dir=True):
		mi_font = pygame.font.SysFont("Arial", 30)
		if dir is True:
			# DRAW NAME HERO
			place.blit(mi_font.render(
				str(self.name),
				0, WHITE), (x + 10, y + 55)
				)
			# DRAW LEVEL ATTACK
			place.blit(mi_font.render(
					str(self.stats.get('attack')), 
					0, NEGRO), (x + 10, y + 115)
				)
			# DRAW HEALTH POINTS
			place.blit(mi_font.render(
					str(self.stats.get('health')), 
					0, NEGRO), (x + 100, y + 115)
				)
			# DRAW DEFENSE POINTS
			place.blit(mi_font.render(
					str(self.stats.get('defense')), 
					0, NEGRO), (x + 10, y + 170)
				)
			# DRAW LEVEL BY HERO
			place.blit(mi_font.render(
					str(self.level), 
					0, NEGRO), (x + 100, y + 170)
				)
			# DRAW MAGIC LEVEL
			place.blit(mi_font.render(
					str(self.stats.get('magic')), 
					0, NEGRO), (x + 10, y + 230)
				)
			# DRAW CURRENT EXP
			place.blit(mi_font.render(
					str(self.current_exp), 
					0, NEGRO), (x + 100, y + 230)
				)
			# DRAW SPEED
			place.blit(mi_font.render(
					str(self.stats.get('speed')), 
					0, NEGRO), (x + 10, y + 300)
				)
			# DRAW EXP TO NEXT LEVEL
			place.blit(mi_font.render(
					str(self.exp_to_next_lv - self.current_exp), 
					0, NEGRO), (x + 100, y + 300)
				)

		else:
			# DRAW NAME HERO
			place.blit(mi_font.render(
				str(self.name),
				0, WHITE), (x + 640, y + 35)
				)
			# DRAW HEALTH POINTS
			place.blit(mi_font.render(
					str(self.stats.get('health')), 
					0, NEGRO), (x + 640, y + 95)
				)
			# DRAW LEVEL ATTACK
			place.blit(mi_font.render(
					str(self.stats.get('attack')), 
					0, NEGRO), (x + 740, y + 95)
				)			
			# DRAW LEVEL BY HERO
			place.blit(mi_font.render(
					str(self.level), 
					0, NEGRO), (x + 640, y + 160)
				)
			# DRAW DEFENSE POINTS
			place.blit(mi_font.render(
					str(self.stats.get('defense')), 
					0, NEGRO), (x + 740, y + 160)
				)			
			# DRAW MAGIC LEVEL
			place.blit(mi_font.render(
					str(self.stats.get('magic')), 
					0, NEGRO), (x + 740, y + 220)
				)
			# DRAW CURRENT EXP
			place.blit(mi_font.render(
					str(self.current_exp), 
					0, NEGRO), (x + 640, y + 220)
				)
			# DRAW SPEED
			place.blit(mi_font.render(
					str(self.stats.get('speed')), 
					0, NEGRO), (x + 740, y + 280)
				)			
			# DRAW EXP TO NEXT LEVEL
			place.blit(mi_font.render(
					str(self.exp_to_next_lv - self.current_exp), 
					0, NEGRO), (x + 640, y + 280)
				)

	def level_Up(self):
		hero_level_next = {
			'name': self.name,
			'race': self.race,
			'gender': self.gender,
			'level': self.level + 1,
			'exp_to_next_lv': self.exp_to_next_lv + 50,
			'current_exp': 0,
			'stats': {
				'health': self.stats.get('health'), 
				'attack': self.stats.get('attack') + 5, 
				'defense': self.stats.get('defense') + 5,
				'magic': self.stats.get('magic') * 2,
				'speed': self.stats.get('speed') + 1
			},
			'stat_point': 0
		}
		self.update_base(hero_level_next)

	def gain_Exp(self):
		self.current_exp += 1
		if self.current_exp >= self.exp_to_next_lv:
			self.level_Up()

	def death(self, list, idx=0):
		if list is not None and type(list) is list:
			del list[idx]

	def save_Character(self):
		pass
 
	def load_Character(self):
		pass

	def Increase_Stats(self, stats):
		if stats is not None and type(stats) is dict:
			self.stats.update(stats)
			if self.stats.get('health') < 0:
				self.stats.update({'health': 0})

class Champion(pygame.sprite.Sprite, Base_Champions):
	"""Champions class

	Args:
		pygame (sprite): librery of pygame inherit
		Base_Champions (class): class base champions
	"""

	def __init__(self, ruta, pos_x, pos_y):
		pygame.sprite.Sprite.__init__(self)
		Base_Champions.__init__(self)
		self.img_base = pygame.image.load(ruta)

		self.arr_walk_right = []
		self.arr_walk_left = []
		self.arr_run_right = []
		self.arr_run_left = []
		self.arr_attack_right = []
		self.arr_attack_left = []
		self.arr_die_right = []
		self.arr_die_left = []
		self.arr_reverse = []

		for i in range(IMG_NUMBER):
			# get imeges from img base
			self.arr_walk_right.append(self.img_base.subsurface(i*300,0,300,300))
			self.arr_attack_right.append(self.img_base.subsurface(i*300,300,300,300))
			self.arr_run_right.append(self.img_base.subsurface(i*300,600,300,300))
			self.arr_die_right.append(self.img_base.subsurface(i*300,900,300,300))
			# copy reflejo vertical of each one
			self.arr_walk_left.append(pygame.transform.flip(self.arr_walk_right[i], True, False))
			self.arr_attack_left.append(pygame.transform.flip(self.arr_attack_right[i], True, False))
			self.arr_run_left.append(pygame.transform.flip(self.arr_run_right[i], True, False))
			self.arr_die_left.append(pygame.transform.flip(self.arr_die_right[i], True, False))

		for i in range(IMG_NUMBER):
			self.arr_reverse.append(self.arr_die_right[-i])
			
			
		self.idx_img = 3
		self.image = self.arr_walk_right[self.idx_img]
		self.rect = self.image.get_rect()
		self.rect.top = pos_y
		self.rect.left = pos_x
		self.step = 0
		self.rev = False

		self.die_sel = False
		self.walk_sel = False
		self.run_sel = False
		self.attack_sel = False
		self.life = True
		self.reverse_life = False
		self.step_reverse = IMG_NUMBER - 1
		self.action = ""
		self.current_time  = pygame.time.get_ticks()
		self.act_img_dict = {
			"walk_r": self.arr_walk_right,
			"walk_l": self.arr_walk_left,
			"attack_r": self.arr_attack_right,
			"attack_l": self.arr_attack_left,
			"run_r": self.arr_run_right,
			"run_l": self.arr_run_left,
			"die_r": self.arr_die_right,
			"die_l": self.arr_die_left,
			"reverse": self.arr_reverse
		}

	def draw_heroe(self, place, dir=True):
		if self.action is "":
			if dir:
				place.blit(self.arr_walk_right[self.idx_img], self.rect)
			else:
				place.blit(self.arr_walk_left[self.idx_img], self.rect)
		else:
			place.blit(self.act_img_dict.get(self.action)[self.step], self.rect)
	
	def animated_arrays(self):
		if self.current_time + 100 < pygame.time.get_ticks():
			if self.step < IMG_NUMBER - 1:
				self.step += 1
			else:
				self.step = 0
			self.current_time = pygame.time.get_ticks()

	def update(self, x, y):
		self.rect.top = x
		self.rect.left = y

	def walk(self, dir=True):
		"""generate walk movement

		Args:
			dir (bool, defaul True): False = walk left, else right.
		"""
		if dir == True:
			self.action = "walk_r"
			self.animated_arrays()
			self.rect.left += self.stats.get('speed')
		else:
			self.action = "walk_l"
			self.animated_arrays()
			self.rect.left -= self.stats.get('speed')
		
	def attack(self, dir=True):
		"""generate attack movement

		Args:
			dir (bool, defaul True): False = attack left, else right.
		"""
		if self.attack_sel:
			if dir:
				self.animated_arrays()
				self.action = "attack_r"
			else:
				self.action = "attack_l"
				self.animated_arrays()
		if self.step >= IMG_NUMBER - 1 and self.attack_sel == True:
			self.attack_sel = False

	def run(self, dir=True):
		"""generate running movement

		Args:
			dir (bool, defaul True): False = running left, else right.
		"""
		if dir:
			self.action = "run_r"
			self.animated_arrays()
			self.rect.left += (self.stats.get('speed') * 2)
		else:
			self.action = "run_l"
			self.animated_arrays()
			self.rect.left -= (self.stats.get('speed') * 2)

	def die(self, dir=True):
		"""generate die movement

		Args:
			dir (bool, defaul True): False = body fall to left, else right.
		"""

		if self.die_sel:
			if dir:
				self.action = "die_r"
				self.animated_arrays()
			else:
				self.action = "die_l"
				self.animated_arrays()
		if self.step >= IMG_NUMBER - 1 and self.die_sel == True:
			self.die_sel = False
			self.life = False

	def reverse(self, dir=True):
		"""method for reload point of life

		Args:
			dir (bool, defaul True): False = body fall to left, else right.
		"""

		if self.reverse_life:
			if dir:
				self.action = "reverse"
				self.animated_arrays()
			if self.step >= IMG_NUMBER - 1 and self.life == False:
				self.reverse_life = False
				self.life = True

class Botton(pygame.sprite.Sprite):
	"""boton for flow control

	Args:
		pygame (sprite): boton
	"""

	def __init__(self, pos_x, pos_y, path_imgs, name=""):
		pygame.sprite.Sprite.__init__(self)
		self.path1 = path_imgs[0]
		self.path2 = path_imgs[1]
		self.name = name
		self.image_boton1 = pygame.image.load(self.path1)
		self.image_boton2 = pygame.image.load(self.path2)

		self.image = self.image_boton1
		self.rect = self.image.get_rect()
		self.rect.top = pos_y
		self.rect.left = pos_x
		self.exit = False
		self.list_champion = []
		self.menu = False
		self.botton_pressed = False

	def draw_botton(self, place, idx=0):
		self.idx = idx
		place.blit(self.image, self.rect)

	def update(self, place, cursor):
		if cursor.colliderect(self.rect):
			self.image = self.image_boton2
			if pygame.mouse.get_pressed() == (1, 0, 0):
				self.botton_pressed = True

				if self.name == "elfo":
					self.list_champion = load_Champion("elfo")
					self.exit = True
				if self.name == "warrior":
					self.list_champion = load_Champion("warrior")
					self.exit = True
				if self.name == "maga":
					self.list_champion = load_Champion("maga")
					self.exit = True
				if self.name == "menu":
					self.menu = True
				else:
					self.menu = False
			else:
				self.exit = False
				self.botton_pressed = False


		if not cursor.colliderect(self.rect):
			self.image = self.image_boton1
		
class Cursor(pygame.Rect):
	"""Cursor mouse

	Args:
		pygame (Rect): coord and rect of cursor
	"""
	def __init__(self):
		pygame.Rect.__init__(self, 0, 0, 1, 1)

	def update(self):
		self.left, self.top = pygame.mouse.get_pos()


HolbWars_Game()

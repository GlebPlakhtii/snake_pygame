import pygame
from random import randint

class Apple():
	def __init__(self,screen,setting):
		self.screen=screen
		self.setting=setting
		self.apple_color=(255,30,30)
		self.apple_height=20
		self.apple_width=20
		
	
		
		
	
	
	
	def get_rect(self,snake_head,tail):
		self.apple_xposition=randint(0,int((self.setting.screen_width-self.apple_width)/20))*20
		self.apple_yposition=randint(0,int((self.setting.screen_height-self.apple_height)/20))*20
		self.rect=pygame.Rect(self.apple_xposition,self.apple_yposition,self.apple_width,self.apple_height)
		self.check_position(snake_head,tail)
	
	
	def draw(self):
		self.apple_color=self.apple_color
		pygame.draw.rect(self.screen,self.apple_color,(self.rect))
	
	
	def check_position(self,snake_head,tail):
		change_position=False
		for i in range(tail.ate_apples_count):
			try:
				if snake_head.coordinates[-(i+2)]["x"]==self.apple_xposition and snake_head.coordinates[-(i+2)]["y"]==self.apple_yposition:
					change_position=True
			except IndexError:
				change_position=False
				
		if change_position:
			self.get_rect(snake_head,tail)
			change_position=False
			
			

		

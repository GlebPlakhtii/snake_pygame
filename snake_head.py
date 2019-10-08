import pygame
class Snake_head():
	def __init__(self,screen,setting):
		self.screen=screen
		self.setting=setting
		self.color=setting.snake_color
		self.rect=pygame.Rect(int(self.setting.screen_width/40)*20,int(self.setting.screen_height/40)*20,20,20)
		
		self.coordinates=[{'x':int(self.setting.screen_width/40)*20,'y':int(self.setting.screen_height/40)*20}]
		self.move_up=True
		self.move_down=False
		self.move_right=False
		self.move_left=False
	
	
	def draw(self):
		self.coordinates.append({'x':self.rect.left,'y':self.rect.top})
		pygame.draw.rect(self.screen,self.color,self.rect)
		
		
	def displacement(self):
		if self.rect.top<0:
			self.rect.bottom=self.setting.screen_height	
		if self.rect.bottom>self.setting.screen_height:
			self.rect.top=0	
		if self.rect.left<0:
			self.rect.right=self.setting.screen_width	
		if self.rect.right>self.setting.screen_width:
			self.rect.left=0
		
	def move(self):
		if self.move_up:
			self.rect.centery-=self.setting.move_speed
		if self.move_down:
			self.rect.centery+=self.setting.move_speed
		if self.move_right:
			self.rect.centerx+=self.setting.move_speed
		if self.move_left:
			self.rect.centerx-=self.setting.move_speed
		self.displacement()
	
	
	
	

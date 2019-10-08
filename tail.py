import pygame
from snake_head import Snake_head
class Tail(Snake_head):
	def __init__(self,screen,setting):
		super().__init__(screen,setting)
		self.ate_apples_count=1
		
		

		
	def draw(self,snake):
		g=155
		
		
		for i in range(self.ate_apples_count):
			if i<100 :
				g+=1
			else :
				g=255
				
			try:
				pygame.draw.rect(self.screen,[20,g,20],(snake.coordinates[-(i+2)]['x'] ,snake.coordinates[-(i+2)]['y'] , 20,20))
			except IndexError:
				pygame.draw.rect(self.screen,[20,g,20],(snake.coordinates[-2]['x'] ,snake.coordinates[-2]['y'] , 20,20))

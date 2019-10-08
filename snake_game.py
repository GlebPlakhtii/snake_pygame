import pygame
import sys
from setting import Setting
from snake_head import Snake_head
from apple import Apple
from tail import Tail
import game_function as gf
def game():
	pygame.init()
	setting=Setting()
	screen=pygame.display.set_mode((setting.screen_width,setting.screen_height)) 
	snake_head=Snake_head(screen,setting)
	apple=Apple(screen,setting)
	tail=Tail(screen,setting)
	apple.get_rect(snake_head,tail)
	start_time=pygame.time.get_ticks()
	
	
	
	while gf.resume_game(setting,snake_head,tail):
		
		gf.check_event(snake_head,start_time)
		
			
			
			
		
			
		gf.update(screen,setting,snake_head,apple,tail)
		
		pygame.time.delay(100)
	print(tail.ate_apples_count)
	
game()





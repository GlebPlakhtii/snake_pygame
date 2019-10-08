import pygame
import sys
pygame.font.init()


def check_event(snake_head,start_time):
	
	for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			if event.type==pygame.KEYDOWN :
				if event.key==pygame.K_a and snake_head.move_right==False and pygame.time.get_ticks()-start_time>100 :
					snake_head.move_up=False
					snake_head.move_down=False
					
					snake_head.move_left=True
					start_time=pygame.time.get_ticks()
					
				if event.key==pygame.K_d and snake_head.move_left==False and pygame.time.get_ticks()-start_time>100 :
					snake_head.move_up=False
					snake_head.move_down=False
					
					snake_head.move_right=True
					start_time=pygame.time.get_ticks()
					
				if event.key==pygame.K_w and snake_head.move_down==False and pygame.time.get_ticks()-start_time>100 :
					snake_head.move_left=False
					snake_head.move_right=False
					
					snake_head.move_up=True
					start_time=pygame.time.get_ticks()
					
				if event.key==pygame.K_s and snake_head.move_up==False and pygame.time.get_ticks()-start_time>100 :
					snake_head.move_left=False
					snake_head.move_right=False
					
					snake_head.move_down=True
					start_time=pygame.time.get_ticks()
				
				
			
					
			
			
				
				
				
def update(screen,setting,snake_head,apple,tail):
	
	screen.fill(setting.bg_color)
	text(screen,tail.ate_apples_count)
	snake_head.move()
	snake_head.draw()
	
	
	
	tail.draw(snake_head)
	if ate_apple(apple,snake_head):
		apple.get_rect(snake_head,tail)
		tail.ate_apples_count+=1
		
	apple.draw()
	
	
	pygame.display.flip() 



def resume_game(setting,snake_head,tail):
	
		
	for i in range(tail.ate_apples_count):
		try:
			if  snake_head.rect.top==snake_head.coordinates[-(i+2)] ['y'] and  snake_head.rect.left==snake_head.coordinates[-(i+2)] ['x']:
				return False
		except IndexError:
			pass
	
	else:
		return True
	
def ate_apple(apple,snake_head):
	if apple.rect.top<snake_head.rect.bottom and apple.rect.bottom>=snake_head.rect.top and apple.rect.centerx==snake_head.rect.centerx  and snake_head.move_down:
		return True
	
	elif apple.rect.bottom>snake_head.rect.top and apple.rect.top<=snake_head.rect.bottom and  apple.rect.centerx==snake_head.rect.centerx and snake_head.move_up:
		return True
	
	elif apple.rect.right>snake_head.rect.left and apple.rect.left<=snake_head.rect.right and apple.rect.centery==snake_head.rect.centery and snake_head.move_left:
		return True
	
	elif apple.rect.left<snake_head.rect.right and apple.rect.right>=snake_head.rect.left and  apple.rect.centery==snake_head.rect.centery and snake_head.move_right:
		return True
	else:
		 return False
	
	
	
def text(screen,ate_apple_count):
	font=pygame.font.SysFont('Comic Sans MS',30)
	text=font.render(str(ate_apple_count),False,(0,0,0))
	screen.blit(text,(10,10))
	
	
	
	
	

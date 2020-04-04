# writing a game in < 100 lines, comments not included
import pygame, random, math
screen, bullet_group, enemy_group = pygame.display.set_mode((300,500)),pygame.sprite.Group(), pygame.sprite.Group()
class Player(pygame.sprite.Sprite):
	def __init__(self):
		self.x, self.y, self.image, self.bar = 125, 400, pygame.Surface((50, 60)), 100
		self.rect = self.image.get_rect()
		self.image.fill((255,255,255))
	def draw(self, display):
		display.blit(self.image, (self.x, self.y))
	def update(self):
		if self.bar < 100:
			self.bar += 0.001
		key = pygame.key.get_pressed()
		if key[pygame.K_w]:
			self.y -= 0.5
		elif key[pygame.K_s]:
			self.y += 0.5
		elif key[pygame.K_a]:
			self.x -= 0.5
		elif key[pygame.K_d]:
			self.x += 0.5
class Bullet(pygame.sprite.Sprite):
	def __init__(self, x, y, typeof, color):
		pygame.sprite.Sprite.__init__(self)
		self.image, self.x, self.y, self.typeof  = pygame.Surface((10,10)), x, y, typeof
		self.rect = self.image.get_rect()
		self.image.fill(color)
	def update(self):
		self.rect.x = self.x
		self.rect.y = self.y
		if self.typeof == 1:
			self.y -= 1
			if self.rect.y + self.rect.height < 0:
				self.kill()
		else:
			self.y += 1
			if self.rect.y - self.rect.height > 500:
				self.kill()
class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.x, self.y , self.image = random.randint(0, 450), random.randint(-1000, 0), pygame.Surface((50,60))
		self.rect, self.fill = self.image.get_rect(), [self.image.fill((255,0,0))]
	def update(self):
		self.y += 0.25
		[i.kill() for i in enemy_group if i.y > 500]
		self.rect.x, self.rect.y = self.x, self.y
		if random.choice([1,2,3,4,5,6]) == 3:
			bullet_group.add(Bullet(self.x+(self.rect.width/2)-5, self.y+self.rect.height,2,(255,0,0)))
player = Player()
e = Enemy()
enemy_group.add(e)
exit = False
while not exit:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit = True
			pygame.quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if player.bar > 0:
					bullet_group.add(Bullet(player.x+(player.rect.width/2)-5, player.y, 1, (0,255,0)))
					player.bar -= 1
	screen.fill((0,0,0))
	pygame.draw.rect(screen,(0,0,255),(10,10,20,player.bar))
	player.draw(screen)
	enemy_group.draw(screen)
	bullet_group.draw(screen)
	player.update()
	enemy_group.update()
	bullet_group.update()
	pygame.display.update()

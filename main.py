import pygame
import time
import keyword_extractor as ke

path = ''

text = ke.pdf_to_text(path)
print("Length of text is: ",len(text))
keyword_string = ke.generate_keywords(text)
print(keyword_string)

pygame.font.init()

screen = pygame.display.set_mode((800,600))
background = (0, 0, 0)
screen.fill((background))

myfont = pygame.font.Font(None, 90)

# Split String to words
display_string = keyword_string.split(" ")

for word in display_string:
    text = myfont.render(word, 1, (0, 255, 0))
    screen.blit(text, (300, 300))
    pygame.display.update()

    time.sleep(0.2)
    screen.fill((background))
    pygame.display.update()

pygame.display.quit()





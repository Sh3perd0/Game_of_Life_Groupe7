import pygame
pygame.init()

screen_width = 1920
screen_height = 1080
image = pygame.image.load("bob_number.png")
slider_length = 400
slider_height = 10

min_value = 0
max_value = 100

current_value = min_value  # La valeur actuelle du slider

# Ajustez la position initiale de slider_x et ajoutez un décalage vertical au curseur
slider_x = int((screen_width - slider_length) / 2)
slider_y = int(screen_height / 2) + 235
cursor_offset_y = -5

# Ajout d'une police de texte
font = pygame.font.Font(None, 36)

def draw_slider():
    pygame.draw.rect(screen, (255, 255, 255), (slider_x, slider_y, slider_length, slider_height))  # Barre
    pygame.draw.rect(screen, (255, 0, 0), (slider_x + (current_value / max_value) * slider_length - 5, slider_y + cursor_offset_y, 10, 20))  # Curseur

    # Convertir la valeur actuelle en texte
    text = font.render(str(int(current_value)), True, (255, 255, 255))
    text_rect = text.get_rect(center=(slider_x + slider_length / 2, slider_y - 30))
    screen.blit(text, text_rect)

pygame.display.set_caption("Settings")

screen = pygame.display.set_mode((screen_width, screen_height))  # Créer la surface de l'écran
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if slider_x <= event.pos[0] <= slider_x + slider_length and slider_y <= event.pos[1] <= slider_y + slider_height:
                current_value = min(max(min_value, (event.pos[0] - slider_x) / slider_length * max_value), max_value)

    screen.blit(image, (0, 0))  # Afficher l'image sans surélévation
    draw_slider()  # Dessiner le slider avec le texte
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

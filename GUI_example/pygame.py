import pygame
import numpy as np

class GameOfLife:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Jeu de la Vie")
        
        # Paramètres de la grille
        self.cell_size = 20  # Taille initiale des cellules
        self.grid_width = width // self.cell_size
        self.grid_height = height // self.cell_size
        
        # Création de la grille
        self.grid = np.zeros((self.grid_height, self.grid_width))
        
        # Variables pour le zoom et le déplacement
        self.offset_x = 0
        self.offset_y = 0
        self.zoom = 1.0
        
    def draw_grid(self):
        self.screen.fill((255, 255, 255))  # Fond blanc
        
        # Calcul des dimensions avec zoom
        cell_size = int(self.cell_size * self.zoom)
        
        # Dessin des cellules
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                if self.grid[y][x]:
                    rect = pygame.Rect(
                        x * cell_size + self.offset_x,
                        y * cell_size + self.offset_y,
                        cell_size - 1,
                        cell_size - 1
                    )
                    pygame.draw.rect(self.screen, (0, 0, 0), rect)
        
        pygame.display.flip()
    
    def handle_mouse(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Zoom in
                self.zoom *= 1.1
            elif event.button == 5:  # Zoom out
                self.zoom /= 1.1
            elif event.button == 1:  # Click gauche
                # Convertir les coordonnées de la souris en coordonnées de la grille
                mouse_x, mouse_y = event.pos
                grid_x = int((mouse_x - self.offset_x) / (self.cell_size * self.zoom))
                grid_y = int((mouse_y - self.offset_y) / (self.cell_size * self.zoom))
                
                if 0 <= grid_x < self.grid_width and 0 <= grid_y < self.grid_height:
                    self.grid[grid_y][grid_x] = not self.grid[grid_y][grid_x]
    
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP):
                    self.handle_mouse(event)
                
            self.draw_grid()
        
        pygame.quit()

if __name__ == "__main__":
    game = GameOfLife()
    game.run()
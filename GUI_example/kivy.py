from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Rectangle, Color
from kivy.core.window import Window
from kivy.properties import NumericProperty
import numpy as np

class GameGrid(Widget):
    cell_size = NumericProperty(20)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Initialisation de la grille
        self.grid_width = 40
        self.grid_height = 30
        self.grid = np.zeros((self.grid_height, self.grid_width))
        
        # Variables pour le zoom et le déplacement
        self.scale = 1
        self.offset_x = 0
        self.offset_y = 0
        
        # Bind à la mise à jour du dessin
        self.bind(pos=self.update_canvas)
        self.bind(size=self.update_canvas)
        
        # Gestion du zoom avec la molette
        Window.bind(on_mouse_scroll=self.on_mouse_scroll)
        
    def update_canvas(self, *args):
        self.canvas.clear()
        with self.canvas:
            # Dessine les cellules
            for y in range(self.grid_height):
                for x in range(self.grid_width):
                    Color(0, 0, 0) if self.grid[y][x] else Color(1, 1, 1)
                    Rectangle(
                        pos=(
                            self.x + (x * self.cell_size + self.offset_x) * self.scale,
                            self.y + (y * self.cell_size + self.offset_y) * self.scale
                        ),
                        size=(
                            self.cell_size * self.scale - 1,
                            self.cell_size * self.scale - 1
                        )
                    )
    
    def on_mouse_scroll(self, window, x, y, scroll_x, scroll_y):
        # Gestion du zoom
        if scroll_y > 0:  # Zoom in
            self.scale *= 1.1
        elif scroll_y < 0:  # Zoom out
            self.scale /= 1.1
        self.update_canvas()

    def on_touch_down(self, touch):
        if self.collide_point(touch.x, touch.y):
            # Convertit les coordonnées de l'écran en coordonnées de la grille
            grid_x = int((touch.x - self.x - self.offset_x * self.scale) / (self.cell_size * self.scale))
            grid_y = int((touch.y - self.y - self.offset_y * self.scale) / (self.cell_size * self.scale))
            
            if 0 <= grid_x < self.grid_width and 0 <= grid_y < self.grid_height:
                self.grid[grid_y][grid_x] = not self.grid[grid_y][grid_x]
                self.update_canvas()
        return super().on_touch_down(touch)

    def on_touch_move(self, touch):
        # Déplacement de la grille
        if hasattr(touch, 'button') and touch.button == 'right':
            self.offset_x += touch.dx / self.scale
            self.offset_y += touch.dy / self.scale
            self.update_canvas()

class GameOfLifeApp(App):
    def build(self):
        # Layout principal
        layout = BoxLayout(orientation='vertical')
        
        # Grille de jeu
        self.game_grid = GameGrid()
        layout.add_widget(self.game_grid)
        
        # Boutons de contrôle
        controls = BoxLayout(size_hint_y=0.1)
        start_button = Button(text='Démarrer')
        clear_button = Button(text='Effacer')
        clear_button.bind(on_press=self.clear_grid)
        
        controls.add_widget(start_button)
        controls.add_widget(clear_button)
        layout.add_widget(controls)
        
        return layout
    
    def clear_grid(self, instance):
        self.game_grid.grid.fill(0)
        self.game_grid.update_canvas()

if __name__ == '__main__':
    GameOfLifeApp().run()
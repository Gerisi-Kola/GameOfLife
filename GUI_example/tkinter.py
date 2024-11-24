import tkinter as tk
from tkinter import ttk
import numpy as np

class GameOfLife:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de la Vie - Tkinter")
        
        # Configuration du style pour enlever le focus
        self.style = ttk.Style()
        self.style.configure("Custom.TButton", focuscolor='none')
        self.style.map('Custom.TButton',
            background=[('active', '!disabled', 'SystemButtonFace')],
            relief=[('pressed', 'sunken'), ('!pressed', 'raised')])
        
        
        # Variables pour la grille
        self.cell_size = 20
        self.grid_width = 40
        self.grid_height = 30
        self.grid = np.zeros((self.grid_height, self.grid_width))
        
        # Variables pour le zoom et le déplacement
        self.zoom = 1.0
        self.offset_x = 0
        self.offset_y = 0
        self.dragging = False
        self.last_x = 0
        self.last_y = 0
        
        # Création du canvas avec scrollbars
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)
        
        # Canvas - configuré pour ne pas prendre le focus
        self.canvas = tk.Canvas(
            self.frame,
            width=800,
            height=600,
            bg='white',
            takefocus=0,
            highlightthickness=0
        )
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Scrollbars
        self.v_scrollbar = ttk.Scrollbar(self.frame, orient=tk.VERTICAL, takefocus=0)
        self.h_scrollbar = ttk.Scrollbar(self.frame, orient=tk.HORIZONTAL, takefocus=0)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Configuration des scrollbars
        self.v_scrollbar.config(command=self.canvas.yview)
        self.h_scrollbar.config(command=self.canvas.xview)
        self.canvas.config(xscrollcommand=self.h_scrollbar.set,
                        yscrollcommand=self.v_scrollbar.set)
        
        # Frame pour les contrôles
        self.control_frame = ttk.Frame(root)
        self.control_frame.pack(fill=tk.X)
        
        # Boutons avec style personnalisé
        self.start_button = ttk.Button(
            self.control_frame, 
            text="Démarrer",
            style="Custom.TButton",
            takefocus=False
        )
        self.clear_button = ttk.Button(
            self.control_frame, 
            text="Effacer",
            command=self.clear_grid,
            style="Custom.TButton",
            takefocus=False
        )
        
        self.start_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.clear_button.pack(side=tk.LEFT, padx=5, pady=5)
        
        # Bind des événements
        self.canvas.bind('<Button-1>', self.on_click)
        self.canvas.bind('<B3-Motion>', self.on_drag)
        self.canvas.bind('<Button-3>', self.start_drag)
        self.canvas.bind('<ButtonRelease-3>', self.stop_drag)
        self.canvas.bind('<MouseWheel>', self.on_mousewheel)
        self.canvas.bind('<Button-4>', self.on_mousewheel)
        self.canvas.bind('<Button-5>', self.on_mousewheel)
        
        # Premier dessin de la grille
        self.draw_grid()
    
    def clear_grid(self):
        self.grid.fill(0)
        self.draw_grid()
    
    def draw_grid(self):
        self.canvas.delete('all')
        cell_size = self.cell_size * self.zoom
        
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                x1 = x * cell_size + self.offset_x
                y1 = y * cell_size + self.offset_y
                x2 = x1 + cell_size - 1
                y2 = y1 + cell_size - 1
                
                color = 'black' if self.grid[y][x] else 'white'
                self.canvas.create_rectangle(x1, y1, x2, y2, 
                                        fill=color, 
                                        outline='gray')
        
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))
    
    def on_click(self, event):
        canvas_x = self.canvas.canvasx(event.x)
        canvas_y = self.canvas.canvasy(event.y)
        
        grid_x = int((canvas_x - self.offset_x) / (self.cell_size * self.zoom))
        grid_y = int((canvas_y - self.offset_y) / (self.cell_size * self.zoom))
        
        if 0 <= grid_x < self.grid_width and 0 <= grid_y < self.grid_height:
            self.grid[grid_y][grid_x] = not self.grid[grid_y][grid_x]
            self.draw_grid()
    
    def start_drag(self, event):
        self.dragging = True
        self.last_x = event.x
        self.last_y = event.y
    
    def stop_drag(self, event):
        self.dragging = False
    
    def on_drag(self, event):
        if self.dragging:
            dx = event.x - self.last_x
            dy = event.y - self.last_y
            
            self.offset_x += dx
            self.offset_y += dy
            
            self.last_x = event.x
            self.last_y = event.y
            
            self.draw_grid()
    
    def on_mousewheel(self, event):
        old_zoom = self.zoom
        
        if event.num == 5 or event.delta < 0:
            self.zoom = max(0.1, self.zoom * 0.9)
        elif event.num == 4 or event.delta > 0:
            self.zoom = min(5.0, self.zoom * 1.1)
            
        if old_zoom != self.zoom:
            canvas_x = self.canvas.canvasx(event.x)
            canvas_y = self.canvas.canvasy(event.y)
            
            self.offset_x += (canvas_x - self.offset_x) * (1 - self.zoom/old_zoom)
            self.offset_y += (canvas_y - self.offset_y) * (1 - self.zoom/old_zoom)
            
            self.draw_grid()

if __name__ == "__main__":
    root = tk.Tk()
    root.option_add('*Focus', '')
    app = GameOfLife(root)
    root.mainloop()
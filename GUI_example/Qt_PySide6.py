from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QVBoxLayout, QWidget, QPushButton
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QPen, QBrush, QColor
import numpy as np
import sys

class GameView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        
        # Active l'anti-aliasing pour un meilleur rendu
        self.setRenderHint(self.renderHints().Antialiasing)
        
        # Permet le zoom avec la molette de la souris
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setDragMode(QGraphicsView.ScrollHandDrag)  # Permet de se déplacer avec la souris
        
        # Initialisation de la grille
        self.cell_size = 20
        self.grid_width = 40
        self.grid_height = 30
        self.grid = np.zeros((self.grid_height, self.grid_width))
        
        self.draw_grid()

    def draw_grid(self):
        self.scene.clear()
        
        # Dessine les cellules
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                cell = self.scene.addRect(
                    x * self.cell_size,
                    y * self.cell_size,
                    self.cell_size - 1,
                    self.cell_size - 1,
                    QPen(QColor(200, 200, 200)),
                    QBrush(QColor(0, 0, 0) if self.grid[y][x] else QColor(255, 255, 255))
                )
                cell.setData(0, (x, y))  # Stocke les coordonnées pour le clic
    
    def wheelEvent(self, event):
        # Gestion du zoom
        zoomInFactor = 1.25
        zoomOutFactor = 1 / zoomInFactor

        # Sauvegarde l'ancienne position
        oldPos = self.mapToScene(event.position().toPoint())

        # Zoom
        if event.angleDelta().y() > 0:
            zoomFactor = zoomInFactor
        else:
            zoomFactor = zoomOutFactor
        self.scale(zoomFactor, zoomFactor)

        # Obtient la nouvelle position
        newPos = self.mapToScene(event.position().toPoint())
        
        # Déplace la vue pour maintenir la position sous la souris
        delta = newPos - oldPos
        self.translate(delta.x(), delta.y())

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            pos = self.mapToScene(event.pos())
            x = int(pos.x() // self.cell_size)
            y = int(pos.y() // self.cell_size)
            
            if 0 <= x < self.grid_width and 0 <= y < self.grid_height:
                self.grid[y][x] = not self.grid[y][x]
                self.draw_grid()
        else:
            super().mousePressEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Jeu de la Vie - Qt")
        
        # Widget principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        
        # Vue du jeu
        self.game_view = GameView()
        layout.addWidget(self.game_view)
        
        # Boutons de contrôle
        button_layout = QVBoxLayout()
        start_button = QPushButton("Démarrer")
        clear_button = QPushButton("Effacer")
        
        button_layout.addWidget(start_button)
        button_layout.addWidget(clear_button)
        layout.addLayout(button_layout)
        
        # Connexion des boutons
        clear_button.clicked.connect(self.clear_grid)
        
        self.resize(800, 600)
    
    def clear_grid(self):
        self.game_view.grid.fill(0)
        self.game_view.draw_grid()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
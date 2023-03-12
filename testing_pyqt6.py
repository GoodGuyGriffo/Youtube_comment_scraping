import sys

from PyQt6.QtWidgets import QApplication, QGridLayout, QPushButton, QWidget, QLabel, QTableWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")
        main_layout = QGridLayout()

        layout = QGridLayout()
        # Add widgets to the layout
        self.button1 = QPushButton("Button at (0, 0)")
        self.label = QLabel("test")
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(QPushButton("Button at (0, 1)"), 0, 1)
        layout.addWidget(QPushButton("Button at (0, 2)"), 0, 2)
        layout.addWidget(QPushButton("Button at (1, 0)"), 1, 0)
        layout.addWidget(QPushButton("Button at (1, 1)"), 1, 1)
        layout.addWidget(QPushButton("Button at (1, 2)"), 1, 2)
        layout.addWidget(QPushButton("Button at (2, 0)"), 2, 0)
        layout.addWidget(QPushButton("Button at (2, 1)"), 2, 1)
        layout.addWidget(QPushButton("Button at (2, 2)"), 2, 2)

        # Set the layout on the application's window
        main_layout.addWidget(QLabel("Outside"))

        main_layout.addLayout(layout,0,1)

        self.table = QTableWidget()
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        main_layout.addWidget(self.table)

        main_layout.setHorizontalSpacing(40)
        main_layout.setContentsMargins(100, 100, 100, 100)
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

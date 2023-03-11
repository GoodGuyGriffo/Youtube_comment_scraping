from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import sys
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(1280, 720)

        # add video Id stuff
        self.video_id_input_label = QLabel("Video ID - ", self)
        self.video_id_input_label.setFont(QFont("Arial", 16))
        self.video_id_input_label.setGeometry(10, 10, 100, 40)

        self.video_id_input = QLineEdit(self)
        self.video_id_input.setGeometry(110, 10, 300, 40)

        # add page number stuff
        self.page_number_label = QLabel("Page number - ", self)
        self.page_number_label.setFont(QFont("Arial", 16))
        self.page_number_label.setGeometry(440, 10, 150, 40)

        self.page_number_input = QLineEdit(self)
        self.page_number_input.setText("1")
        self.page_number_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_number_input.setFont(QFont("Arial", 14))
        self.page_number_input.setGeometry(580, 10, 80, 40)

        # add the GO button
        self.go_button = QPushButton("GO", self)
        self.go_button.setFont(QFont("Arial", 18))
        self.go_button.setGeometry(690, 10, 70, 40)


        # add comment display stuff
        self.comment_label = QLabel("Current Comment - ", self)
        self.comment_label.setFont(QFont("Arial", 18))
        self.comment_label.setGeometry(10, 100, 230, 40)

        self.next_comment_button = QPushButton("Next Comment", self)
        self.next_comment_button.setFont(QFont("Comic Sans", 12))
        self.next_comment_button.setGeometry(330, 100, 200, 40)

        self.save_comment_button = QPushButton("Save Comment", self)
        self.save_comment_button.setFont(QFont("Comic Sans", 12))
        self.save_comment_button.setGeometry(560, 100, 200, 40)

        self.comment_area = QTextEdit(self)
        self.comment_area.setGeometry(10, 150, 750, 60)
        self.comment_area.setReadOnly(True)


        # now to add the saved comments
        self.saved_comments_label = QLabel("Saved Comments - ", self)
        self.saved_comments_label.setFont(QFont("Arial", 18))
        self.saved_comments_label.setGeometry(10, 250, 230, 40)


        # add button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(1200, 670, 80, 40)

        self.show()



app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())

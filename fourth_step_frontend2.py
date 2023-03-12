import sys
import sqlite3
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QGridLayout Example")
        main_layout = QGridLayout()

        video_info_layout = QGridLayout()
        adding_comments_layout = QGridLayout()
        saved_comments_layout = QGridLayout()


        # ---------------- Video Info Layout ----------------------------

        self.video_id_label = QLabel("Video Id - ")
        self.video_id_label.setFont(QFont("Arial", 16))
        video_info_layout.addWidget(self.video_id_label, 0, 0)

        self.video_id_input = QLineEdit(self)
        self.video_id_input.setFixedSize(300, 40)
        video_info_layout.addWidget(self.video_id_input, 0, 1)

        self.spacer = QLabel()
        self.spacer.setFixedSize(20, 40)
        video_info_layout.addWidget(self.spacer, 0, 2)

        self.page_number_label = QLabel("Page number - ", self)
        self.page_number_label.setFont(QFont("Arial", 16))
        video_info_layout.addWidget(self.page_number_label, 0, 3)

        self.page_number_input = QLineEdit(self)
        self.page_number_input.setText("1")
        self.page_number_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page_number_input.setFont(QFont("Arial", 14))
        self.page_number_input.setFixedSize(60, 40)
        video_info_layout.addWidget(self.page_number_input, 0, 4)

        video_info_layout.addWidget(self.spacer, 0, 5)

        self.go_button = QPushButton("GO", self)
        self.go_button.setFont(QFont("Arial", 18))
        self.go_button.setFixedSize(70, 40)
        video_info_layout.addWidget(self.go_button, 0, 6)


        # ---------------- Next comment Layout ----------------------------

        adding_comments_layout.setVerticalSpacing(5)
        adding_comments_layout.setHorizontalSpacing(3)

        self.comment_label = QLabel("Current Comment - ", self)
        self.comment_label.setFont(QFont("Arial", 18))
        adding_comments_layout.addWidget(self.comment_label, 0, 0)

        self.next_comment_button = QPushButton("Next Comment", self)
        self.next_comment_button.setFont(QFont("Comic Sans", 12))
        self.next_comment_button.setFixedSize(200, 40)
        adding_comments_layout.addWidget(self.next_comment_button, 0, 1)

        self.save_comment_button = QPushButton("Save Comment", self)
        self.save_comment_button.setFont(QFont("Comic Sans", 12))
        self.save_comment_button.setFixedSize(200, 40)
        adding_comments_layout.addWidget(self.save_comment_button, 0, 2)

        self.comment_area = QTextEdit(self)
        self.comment_area.setFixedHeight(60)
        self.comment_area.setReadOnly(True)
        adding_comments_layout.addWidget(self.comment_area, 1, 0, 1, 3)


        # ---------------- Saved comment Layout ----------------------------

        saved_comments_layout.setVerticalSpacing(5)

        self.table = QTableWidget()
        self.table.setColumnCount(2)
        self.table.setColumnWidth(0, 60)
        self.table.setColumnWidth(1, 645)
        self.table.setHorizontalHeaderLabels(("Id", "Comment"))
        self.table.horizontalHeaderItem(0).setFont(QFont("Arial", 14))
        self.table.horizontalHeaderItem(1).setFont(QFont("Arial", 14))
        self.table.verticalHeader().setVisible(False)
        saved_comments_layout.addWidget(self.table, 0, 0, 1, 2)

        self.delete_button = QPushButton("Delete Comment")
        self.delete_button.setFont(QFont("Arial", 12))
        self.delete_button.setFixedSize(200, 40)
        saved_comments_layout.addWidget(self.delete_button, 1, 1)


        # ---------------- combining Layouts ----------------------------

        main_layout.addLayout(video_info_layout, 0, 0)
        main_layout.addLayout(adding_comments_layout, 1, 0)
        main_layout.addLayout(saved_comments_layout, 2, 0)

        main_layout.setHorizontalSpacing(40)
        main_layout.setVerticalSpacing(30)
        main_layout.setContentsMargins(20, 20, 20, 20)
        self.setLayout(main_layout)
        self.load_data()


    def load_data(self):
        connection = sqlite3.connect("data.db")
        results = connection.execute("SELECT * FROM comments")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(results):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())

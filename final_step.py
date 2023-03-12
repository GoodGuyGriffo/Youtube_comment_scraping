import sys
import sqlite3
import requests
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt


api_key = "AIzaSyDofIhaRG0P3uvcDi34sqNTvWWdcpm455U"


class Window(QWidget):
    def __init__(self):
        super().__init__()


        # ---------------- Initial variables and such ----------------------------

        self.comments = []
        self.next_comment_page = ""

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
        self.go_button.clicked.connect(self.go)
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
        self.next_comment_button.clicked.connect(self.next_comment)
        adding_comments_layout.addWidget(self.next_comment_button, 0, 1)

        self.save_comment_button = QPushButton("Save Comment", self)
        self.save_comment_button.setFont(QFont("Comic Sans", 12))
        self.save_comment_button.setFixedSize(200, 40)
        self.save_comment_button.clicked.connect(self.save_comment)
        adding_comments_layout.addWidget(self.save_comment_button, 0, 2)

        self.comment_area = QTextEdit(self)
        self.comment_area.setFont(QFont("Arial", 10))
        self.comment_area.setFixedHeight(90)
        self.comment_area.setReadOnly(True)
        adding_comments_layout.addWidget(self.comment_area, 1, 0, 1, 3)


        # ---------------- Saved comment Layout ----------------------------

        saved_comments_layout.setVerticalSpacing(5)

        self.table = QTableWidget()
        self.table.setColumnCount(1)
        #self.table.setColumnWidth(0, 705)
        # self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(True)
        saved_comments_layout.addWidget(self.table, 0, 0, 1, 2)

        self.delete_button = QPushButton("Delete Comment")
        self.delete_button.setFont(QFont("Arial", 12))
        self.delete_button.setFixedSize(200, 40)
        self.delete_button.clicked.connect(self.delete_comment)
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

    def go(self):
        """ Ok we have to get the stuff based off the stuff"""
        video_id = self.video_id_input.text().strip()
        desired_page_number = int(self.page_number_input.text().strip())

        self.comments = []
        page_number = 1

        # we always need to grab the first page
        comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&order=relevance&key={api_key}"
        comments_response = requests.get(comments_url)
        comments_data = comments_response.json()
        self.next_comment_page = comments_data["nextPageToken"]


        while page_number != desired_page_number:
            comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&order=relevance&pageToken={self.next_comment_page}&key={api_key}"
            comments_response = requests.get(comments_url)
            comments_data = comments_response.json()
            page_number = page_number + 1

        for item in comments_data["items"]:
            self.comments.append(item["snippet"]["topLevelComment"]["snippet"]["textDisplay"])

        self.comment_area.setText(self.comments[0])
        self.comments.pop(0)


    def next_comment(self):
        comments_len = len(self.comments)
        if comments_len == 0:
            video_id = self.video_id_input.text().strip()
            comments_url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&order=relevance&pageToken={self.next_comment_page}&key={api_key}"
            comments_response = requests.get(comments_url)
            comments_data = comments_response.json()
            self.next_comment_page = comments_data["nextPageToken"]

            for item in comments_data["items"]:
                self.comments.append(item["snippet"]["topLevelComment"]["snippet"]["textDisplay"])

            self.page_number_input.setText(str(int(self.page_number_input.text()) + 1))

        self.comment_area.setText(self.comments[0])
        self.comments.pop(0)

    def save_comment(self):
        comment_to_add = window.comment_area.toPlainText()

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO comments VALUES ('{comment_to_add}')")
        connection.commit()
        cursor.close()
        connection.close()
        window.load_data()

    def delete_comment(self):
        row = window.table.currentRow()
        comment_to_delete = window.table.item(row, 0).text()

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM comments WHERE comment = '{comment_to_delete}'")
        connection.commit()
        cursor.close()
        connection.close()
        window.load_data()

    def load_data(self):
        connection = sqlite3.connect("data.db")
        results = connection.execute("SELECT * FROM comments")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(results):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()
        try:
            window.table.resizeColumnsToContents()
        except:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    window.table.resizeColumnsToContents()
    sys.exit(app.exec())

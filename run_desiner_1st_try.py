from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication,QFileDialog,QLabel,QScrollArea,QVBoxLayout
from PySide6.QtCore import Qt,QCoreApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PIL import Image, ImageQt
from txt_to_html import txt_to_html

class MainWindow:
    def __init__(self):
        loader = QUiLoader()
        self.ui = loader.load("designer_1st_try.ui")

        self.ui.pushButton.clicked.connect(self.say_hello)

        self._image: "Image" = None
        self.ui.pushButton_2.clicked.connect(self.load)

        self.ui.show_blog_btn.clicked.connect(self.show_blog)

        self.scroll = QScrollArea(self.ui.centralwidget)
        self.scroll.setGeometry(300, 10, 920, 550)

        self.blog = QLabel()
        self.blog.setGeometry(10, 10, 896, 1000)
        self.scroll.setWidget(self.blog)
        self.scroll.setWidgetResizable(True)




    def say_hello(self):
        self.ui.label.setText("putton pressed!!")

    def load(self):
        file_name, file_type = QFileDialog.getOpenFileName(
            self.ui,
            "Select Image",
            "./",
            "Image (*.png *.bmp *.jpg *.jpeg);;All Files(*)"
        )

        if file_name:
            self._image = Image.open(file_name)

        self.show_image()
    def show_image(self):
        if self._image:
            # #specify the ideal size of the picture
            max_size = (896, 896*10) #height don't care

            # # 调整图像大小，保持宽高比
            self._image.thumbnail(max_size, Image.Resampling.LANCZOS)
            qt_img = ImageQt.ImageQt(self._image)
            q_pixmap = QPixmap.fromImage(qt_img)
            # self.ui.show_pic.setPixmap(q_pixmap.scaled(896, 896*10, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            self.ui.label_2.setPixmap(q_pixmap)
            self.ui.label_2.adjustSize()

    def show_blog(self):
        html_content = txt_to_html("raw_blog.txt")
        print(html_content)
        
        # self.ui.show_pic.setTextFormat(Qt.TextFormat.RichText)
        # self.ui.show_pic.setText(html_content)

        # scroll = QScrollArea(self.ui.centralwidget)
        # scroll.setGeometry(300, 10, 920, 550)
        # scroll.setGeometry(300, 10, 896, 1000)
        self.blog.setTextFormat(Qt.TextFormat.RichText)
        self.blog.setText(html_content)
        # self.blog.setText("hhh")
        # scroll.setWidget(blog)
        # scroll.setWidgetResizable(True)


    def scroll(self):
        imageLabel = QLabel()
        image = Image.open("saku_nagi.jpg")
        qt_img = ImageQt.ImageQt(image)
        imageLabel.setPixmap(QPixmap.fromImage(qt_img))

        scrollArea = QScrollArea()
        scrollArea.setWidget(imageLabel)
        scrollArea.show()

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    window = MainWindow()
    window.ui.show()
    app.exec()

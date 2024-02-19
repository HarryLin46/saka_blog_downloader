from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication,QFileDialog,QLabel,QScrollArea,QVBoxLayout,QStackedWidget,QWidget,QMainWindow,QPushButton
from PySide6.QtCore import Qt,QCoreApplication
from PySide6.QtWebEngineWidgets import QWebEngineView
from PIL import Image, ImageQt
from txt_to_html import txt_to_html,prepare_html

from member_window import nogi_member_window,hina_member_window,saku_member_window

import requests,bs4,os,json,time

from update_member import update_nogi,update_hinata,update_sakura

from nogi_crawler import nogi_crawling

class MainWindow:
    def __init__(self):
        loader = QUiLoader()
        self.ui = loader.load("main.ui")

        #create stack widget, which has 3 pages, for showing a blog 
        self.show_blog_stack = QStackedWidget(self.ui.centralwidget)
        self.show_blog_stack.setGeometry(320,10, 920, 550)
        self.page0 = QWidget()
        self.page1 = QWidget()
        self.page2 = QWidget()


        self.show_blog_stack.addWidget(self.page0)
        self.show_blog_stack.addWidget(self.page1)
        self.show_blog_stack.addWidget(self.page2)

        self.nogi_scroll = QScrollArea(self.page0)
        self.nogi_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.nogi_scroll.setGeometry(0,0, 920, 550)

        self.nogi_blog = QLabel()
        self.nogi_blog.setWordWrap(True)
        self.nogi_scroll.setWidget(self.nogi_blog)
        self.nogi_blog.setGeometry(0, 0, 896, 1000)
        self.nogi_scroll.setWidgetResizable(True)

        self.hina_scroll = QScrollArea(self.page1)
        self.hina_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.hina_scroll.setGeometry(0,0, 920, 550)

        self.hina_blog = QLabel()
        self.hina_blog.setWordWrap(True)
        self.hina_scroll.setWidget(self.hina_blog)
        self.hina_blog.setGeometry(0, 0, 896, 1000)
        self.hina_scroll.setWidgetResizable(True)

        self.saku_scroll = QScrollArea(self.page2)
        self.saku_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.saku_scroll.setGeometry(0,0, 920, 550)

        self.saku_blog = QLabel()
        self.saku_blog.setWordWrap(True)
        self.saku_scroll.setWidget(self.saku_blog)
        self.saku_blog.setGeometry(0, 0, 896, 1000)
        self.saku_scroll.setWidgetResizable(True)

        self.ui.nogi_btn.clicked.connect(self.set_nogi_blog)
        self.ui.hina_btn.clicked.connect(self.set_hina_blog)
        self.ui.saku_btn.clicked.connect(self.set_saku_blog)

        self.nogi_mem_window = nogi_member_window(self.ui)
        self.hina_mem_window = hina_member_window(self.ui)
        self.saku_mem_window = saku_member_window(self.ui)
        self.ui.mem_btn.clicked.connect(self.switch_mem_window)

        self.ui.update_mem_btn.clicked.connect(self.update_members)

        self.ui.crawling_btn.clicked.connect(self.run_crawling)

        nogi_mem_lists = []
        with open("member/nogi/member_list.txt",'r',encoding='utf-8') as file:
            for member in file:
                nogi_mem_lists.append(member.rstrip("\n")) #nogi_mem_lists = ['五百城 茉央', '池田 瑛紗', ...]
        self.ui.member_cbbox.addItems(nogi_mem_lists)
        # self.ui.member_cbbox.setCurrentIndex(1)

        self.ui.member_cbbox.currentIndexChanged.connect(self.show_blog2)
        
        


    def show_blog(self):
        current_idx = self.show_blog_stack.currentIndex() #0: nogi, 1: hinata, 2: sakura
        if current_idx==0: #it's nogi
            # html_content = txt_to_html("blog_source/raw_blog.txt")
            with open('blog_article.html', 'r', encoding='utf-8') as file:
                html_content = file.read()
            self.nogi_blog.setTextFormat(Qt.TextFormat.RichText)
            self.nogi_blog.setText(html_content)
            self.nogi_scroll.verticalScrollBar().setValue(0)
        elif current_idx==1: #it's hinata
            html_content = txt_to_html("blog_source/raw_blog_h.txt")
            self.hina_blog.setTextFormat(Qt.TextFormat.RichText)
            self.hina_blog.setText(html_content)
            self.hina_scroll.verticalScrollBar().setValue(0)
        elif current_idx==2: #it's sakura
            html_content = txt_to_html("blog_source/raw_blog_s.txt")
            self.saku_blog.setTextFormat(Qt.TextFormat.RichText)
            self.saku_blog.setText(html_content)
            self.saku_scroll.verticalScrollBar().setValue(0)

    def set_nogi_blog(self):
        self.show_blog_stack.setCurrentIndex(0)
        self.show_blog()
    def set_hina_blog(self):
        self.show_blog_stack.setCurrentIndex(1)
        self.show_blog()
    def set_saku_blog(self):
        self.show_blog_stack.setCurrentIndex(2)
        self.show_blog()

    def switch_mem_window(self):
        # self.nogi_mem_window.setGeometry(self.ui.geometry()) #move 1st line of nogi_member_window class
        current_idx = self.show_blog_stack.currentIndex()
        if current_idx==0: #it's nogi
            self.nogi_mem_window.show()
        elif current_idx==1: #it's hinata
            self.hina_mem_window.show()
        elif current_idx==2: #it's sakura
            self.saku_mem_window.show()
        
    def update_members(self):
        current_idx = self.show_blog_stack.currentIndex()
        if current_idx==0: #it's nogi
            update_nogi()
        elif current_idx==1: #it's hinata
            update_hinata()
        elif current_idx==2: #it's sakura
            update_sakura()

    def run_crawling(self):
        current_idx = self.show_blog_stack.currentIndex()
        if current_idx==0: #it's nogi
            nogi_crawling()
        elif current_idx==1: #it's hinata
            hina_crawling()
        elif current_idx==2: #it's sakura
            saku_crawling()

    def show_blog2(self):
        select_mem = self.ui.member_cbbox.currentText() #ex. 遠藤さくら

        blogs_root = os.path.join("blog_source/Nogizaka46/",select_mem) #ex.blog_source/Nogizaka46/遠藤さくら

        blogs = os.listdir(blogs_root)

        print(blogs)


        



if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication([])
    window = MainWindow()
    window.ui.show()
    app.exec()

import re
import os
import sys
import cv2
from PySide2 import QtWidgets
from enity_sql import *
from welcome import *
from Custom_Widgets.Widgets import *
from video_play import play_Work, cvDecode
from camera_play import camera_play


class MainApp(QMainWindow):
    change_mainPages = 0
    camera_on = 0
    # 构造方法
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)
        self.ui.mainPages.setCurrentIndex(4)
        self.fileName = os.getcwd() + "\output001.avi"
        self.handle_buttons()
        self.show_sql()

    # 加载数据库
    def show_sql(self):
        self.ui.feature_ifo.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.feature_ifo.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.feature_ifo.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.feature_ifo.verticalHeader().setVisible(False)
        self.ui.feature_ifo.sortItems(0, Qt.AscendingOrder)
        self.conn = openSql()  # 获取数据库连接
        self.cur = self.conn.cursor()
        sql = "SELECT * from feacture_ifo"
        # 执行sql语句
        self.cur.execute(sql)
        # 获取所有的数据
        data = self.cur.fetchall()

        if data:
            # 行列遍历并插入
            self.ui.feature_ifo.setRowCount(self.cur.rowcount)
            self.ui.feature_ifo.setColumnCount(len(data[0]) + 1)
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.ui.feature_ifo.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                self.ui.feature_ifo.setCellWidget(row, len(data[0]), self.button_new())
                row += 1
        closeSql(self.conn, self.cur)

    # 创建视频播放线程函数
    def init_video(self):
        self.decodework = cvDecode()
        self.decodework.threadFlag = 1
        self.decodework.start()
        self.playwork = play_Work()
        self.playwork.threadFlag = 1
        self.playwork.playLabel = self.ui.play_view
        self.play_thread = QThread()  # 创建线程
        self.playwork.moveToThread(self.play_thread)
        self.play_thread.started.connect(self.playwork.play)  # 线程与类方法进行绑定
        self.play_thread.start()

    # 创建摄像头的播放线程
    def init_camera(self):
        self.cameraply = camera_play()
        self.cameraply.play_on = 1
        self.cameraply.viedo_area = self.ui.viedo_area
        self.cameraply.loadpath = self.fileName
        self.cameraply_thread = QThread()  # 创建线程
        self.cameraply.moveToThread(self.cameraply_thread)
        self.cameraply_thread.started.connect(self.cameraply.show_camera)  # 线程与类方法进行绑定
        self.cameraply_thread.start()

    # 所有Button的消息与槽的通信
    def handle_buttons(self):
        self.ui.play_cutbtn.clicked.connect(self.changeCamera)
        self.ui.playButton.clicked.connect(self.play_video)
        self.ui.viewButton.clicked.connect(self.load_video)
        self.ui.playButton.setEnabled(False)
        self.ui.videobtn.clicked.connect(self.change_to_video)
        self.ui.homebtn.clicked.connect(self.change_to_home)
        self.ui.loginbtn.clicked.connect(self.change_to_login)
        self.ui.cambtn.clicked.connect(self.change_to_cam)
        self.ui.ifobtn.clicked.connect(self.change_to_ifo)
        self.ui.refreshbtn.clicked.connect(self.show_sql)
        self.ui.searchbtn.clicked.connect(self.quaryIfo_Table)
        self.ui.searchbtn_3.clicked.connect(self.choose_files)
        self.ui.searchlabel.setText(self.fileName)

    # 更改mainPages
    def change_to_video(self):
        self.init_video()
        self.change_mainPages = 1
        self.ui.mainPages.setCurrentIndex(0)

    def change_to_home(self):
        if self.change_mainPages == 1:
            self.ui.play_view.clear()
            if self.decodework.isRunning():
                self.decodework.threadFlag = 0
                self.decodework.quit()
            if self.play_thread.isRunning():
                self.playwork.threadFlag = 0
                self.play_thread.quit()
            self.change_mainPages = 0
        self.ui.mainPages.setCurrentIndex(4)

    def change_to_ifo(self):
        if self.change_mainPages == 1:
            self.ui.play_view.clear()
            if self.decodework.isRunning():
                self.decodework.threadFlag = 0
                self.decodework.quit()
            if self.play_thread.isRunning():
                self.playwork.threadFlag = 0
                self.play_thread.quit()
            self.change_mainPages = 0
        self.ui.mainPages.setCurrentIndex(3)

    def change_to_cam(self):
        if self.change_mainPages == 1:
            self.ui.play_view.clear()
            if self.decodework.isRunning():
                self.decodework.threadFlag = 0
                self.decodework.quit()
            if self.play_thread.isRunning():
                self.playwork.threadFlag = 0
                self.play_thread.quit()
            self.change_mainPages = 0
        self.ui.mainPages.setCurrentIndex(2)

    def change_to_login(self):
        if self.change_mainPages == 1:
            self.ui.play_view.clear()
            if self.decodework.isRunning():
                self.decodework.threadFlag = 0
                self.decodework.quit()
            if self.play_thread.isRunning():
                self.playwork.threadFlag = 0
                self.play_thread.quit()
            self.change_mainPages = 0
        self.ui.mainPages.setCurrentIndex(1)

    #选择视频文件的保存位置
    def choose_files(self):
        self.fileName, fileType = QtWidgets.QFileDialog.getSaveFileName(self, "选取文件", os.getcwd(),
                                                                   "All Files(*);;AVI Files(*.avi)")
        self.ui.searchlabel.setText(self.fileName)

    # 开关摄像头
    def changeCamera(self):
        if self.camera_on == 0:
            self.init_camera()
            self.camera_on=1
            self.ui.play_cutbtn.setText("关闭摄像头")
            self.ui.searchbtn_3.setEnabled(False)
        elif self.camera_on == 1:
            self.ui.play_cutbtn.setText("打开摄像头")
            self.cameraply.play_on = 0
            self.cameraply.cap.release()  # 释放视频流
            self.cameraply.viedo_area.clear()
            self.cameraply.out.release()
            self.ui.searchbtn_3.setEnabled(True)
            cv2.destroyAllWindows()
            if self.cameraply_thread.isRunning():
                self.cameraply.play_on = 0
                self.cameraply_thread.quit()
                self.ui.viedo_area.clear()
            self.camera_on = 0




    #   视频导入功能
    def load_video(self):
        self.ui.playButton.setText("暂停")
        self.ui.playButton.setEnabled(True)
        #   设置文件扩展名过滤,注意用双分号间隔
        fileName, filetype = QFileDialog.getOpenFileName(self, "选取文件", "./", "Excel Files (*.mp4);;Excel Files (*.avi)")
        self.decodework.changeFlag = 1
        self.decodework.video_path = r"" + fileName
        self.playwork.playFlag = 1

    #   暂停/播放功能
    def play_video(self):
        if self.ui.playButton.text() == "暂停":
            self.ui.playButton.setText("播放")
            self.playwork.playFlag = 0
        else:
            self.ui.playButton.setText("暂停")
            self.playwork.playFlag = 1

    # 在tableWight中新建按钮
    def button_new(self):
        widget = QtWidgets.QWidget()
        widget.setWindowFlag(Qt.FramelessWindowHint)
        widget.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        # 修改
        self.updateBtn = QtWidgets.QPushButton('修改')
        self.updateBtn
        self.updateBtn.setStyleSheet('''  QPushButton{text-align : center;
                                                  color : #0cc2aa;
                                                  background:transparent;
                                                  height : 24px;
                                                   border-radius: 6px;
                                                    border: none;
                                                  font-family:'宋体';
                                                  font-size:15px;}
                                                  QPushButton:pressed{
                                           text-align : center;
                                                  color : #0cc2aa;
                                                  background-color:#354759;
                                                  height : 24px;
                                                   border-radius: 6px;
                                                    border: none;
                                                  font-family:'宋体';
                                                  font-size:15px;
                                            }
                                                    ''')
        self.updateBtn.clicked.connect(self.updateIfo_Table)
        # 删除
        self.deleteBtn = QtWidgets.QPushButton('删除')
        self.deleteBtn.setStyleSheet(''' QPushButton{ text-align : center;
                                            color :#f44455;
                                                  background:transparent;
                                            height : 24px;
                                            border-radius: 6px;
                                            border: none;
                                            font-family:'宋体';
                                                  font-size:15px; }
                                            QPushButton:pressed{
                                            text-align : center;
                                            color :#f44455;
                                                   background-color:#354759;
                                            height : 24px;
                                            border-radius: 6px;
                                            border: none;
                                            font-family:'宋体';
                                                  font-size:15px;
                                            }
                                                   ''')
        self.deleteBtn.clicked.connect(self.deleteIfo_Table)
        hLayout = QtWidgets.QHBoxLayout()
        hLayout.addWidget(self.updateBtn)
        hLayout.addWidget(self.deleteBtn)
        hLayout.setContentsMargins(5, 3, 5, 3)
        widget.setLayout(hLayout)
        return widget

    # 删除tableWight中的一行
    def deleteIfo_Table(self):
        button = self.sender()
        if button:
            # 确定位置的时候这里是关键
            row = self.ui.feature_ifo.indexAt(button.parent().pos()).row()
        deldata = self.ui.feature_ifo.item(row, 0).text()
        text = '删除'
        informativeText = '是否确定删除该条数据,该操作不可逆'
        ret = QMessageBox.warning(self, text, informativeText, QMessageBox.Yes | QMessageBox.No,
                                  QMessageBox.No)
        if ret == QMessageBox.Yes:
            self.conn = openSql()  # 获取数据库连接
            self.cur = self.conn.cursor()
            self.cur.execute('DELETE FROM feacture_ifo WHERE id = %s', (str(deldata)))
            self.conn.commit()
            closeSql(self.conn, self.cur)
            text1 = '删除成功!'
            QMessageBox.about(self, "标题", text1)
            self.show_sql()

    # 查询tableWight的信息
    def quaryIfo_Table(self):
        search = self.ui.searchEdit.text()
        self.conn = openSql()  # 获取数据库连接
        self.cur = self.conn.cursor()
        sql = "SELECT * from feacture_ifo"
        # 执行sql语句
        self.cur.execute(sql)
        # 获取所有的数据
        data = self.cur.fetchall()
        self.ui.feature_ifo.clearContents()
        finall=[]
        if data:
            # 行列遍历并插入
            self.ui.feature_ifo.setColumnCount(len(data[0]) + 1)
            for row, form in enumerate(data):
                if re.search(".*"+search+".*",str(form[0]))!=None or re.search(".*"+search+".*",form[1])!=None:
                    finall.append(form)
                row+=1
        if finall:
            # 行列遍历并插入
            self.ui.feature_ifo.setRowCount(len(finall))
            self.ui.feature_ifo.setColumnCount(len(finall[0]) + 1)
            for row, form in enumerate(finall):
                for col, item in enumerate(form):
                    self.ui.feature_ifo.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1
                self.ui.feature_ifo.setCellWidget(row, len(finall[0]), self.button_new())
                row += 1
        closeSql(self.conn, self.cur)

    # 修改tableWight中的一行
    def updateIfo_Table(self):
        pass

    # 关闭线程
    def closeEvent(self, event):
        if self.decodework.isRunning():
            self.decodework.threadFlag = 0
            self.decodework.quit()
        if self.play_thread.isRunning():
            self.playwork.threadFlag = 0
            self.play_thread.quit()
        if self.cameraply_thread.isRunning():
            self.cameraply.play_on = 0
            self.cameraply_thread.quit()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()

    # 进入程序的主循环,通过exit退出
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

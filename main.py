import sys
import os
import webbrowser
import json
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import QThread, QFile, QDir
from ui_mainwindow import Ui_MainWindow
from worker import Worker


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.inputFileButton.clicked.connect(self.handle_input)
        self.ui.openButton.clicked.connect(self.handle_open)
        self.ui.startButton.clicked.connect(self.handle_start)

    def handle_input(self):
        current_path = QDir.currentPath()
        filter = QDir(current_path, "text files (*.txt)").filter()
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(filter)
        filename = dlg.getOpenFileName()
        f = open(filename[0], 'r')
        self.ui.inputFileLabel.setText(filename[0].split('/')[-1])
        with f:
            self.query_list = f.read().splitlines()
        return

    def handle_open(self):
        path = os.getcwd()+"/result"
        webbrowser.open("file:///"+path)

    def handle_start(self):
        self.thread = QThread()
        self.worker = Worker(self.query_list, self.ui.delaySpinBox.text())
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.progress.connect(self.ui.progressBar.setValue)
        self.thread.start()
        self.ui.buttonFrame.setEnabled(False)
        self.ui.inputFrame.setEnabled(False)
        self.thread.finished.connect(self.handle_finished)

    def handle_finished(self):
        self.ui.buttonFrame.setEnabled(True)
        self.ui.inputFrame.setEnabled(True)
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("수집이 완료되었습니다.")
        msgBox.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

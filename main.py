from gui import *
from swgoh_parser import getInfoFromSWGOH
from swgoh_parser import NotFoundPlayer
import threading
import sys

def run(id,needGuild, pathForSave):
    print('run')
    getInfoFromSWGOH(id=id.replace('-',''),needGuild=needGuild, pathForSave=pathForSave + '/')

def swCall():
    try:
        myThread2 = threading.Thread(target=run, args=(ui.lineEdit.text(), ui.checkBox.isChecked(), ui.lineEdit_2.text(), ))
        myThread2.start()
        myThread = threading.Thread(target=ui.startProgressBar())
        myThread.start()
        # result = getInfoFromSWGOH(id=ui.lineEdit.text().replace('-',''),needGuild=ui.checkBox.isChecked(), pathForSave=ui.lineEdit_2.text() + '/')
        # if result == 0:
        #     pass
    except NotFoundPlayer:
        ui.show_popup()
    except Exception as ex:
        print(ex)
        ui.show_popup_ex()


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    global ui
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(swCall) 
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

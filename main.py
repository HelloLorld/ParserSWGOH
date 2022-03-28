from gui import *
from swgoh_parser import getInfoFromSWGOH
from swgoh_parser import NotFoundPlayer
import threading
import sys


class ParserThread(threading.Thread):
    def __init__(self, id,needGuild, pathForSave, mainWindow):
        super().__init__()
        self.PlayerId = id
        self.PlayerNeedGuild = needGuild
        self.PlayerPathForSave = pathForSave
        self.window = mainWindow
    def run(self):
        print('run')
        try:
            getInfoFromSWGOH(id=self.PlayerId,needGuild=self.PlayerNeedGuild, pathForSave=self.PlayerPathForSave)
        except NotFoundPlayer:
            self.window.show_popup()
        except Exception as ex:
            print(ex)
            self.window.show_popup_ex()

def swCall():
    try:
        myThread2 = ParserThread(id=ui.lineEdit.text().replace('-',''),needGuild=ui.checkBox.isChecked(), pathForSave=ui.lineEdit_2.text() + '/', mainWindow=ui)
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

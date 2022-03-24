from gui import *
from swgoh_parser import getInfoFromSWGOH
from swgoh_parser import NotFoundPlayer
import sys


def swCall():
    try:
        getInfoFromSWGOH(id=ui.lineEdit.text(),needGuild=ui.checkBox.isChecked(), pathForSave=ui.lineEdit_2.text())
    except NotFoundPlayer as notFound:
        print(notFound)
    except Exception as ex:
        print(ex)


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

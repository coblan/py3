import sys
from PyQt5.Qt import QApplication,QWidget


if __name__=='__main__':
    app = QApplication(sys.argv)
    dialog = QWidget()
    dialog.show()
    sys.exit(app.exec_())

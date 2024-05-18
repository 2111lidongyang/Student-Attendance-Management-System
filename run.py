import sys

from PyQt5.QtWidgets import QApplication
from page.loginPage import LoginPage

if __name__ == '__main__':
    app = QApplication(sys.argv)
    page = LoginPage()
    page.show()
    sys.exit(app.exec())



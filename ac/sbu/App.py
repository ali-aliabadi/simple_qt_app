from PyQt5.QtWidgets import QApplication, QLabel

from ac.sbu.model.Human import Human


def start():
    app = QApplication([])
    label = QLabel()
    human = Human('Hello', ', World!')
    label.setText(human.get_name() + human.family)
    label.setFixedSize(200, 100)
    label.show()
    app.exec_()


if __name__ == '__main__':
    start()

import pygame as pg
import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # add a title
        self.setWindowTitle("Hello World")

        # set a vertical layout
        self.setLayout(qtw.QVBoxLayout())

        # create a label
        my_label = qtw.QLabel("Hello World What's your name")
        # label font size
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)
        
        # create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        # create a button
        my_button = qtw.QPushButton("Press me", clicked = lambda: press_it())
        self.layout().addWidget(my_button)



        # show the app
        self.show()

        def press_it():
            # add theme
            my_label.setText(f'Hello {my_entry.text()}')
            # clear entry box
            my_entry.setText("")


app = qtw.QApplication([])
mw = MainWindow()

# Run The App
app.exec_()
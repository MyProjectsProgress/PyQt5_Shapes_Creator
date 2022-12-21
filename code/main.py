from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QGridLayout,QGroupBox,QLabel,QSpinBox,QDoubleSpinBox,QGraphicsScene,QGraphicsView,QPushButton

class DrawWindow(QWidget):
    width = 800
    height = int(0.618 * width)
    
    translateXValue = 0
    translateYValue = 0
    rotateValue = 0
    scaleXValue = 1
    scaleYValue = 1

    def __init__(self):
        super().__init__()

        # Set Window title/size/layout
        self.setWindowTitle("Draw Shapes")
        self.resize(self.width, self.height)

#--------------------------------------------------------------------------------------#
        # Add the GroupBox of widgets (tools)
        self.groupBoxLayout = QGridLayout()
        self.toolsGroupBox = QGroupBox("Tools")
        self.toolsGroupBox.setFlat(False)
        self.toolsGroupBox.setLayout(self.groupBoxLayout)

#--------------------------------------------------------------------------------------#
        # Widgets in the Group box
        labels = [QLabel("TranslateX (px)"),QLabel("TranslateY (px)"),QLabel("Rotate (angle)"),QLabel("ScaleX (scaleFactor)"),QLabel("ScaleY (scaleFactor)")]
        self.inputs = [QSpinBox(self),QSpinBox(self),QSpinBox(self),QDoubleSpinBox(self),QDoubleSpinBox(self)]
        
        applyButton = QPushButton("Apply")
        applyButton.clicked.connect(self.onApply)

        self.inputs[0].setMinimum(-500)
        self.inputs[0].valueChanged.connect(self.onTranslateX)

        self.inputs[1].setMinimum(-500)
        self.inputs[1].valueChanged.connect(self.onTranslateY)

        self.inputs[2].setMinimum(-360)
        self.inputs[2].setMaximum(360)
        self.inputs[2].valueChanged.connect(self.onRotate)

        self.inputs[3].setValue(1)
        self.inputs[3].setMinimum(0)
        self.inputs[3].setMaximum(5)
        self.inputs[3].setSingleStep(0.1)
        self.inputs[3].valueChanged.connect(self.onScaleX)

        self.inputs[4].setValue(1)
        self.inputs[4].setMinimum(0)
        self.inputs[4].setMaximum(5)
        self.inputs[4].setSingleStep(0.1)
        self.inputs[4].valueChanged.connect(self.onScaleY)

        for i in range(len(labels)):
            self.groupBoxLayout.addWidget(labels[i])
            self.groupBoxLayout.addWidget(self.inputs[i])
        self.groupBoxLayout.addWidget(applyButton)

#--------------------------------------------------------------------------------------#
        scene = QGraphicsScene(self)
        self.drawingCanvas = QGraphicsView(scene,self)

        scene.addRect(0,0,200,100)
        scene.addEllipse(100,100,200,100)

#--------------------------------------------------------------------------------------#
        # Add Group box and drawing canvas to the window layout
        windowLayout = QHBoxLayout()
        windowLayout.addWidget(self.toolsGroupBox)
        windowLayout.addWidget(self.drawingCanvas)
        self.setLayout(windowLayout)

#--------------------------------------------------------------------------------------#
    # On changing the translationX spinbox  
    def onTranslateX(self):
        self.translateXValue = self.inputs[0].value()
    
    # On changing the translationY spinbox  
    def onTranslateY(self):
        self.translateYValue = self.inputs[1].value()

    # On changing the rotation spinbox  
    def onRotate(self):
        self.rotateValue = self.inputs[2].value()

    # On changing the scalingX spinbox  
    def onScaleX(self):
        self.scaleXValue = self.inputs[3].value()

    # On changing the scalingY spinbox  
    def onScaleY(self):
        self.scaleYValue = self.inputs[4].value()

    def onApply(self):
        self.drawingCanvas.translate(self.translateXValue,self.translateYValue)
        self.drawingCanvas.rotate(self.rotateValue)
        self.drawingCanvas.scale(self.scaleXValue,self.scaleYValue)

#--------------------------------------------------------------------------------------#
# Start the app and show the window
app = QApplication([])
appWindow = DrawWindow()
appWindow.show()
app.exec_()

import math
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QGroupBox,QLabel,QSpinBox,QDoubleSpinBox,QGraphicsScene,QGraphicsView,QPushButton,QGraphicsRectItem,QGraphicsPolygonItem,QGraphicsEllipseItem
from PyQt5.QtCore import QPointF
from PyQt5.QtGui import QTransform,QPolygonF

class DrawWindow(QWidget):

    # Variables
    windowWidth = 1200
    windowheight = int(0.618 * windowWidth)
    
    translateXValue = 0
    translateYValue = 0
    rotateValue = 0
    scaleXValue = 1
    scaleYValue = 1
    shearXValue = 0
    shearYValue = 0

    def __init__(self):
        super().__init__()

        # Set Window title/size/layout
        self.setWindowTitle("Draw Shapes")
        self.resize(self.windowWidth,self.windowheight)

#--------------------------------------------------------------------------------------#
        # Add the GroupBox of widgets (tools)
        self.groupBoxLayout = QVBoxLayout()
        self.toolsGroupBox = QGroupBox("Tools")
        self.toolsGroupBox.setFlat(False)
        self.toolsGroupBox.setLayout(self.groupBoxLayout)

#--------------------------------------------------------------------------------------#
        # Widgets in the Group box
        labels = [QLabel("TranslateX (px)"),QLabel("TranslateY (px)"),QLabel("Rotate (angle)"),QLabel("ScaleX (scaleFactor)"),QLabel("ScaleY (scaleFactor)"),QLabel("ShearX (shearFactor)"),QLabel("ShearY (shearFactor)")]
        self.inputs = [QSpinBox(self),QSpinBox(self),QSpinBox(self),QDoubleSpinBox(self),QDoubleSpinBox(self),QDoubleSpinBox(self),QDoubleSpinBox(self),]
        
        # Set spinbox properties
        self.inputs[0].setMinimum(-500)
        self.inputs[0].setMaximum(500)
        self.inputs[0].valueChanged.connect(self.onTranslateX)

        self.inputs[1].setMinimum(-500)
        self.inputs[1].setMaximum(500)
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

        self.inputs[5].setMinimum(-1)
        self.inputs[5].setMaximum(1)
        self.inputs[5].setSingleStep(0.1)
        self.inputs[5].valueChanged.connect(self.onShearX)

        self.inputs[6].setMinimum(-1)
        self.inputs[6].setMaximum(1)
        self.inputs[6].setSingleStep(0.1)
        self.inputs[6].valueChanged.connect(self.onShearY)

        applyButton = QPushButton("Apply")
        applyButton.clicked.connect(self.onApply)

        # Put the widgets in the groupbox
        for i in range(len(labels)):
            self.groupBoxLayout.addWidget(labels[i])
            self.groupBoxLayout.addWidget(self.inputs[i])
        self.groupBoxLayout.addWidget(applyButton)

#--------------------------------------------------------------------------------------#
        # Draw the shapes on the Canvas
        self.shapes = [QGraphicsEllipseItem(0,0,500,500),QGraphicsRectItem(300,100,60,20),QGraphicsRectItem(400,100,60,20),QGraphicsEllipseItem(300,150,50,50),QGraphicsEllipseItem(400,150,50,50),QGraphicsPolygonItem(self.createPoly(6,50,0)),QGraphicsPolygonItem(self.createTriangle(250,0))]
        scene = QGraphicsScene(self)
        self.canvas = QGraphicsView(scene, self)
        for shape in self.shapes:
            scene.addItem(shape)

#--------------------------------------------------------------------------------------#
        # Add the groupbox and canvas to the window
        windowLayout = QHBoxLayout()
        windowLayout.addWidget(self.toolsGroupBox)
        windowLayout.addWidget(self.canvas)
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

    # On changing the shearingX spinbox  
    def onShearX(self):
        self.shearXValue = self.inputs[5].value()

    # On changing the shearingY spinbox  
    def onShearY(self):
        self.shearYValue = self.inputs[6].value()

    # On clicking the apply button
    def onApply(self):
        t = QTransform()
        t.translate(self.translateXValue,self.translateYValue)
        for shape in self.shapes:
            shape.setTransform(t)
        self.canvas.shear(self.shearXValue,self.shearYValue)
        self.canvas.rotate(self.rotateValue)
        self.canvas.scale(self.scaleXValue,self.scaleYValue)

    # Creating a regular polygon
    def createPoly(self, n, r, s):
            polygon = QPolygonF()
            w = 360/n                                                     # angle per step
            for i in range(n):                                              # add the points of polygon
                t = w*i + s
                x = r*math.cos(math.radians(t))
                y = r*math.sin(math.radians(t))
                polygon.append(QPointF(self.width()/3 + x, self.height()/2 + y))
            return polygon
    
    # Creating a custom triangle
    def createTriangle(self, r, s):
        polygon = QPolygonF()
        w = 120                                                     # angle per step
        for i in range(3):                                              # add the points of polygon
            t = w*i + s
            x = r*math.cos(math.radians(t))
            y = r*math.sin(math.radians(t))
            polygon.append(QPointF(self.width()/10 + x, self.height()/20 + y))
        return polygon

#--------------------------------------------------------------------------------------#
# Start the app and show the window
app = QApplication([])
appWindow = DrawWindow()
appWindow.show()
app.exec_()

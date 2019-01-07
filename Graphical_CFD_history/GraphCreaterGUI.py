import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


class UI_form(QWidget):
    def __init__(self, parent=None):
        #super() でスーパークラスのインスタンスメソッドを呼び出す
        super(UI_form, self).__init__(parent)
        self.setup_ui()

    def setup_ui(self):

        # Set window background color
        #self.setAutoFillBackground(True)
        #p = self.palette()
        #p.setColor(self.backgroundRole(), Qt.gray)
        #self.setPalette(p)

        #button UI
        self.CreateButton = QPushButton('Create Graphs', self)
        self.ClearButton = QPushButton('All Clear', self)
        self.QuitButton = QPushButton('Quit', self)

        Flame_Layout = QVBoxLayout()

        Button_Layout = QGridLayout()
        Button_Layout.addWidget(self.CreateButton, 0, 0)
        Button_Layout.addWidget(self.ClearButton, 0, 1)
        #Button_Layout.addWidget(self.QuitButton, 2, 1)

        #process
        self.processTitle = QLabel('Now......', self)
        self.pbar = QProgressBar(self)
        self.step = 0
        self.pbar.setValue(self.step)


        #入力項目 Label
        self.ModelShapeLabel = QLabel('格子形状', self)
        self.FlowConditionLabel = QLabel('気流条件', self)
        self.AtmosphereLabel = QLabel('使用大気', self)
        self.GasModelLabel = QLabel('気体モデル', self)
        self.ViscoseModelLabel = QLabel('粘性モデル', self)
        self.SchemeLabel = QLabel('移流項スキーム', self)
        self.ThermalModelLabel = QLabel('温度モデル', self)
        self.AreaLabel = QLabel('抵抗面積', self)
        self.DensityLabel = QLabel('大気密度', self)
        self.VelocityLabel = QLabel('気流速度', self)

        #入力エリア LineEdit
        self.ModelShape = QLineEdit(self)
        self.FlowCondition = QLineEdit(self)
        self.Area = QLineEdit(self)
        self.Density = QLineEdit(self)
        self.Velocity = QLineEdit(self)
        self.ModelShape.setText('MartianPenetrator')
        self.FlowCondition.setText('OrbitalCalc')
        self.Area.setText('1')
        self.Density.setText('1')
        self.Velocity.setText('1')

        #入力エリア QComboBoxオブジェクトの作成
        self.Atmosphere = QComboBox(self)
        self.Atmosphere.addItems(['Mars','Earth'])
        self.GasModel = QComboBox(self)
        self.GasModel.addItems(['Ideal','Real'])
        self.ViscoseModel = QComboBox(self)
        self.ViscoseModel.addItems(['Laminar','SST-2003'])
        self.Scheme = QComboBox(self)
        self.Scheme.addItems(['SLAU2','AUSM+-2UP'])
        self.ThermalModel = QComboBox(self)
        self.ThermalModel.addItems(['Single','Two','Two-park','Four'])


        #最終表示
        self.ModelShapeDisplay = QLabel('no choice', self)
        self.FlowConditionDisplay = QLabel('no choice', self)
        self.AtmosphereDisplay = QLabel('no choice', self)
        self.GasModelDisplay = QLabel('no choice', self)
        self.ViscoseModelDisplay = QLabel('no choice', self)
        self.SchemeDisplay = QLabel('no choice', self)
        self.ThermalModelDisplay = QLabel('no choice', self)
        self.AreaDisplay = QLabel('no choice', self)
        self.DensityDisplay = QLabel('no choice', self)
        self.VelocityDisplay = QLabel('no choice', self)

        #表示更新
        self.ModelShape.textChanged.connect(self.ModelShapeDisplay.setText)
        self.FlowCondition.textChanged.connect(self.FlowConditionDisplay.setText)
        self.Atmosphere.activated[str].connect(self.AtmosphereDisplay.setText)
        self.GasModel.activated[str].connect(self.GasModelDisplay.setText)
        self.ViscoseModel.activated[str].connect(self.ViscoseModelDisplay.setText)
        self.Scheme.activated[str].connect(self.SchemeDisplay.setText)
        self.ThermalModel.activated[str].connect(self.ThermalModelDisplay.setText)
        self.Area.textChanged.connect(self.AreaDisplay.setText)
        self.Density.textChanged.connect(self.DensityDisplay.setText)
        self.Velocity.textChanged.connect(self.VelocityDisplay.setText)

        #Button connect
        self.QuitButton.clicked.connect(self.closeEvent)

        self.ClearButton.clicked.connect(self.ModelShapeDisplay.clear)
        self.ClearButton.clicked.connect(self.FlowConditionDisplay.clear)
        self.ClearButton.clicked.connect(self.AtmosphereDisplay.clear)
        self.ClearButton.clicked.connect(self.GasModelDisplay.clear)
        self.ClearButton.clicked.connect(self.ViscoseModelDisplay.clear)
        self.ClearButton.clicked.connect(self.SchemeDisplay.clear)
        self.ClearButton.clicked.connect(self.ThermalModelDisplay.clear)
        self.ClearButton.clicked.connect(self.AreaDisplay.clear)
        self.ClearButton.clicked.connect(self.DensityDisplay.clear)
        self.ClearButton.clicked.connect(self.VelocityDisplay.clear)

        self.CreateButton.clicked.connect(self.typeChange)

        #Layout
        Line_Layout = QGridLayout()
        Line_Layout.addWidget(self.ModelShapeLabel, 0, 0)
        Line_Layout.addWidget(self.ModelShape, 0, 1)
        Line_Layout.addWidget(self.ModelShapeDisplay, 0, 2)
        Line_Layout.addWidget(self.FlowConditionLabel, 1, 0)
        Line_Layout.addWidget(self.FlowCondition, 1, 1)
        Line_Layout.addWidget(self.FlowConditionDisplay, 1, 2)
        Line_Layout.addWidget(self.AtmosphereLabel, 2, 0)
        Line_Layout.addWidget(self.Atmosphere, 2, 1)
        Line_Layout.addWidget(self.AtmosphereDisplay, 2, 2)
        Line_Layout.addWidget(self.GasModelLabel, 3, 0)
        Line_Layout.addWidget(self.GasModel, 3, 1)
        Line_Layout.addWidget(self.GasModelDisplay, 3, 2)
        Line_Layout.addWidget(self.ViscoseModelLabel, 4, 0)
        Line_Layout.addWidget(self.ViscoseModel, 4, 1)
        Line_Layout.addWidget(self.ViscoseModelDisplay, 4, 2)
        Line_Layout.addWidget(self.SchemeLabel, 5, 0)
        Line_Layout.addWidget(self.Scheme, 5, 1)
        Line_Layout.addWidget(self.SchemeDisplay, 5, 2)
        Line_Layout.addWidget(self.ThermalModelLabel, 6, 0)
        Line_Layout.addWidget(self.ThermalModel, 6, 1)
        Line_Layout.addWidget(self.ThermalModelDisplay, 6, 2)
        Line_Layout.addWidget(self.AreaLabel, 7, 0)
        Line_Layout.addWidget(self.Area, 7, 1)
        Line_Layout.addWidget(self.AreaDisplay, 7, 2)
        Line_Layout.addWidget(self.DensityLabel, 8, 0)
        Line_Layout.addWidget(self.Density, 8, 1)
        Line_Layout.addWidget(self.DensityDisplay, 8, 2)
        Line_Layout.addWidget(self.VelocityLabel, 9, 0)
        Line_Layout.addWidget(self.Velocity, 9, 1)
        Line_Layout.addWidget(self.VelocityDisplay, 9, 2)

        Process_Layout = QVBoxLayout()
        Process_Layout.addWidget(self.processTitle)
        Process_Layout.addWidget(self.pbar)
        Process_Layout.addWidget(self.QuitButton)

        Flame_Layout.addLayout(Line_Layout)
        Flame_Layout.addLayout(Button_Layout)
        Flame_Layout.addLayout(Process_Layout)
        self.setLayout(Flame_Layout)
    
    def closeEvent(self):
        sys.exit(0)

    def typeChange(self):
        self.step = 0
        self.num_area = float(self.Area.text())
        self.num_density = float(self.Density.text())
        self.num_velocity = float(self.Velocity.text())
        self.str_model = str(self.ModelShape.text())
        self.str_flow = str(self.FlowCondition.text())
        self.str_atom = str(self.Atmosphere.currentText())
        self.str_gas = str(self.GasModel.currentText())
        self.str_viscose = str(self.ViscoseModel.currentText())
        self.str_scheme = str(self.Scheme.currentText())
        self.str_thermal = str(self.ThermalModel.currentText())

        #graphicCreate = GraphCreate(self.num_area,self.num_density,self.num_velocity,self.str_model,self.str_flow,self.str_atom,self.str_gas,self.str_viscose,self.str_scheme,self.str_thermal)

#class GraphCreate:
    #def __init__(self,num_area,num_density,num_velocity,str_model,str_flow,str_atom,str_gas,str_viscose,str_scheme,str_thermal,parent=None):

        self.Area = self.num_area
        self.Density = self.num_density
        self.Velocity = self.num_velocity
        self.GridModel = self.str_model
        self.FlowModel = self.str_flow
        self.GasSpecies = self.str_atom
        self.GasModel = self.str_gas
        self.ViscousModel = self.str_viscose
        self.SchemeForAdvectionTerm = self.str_scheme
        self.ThermalModel = self.str_thermal

        self.step = self.step + 5
        self.pbar.setValue(self.step)


        #print('=======================================================================')
        #print('Okay')

        self.path = self.GridModel + '_' + self.FlowModel + '_' + self.GasModel + '_' + self.ViscousModel + '_' + self.SchemeForAdvectionTerm + '_' + self.ThermalModel

        def my_makedirs( path ):
            if not os.path.isdir( self.path ):
                os.makedirs( self.path )
        
        my_makedirs( self.path )

        self.step = self.step + 5
        self.pbar.setValue(self.step)


        for num_exection in range(3):
            plt.cla()

            self.step = self.step + 5
            self.pbar.setValue(self.step)

            if num_exection==0:
                self.ReadTitleParts = 'hist_cdclcm_'
            elif num_exection==1:
                self.ReadTitleParts = 'hist_resi_'
            elif num_exection==2:
                self.ReadTitleParts = 'hist_rhs_'

            self.ReadTitle = self.ReadTitleParts + self.GasSpecies
            self.ReadFile = self.ReadTitle + ".txt"
            self.ReadPath = './InputFiles/' + self.ReadFile

            self.step = self.step + 5
            self.pbar.setValue(self.step)


            #print( "Visualizing Now : " + self.ReadPath )

            self.out_image =  './' + self.path + '/' + self.ReadTitle + ".png"
            #print( "Output file     : " + self.out_image )

            val = np.loadtxt( self.ReadPath )

            self.step = self.step + 5
            self.pbar.setValue(self.step)

            x = val[:,0]
            y = val[:,1]
            if num_exection==0:
                y = y*2/(self.Area*self.Density*self.Velocity*self.Velocity)

            self.step = self.step + 5
            self.pbar.setValue(self.step)

            plt.figure(figsize=( 8 , 6 ), dpi= 300 )
            plt.plot( x , y )
            plt.title( self.ReadTitle , fontsize = 18 )
            if num_exection!=0:
                plt.yscale('log')
            plt.grid(which='major',color='black',linestyle='--')
            plt.grid(which='minor',color='black',linestyle='--')
            plt.xlabel('Step number',fontsize=15)
            plt.ylabel('Value',fontsize=15)

            self.step = self.step + 5
            self.pbar.setValue(self.step)
    
            plt.savefig( self.out_image )
            plt.close()

            self.step = self.step + 5
            self.pbar.setValue(self.step)

            #print( "Finish                  : " + self.out_image )

        #print( 'All done !!')
        #print( '**********************  Please check it  ***********************' )
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    style = 'QLineEdit{color: black}'
    app.setStyleSheet(style)

    panel1 = QWidget()
    UI_window = UI_form(parent=panel1)

    panel1_layout = QVBoxLayout()
    panel1_layout.addWidget(UI_window)
    panel1.setLayout(panel1_layout)
    #panel1.setFixedSize(400, 600)

    main_window = QMainWindow()
    main_window.setWindowTitle("Graphic Creater by kazama")
    main_window.setCentralWidget(panel1)
    main_window.show()
    sys.exit(app.exec_())
import sys
import pyvisa
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QLineEdit, QHBoxLayout, QMessageBox, QComboBox, QCheckBox
from PyQt5.QtCore import Qt, QTimer

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.rm = pyvisa.ResourceManager()
        self.instrument = None
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.status_action)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('MAIN-Power-Supply Control Application')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.serial_port_combo = QComboBox(self)
        self.populate_serial_ports()
        layout.addWidget(self.serial_port_combo)

        self.buttonCONNECT = QPushButton('CONNECT', self)
        self.buttonCONNECT.clicked.connect(self.connect_serial)
        layout.addWidget(self.buttonCONNECT)

        self.buttonDISCONNECT = QPushButton('DISCONNECT', self)
        self.buttonDISCONNECT.clicked.connect(self.disconnect_serial)
        layout.addWidget(self.buttonDISCONNECT)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        self.labelConnection = QLabel('Disconnected', self)
        self.labelConnection.setStyleSheet("font-size: 18px;")
        hbox.addWidget(self.labelConnection)
        hbox.addStretch(1)

        layout.addLayout(hbox)

        self.buttonON = QPushButton('ON', self)
        self.buttonON.clicked.connect(self.turn_on)
        layout.addWidget(self.buttonON)

        self.buttonOFF = QPushButton('OFF', self)
        self.buttonOFF.clicked.connect(self.turn_off)
        layout.addWidget(self.buttonOFF)

        self.buttonSTATUS = QPushButton('Power Supply Status', self)
        self.buttonSTATUS.clicked.connect(self.status_action)
        layout.addWidget(self.buttonSTATUS)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        self.checkboxSTATUS = QCheckBox('Monitor Power Supply Status', self)
        self.checkboxSTATUS.stateChanged.connect(self.toggle_monitoring)
        hbox.addWidget(self.checkboxSTATUS)
        hbox.addStretch(1)

        layout.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        self.labelStatusONOFF = QLabel('Power Supply Status', self)
        self.labelStatusONOFF.setStyleSheet("font-size: 18px;")
        hbox.addWidget(self.labelStatusONOFF)
        hbox.addStretch(1)

        layout.addLayout(hbox)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        self.labelStatusVA = QLabel('x V x A', self)
        self.labelStatusVA.setStyleSheet("font-size: 18px;")
        hbox.addWidget(self.labelStatusVA)
        hbox.addStretch(1)
        layout.addLayout(hbox)

        self.entry = QLineEdit(self)
        self.entry.setPlaceholderText("13.00")
        self.entry.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.entry)

        self.buttonPROGRAM = QPushButton('Program Voltage', self)
        self.buttonPROGRAM.clicked.connect(self.program_voltage)
        layout.addWidget(self.buttonPROGRAM)

        self.buttonCloseWindow = QPushButton('Close Window', self)
        self.buttonCloseWindow.clicked.connect(self.close)
        layout.addWidget(self.buttonCloseWindow)

        self.setLayout(layout)

    def populate_serial_ports(self):
        resources = self.rm.list_resources()
        for resource in resources:
            self.serial_port_combo.addItem(resource)

    def connect_serial(self):
        selected_port = self.serial_port_combo.currentText()
        try:
            self.instrument = self.rm.open_resource(selected_port)
            self.labelConnection.setText('Connected')
        except pyvisa.VisaIOError as e:
            QMessageBox.critical(self, 'Connection Error', f'Failed to connect to instrument: {e}')

    def disconnect_serial(self):
        if self.instrument:
            self.instrument.close()
            self.labelConnection.setText('Disconnected')
        else:
            QMessageBox.warning(self, 'Connection Warning', 'No active connection to disconnect.')

    def closeEvent(self, event):
        if self.instrument:
            self.instrument.close()
            QMessageBox.information(self, 'Connection', 'Connection has been closed.')
        event.accept()

    def turn_on(self):
        if self.instrument:
            try:
                self.instrument.write("OUTP ON")
                self.labelStatusONOFF.setText('Power Supply ON')
                self.labelStatusONOFF.setStyleSheet("font-size: 18px; color: green;")
            except pyvisa.VisaIOError as e:
                QMessageBox.critical(self, 'Command Error', f'Failed to send command: {e}')
        else:
            QMessageBox.warning(self, 'Connection Warning', 'No active connection.')

    def turn_off(self):
        if self.instrument:
            try:
                self.instrument.write("OUTP OFF")
                self.labelStatusONOFF.setText('Power Supply OFF')
                self.labelStatusONOFF.setStyleSheet("font-size: 18px; color: red;")
            except pyvisa.VisaIOError as e:
                QMessageBox.critical(self, 'Command Error', f'Failed to send command: {e}')
        else:
            QMessageBox.warning(self, 'Connection Warning', 'No active connection.')

    def status_action(self):
        if self.instrument:
            try:
                self.instrument.write("OUTP?")
                response = self.instrument.read()
                state_value = response.strip()

                if state_value == '0':
                    self.labelStatusONOFF.setText('Power Supply OFF')
                    self.labelStatusONOFF.setStyleSheet("font-size: 18px; color: red;")
                elif state_value == '1':
                    self.labelStatusONOFF.setText('Power Supply ON')
                    self.labelStatusONOFF.setStyleSheet("font-size: 18px; color: green;")

                    self.instrument.write("VOLT?")
                    voltage = float(self.instrument.read().strip())

                    self.instrument.write("MEAS:CURR?")
                    current = float(self.instrument.read().strip())

                    self.labelStatusVA.setText(f'{voltage:.2f} V {current:.2f} A')

            except pyvisa.VisaIOError as e:
                QMessageBox.critical(self, 'Command Error', f'Failed to send command: {e}')
        else:
            QMessageBox.warning(self, 'Connection Warning', 'No active connection.')

    def toggle_monitoring(self, state):
        if state == Qt.Checked:
            self.timer.start(1000)
        else:
            self.timer.stop()

    def program_voltage(self):
        if self.instrument:
            try:
                voltage = self.entry.text().strip()
                if voltage:
                    self.instrument.write(f'VOLT {voltage}')
                else:
                    QMessageBox.warning(self, 'Input Error', 'Please enter a valid voltage.')
            except pyvisa.VisaIOError as e:
                QMessageBox.critical(self, 'Command Error', f'Failed to send command: {e}')
        else:
            QMessageBox.warning(self, 'Connection Warning', 'No active connection.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

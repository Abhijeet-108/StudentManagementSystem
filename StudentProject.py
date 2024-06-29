from PyQt6.QtWidgets import QApplication, QPushButton, \
    QLineEdit, QVBoxLayout, QLabel, QWidget, QGridLayout, QComboBox

import sys
from datetime import datetime


class DisCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout()

        distance_label = QLabel("Distance: ")
        self.distance_label_edit = QLineEdit()

        time_label = QLabel("Time (hour): ")
        self.time_label_edit = QLineEdit()

        self.unit_combo = QComboBox()
        self.unit_combo.addItems(['Metric (km)', 'Imperial (miles)'])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.Calculate)

        self.result_label = QLabel("")

        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_label_edit, 0, 1)
        grid.addWidget(self.unit_combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_label_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.result_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def Calculate(self):
        distance = float(self.distance_label_edit.text())
        time = float(self.time_label_edit.text())

        speed = distance / time

        if self.unit_combo.currentText() == 'Metric (km)':
            speed = round(speed, 2)
            unit = 'kmph'
        if self.unit_combo.currentText() == 'Imperial (miles)':
            speed = round(speed * 0.621371, 2)
            unit = 'mph'

        self.result_label.setText(f"Average Speed: {speed} {unit}")


app = QApplication(sys.argv)
avg_calculator = DisCalculator()
avg_calculator.show()
sys.exit(app.exec())

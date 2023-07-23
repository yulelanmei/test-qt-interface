
from PyQt5.QtCore import Qt, QAbstractTableModel, QVariant
from PyQt5.QtWidgets import QVBoxLayout, QWidget
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter
import pandas as pd


class MyPieChart(QWidget):
    def __init__(self, title="动作类别图"):
        super().__init__()
        self.series = QPieSeries()
        self.chart = QChart()
        self.series.setLabelsVisible(True)
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        # self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle(title)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.chart_view)

    
    def update_data(self, data):
        self.series.clear()

        for key, value in data:
            self.series.append(key, int(value))
        
        self.chart_view.chart().update()



class MyTableModel(QAbstractTableModel):
    def __init__(self, data=pd.DataFrame(), headers=[]):
        super().__init__()
        self._data = data
        self._headers = headers

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            return str(self._data.iloc[index.row(), index.column()])
        return QVariant()

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self._headers[section]
        return QVariant()

    def updateData(self, new_data):
        self.beginResetModel()
        self._data = new_data
        self.endResetModel()

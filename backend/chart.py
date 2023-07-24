
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
        self.series.setLabelsPosition(QPieSlice.LabelPosition.LabelOutside)  # 设置标签显示位置。outside表示显示在饼图外围
        # self.series.setLabelsPosition(QPieSlice.LabelInsideHorizontal)
        self.series.setLabelsVisible(True)   # 显示饼图标签
        self.chart.legend().hide()   # 隐藏图例
        self.chart.addSeries(self.series)
        # self.chart.createDefaultAxes()
        # self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle(title)

        # self.chart.legend().setVisible(True)
        # self.chart.legend().setAlignment(Qt.AlignBottom)
        

        # self.chart.legend().show()  # 显示图例
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.Antialiasing)

        # self.layout = QVBoxLayout(self)
        # self.layout.addWidget(self.chart_view)

    
    def update_data(self, data):
        self.series.clear()

        for key, value in data.items():
            self.series.append(key, int(value))
        
        for slice in self.series.slices():
            slice.setLabel(f'{slice.label()} - {100 * slice.percentage():.1f}%')
            slice.setLabelVisible(True)  # 使用clear后，标签显示会失效，需要重新配置
        
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

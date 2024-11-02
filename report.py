# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import requests
import json
import time
import threading
import time
import random
import matplotlib.pyplot as plt
import image
import led
import modetree
import pump
import pandas as pd


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 701)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.lcd_nhietdo = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_kk = QtWidgets.QLCDNumber(self.centralwidget)
        self.data_lock = threading.Lock()
        self.temperature = None
        self.humidity = None
        self.label.setEnabled(True)
        self.lcd_land = QtWidgets.QProgressBar(self.centralwidget)
        self.lcd_land.setMaximum(100)  # Set maximum value to 100%
        self.soil_moisture_data = [random.randint(0, 100) for _ in range(10)]  # Sample data
        self.data_index = 0
        self.update_thread = threading.Thread(target=self.update_soil_moisture)
        self.update_thread.daemon = True
        self.update_thread.start()
        self.gia_tri_do_am = 0  # Khởi tạo thuộc tính gia_tri_do_am với giá trị mặc định
        self.current_moisture = 0  # Khởi tạo thuộc tính current_moisture với giá trị mặc định

        

        self.data_thread = threading.Thread(target=self.get_and_update_data)
        self.data_thread.daemon = True
        self.data_thread.start()
        self.label.setGeometry(QtCore.QRect(280, 30, 571, 121))
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(28)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(570, 0, 241, 181))
        self.label_2.setStyleSheet("image: url(:/myImage/logo.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 181, 131))
        self.label_3.setStyleSheet("image: url(:/myImage/Tomato.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(190, 170, 241, 311))
        self.groupBox.setObjectName("groupBox")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Mincho Demibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.swpump = QtWidgets.QRadioButton(self.groupBox)
        self.swpump.setGeometry(QtCore.QRect(30, 250, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Mincho Demibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.swpump.setFont(font)
        self.swpump.setObjectName("swpump")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(60, 20, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Yu Mincho Demibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(False)
        self.label_4.setTabletTracking(False)
        self.label_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_4.setObjectName("label_4")
        self.swHumidity = QtWidgets.QSlider(self.groupBox)
        self.swHumidity.setGeometry(QtCore.QRect(30, 200, 191, 21))
        self.swHumidity.setOrientation(QtCore.Qt.Horizontal)
        self.swHumidity.setObjectName("swHumidity")
        self.led_on = QtWidgets.QPushButton(self.groupBox)
        self.led_on.setGeometry(QtCore.QRect(20, 50, 91, 41))
        self.led_on.setObjectName("led_on")
        self.led_off = QtWidgets.QPushButton(self.groupBox)
        self.led_off.setGeometry(QtCore.QRect(120, 50, 101, 41))
        self.led_off.setObjectName("led_off")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 160, 141, 121))
        self.label_6.setStyleSheet("image: url(:/myImage/led_off.png);\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(460, 380, 151, 131))
        self.label_7.setStyleSheet("image: url(:/pump/pump_off.png);")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.lcd_nhietdo = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_nhietdo.setGeometry(QtCore.QRect(640, 480, 91, 61))
        self.lcd_nhietdo.setObjectName("lcd_nhietdo")
        self.lcd_kk = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd_kk.setGeometry(QtCore.QRect(740, 480, 91, 61))
        self.lcd_kk.setObjectName("lcd_kk")
        self.lcd_land = QtWidgets.QProgressBar(self.centralwidget)
        self.lcd_land.setGeometry(QtCore.QRect(640, 430, 181, 21))
        self.lcd_land.setProperty("value", 24)
        self.lcd_land.setObjectName("lcd_land")
        self.Lcd_humidity = QtWidgets.QLCDNumber(self.centralwidget)
        self.Lcd_humidity.setGeometry(QtCore.QRect(490, 300, 91, 61))
        self.Lcd_humidity.setObjectName("Lcd_humidity")
        self.clear = QtWidgets.QPushButton(self.centralwidget)
        self.clear.setGeometry(QtCore.QRect(240, 540, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Mincho Demibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(480, 540, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Mincho Demibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(250, 610, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Yu Mincho Demibold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.mode2 = QtWidgets.QPushButton(self.centralwidget)
        self.mode2.setGeometry(QtCore.QRect(40, 268, 107, 48))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.mode2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.mode2.setFont(font)
        self.mode2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mode2.setObjectName("mode2")
        self.mode1 = QtWidgets.QPushButton(self.centralwidget)
        self.mode1.setGeometry(QtCore.QRect(40, 196, 104, 48))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.mode1.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.mode1.setFont(font)
        self.mode1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mode1.setObjectName("mode1")
        self.mode4 = QtWidgets.QPushButton(self.centralwidget)
        self.mode4.setGeometry(QtCore.QRect(40, 412, 108, 48))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.mode4.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.mode4.setFont(font)
        self.mode4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mode4.setObjectName("mode4")
        self.mode3 = QtWidgets.QPushButton(self.centralwidget)
        self.mode3.setGeometry(QtCore.QRect(40, 340, 107, 48))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.mode3.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Sitka Text")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.mode3.setFont(font)
        self.mode3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mode3.setObjectName("mode3")
        # Thêm FigureCanvas vào giao diện
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setGeometry(QtCore.QRect(600, 175, 250, 215))  # Đặt vị trí và kích thước của biểu đồ
        self.canvas.setParent(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        #kiem tra nut button mode
        self.mode1.clicked.connect(self.mode_1)
        self.mode2.clicked.connect(self.mode_2)
        self.mode3.clicked.connect(self.mode_3)
        self.mode4.clicked.connect(self.mode_4)
        #kiem tra button bat tat led
        self.led_on.clicked.connect(self.on_led)
        self.led_off.clicked.connect(self.off_led)
        #kiem tra button bat tat pump
        self.swpump.clicked.connect(self.pump_button_clicked)
        #ket noi thanh truot voi lcd nguong
        self.swHumidity.valueChanged.connect(self.thay_doi_do_am)
        self.clear.clicked.connect(self.clear_all)
        self.exit.clicked.connect(MainWindow.close)
        self.get_data_and_display()
        self.retranslateUi(MainWindow)
        self.data_thread = threading.Thread(target=self.get_and_update_data)
        self.data_thread.daemon = True
        self.data_thread.start()
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "EcoFarm"))
        self.groupBox.setTitle(_translate("MainWindow", "Control Device"))
        self.label_5.setText(_translate("MainWindow", "Control Humidity Threshold"))
        self.swpump.setText(_translate("MainWindow", "ON/OFF PUMP"))
        self.label_4.setText(_translate("MainWindow", "ON/OFF Lamp"))
        self.led_on.setText(_translate("MainWindow", "ON"))
        self.led_off.setText(_translate("MainWindow", "OFF"))
        self.clear.setText(_translate("MainWindow", "Clear"))
        self.exit.setText(_translate("MainWindow", "Exit"))
        self.label_8.setText(_translate("MainWindow", "Design By Code & Craft"))
        self.mode2.setText(_translate("MainWindow", "Mode 2"))
        self.mode1.setText(_translate("MainWindow", "Mode 1"))
        self.mode4.setText(_translate("MainWindow", "Mode 4"))
        self.mode3.setText(_translate("MainWindow", "Mode 3"))
    #set cac mode ung voi tung anh 
    def mode_1(self):
        self.label_3.setStyleSheet("image: url(:/myImage/cabbage);")
        self.gia_tri_do_am = 60  # Đặt giá trị ngưỡng độ ẩm đất
        self.swHumidity.setValue(60)  # Cập nhật giá trị thanh trượt
        self.Lcd_humidity.display(60)  # Hiển thị giá trị trên LCD
        self.check_and_control_pump()  # Kiểm tra và điều khiển pump

    def mode_2(self):
        self.label_3.setStyleSheet("image: url(:/myImage/Tomato);")
        self.gia_tri_do_am = 50  # Đặt giá trị ngưỡng độ ẩm đất
        self.swHumidity.setValue(50)  # Cập nhật giá trị thanh trượt
        self.Lcd_humidity.display(50)  # Hiển thị giá trị trên LCD
        self.check_and_control_pump()  # Kiểm tra và điều khiển pump

    def mode_3(self):
        self.label_3.setStyleSheet("image: url(:/myImage/cucumber);")
        self.gia_tri_do_am = 70  # Đặt giá trị ngưỡng độ ẩm đất
        self.swHumidity.setValue(70)  # Cập nhật giá trị thanh trượt
        self.Lcd_humidity.display(70)  # Hiển thị giá trị trên LCD
        self.check_and_control_pump()  # Kiểm tra và điều khiển pump

    def mode_4(self):
        self.label_3.setStyleSheet("image: url(:/myImage/senda);")
        self.gia_tri_do_am = 30  # Đặt giá trị ngưỡng độ ẩm đất
        self.swHumidity.setValue(30)  # Cập nhật giá trị thanh trượt
        self.Lcd_humidity.display(30)  # Hiển thị giá trị trên LCD
        self.check_and_control_pump()  # Kiểm tra và điều khiển pump

    def check_and_control_pump(self):
        moisture = self.get_current_moisture()  # Lấy giá trị độ ẩm đất hiện tại
        if moisture is not None:
            if moisture < self.gia_tri_do_am:
                self.label_7.setStyleSheet("image: url(:/pump/pump_on);")
                self.swpump.setChecked(True)
            else:
                self.label_7.setStyleSheet("image: url(:/pump/pump_off);")
                self.swpump.setChecked(False)

    def get_current_moisture(self):
        # Trả về giá trị độ ẩm đất hiện tại
        return self.current_moisture

    #set cac mode bat tat led
    def on_led(self):
        self.label_6.setStyleSheet("image: url(:/myImage/led_on);")
    def off_led(self):
        self.label_6.setStyleSheet("image: url(:/myImage/led_off);")
    #set cac mode bat tat pump
    def pump_button_clicked(self):
        if self.swpump.isChecked():
            # Logic to turn pump ON (e.g., calling a function in pump.py)
            self.label_7.setStyleSheet("image: url(:/pump/pump_on);") # Update the image


        else:
            # Logic to turn pump OFF
            self.label_7.setStyleSheet("image: url(:/pump/pump_off);") # Update the image
    #set gia tri thanh truot voi LCD
    def thay_doi_do_am(self):
        gia_tri_do_am = self.swHumidity.value()
        self.Lcd_humidity.display(gia_tri_do_am)

    #set gia tri nhiet do do am
    def get_data_and_display(self):
        API_KEY = 'ad50585e1d724bf8a5003211240211'  # API Key
        CITY = 'Binh Dinh'  # Tên thành phố

        # Tạo URL đúng cách bằng f-string
        api_url =  f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=no"
        try:
            response = requests.get(api_url)
            response.raise_for_status()  # Kiểm tra lỗi
            data = response.json()

            temperature = data.get("current", {}).get("temp_c", None)
            humidity = data.get("current", {}).get("humidity", None)

            if temperature is not None and humidity is not None:
                try:
                    temperature = float(temperature)
                    humidity = float(humidity)
                    self.lcd_nhietdo.display(temperature)
                    self.lcd_kk.display(humidity)
                except ValueError:
                    print("Lỗi chuyển đổi giá trị thành số.")
                    self.lcd_nhietdo.display("Error")
                    self.lcd_kk.display("Error")
            else:
                print("Lỗi: Không tìm thấy dữ liệu nhiệt độ hoặc độ ẩm trong phản hồi API.")
                self.lcd_nhietdo.display("Error")
                self.lcd_kk.display("Error")
        except requests.exceptions.RequestException as e:
            print(f"Lỗi khi truy vấn API: {e}")
            self.lcd_nhietdo.display("Error")
            self.lcd_kk.display("Error")
        except Exception as e:
            print(f"Lỗi không xác định: {e}")
            self.lcd_nhietdo.display("Error")
            self.lcd_kk.display("Error")
    def get_and_update_data(self):
        while True: 
            try:
                temperature, humidity = self.get_weather_data()
                if temperature is not None and humidity is not None:
                    with self.data_lock:
                        self.temperature = temperature
                        self.humidity = humidity
                    self.update_labels()  # Update labels in the main thread
                time.sleep(5)  # Wait for 5 seconds
            except requests.exceptions.RequestException as e:
                print(f"Loi mạng: {e}")
                time.sleep(10) # Delay if network error
            except (KeyError, ValueError) as e:
                print(f"Lỗi dữ liệu: {e}")
                time.sleep(10)


            except Exception as e:
                print(f"Lỗi khác: {e}")
                time.sleep(10)
    def get_weather_data(self):
        # Replace with your API call
        api_key = 'ad50585e1d724bf8a5003211240211'
        city = 'Binh Dinh'
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"  # Example: http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no

        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        temperature = data.get("current", {}).get("temp_c", None)
        humidity = data.get("current", {}).get("humidity", None)

        return temperature, humidity
    def update_labels(self):
        with self.data_lock:
            if self.temperature is not None and self.humidity is not None:
                self.lcd_nhietdo.display(self.temperature)
                self.lcd_kk.display(self.humidity)
                self.plot_data()  # Cập nhật biểu đồ
    def update_soil_moisture(self):
        while True:
            time.sleep(5)  # Wait for 5 seconds
            self.data_index = (self.data_index + 1) % len(self.soil_moisture_data)
            moisture = self.soil_moisture_data[self.data_index]
            self.lcd_land.setValue(moisture)  # Update LCD display
            self.current_moisture = moisture  # Lưu giá trị độ ẩm đất vào thuộc tính
            self.check_and_control_pump()  # Kiểm tra và điều khiển pump
            self.plot_data()  # Cập nhật biểu đồ

    def get_current_data(self):
        key = 'ad50585e1d724bf8a5003211240211'
        City = 'Binh Dinh'
        api_url = f"http://api.weatherapi.com/v1/current.json?key={key}&q={City}&aqi=no"
        
        data_points = []
        for _ in range(3):  # Lấy dữ liệu 3 lần
            response = requests.get(api_url)
            response.raise_for_status()
            data = response.json()
            data_points.append({
                'time': data['current']['last_updated'],
                'temp_c': data['current']['temp_c'],
                'humidity': data['current']['humidity'],
                'moisture': random.randint(30, 40)  # Giả sử bạn có dữ liệu độ ẩm đất
            })
            time.sleep(5)  # Chờ 5 giây trước khi lấy dữ liệu lần tiếp theo

        df = pd.DataFrame(data_points)
        return df

    # Phương thức mới để tắt pump, tắt led và reset gia_tri_do_am về 0
    def clear_all(self):
        # Tắt pump
        self.label_7.setStyleSheet("image: url(:/pump/pump_off);")
        self.swpump.setChecked(False)
        
        # Tắt led
        self.label_6.setStyleSheet("image: url(:/myImage/led_off);")
        
        # Reset gia_tri_do_am về 0
        self.swHumidity.setValue(0)
        self.Lcd_humidity.display(0)
    def plot_data(self):
        # Xóa biểu đồ cũ
        self.figure.clear()

        # Tạo trục mới
        ax = self.figure.add_subplot(111)

        # Dữ liệu để vẽ biểu đồ
        labels = ['Temp (C)', 'Humidity', 'Moisture']
        values = [self.temperature, self.humidity, self.current_moisture]

        # Vẽ biểu đồ cột
        ax.bar(labels, values, color=['blue', 'green', 'red'])

        # Cập nhật canvas
        self.canvas.draw()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

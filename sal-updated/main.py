"""
TODO: 
- system note text area ? 
- creating progress gauge 

"""

# from within module 


# from fake_sensor import cl_startup
import re
from excel_exporter import append_or_create_excel
from ui_sal import Ui_MainWindow
# from fake_sensor import FakeDevice, FakeSensor, FakeGoDirect
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils import Timer 
from ui_sal import Ui_MainWindow
from PySide6.QtWidgets import QLineEdit
from PySide6.QtWidgets import QTextEdit
from PySide6.QtCore import Qt

try: # try importing external packages 
    import subprocess
    import pandas as pd 
    from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressDialog, QSizePolicy, QVBoxLayout
    from PySide6.QtGui import QPalette
    from PySide6.QtCore import QTimer, QCoreApplication
    #from PyQt6.QtCore import QTimer, QTime
    from ui_sal import Ui_MainWindow  # or use QUiLoader if not converted

    import time 
    import scipy
    from godirect import GoDirect
    import shutil 
    from datetime import datetime
    import numpy as np 
    import matplotlib.pyplot as plt
    import inspect 
    
except ImportError as e: # if one of the required packages wasn't found, try to install it 
    print(e) # print error info to the user 
    response = input("Error importing required package. try installing dependencies now? (y/N)") # ask if user wants to install required packages 
    if response.upper() == "Y":
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("installed missing package(s)! please try running the code again now. ")
            sys.exit()
        except Exception as e: 
            print("something went wrong installing dependencies. ")
            print(e)
            sys.exit()
    else: 
        print("okay, exiting now.")
        sys.exit()
def cl_startup(period_ms):
    print("🔍 Attempting to connect to GoDirect sensors...")
    try:
        from godirect import GoDirect
        godirect = GoDirect(use_ble=False)
        device = godirect.get_device()

        if device is not None and device.open():
            device.start(period=period_ms)
            sensors = device.get_enabled_sensors()

            if sensors is None or len(sensors) == 0:
                raise RuntimeError("❌ Sensors could not be enabled.")

            print("✅ Device initialized and started.")
            return device, sensors, godirect
        else:
            raise RuntimeError("❌ Sensor not found or failed to open.")

    except Exception as e:
        print("⚠️ Real sensor connection failed, using fake sensor.")
        print(f"⚠️ Exception: {e}")
        from fake_sensor import FakeDevice, FakeSensor, FakeGoDirect
        return FakeDevice(), [FakeSensor()], FakeGoDirect()


    


class Window(QMainWindow, Ui_MainWindow):

    
    def __init__(self, testing=False):
        """initialise app, calls main function 
        
        Args:
            testing (bool, optional): whether we are in testing mode (no physical system connected) or not. Defaults to False.
        """
        
        self.ion_timer = None
        super().__init__()
        self.setupUi(self) 
        from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
        from matplotlib.figure import Figure
        #grpah
        
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.axes = self.figure.add_subplot(111)


# Add canvas to layout or set its geometry manually
        layout = QVBoxLayout(self.graph_frame)
        layout.setContentsMargins(0, 0, 0, 0)  # Optional: remove padding
        layout.addWidget(self.canvas)



        # --- initialising attributes --- # 
        self.testing = testing # bool whether we are just testing the app or not (set to False when using)

        # system connection 
        self.rawFileName = "rawDataset_SAL.xlsx"
        self.plotMode = "Potential"
        self.ionTableData = {}
        self.measurementData = None   
        self.stddata = None    
        self.rawGraphData = None    

        # calibrations 
        self.time = 0.0
        self.ionUpdateTimer = float('nan')
        self.ion_data = []
        self.rawData = []
        self.period = 0.1
        self.samplingPeriod = 0.2
        self.stabilityError = 0.01 
        self.std10ppm = None    
        self.std100ppm  = None   
        self.std1000ppm  = None    
        self.std5000ppm = None    
        self.STDValues = [[float('nan'), float('nan'), float('nan'), float('nan')], [10, 100, 1000, 5000]]
        self.filteredSTD = None    
        self.coeff = None    
        self.structure = None    
        self.rsquared = None    
        self.ionEquation = float('nan')

        # guideline selection 
        self.index = None    
        self.cl_criteria = None    
        self.guidelineType = None    
        self.mainParameter = None    
        self.subParameter = None    
        self.depth1value  = None   
        self.depth2value   = None  
        self.topDepthSetting = None    
        self.bottomDepthSetting = None    

        # measurement condition 
        self.guideline  = None  
        self.buffer = None    
        self.moisture  = None   
        self.lower_val = 50
        self.higher_val = 5000
        self.baseline = 100
        self.baselineType = None    
        self.liquidSoilFactor = 30/18
        self.liquidCarbonFactor = 20/18
        self.stdPotential = None    
        self.stdCheck = None    
        self.samplePotential  = None   
        self.rawSample  = None   
        self.rawSample_liquid    = None 
        self.rawSample_soil  = None 
        self.sampleConc  = None 

        # data export 
        self.check = True 
        self.date = None  
        self.projectName  = None 
        self.sampleNo  = None 
        self.sampleID  = None 
        self.replication  = None 
        self.stabilizationTime  = None 
        self.filename = None 
        
        print("✅ btn_system_connect found:", self.btn_system_connect is not None)
        print("✅ indicator_connection found:", self.indicator_connection is not None)
        print("✅ txt_system_note found:", self.txt_system_note is not None)
        
        self.main()

    def main(self): 
        """_summary_
        """
        self.btn_system_connect.clicked.connect(self.systemConnectionButtonPushed)
        self.STD10MeasurementButton.clicked.connect(self.STD10MeasurementButtonPushed)
        self.STD100MeasurementButton.clicked.connect(self.STD100MeasurementButtonPushed)
        self.STD1000MeasurementButton.clicked.connect(self.STD1000MeasurementButtonPushed)
        self.STD5000MeasurementButton.clicked.connect(self.STD5000MeasurementButtonPushed)
        self.reset_button_measurement.clicked.connect(self.resetSTDValues)





    def cl_close(self):
        """Disconnects the Go Direct Cl sensor."""
        try:
            self.device.stop()
            self.device.close()
            self.godirect.quit()
        except Exception as e:
            print("No Cl sensor to close or already disconnected.")

    def update_progress(self, value, message):
        self.bar_progress.setValue(value)
        self.lbl_progress_status.setText(message)
        QCoreApplication.processEvents()  # Force UI to update
        
        time.sleep(0.5)  # Give user time to see the update
    
    def cl_read(self):
        """Mimics the MATLAB cl_read() function — reads latest data from sensors."""
        if self.device is None or self.sensors is None:
            print("Device or sensors not initialized")
            return float('nan')

        try:
            if self.device.read():
                values = []
                for sensor in self.sensors:
                    if sensor.values:
                        values.append(sensor.values[0])
                        sensor.clear()
                    if hasattr(sensor, "update_value"):
                        sensor.update_value()
                    else:
                        values.append(float('nan'))
                return values[0] if values else float('nan')  # Assuming first sensor is used
            else:
                return float('nan')
        except Exception as e:
            print("❌ cl_read() error:", e)
            return float('nan')




    def get_sensor_voltage(self):
        return self.cl_read()



    
    def try_sensor_restart(self):
        """Simulate reconnect attempt."""
        self.device, self.sensors, self.godirect = cl_startup(self.period * 1000)
        return self.device is not None and self.sensors is not None


    def startPlotting(self):
        """Start real-time plotting of sensor data"""
        # Stop timer if it's already running
        if self.ion_timer:
            self.ion_timer.stop()
         # 🔐 Safety check
        if self.device is None or self.sensors is None:
            print("❌ Cannot start plotting — device or sensors not set.")
            return
        # Clear previous data
        self.ion_data = []
        self.start_time = time.time()

        # Define the update function
        def update_ion_plot():
            # Simulated reading function (replace with cl_read())
            reading = self.get_sensor_voltage()

            # Detect disconnect
            if np.isnan(reading):
                self.setCircleColour(self.indicator_connection, "red")
                self.refresh_plot_button.setEnabled(False)

                # Attempt reconnect (replace cl_startup logic)
                if self.try_sensor_restart():
                    reading = self.get_sensor_voltage()
                    self.setCircleColour(self.indicator_connection, "green")
                    self.refresh_plot_button.setEnabled(True)
                else:
                    return

            # Time relative to start
            t = time.time() - self.start_time

            # Compute concentration (if equation is set)
            conc = self.ionEquation(reading) if callable(self.ionEquation) else np.nan

            # Save data
            self.ion_data.append([t, reading, conc])

            # Update live fields
            self.potential_input.setPlainText(f"{reading:.3f}")
            self.cl_conc_input.setPlainText(f"{conc:.3f}")
            self.potential_input.setStyleSheet("color: black;")
            self.cl_conc_input.setStyleSheet("color: black;")

            data = np.array(self.ion_data)
            self.axes.clear()
            if self.plotMode == "Potential":
                self.axes.plot(data[:, 0], data[:, 1], 'r')
                self.axes.set_ylabel("Electric Potential (mV)")  # <-- Match MATLAB label
            elif self.plotMode == "Concentration":
                self.axes.plot(data[:, 0], data[:, 2], 'b')
                self.axes.set_ylabel("Concentration (mg/L)")
            self.axes.set_xlabel("Time (s)")
            self.canvas.draw()

        # Start a QTimer for real-time plotting
        self.ion_timer = QTimer()
        self.ion_timer.timeout.connect(update_ion_plot)
        self.ion_timer.start(int(self.period * 1000))  # milliseconds

    def setCircleColour(self, widget, color):

        """Set the background color of a circular indicator."""
        widget.setStyleSheet(f"""
            background-color: {color};
            border-radius: {widget.width()//2}px;
        """)
    
    # Python version of MATLAB's btn_system_connectPushed

    def systemConnectionButtonPushed(self):
        # Deactivate the button
        self.btn_system_connect.setEnabled(False)

        # Reset lamp and note
        self.setCircleColour(self.indicator_connection, "grey")
        self.txt_system_note.clear()
        self.setCircleColour(self.indicator_note_status, "grey")
        self.lbl_system_note.setText("")

        # Looks for old files
        if os.path.isfile(self.rawFileName):
            file_choice = QMessageBox.question(self,
                "Old File Detection",
                f'An older "{self.rawFileName}" file was detected.\n\nDo you want to Delete the file or Backup it or Restore the past session?\n\nYou can also Cancel and move the file before starting a new session.',
                QMessageBox.StandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel),
                QMessageBox.Cancel)

            if file_choice == QMessageBox.Yes:
                confirm = QMessageBox.warning(self,
                    "Confirm Delete",
                    "Do you really want to delete the files?",
                    QMessageBox.Ok | QMessageBox.Cancel)
                if confirm == QMessageBox.Ok:
                    os.remove(self.rawFileName)

            elif file_choice == QMessageBox.Restore:
                dlg = QProgressDialog("Restoring session from past data", None, 0, 0, self)
                dlg.setWindowTitle("Restore Session")
                dlg.setCancelButton(None)
                dlg.setMinimumDuration(0)
                dlg.setValue(0)
                dlg.show()

                self.ion_table_data = pd.read_excel(self.rawFileName, sheet_name="AISCT_SAL", skiprows=1)
                self.table_widget.setDataFrame(self.ion_table_data)

                self.measurement_data = pd.read_excel(self.rawFileName, sheet_name="Measurement Conditions", skiprows=1)
                self.std_data = pd.read_excel(self.rawFileName, sheet_name="STD value", skiprows=1)

                self.std_10.setValue(float(self.std_data.iloc[-1, 5]))
                self.std_100.setValue(float(self.std_data.iloc[-1, 6]))
                self.std_1000.setValue(float(self.std_data.iloc[-1, 7]))
                self.std_5000.setValue(float(self.std_data.iloc[-1, 8]))
                self.btn_curve_fitting.setEnabled(True)

                self.std_values = [
                    float(self.std_10.value()),
                    float(self.std_100.value()),
                    float(self.std_1000.value()),
                    float(self.std_5000.value())
                ]
                self.spinner_sample_no.setValue(len(self.ion_table_data) + 1)
                dlg.close()

            elif file_choice == QMessageBox.Backup:
                dlg = QProgressDialog("Backup the past data", None, 0, 0, self)
                dlg.setWindowTitle("Backup Session")
                dlg.setCancelButton(None)
                dlg.setMinimumDuration(0)
                dlg.setValue(0)
                dlg.show()

                curr_date = f'SAL_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_Old'
                os.makedirs(curr_date, exist_ok=True)
                shutil.move(self.rawFileName, os.path.join(curr_date, os.path.basename(self.rawFileName)))

                os.makedirs("AISCT-DATA", exist_ok=True)
                shutil.move(curr_date, os.path.join("AISCT-DATA", curr_date))
                dlg.close()

        # Python checking
        self.txt_system_note.setVisible(False)
        self.bar_progress.setVisible(True)
        self.lbl_progress_status.setVisible(True)
        self.update_progress(0, "Preparing to setup system")
        QTimer.singleShot(500, lambda: None)
        self.update_progress(20, "Skipping Python check (manual config)")

        
            # I'm on (mac) subprocess.call(["reload.cmd"], shell=True)
        
        self.update_progress(40,"Checking for godirect python module")
        QTimer.singleShot(500, lambda: None)

        _, cmdout = subprocess.getstatusoutput("pip freeze")
        if "godirect==" in cmdout:
            self.lbl_progress_status.setText("godirect Module Detected")
        else:
            self.update_progress(50,"Installing godirect module...")
            _, cmdout = subprocess.getstatusoutput("pip install godirect")
            self.lbl_progress_status.setText(f"Command Output: {cmdout}")
            QTimer.singleShot(1000, lambda: None)
            self.lbl_progress_status.setText("Installed godirect Module!")
       
        self.update_progress(60,"Starting godirect Connection")
        QTimer.singleShot(500, lambda: None)

        self.update_progress(60, "Starting GoDirect connection")
        QTimer.singleShot(500, lambda: None)

        try:
            self.device, self.sensors, self.godirect = cl_startup(self.period * 1000)
            
            print("🧪 self.device:", self.device)
            print("🧪 self.sensors:", self.sensors)

            if self.device is None or self.sensors is None:
                raise RuntimeError("Device or sensors not initialized")

            self.startPlotting()  # Start plotting immediately now that connection is confirmed

        except RuntimeError as e:
            QMessageBox.warning(self, "Sensor Not Found", f"Sensor connection error [code 01.02]\n\n{str(e)}")
            self.txt_system_note.setText(
                """Sensor connection error [code 01.02]
        Unable to collect sensor signal.
        1. Retry to check the sensor connection.
        2. Exit the software and check:
            - Sensor is powered on
            - USB is properly connected
        3. Restart the software and try again.
        !!! Contact technician if issue persists !!!""")
            self.lbl_system_note.setText("ERROR")
            self.setCircleColour(self.indicator_note_status, "red")
            self.setCircleColour(self.indicator_connection, "red")
            self.txt_system_note.setVisible(True)
            self.bar_progress.setVisible(False)
            self.lbl_progress_status.setVisible(False)
            self.btn_system_connect.setEnabled(True)
            return


        self.update_progress(80, "Wrapping up startup processes")
        QTimer.singleShot(500, lambda: None)
        self.update_progress(100, "Finishing...")
        QTimer.singleShot(1000, lambda: None)
        self.txt_system_note.setVisible(True)
        self.bar_progress.setVisible(False)
        self.lbl_progress_status.setVisible(False)


        timer_choice = QMessageBox.question(self, "High Concentration Stabilization",
    "Have you submerged the probe in the 1000 ppm STD solution for 30 minutes yet?\n\nIf not, do so and start the Timer. Otherwise, Skip this step to get started.",
    QMessageBox.Yes | QMessageBox.No)

        if timer_choice == QMessageBox.Yes:
            dlg = QProgressDialog("Preparing to setup timer", "Stop Timer", 0, 1800, self)
            dlg.setWindowTitle("30 Minute Timer")
            dlg.setAutoClose(False)
            dlg.setAutoReset(False)

            for i in range(1800):
                if dlg.wasCanceled():
                    dlg.setLabelText("Stopping Timer...")
                    time.sleep(1)
                    break
                time_r = 1800 - i
                dlg.setValue(i)
                dlg.setLabelText(f"Waiting... ({time_r // 60}:{time_r % 60:02d})")
                QCoreApplication.processEvents()
                time.sleep(1)

            dlg.setValue(1800)
            dlg.setLabelText("Finishing...")
            time.sleep(1)
            dlg.close()


        self.txt_system_note.setText("The AISCT sensor has been successfully connected.")
        self.lbl_system_note.setText("CONNECTED")
        self.setCircleColour(self.indicator_note_status, "green")
        self.setCircleColour(self.indicator_connection, "green")


        self.STD10MeasurementButton.setEnabled(True)
        self.STD100MeasurementButton.setEnabled(True)
        self.STD1000MeasurementButton.setEnabled(True)
        self.STD5000MeasurementButton.setEnabled(True)
        self.calibration_frame.setEnabled(True)

    def ReadyForCalibration(self):
        return all(not np.isnan(val) for val in self.STDValues[0])
   
    def resetSTDValues(self):
        # Clear all STD fields visually
        self.STD10ppmEditField.setPlainText("")
        self.STD100ppmEditField.setPlainText("")
        self.STD1000ppmEditField.setPlainText("")
        self.STD5000ppmEditField.setPlainText("")

        # Reset internal values
        self.STDValues[0] = [np.nan, np.nan, np.nan, np.nan]
        self.STD10ppm = None
        self.STD100ppm = None
        self.STD1000ppm = None
        self.STD5000ppm = None

        # Disable Calibration button and Reset button
        self.CalibrationCurveFittingButton.setEnabled(False)
        self.reset_button_measurement.setEnabled(False)

        # ✅ Visual confirmation
        self.txt_system_note.setVisible(True)
        self.txt_system_note.setText("All STD values have been cleared.")
        self.lbl_system_note.setText("RESET")
        self.indicator_note_status.setStyleSheet("background-color: orange")  # or another color like gray

        # Optional: hide progress
        self.bar_progress.setVisible(False)
        self.lbl_progress_status.setVisible(False)



    def STD10MeasurementButtonPushed(self):
        # Disable Buttons for Update
        self.SetEnableButtonsIon("off")
        self.STD10MeasurementButton.setEnabled(False)
        self.STD100MeasurementButton.setEnabled(False)
        self.STD1000MeasurementButton.setEnabled(False)
        self.STD5000MeasurementButton.setEnabled(False)

        # Confirm 10 ppm solution placement
        std_check = QMessageBox.question(
            self, "STD Check", "Is 10 ppm standard solution correct??",
            QMessageBox.Yes | QMessageBox.No
        )
        if std_check == QMessageBox.No:
            self.txt_system_note.setText("Before collecting the 10 ppm standard solution, place the correct standard solution.")
            self.lbl_system_note.setText("REQUIRED")
            self.indicator_note_status.setStyleSheet("background-color: yellow")
            self.SetEnableButtonsIon("on")
            return
        elif std_check == QMessageBox.Yes:
            time.sleep(1)

        # Sensor Stabilization prompt
        stab_choice = QMessageBox.question(
            self,
            "Sensor Stabilization",
            "Have you stabilized the sensor yet?\nIf not, do so and start the Timer. Otherwise, Skip this step to get started.",
            QMessageBox.Yes | QMessageBox.No
        )
        if stab_choice == QMessageBox.Yes:
            dlg = QProgressDialog("Preparing to setup timer", "Stop Timer", 0, self.StabilizationTimeEditField.value(), self)
            dlg.setWindowTitle("Sensor Stabilization Timer")
            dlg.setWindowModality(Qt.ApplicationModal)
            dlg.setCancelButtonText("Stop Timer")
            dlg.setAutoClose(True)
            dlg.setMinimumDuration(0)

            for i in range(1, self.StabilizationTimeEditField.value() + 1):
                if dlg.wasCanceled():
                    dlg.setLabelText("Stopping Timer...")
                    time.sleep(1)
                    break
                time_r = self.StabilizationTimeEditField.value() - i
                dlg.setValue(i)
                dlg.setLabelText(f"Waiting... ({time_r // 60}:{time_r % 60:02d})")
                QCoreApplication.processEvents()
                time.sleep(1)

            dlg.setValue(self.StabilizationTimeEditField.value())
            dlg.setLabelText("Finishing...")
            time.sleep(1)

        # Start Progress Gauge
        self.txt_system_note.setVisible(False)
        self.bar_progress.setVisible(True)
        self.lbl_progress_status.setVisible(True)
        self.bar_progress.setValue(0)
        self.lbl_progress_status.setText("Preparing to gather 100 data point to stablization")
        time.sleep(0.5)

        # Start plotting
        self.startPlotting()
        self.bar_progress.setValue(20)
        self.lbl_progress_status.setText("Collecting Data...")
        time.sleep(0.5)

        valid_data = []

        timeout = time.time() + 30  # Wait up to 30 seconds max
        while len(valid_data) < 100:
            QCoreApplication.processEvents()
            if self.ion_data:
                # Append new value if it's valid
                latest = self.ion_data[-1]
                if not np.isnan(latest[1]):
                    valid_data.append(latest[1])

                    # Update progress
                    pct = int(60 * len(valid_data) / 100)
                    self.bar_progress.setValue(20 + pct)
                    self.lbl_progress_status.setText(f"Collecting Data...  ({len(valid_data)}/100)")

            if time.time() > timeout:
                QMessageBox.warning(self, "Data Timeout", f"Only collected {len(valid_data)} valid points.")
                self.SetEnableButtonsIon("on")
                return
            time.sleep(self.samplingPeriod / 2)

        self.rawData = np.array(valid_data)

        # Calculate average and error
        avg = np.mean(self.rawData)
        err = np.abs(self.rawData - avg) / avg
        # Stability loop
        while np.all(err > self.stabilityError):
            remeasure = QMessageBox.question(
                self,
                "Sensor Stabilization",
                "Sensor was not stable during the measurement.\nDo you want to remeasure the sample?\nIf you want, click the Remeasurement button. Otherwise, Skip this step to get finished.",
                QMessageBox.Yes | QMessageBox.No
            )
            if remeasure == QMessageBox.No:
                break
            elif remeasure == QMessageBox.Yes:
                dlg = QProgressDialog("Stabilizing the sensor", "Stop Timer", 0, self.StabilizationTimeEditField.value(), self)
                dlg.setWindowTitle("Sensor Stabilization Timer")
                dlg.setCancelButtonText("Stop Timer")
                dlg.setWindowModality(Qt.ApplicationModal)
                dlg.setAutoClose(True)

                for i in range(1, self.StabilizationTimeEditField.value() + 1):
                    if dlg.wasCanceled():
                        dlg.setLabelText("Stopping Timer...")
                        time.sleep(1)
                        break
                    time_r = self.StabilizationTimeEditField.value() - i
                    dlg.setValue(i)
                    dlg.setLabelText(f"Waiting... ({time_r // 60}:{time_r % 60:02d})")
                    QCoreApplication.processEvents()
                    time.sleep(1)

                dlg.setValue(self.StabilizationTimeEditField.value())
                dlg.setLabelText("Finishing...")
                time.sleep(1)

                self.bar_progress.setValue(0)
                self.lbl_progress_status.setText("Preparing to gather 100 data point to stablization")
                time.sleep(0.5)

                self.startPlotting()

                self.bar_progress.setValue(20)
                self.lbl_progress_status.setText("Collecting Data...")
                time.sleep(0.5)

                for i in range(1, 101):
                    self.bar_progress.setValue(20 + int(60 * i / 100))
                    self.lbl_progress_status.setText(f"Collecting Data...  ({i}/100)")
                    time.sleep(self.samplingPeriod)


                
                self.rawData = [row[1] for row in self.ion_data[-100:] if not np.isnan(row[1])]

                # Check if we have enough valid data
                if len(self.rawData) < 100:
                    QMessageBox.warning(self, "Data Error", "Not enough valid data points collected from the sensor.")
                    self.SetEnableButtonsIon("on")
                    return

                # Convert to NumPy array
                self.rawData = np.array(self.rawData)

                # Calculate average and error
                avg = np.mean(self.rawData)
                err = np.abs(self.rawData - avg) / avg

        # Final calculations
        self.bar_progress.setValue(80)
        self.lbl_progress_status.setText("Calculating data for 10 ppm STD solution")
        time.sleep(0.5)

        std_val = np.mean(self.rawData)
        self.STD10ppmEditField.setVisible(True)
        self.STD10ppmEditField.setPlainText(f"{std_val:.2f}")

        self.STD10ppmEditField.setStyleSheet("color: black; background-color: white;")  # <-- Add here

        self.STD10ppm = std_val
        self.STDValues[0][0] = std_val  # 10 ppm slot
        if any(not np.isnan(val) for val in self.STDValues[0]):
            self.reset_button_measurement.setEnabled(True)


        if self.ReadyForCalibration():
            self.CalibrationCurveFittingButton.setEnabled(True)
        else:
            self.CalibrationCurveFittingButton.setEnabled(False)

        self.bar_progress.setValue(100)
        self.lbl_progress_status.setText("Finishing...")
        time.sleep(1)

        # System Note Update
        self.txt_system_note.setVisible(True)
        self.bar_progress.setVisible(False)
        self.lbl_progress_status.setVisible(False)
        self.txt_system_note.setText("The value of 10 ppm standard solution has been successfully collected.")
        self.lbl_system_note.setText("SUCCEED")
        self.indicator_note_status.setStyleSheet("background-color: green")

        # Reactivate all buttons
        self.btn_system_connect.setEnabled(True)
        self.STD10MeasurementButton.setEnabled(True)
        self.STD100MeasurementButton.setEnabled(True)
        self.STD1000MeasurementButton.setEnabled(True)
        self.STD5000MeasurementButton.setEnabled(True)

    def STD100MeasurementButtonPushed(self):
    # Disable Buttons for Update
        self.SetEnableButtonsIon("off")
        self.STD10MeasurementButton.setEnabled(False)
        self.STD100MeasurementButton.setEnabled(False)
        self.STD1000MeasurementButton.setEnabled(False)
        self.STD5000MeasurementButton.setEnabled(False)

        # Confirm correct 100 ppm standard solution
        std_check = QMessageBox.question(
            self,
            "STD Check",
            "Is 100 ppm standard solution correct??",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if std_check == QMessageBox.No:
            self.txt_system_note.setText("Before collecting the 100 ppm standard solution, place the correct standard solution.")
            self.lbl_system_note.setText("REQUIRED")
            self.indicator_note_status.setStyleSheet("background-color: yellow")
            self.SetEnableButtonsIon("on")
            return

        elif std_check == QMessageBox.Yes:
            time.sleep(1)

        # Sensor stabilization prompt
        stability_timer = QMessageBox.question(
            self,
            "Sensor Stabilization",
            "Have you stabilized the sensor yet?\nIf not, do so and start the Timer.\nOtherwise, Skip this step to get started.",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if stability_timer == QMessageBox.Yes:  # Timer
            progress = QProgressDialog("Preparing to setup timer...", "Stop Timer", 0, self.StabilizationTimeEditField.value(), self)
            progress.setWindowTitle("Sensor Stabilization Timer")
            progress.setWindowModality(Qt.WindowModal)
            progress.setMinimumDuration(0)
            for i in range(1, self.StabilizationTimeEditField.value() + 1):
                if progress.wasCanceled():
                    progress.setLabelText("Stopping Timer...")
                    time.sleep(1)
                    break
                time_r = self.StabilizationTimeEditField.value() - i
                progress.setValue(i)
                progress.setLabelText(f"Waiting... ({time_r // 60}:{time_r % 60:02d})")
                time.sleep(1)
            progress.setValue(self.StabilizationTimeEditField.value())
            progress.setLabelText("Finishing...")
            time.sleep(1)
            progress.close()

        # Start progress bar
        self.txt_system_note.setVisible(False)
        self.bar_progress.setVisible(True)
        self.lbl_progress_status.setVisible(True)
        self.bar_progress.setValue(0)
        self.lbl_progress_status.setText("Preparing to gather 100 data point to stabilization")
        time.sleep(0.5)

        self.startPlotting()
        self.bar_progress.setValue(20)
        self.lbl_progress_status.setText("Collecting Data...")
        time.sleep(0.5)

        valid_data = []

        timeout = time.time() + 30  # Wait up to 30 seconds max
        while len(valid_data) < 100:
            QCoreApplication.processEvents()
            if self.ion_data:
                # Append new value if it's valid
                latest = self.ion_data[-1]
                if not np.isnan(latest[1]):
                    valid_data.append(latest[1])

                    # Update progress
                    pct = int(60 * len(valid_data) / 100)
                    self.bar_progress.setValue(20 + pct)
                    self.lbl_progress_status.setText(f"Collecting Data...  ({len(valid_data)}/100)")

            if time.time() > timeout:
                QMessageBox.warning(self, "Data Timeout", f"Only collected {len(valid_data)} valid points.")
                self.SetEnableButtonsIon("on")
                return
            time.sleep(self.samplingPeriod / 2)

        self.rawData = np.array(valid_data)
        avg = np.mean(self.rawData)
        err = np.abs(self.rawData - avg) / avg

        # Stability check

        while np.any(err > self.stabilityError):
            stability_timer = QMessageBox.question(
                self,
                "Sensor Stabilization",
                "Sensor was not stable during the measurement.\nDo you want to remeasure the sample?\nClick Remeasurement or Skip.",
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if stability_timer == QMessageBox.No:
                break
            elif stability_timer == QMessageBox.Yes:
                progress = QProgressDialog("Stabilizing the sensor", "Stop Timer", 0, self.StabilizationTimeEditField.value(), self)
                progress.setWindowTitle("Sensor Stabilization Timer")
                progress.setWindowModality(Qt.WindowModal)
                progress.setMinimumDuration(0)
                for i in range(1, self.StabilizationTimeEditField.value() + 1):
                    if progress.wasCanceled():
                        progress.setLabelText("Stopping Timer...")
                        time.sleep(1)
                        break
                    time_r = self.StabilizationTimeEditField.value() - i
                    progress.setValue(i)
                    progress.setLabelText(f"Waiting... ({time_r // 60}:{time_r % 60:02d})")
                    time.sleep(1)
                progress.setValue(self.StabilizationTimeEditField.value())
                progress.setLabelText("Finishing...")
                time.sleep(1)
                progress.close()

                self.bar_progress.setValue(0)
                self.lbl_progress_status.setText("Preparing to gather 100 data point to stabilization")
                time.sleep(0.5)
                self.startPlotting()
                self.bar_progress.setValue(20)
                self.lbl_progress_status.setText("Collecting Data...")
                time.sleep(0.5)
                for i in range(1, 101):
                    self.bar_progress.setValue(20 + 60 * i / 100)
                    self.lbl_progress_status.setText(f"Collecting Data...  ({i}/100)")
                    time.sleep(self.samplingPeriod)


                self.rawData = [row[1] for row in self.ion_data[-100:]]
                avg = sum(self.rawData) / len(self.rawData)
                err = [abs(val - avg) / avg for val in self.rawData]

        # Final calculations
        self.bar_progress.setValue(80)
        self.lbl_progress_status.setText("Calculating data for 100 ppm STD solution")
        time.sleep(0.5)

        result = sum(self.rawData) / len(self.rawData)
        self.STD100ppmEditField.setVisible(True)
        self.STD100ppmEditField.setPlainText(f"{result:.2f}")
        self.STD100ppmEditField.setStyleSheet("color: black; background-color: white;")
        self.STD100ppm = result
        self.STDValues[0][1] = result
        if any(not np.isnan(val) for val in self.STDValues[0]):
            self.reset_button_measurement.setEnabled(True)


        if self.ReadyForCalibration():
            self.CalibrationCurveFittingButton.setEnabled(True)
        else:
            self.CalibrationCurveFittingButton.setEnabled(False)

        self.bar_progress.setValue(100)
        self.lbl_progress_status.setText("Finishing...")
        time.sleep(1)

        self.txt_system_note.setVisible(True)
        self.bar_progress.setVisible(False)
        self.lbl_progress_status.setVisible(False)
        self.txt_system_note.setText("The value of 100 ppm standard solution has been successfully collected.")
        self.lbl_system_note.setText("SUCCEED")
        self.indicator_note_status.setStyleSheet("background-color: green")

        # Reactivate buttons
        self.btn_system_connect.setEnabled(True)
        self.STD10MeasurementButton.setEnabled(True)
        self.STD100MeasurementButton.setEnabled(True)
        self.STD1000MeasurementButton.setEnabled(True)
        self.STD5000MeasurementButton.setEnabled(True)
    
    def STD1000MeasurementButtonPushed(self):
        # Disable Buttons for Update
        self.SetEnableButtonsIon("off")
        self.STD10MeasurementButton.setEnabled(False)
        self.STD100MeasurementButton.setEnabled(False)
        self.STD1000MeasurementButton.setEnabled(False)
        self.STD5000MeasurementButton.setEnabled(False)

        # Confirm 1000 ppm standard solution
        std_check = QMessageBox.question(self, "STD Check", "Is 1000 ppm standard solution correct??")
        if std_check == QMessageBox.No:
            self.txt_system_note.setText("Before collecting the 1000 ppm standard solution, place the correct standard solution.")
            self.lbl_system_note.setText("REQUIRED")
            self.indicator_note_status.setStyleSheet("background-color: yellow")
            self.SetEnableButtonsIon("on")
            return

        time.sleep(1)

        # Sensor stabilization check
        stability_check = QMessageBox.question(self, "Sensor Stabilization", "Have you stabilized the sensor yet?\nIf not, start the Timer. Otherwise, skip.")
        if stability_check == QMessageBox.Yes:  # Timer
            dlg = QProgressDialog("Preparing to setup timer", "Stop Timer", 0, self.StabilizationTimeEditField.value(), self)
            dlg.setWindowTitle("Sensor Stabilization Timer")
            dlg.setAutoClose(False)
            dlg.setCancelButtonText("Stop Timer")
            dlg.setMinimumDuration(0)

            for i in range(self.StabilizationTimeEditField.value()):
                if dlg.wasCanceled():
                    dlg.setLabelText("Stopping Timer...")
                    time.sleep(1)
                    break
                time_r = self.StabilizationTimeEditField.value() - i
                dlg.setValue(i)
                dlg.setLabelText(f"Waiting... ({time_r // 60}:{time_r % 60:02d})")
                QApplication.processEvents()
                time.sleep(1)

            dlg.setValue(self.StabilizationTimeEditField.value())
            dlg.setLabelText("Finishing...")
            time.sleep(1)
            dlg.close()

        # Show progress
        self.txt_system_note.hide()
        self.bar_progress.setVisible(True)
        self.lbl_progress_status.setVisible(True)
        self.bar_progress.setValue(0)
        self.lbl_progress_status.setText("Preparing to gather 100 data point to stablization")
        time.sleep(0.5)


        # Reset plotting
        self.startPlotting()

        # Collect data
        self.bar_progress.setValue(20)
        self.lbl_progress_status.setText("Collecting Data...")
        time.sleep(0.5)

        valid_data = []

        timeout = time.time() + 30  # Wait up to 30 seconds max
        while len(valid_data) < 100:
            QCoreApplication.processEvents()
            if self.ion_data:
                # Append new value if it's valid
                latest = self.ion_data[-1]
                if not np.isnan(latest[1]):
                    valid_data.append(latest[1])

                    # Update progress
                    pct = int(60 * len(valid_data) / 100)
                    self.bar_progress.setValue(20 + pct)
                    self.lbl_progress_status.setText(f"Collecting Data...  ({len(valid_data)}/100)")

            if time.time() > timeout:
                QMessageBox.warning(self, "Data Timeout", f"Only collected {len(valid_data)} valid points.")
                self.SetEnableButtonsIon("on")
                return
            time.sleep(self.samplingPeriod / 2)

        self.rawData = np.array(valid_data)
        avg = np.mean(self.rawData)
        err = np.abs(self.rawData - avg) / avg

        while np.all(err > self.stabilityError):
            retry = QMessageBox.question(self, "Sensor Stabilization", 
                                        "Sensor was not stable during the measurement.\nDo you want to remeasure the sample?",
                                        QMessageBox.Yes | QMessageBox.No)
            if retry == QMessageBox.No:
                break

            # Retry Stabilization Timer
            dlg = QProgressDialog("Stablizating the sensor", "Stop Timer", 0, self.StabilizationTimeEditField.value(), self)
            dlg.setWindowTitle("Sensor Stabilization Timer")
            dlg.setCancelButtonText("Stop Timer")
            dlg.setMinimumDuration(0)

            for i in range(self.StabilizationTimeEditField.value()):
                if dlg.wasCanceled():
                    dlg.setLabelText("Stopping Timer...")
                    time.sleep(1)
                    break
                time_r = self.StabilizationTimeEditField.value() - i
                dlg.setValue(i)
                dlg.setLabelText(f"Waiting... ({time_r // 60}:{time_r % 60:02d})")
                QApplication.processEvents()
                time.sleep(1)

            dlg.setValue(self.StabilizationTimeEditField.value())
            dlg.setLabelText("Finishing...")
            time.sleep(1)
            dlg.close()

            self.bar_progress.setValue(0)
            self.lbl_progress_status.setText("Preparing to gather 100 data point to stablization")
            time.sleep(0.5)
            self.startPlotting()

            self.bar_progress.setValue(20)
            self.lbl_progress_status.setText("Collecting Data...")
            time.sleep(0.5)

            for i in range(1, 101):
                self.bar_progress.setValue(20 + 60 * i / 100)
                self.lbl_progress_status.setText(f"Collecting Data...  ({i}/100)")
                QApplication.processEvents()
                time.sleep(self.samplingPeriod)


            self.rawData = [row[1] for row in self.ion_data[-100:]]
            avg = np.mean(self.rawData)
            err = np.abs(np.array(self.rawData) - avg) / avg

        # Compute average
        self.bar_progress.setValue(80)
        self.lbl_progress_status.setText("Calculating data for 1000 ppm STD solution")
        time.sleep(0.5)

        result = sum(self.rawData) / len(self.rawData)
        self.STD1000ppmEditField.setVisible(True)
        self.STD1000ppmEditField.setPlainText(f"{result:.2f}")
        self.STD1000ppmEditField.setStyleSheet("color: black; background-color: white;")
        self.STD1000ppm = result
        self.STDValues[0][2] = result
        if any(not np.isnan(val) for val in self.STDValues[0]):
            self.reset_button_measurement.setEnabled(True)


        if self.ReadyForCalibration():
            self.CalibrationCurveFittingButton.setEnabled(True)
        else:
            self.CalibrationCurveFittingButton.setEnabled(False)

        self.bar_progress.setValue(100)
        self.lbl_progress_status.setText("Finishing...")
        time.sleep(1)

        self.txt_system_note.show()
        self.bar_progress.setVisible(False)
        self.lbl_progress_status.setVisible(False)
        self.txt_system_note.setText("The value of 1000 ppm standard solution has been successfully collected.")
        self.lbl_system_note.setText("SUCCEED")
        self.indicator_note_status.setStyleSheet("background-color: green")

        # Reactivate buttons
        self.btn_system_connect.setEnabled(True)
        self.STD10MeasurementButton.setEnabled(True)
        self.STD100MeasurementButton.setEnabled(True)
        self.STD1000MeasurementButton.setEnabled(True)
        self.STD5000MeasurementButton.setEnabled(True)

    def STD5000MeasurementButtonPushed(self):
        # Disable buttons for update
        self.SetEnableButtonsIon("off")
        self.STD10MeasurementButton.setEnabled(False)
        self.STD100MeasurementButton.setEnabled(False)
        self.STD1000MeasurementButton.setEnabled(False)
        self.STD5000MeasurementButton.setEnabled(False)

        # Check standard placement
        std_check = QMessageBox.question(
            self, "STD Check", "Is 5000 ppm standard solution correct??",
            QMessageBox.Yes | QMessageBox.No
        )

        if std_check == QMessageBox.No:
            self.txt_system_note.setText("Before collecting the 5000 ppm standard solution, place the correct standard solution.")
            self.lbl_system_note.setText("REQUIRED")
            self.indicator_note_status.setStyleSheet("background-color: yellow")
            self.SetEnableButtonsIon("on")
            return
        elif std_check == QMessageBox.Yes:
            QTimer.singleShot(1000, lambda: None)

        # Stability prompt
        stab_confirm = QMessageBox.question(
            self, "Sensor Stabilization",
            "Have you stabilized the sensor yet?\nIf not, do so and start the Timer. Otherwise, Skip this step to get started.",
            QMessageBox.Yes | QMessageBox.No
        )

        if stab_confirm == QMessageBox.Yes:
            dlg = QProgressDialog("Preparing to setup timer", "Stop Timer", 0, self.StabilizationTimeEditField.value(), self)
            dlg.setWindowTitle("Sensor Stabilization Timer")
            dlg.setWindowModality(Qt.ApplicationModal)
            dlg.setAutoClose(True)
            dlg.setMinimumDuration(0)

            for i in range(1, self.StabilizationTimeEditField.value() + 1):
                if dlg.wasCanceled():
                    dlg.setLabelText("Stopping Timer...")
                    time.sleep(1)
                    break
                time_r = self.StabilizationTimeEditField.value() - i
                dlg.setValue(i)
                dlg.setLabelText(f"Waiting... ({time_r//60}:{time_r%60:02d})")
                QCoreApplication.processEvents()
                time.sleep(1)

            dlg.setValue(self.StabilizationTimeEditField.value())
            dlg.setLabelText("Finishing...")
            time.sleep(1)

        # Start progress
        self.txt_system_note.setVisible(False)
        self.bar_progress.setVisible(True)
        self.lbl_progress_status.setVisible(True)
        self.bar_progress.setValue(0)
        self.lbl_progress_status.setText("Preparing to gather 100 data point to stablization")
        time.sleep(0.5)

        self.startPlotting()
        self.bar_progress.setValue(20)
        self.lbl_progress_status.setText("Collecting Data...")
        time.sleep(0.5)

        valid_data = []

        timeout = time.time() + 30  # Wait up to 30 seconds max
        while len(valid_data) < 100:
            QCoreApplication.processEvents()
            if self.ion_data:
                # Append new value if it's valid
                latest = self.ion_data[-1]
                if not np.isnan(latest[1]):
                    valid_data.append(latest[1])

                    # Update progress
                    pct = int(60 * len(valid_data) / 100)
                    self.bar_progress.setValue(20 + pct)
                    self.lbl_progress_status.setText(f"Collecting Data...  ({len(valid_data)}/100)")

            if time.time() > timeout:
                QMessageBox.warning(self, "Data Timeout", f"Only collected {len(valid_data)} valid points.")
                self.SetEnableButtonsIon("on")
                return
            time.sleep(self.samplingPeriod / 2)

        self.rawData = np.array(valid_data)
        avg = np.mean(self.rawData)
        err = np.abs(self.rawData - avg) / avg

        while np.all(err > self.stabilityError):
            stab_confirm = QMessageBox.question(
                self, "Sensor Stabilization",
                "Sensor was not stable during the measurement.\nDo you want to remeasure the sample?\nClick Remeasurement to repeat or Skip to finish.",
                QMessageBox.Yes | QMessageBox.No
            )
            if stab_confirm == QMessageBox.No:
                break

            dlg = QProgressDialog("Stabilizing the sensor", "Stop Timer", 0, self.StabilizationTimeEditField.value(), self)
            dlg.setWindowTitle("Sensor Stabilization Timer")
            dlg.setWindowModality(Qt.ApplicationModal)
            dlg.setAutoClose(True)

            for i in range(1, self.StabilizationTimeEditField.value() + 1):
                if dlg.wasCanceled():
                    dlg.setLabelText("Stopping Timer...")
                    time.sleep(1)
                    break
                time_r = self.StabilizationTimeEditField.value() - i
                dlg.setValue(i)
                dlg.setLabelText(f"Waiting... ({time_r//60}:{time_r%60:02d})")
                QCoreApplication.processEvents()
                time.sleep(1)

            dlg.setValue(self.StabilizationTimeEditField.value())
            dlg.setLabelText("Finishing...")
            time.sleep(1)

            self.bar_progress.setValue(0)
            self.lbl_progress_status.setText("Preparing to gather 100 data point to stablization")
            time.sleep(0.5)

            self.startPlotting()
            self.bar_progress.setValue(20)
            self.lbl_progress_status.setText("Collecting Data...")
            time.sleep(0.5)

            for i in range(1, 101):
                self.bar_progress.setValue(20 + int(60 * i / 100))
                self.lbl_progress_status.setText(f"Collecting Data... ({i}/100)")
                time.sleep(self.samplingPeriod)


            self.rawData = [row[1] for row in self.ion_data[-100:]]
            avg = np.mean(self.rawData)
            err = np.abs(self.rawData - avg) / avg

        self.bar_progress.setValue(80)
        self.lbl_progress_status.setText("Calculating data for 5000 ppm STD solution")
        time.sleep(0.5)

        result = sum(self.rawData) / len(self.rawData)
        self.STD5000ppmEditField.setVisible(True)
        self.STD5000ppmEditField.setPlainText(f"{result:.2f}")
        self.STD5000ppmEditField.setStyleSheet("color: black; background-color: white;")
        self.STD5000ppm = result
        self.STDValues[0][3] = result
        if any(not np.isnan(val) for val in self.STDValues[0]):
            self.reset_button_measurement.setEnabled(True)



        if self.ReadyForCalibration():
            self.CalibrationCurveFittingButton.setEnabled(True)
        else:
            self.CalibrationCurveFittingButton.setEnabled(False)

        self.bar_progress.setValue(100)
        self.lbl_progress_status.setText("Finishing...")
        time.sleep(1)

        self.txt_system_note.setVisible(True)
        self.bar_progress.setVisible(False)
        self.lbl_progress_status.setVisible(False)
        self.txt_system_note.setText("The value of 5000 ppm standard solution has been successfully collected.")
        self.lbl_system_note.setText("SUCCEED")
        self.indicator_note_status.setStyleSheet("background-color: green")

        self.btn_system_connect.setEnabled(True)
        self.STD10MeasurementButton.setEnabled(True)
        self.STD100MeasurementButton.setEnabled(True)
        self.STD1000MeasurementButton.setEnabled(True)
        self.STD5000MeasurementButton.setEnabled(True)

    def calibrationApplyButtonPushed(self):
        # Disable measurement buttons
        self.std10_measurement_button.setEnabled(False)
        self.std100_measurement_button.setEnabled(False)
        self.std1000_measurement_button.setEnabled(False)
        self.std5000_measurement_button.setEnabled(False)
        # Disable curve fitting and apply buttons
        self.calibration_curve_button.setEnabled(False)
        self.calibration_apply_button.setEnabled(False)
        # Enable reset button
        self.calibration_reset_button.setEnabled(True)
        # Restart live plotting
        self.startPlotting()
        # Re-enable core UI
        self.setEnableButtons(True)
    
    def SetEnableButtonsIon(self, mode):
        state = mode.lower() == "on"
        self.STD10MeasurementButton.setEnabled(state)
        self.STD100MeasurementButton.setEnabled(state)
        self.STD1000MeasurementButton.setEnabled(state)
        self.STD5000MeasurementButton.setEnabled(state)

    def calibrationResetButtonPushed(self):
        # Disable measurement buttons
        self.std10_measurement_button.setEnabled(True)
        self.std100_measurement_button.setEnabled(True)
        self.std1000_measurement_button.setEnabled(True)
        self.std5000_measurement_button.setEnabled(True)
        # Disable curve fitting and apply buttons
        self.calibration_curve_button.setEnabled(True)
        self.calibration_apply_button.setEnabled(True)
        # Enable reset button
        self.calibration_reset_button.setEnabled(False)
   
    def sampleTypeDropdownValueChanged(self):
        selected = self.sample_type_dropdown.currentText()

        if selected == "Soil":
            self.cl_conc_extract_label.setText("Cl Conc. in Extract (mg/L)")
            self.cl_conc_soil_label.setText("Cl Conc. in Soil (mg/kg)")
            self.cl_criteria_label.setText("Cl Criteria (mg/kg)")
        elif selected == "Ground Water":
            self.cl_conc_extract_label.setText("Cl Conc. in GW (mg/L)")
            self.cl_conc_soil_label.setText("Cl Conc. in GW (mg/L)")
            self.cl_criteria_label.setText("Cl Criteria (mg/L)")
        elif selected == "Surface Water":
            self.cl_conc_extract_label.setText("Cl Conc. in SW (mg/L)")
            self.cl_conc_soil_label.setText("Cl Conc. in SW (mg/L)")
            self.cl_criteria_label.setText("Cl Criteria (mg/L)")
    
    def autoSampleNamingCheckboxValueChanged(self):
        value_of_auto_sample_naming = self.auto_sample_naming_checkbox.isChecked()

        if value_of_auto_sample_naming:
            self.auto_sample_naming_panel.setVisible(True)
            self.sample_id_edit_field.setVisible(False)
            self.sample_id_edit_field_label.setVisible(False)
        else:
            self.auto_sample_naming_panel.setVisible(False)
            self.sample_id_edit_field.setVisible(True)
            self.sample_id_edit_field_label.setVisible(True)

            if self.multiple_guideline_checkbox.isChecked():
                QMessageBox.information(
                    self,
                    "Auto Sample Naming",
                    "The multiple guideline is using.\nYou must use the auto sample naming function."
                )
                # Revert to auto naming
                self.auto_sample_naming_checkbox.setChecked(True)
                self.auto_sample_naming_panel.setVisible(True)
                self.sample_id_edit_field.setVisible(False)
                self.sample_id_edit_field_label.setVisible(False)

    def topDepthFieldValueChanged(self):
        self.topDepthSetting = self.top_depth_field.value()
        self.bottomDepthSetting = self.bottom_depth_field.value()
        self.depth1value = self.top_depth1.value()
        self.depth2value = self.top_depth2.value()

        if self.topDepthSetting >= self.bottomDepthSetting:
            QMessageBox.warning(
                self,
                "Sample Depth Setting",
                "The bottom depth is lower than or equal to the top depth.\nThe bottom depth must be higher than top depth.",
                QMessageBox.Ok
            )
            self.bottom_depth_field.setValue(self.topDepthSetting + 0.1)

        if not self.rd_zone_checkbox.isChecked():
            if self.topDepthSetting < self.depth1value:
                self.cl_criteria_field.setText(str(self.cl_zone1.value()))
            else:
                self.cl_criteria_field.setText(str(self.cl_zone2.value()))
        else:
            if self.topDepthSetting < self.depth1value:
                self.cl_criteria_field.setText(str(self.cl_zone1.value()))
            elif self.topDepthSetting < self.depth2value:
                self.cl_criteria_field.setText(str(self.cl_zone2.value()))
            else:
                self.cl_criteria_field.setText(str(self.cl_zone3.value()))
    
    def bottomDepthFieldValueChanged(self):
        self.topDepthSetting = self.top_depth_field.value()
        self.bottomDepthSetting = self.bottom_depth_field.value()

        if self.topDepthSetting >= self.bottomDepthSetting:
            QMessageBox.warning(
                self,
                "Sample Depth Setting",
                "The bottom depth is lower than or equal to the top depth.\nThe bottom depth must be higher than the top depth.",
            QMessageBox.Ok
            )
            self.bottom_depth_field.setValue(self.topDepthSetting + 0.1)

    def singleGuidelineCheckboxChanged(self):
        value_of_single_guideline = self.single_guideline_checkbox.isChecked()

        if value_of_single_guideline:
            self.multiple_guideline_checkbox.setChecked(False)
            self.single_guideline_panel.setVisible(True)
            self.multi_guideline_panel.setVisible(False)
            self.apply_button.setVisible(False)
            self.reset_button.setVisible(False)

            self.top_depth_field.setValue(0)
            self.bottom_depth_field.setValue(0.1)

            # Set the default criteria
            self.guideline_type_dropdown.setCurrentText("Manual")
            self.main_parameter_field.setVisible(True)
            self.sub_parameter_field.setVisible(True)
            self.main_parameter_field.setText("N/A")
            self.sub_parameter_field.setText("N/A")

            self.chloride_mgkg_field.setValue(100)
            self.cl_criteria_field.setText(str(100))

        else:
            self.multiple_guideline_checkbox.setChecked(True)
            self.single_guideline_panel.setVisible(False)
            self.multi_guideline_panel.setVisible(True)
            self.apply_button.setVisible(True)
            self.reset_button.setVisible(True)
            self.apply_button.setEnabled(True)
            self.reset_button.setEnabled(False)
            self.auto_sample_naming_checkbox.setChecked(True)
            self.auto_sample_naming_panel.setVisible(True)
            self.sample_id_field.setVisible(False)
            self.sample_id_label.setVisible(False)
            self.top_depth1.setEnabled(True)
            self.top_depth2.setEnabled(True)
            self.cl_zone1.setEnabled(True)
            self.cl_zone2.setEnabled(True)
            self.cl_zone3.setEnabled(True)
            self.rd_zone_checkbox.setEnabled(True)

            self.top_depth_field.setValue(0)
            self.bottom_depth_field.setValue(0.1)

            self.top_depth1.setValue(0)
            self.top_depth2.setValue(0)
            self.cl_zone1.setValue(0)
            self.cl_zone2.setValue(0)
            self.cl_zone3.setValue(0)
            self.rd_zone_checkbox.setChecked(False)
            self.top_depth2.setVisible(False)
            self.cl_zone3.setVisible(False)
            self.st_zone_label.setText("1st Zone")
            self.nd_zone_label.setText("2nd Zone")
            self.rd_zone_label.setText("3rd Zone")
            self.cl_criteria_field.setText(str(self.cl_zone1.value()))

    def chlorideMgkgFieldValueChanged(self):
        value_of_single_chloride_criteria = self.chloride_mgkg_field.value()
        self.cl_criteria_field.setText(str(value_of_single_chloride_criteria))

    def multipleGuidelineCheckboxValueChanged(self):
        value_of_multiple_guideline = self.multiple_guideline_checkbox.isChecked()

        if value_of_multiple_guideline:
            self.single_guideline_checkbox.setChecked(False)
            self.single_guideline_panel.setVisible(False)
            self.multi_guideline_panel.setVisible(True)
            self.auto_sample_naming_checkbox.setChecked(True)
            self.auto_sample_naming_panel.setVisible(True)
            self.sample_id_edit_field.setVisible(False)
            self.sample_id_edit_field_label.setVisible(False)
            self.apply_button.setVisible(True)
            self.reset_button.setVisible(True)
            self.apply_button.setEnabled(True)
            self.reset_button.setEnabled(False)
            self.top_depth1.setEnabled(True)
            self.top_depth2.setEnabled(True)
            self.cl_zone1.setEnabled(True)
            self.cl_zone2.setEnabled(True)
            self.cl_zone3.setEnabled(True)
            self.rd_zone_checkbox.setEnabled(True)

            self.top_depth_field.setValue(0)
            self.bottom_depth_field.setValue(0.1)

            self.top_depth1.setValue(0)
            self.top_depth2.setValue(0)
            self.cl_zone1.setValue(0)
            self.cl_zone2.setValue(0)
            self.cl_zone3.setValue(0)
            self.rd_zone_checkbox.setChecked(False)
            self.top_depth2.setVisible(False)
            self.cl_zone3.setVisible(False)

            self.st_zone_label.setText("1st Zone")
            self.nd_zone_label.setText("2nd Zone")
            self.rd_zone_label.setText("3rd Zone")
            self.cl_criteria_field.setText(str(self.cl_zone1.value()))
        else:
            self.single_guideline_checkbox.setChecked(True)
            self.single_guideline_panel.setVisible(True)
            self.multi_guideline_panel.setVisible(False)
            self.apply_button.setVisible(False)
            self.reset_button.setVisible(False)

            self.top_depth_field.setValue(0)
            self.bottom_depth_field.setValue(0.1)

            self.guideline_type_dropdown.setCurrentText("Manual")
            self.main_parameter_edit_field.setVisible(True)
            self.sub_parameter_edit_field.setVisible(True)
            self.main_parameter_edit_field.setText("N/A")
            self.sub_parameter_edit_field.setText("N/A")

            self.chloride_mgkg_field.setValue(100)
            self.cl_criteria_field.setText(str(100))
    
    def applyButtonPushed(self):
        self.depth1value = self.top_depth1.value()
        self.depth2value = self.top_depth2.value()

        if self.rd_zone_checkbox.isChecked():
            if self.depth2value <= self.depth1value:
                QMessageBox.warning(
                    self,
                    "3rd Zone Depth Setting",
                    "The 3rd zone is lower than or equal to the 2nd zone.\nThe 3rd zone depth must be higher than 2nd zone.",
                    QMessageBox.Ok
                )
                return

        if not self.rd_zone_checkbox.isChecked():
            self.st_zone_label.setText(f"1st Zone (0-{self.depth1value})")
            self.nd_zone_label.setText(f"2nd Zone ({self.depth1value}~)")
        else:
            self.st_zone_label.setText(f"1st Zone (0-{self.depth1value})")
            self.nd_zone_label.setText(f"2nd Zone ({self.depth1value}-{self.depth2value})")
            self.rd_zone_label.setText(f"3rd Zone ({self.depth2value}~)")

        self.cl_criteria_field.setText(str(self.cl_zone1.value()))
        self.top_depth_field.setValue(0)
        self.bottom_depth_field.setValue(0.1)

        # Deactivate editing
        self.reset_button.setEnabled(True)
        self.top_depth1.setEnabled(False)
        self.top_depth2.setEnabled(False)
        self.cl_zone1.setEnabled(False)
        self.cl_zone2.setEnabled(False)
        self.cl_zone3.setEnabled(False)
        self.rd_zone_checkbox.setEnabled(False)
        self.apply_button.setEnabled(False)
    
    def resetButtonPushed(self):
        # Activate the edit
        self.reset_button.setEnabled(False)
        self.top_depth1.setEnabled(True)
        self.top_depth2.setEnabled(True)
        self.cl_zone1.setEnabled(True)
        self.cl_zone2.setEnabled(True)
        self.cl_zone3.setEnabled(True)
        self.rd_zone_checkbox.setEnabled(True)
        self.apply_button.setEnabled(True)

        self.top_depth_field.setValue(0)
        self.bottom_depth_field.setValue(0.1)
    
    def rdZoneCheckboxValueChanged(self):
        rd_zone_active = self.rd_zone_checkbox.isChecked()

        if rd_zone_active:
            self.top_depth2.setVisible(True)
            self.cl_zone3.setVisible(True)
        else:
            self.top_depth2.setVisible(False)
            self.cl_zone3.setVisible(False)
            self.st_zone_label.setText("1st Zone")
            self.nd_zone_label.setText("2nd Zone")
            self.rd_zone_label.setText("3rd Zone")
    
    def advancedParametersCheckboxValueChanged(self):
        value_of_advanced_parameters = self.advanced_parameters_checkbox.isChecked()

        if value_of_advanced_parameters:
            self.advanced_parameters_panel.setVisible(True)
        else:
            self.advanced_parameters_panel.setVisible(False)

    def graphSelectorDropdownValueChanged(self):
        value_of_graph_selector = self.graph_selector_dropdown.currentText()

        if value_of_graph_selector == "Potential":
            self.ISEUIAxes.set_ylabel("Electric Potential (mV)")
            self.plotMode = "Potential"
        elif value_of_graph_selector == "Concentration":
            if not callable(self.ionEquation):
                self.graph_selector_dropdown.setCurrentText("Potential")
                QMessageBox.warning(
                    self,
                    "Error",
                    "Concentration graph unavailable until calibration is complete.",
                    QMessageBox.Ok
                )
                return
            self.ISEUIAxes.set_ylabel("Concentration (mg/L)")
            self.plotMode = "Concentration"
    
    def refreshPlotButtonPushed(self):
        self.startPlotting()
   
    def STDcheckButtonPushed(self):
            # Disable buttons
        self.setEnableButtons(False)

        # Confirm standard placement
        confirm = QMessageBox.question(
            self, "STD Check", "Is 100 ppm standard solution correct?",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm == QMessageBox.No:
            self.system_note_sign_label.setText("REQUIRED")
            self.setCircleColour(self.system_note_circle, "yellow")
            self.showMessage("STD Check", "Before collecting the 100 ppm standard solution, place the correct standard solution.")
            self.setEnableButtons(True)
            return

        # Sensor stabilization dialog
        stab_dialog = QMessageBox(self)
        stab_dialog.setWindowTitle("Sensor Stabilization")
        stab_dialog.setText("Have you stabilized the sensor yet?\n\nStart the timer if not.")
        timer_btn = stab_dialog.addButton("Timer", QMessageBox.AcceptRole)
        skip_btn = stab_dialog.addButton("Skip", QMessageBox.RejectRole)
        stab_dialog.exec()

        if stab_dialog.clickedButton() == timer_btn:
            duration = self.stabilizationTime if self.stabilizationTime else 60
            self.timer_dialog = Timer(duration)
            self.timer_dialog.canceled.connect(self.timer_dialog.cancelEvent)

        # Start plot & progress
        self.startPlotting()
        self.ion_data = []
        progress = QProgressDialog("Collecting 100 data points...", "Cancel", 0, 100, self)
        progress.setWindowTitle("Sensor Data Collection")
        progress.setValue(0)
        progress.setAutoClose(True)
        progress.setAutoReset(True)
        progress.setCancelButton(None)
        progress.show()

        for i in range(100):
            QApplication.processEvents()
            if progress.wasCanceled():
                break
            self.ion_data.append([time.time(), self.cl_read(), np.nan])
            progress.setValue(i + 1)
            time.sleep(self.samplingPeriod)

        raw = np.array([x[1] for x in self.ion_data[-100:]])
        avg = np.mean(raw)
        err = np.abs(raw - avg) / avg

        # Retry loop if unstable
        while np.any(err > self.stabilityError):
            retry = QMessageBox.question(
                self, "Sensor Stabilization",
                "Sensor was not stable during measurement.\nRetry or skip?",
                QMessageBox.Retry | QMessageBox.Ignore
            )
            if retry == QMessageBox.Ignore:
                break
            else:
                self.startPlotting()
                self.ion_data = []
                for i in range(100):
                    QApplication.processEvents()
                    self.ion_data.append([time.time(), self.cl_read(), np.nan])
                    time.sleep(self.samplingPeriod)
                raw = np.array([x[1] for x in self.ion_data[-100:]])
                avg = np.mean(raw)
                err = np.abs(raw - avg) / avg

        self.stdPotential = avg
        if callable(self.ionEquation):
            self.stdCheck = self.ionEquation(avg)
        else:
            self.showMessage("Error", "Calibration equation not available.")
            self.setEnableButtons(True)
            return

        # Validation of STD result
        if self.stdCheck < 80 or self.stdCheck > 120:
            code = "02.01" if self.stdCheck < 80 else "02.02"
            self.showMessage("STD Check Error", f"STD check error [code {code}]\nSTD value out of expected range.\nReset calibration and retry.")
            self.system_note_sign_label.setText("REQUIRED")
            self.setCircleColour(self.system_note_circle, "yellow")
            self.setEnableButtons(True)
            return

        # If valid
        self.system_note_sign_label.setText("NORMAL")
        self.setCircleColour(self.system_note_circle, "green")
        self.showMessage("STD Check", f"The standard solution is valid.\nCurrent STD value: {self.stdCheck:.2f}")

        # Re-enable buttons
        self.setEnableButtons(True)
                   
    def measurementButtonPushed(self):
        # Disable all relevant buttons
        self.setEnableButtons(False)

        # Reset status indicators
        self.system_note_text_area.setText("")
        self.setCircleColour(self.system_note_circle, "grey")
        self.system_note_sign_label.setText("")
        self.average_potential_field.setValue(0)
        self.cl_conc_extract_field.setText("")
        self.cl_conc_sample_field.setText("")
        self.setCircleColour(self.chloride_measurement_circle, "grey")

        # Auto-fill N/A where fields are empty
        if not self.borehole_id_field.text():
            self.borehole_id_field.setText("N/A")
        if not self.borehole_no_field.text():
            self.borehole_no_field.setText("N/A")
        if not self.sample_id_edit_field.text():
            self.sample_id_edit_field.setText("N/A")

        borehole_id = self.borehole_id_field.text()
        borehole_no = self.borehole_no_field.text()
        top_depth = str(self.top_depth_field.value())
        bottom_depth = str(self.bottom_depth_field.value())

        if self.auto_sample_naming_checkbox.isChecked():
            self.sampleID = f"{borehole_id}-{borehole_no}_{top_depth}-{bottom_depth}"
        else:
            self.sampleID = self.sample_id_edit_field.text()

        # Confirm sample info
        confirm = QMessageBox.question(
            self, "Sample Information Check",
            f"Confirm the below information.\n\nSample ID: {self.sampleID}\n\nAre the sample ID accurate?\nDid you place sensor probe into this sample properly?",
            QMessageBox.Yes | QMessageBox.Retry
        )
        if confirm == QMessageBox.Retry:
            self.setEnableButtons(True)
            return

        # Measurement conditions
        self.guideline = float(self.cl_criteria_field.text())
        self.date = datetime.now()
        self.projectName = self.project_name_field.text()
        self.sampleNo = self.sample_no_spinner.value()
        self.replication = self.replication_spinner.value()
        self.moisture = self.moisture_dropdown.currentText()
        self.buffer = self.buffer_dropdown.currentText()
        self.guidelineType = self.guideline_type_dropdown.currentText()
        self.stabilizationTime = self.stabilization_time_field.value()
        self.baselineType = self.baseline_dropdown.currentText()

        self.mainParameter = (self.main_parameter_field.text()
                            if self.guidelineType == "Manual"
                            else self.main_parameter_dropdown.currentText())
        self.subParameter = (self.sub_parameter_field.text()
                            if self.guidelineType == "Manual"
                            else self.sub_parameter_dropdown.currentText())

        # Convert moisture category to numeric
        moisture_map = {
            "Dry (0)": 0.0,
            "Damp (1-25)": 0.125,
            "Moist (26-50)": 0.375,
            "Wet (51-75)": 0.625,
            "Saturated (76-99)": 0.875
        }
        self.moisture = moisture_map.get(self.moisture, 0.0)

        buffer_map = {
            "20": 0.2,
            "30": 0.3,
            "40": 0.4,
            "50": 0.5
        }
        self.buffer = buffer_map.get(self.buffer, 0.2)

        self.cl_criteria = self.guideline
        if self.cl_criteria < 50:
            reset = QMessageBox.question(
                self, "Guideline Double-Check",
                "The current criteria (<50 mg/kg) is outside the working range. Reset?",
                QMessageBox.Yes | QMessageBox.Ignore
            )
            if reset == QMessageBox.Yes:
                self.setEnableButtons(True)
                return

        # Stabilization Timer
        stab_choice = QMessageBox.question(
            self, "Sensor Stabilization",
            "Have you stabilized the sensor yet?\nStart the Timer if not.",
            QMessageBox.Yes | QMessageBox.Ignore
        )
        if stab_choice == QMessageBox.Yes:
            self.timer_dialog = Timer(self.stabilizationTime)
            self.timer_dialog.canceled.connect(self.timer_dialog.cancelEvent)

        # Progress gauge
        self.system_note_text_area.setVisible(False)
        self.progress_gauge.setVisible(True)
        self.progress_gauge_label.setVisible(True)
        self.progress_gauge.setValue(0)
        self.progress_gauge_label.setText("Preparing to gather 100 data point to stabilization")
        QApplication.processEvents()
        time.sleep(0.5)

        # Start new plot
        self.startPlotting()

        self.progress_gauge.setValue(20)
        self.progress_gauge_label.setText("Collecting Data...")
        QApplication.processEvents()
        time.sleep(0.5)

        self.rawData = []
        for i in range(100):
            self.rawData.append(self.cl_read())
            self.progress_gauge.setValue(20 + 60 * i // 100)
            self.progress_gauge_label.setText(f"Collecting Data... ({i+1}/100)")
            QApplication.processEvents()
            time.sleep(self.samplingPeriod)

        self.rawData = np.array(self.rawData[-100:])
        avg = np.mean(self.rawData)
        err = np.abs(self.rawData - avg) / avg

        while np.any(err > self.stabilityError):
            retry = QMessageBox.question(
                self, "Sensor Stability",
                "Sensor not stable.\nRemeasure or skip?",
                QMessageBox.Retry | QMessageBox.Ignore
            )
            if retry == QMessageBox.Ignore:
                break
            else:
                self.timer_dialog = Timer(self.stabilizationTime)
                self.timer_dialog.canceled.connect(self.timer_dialog.cancelEvent)
                self.startPlotting()
                self.rawData = []
                for i in range(100):
                    self.rawData.append(self.cl_read())
                    time.sleep(self.samplingPeriod)
                self.rawData = np.array(self.rawData[-100:])
                avg = np.mean(self.rawData)
                err = np.abs(self.rawData - avg) / avg

        self.samplePotential = avg
        self.rawSample = self.ionEquation(avg)
        self.progress_gauge.setValue(80)
        self.progress_gauge_label.setText("Calculating sample concentration")
        QApplication.processEvents()
        time.sleep(0.5)

        self.average_potential_field.setValue(self.samplePotential)

        if self.sample_type_dropdown.currentText() == "Soil":
            self.rawSample_liquid = (self.rawSample - self.baseline) if self.baselineType == "Yes" else self.rawSample
            if self.rawSample_liquid <= self.lower_val:
                self.cl_conc_extract_field.setText("N.D.")
            else:
                self.cl_conc_extract_field.setText(str(self.rawSample_liquid))

            self.rawSample_soil = self.rawSample_liquid * self.liquidSoilFactor / (1 - self.moisture)
        else:
            self.rawSample_liquid = (self.rawSample - (self.baseline / 2)) * 2 if self.baselineType == "Yes" else self.rawSample
            if self.rawSample_liquid <= self.lower_val:
                self.cl_conc_extract_field.setText("N.D.")
            else:
                self.cl_conc_extract_field.setText(str(self.rawSample_liquid))
            self.rawSample_soil = self.rawSample_liquid

        value = self.rawSample_soil
        if value <= self.lower_val:
            result = "N.D."; color = "green"
        elif value <= self.guideline * (1 - self.buffer):
            result = "M.C."; color = "green"
        elif value <= self.guideline:
            result = "M.C. (within Buffer)"; color = "yellow"
        elif value <= self.guideline * (1 + self.buffer):
            result = f"{value:.2f} (within Buffer)"; color = "#EDA500"
        elif value <= self.higher_val:
            result = f"{value:.2f}"; color = "red"
        else:
            result = "Exceeded Max."; color = "red"

        self.cl_conc_sample_field.setText(result)
        self.setCircleColour(self.chloride_measurement_circle, color)

        # Save to table and Excel — implementation would follow same as your exportToExcel() or related
        # Code for storing/appending to dataframes or writing to Excel goes here...

        self.progress_gauge.setValue(100)
        self.progress_gauge_label.setText("Finishing")
        QApplication.processEvents()
        time.sleep(1)

        self.system_note_text_area.setVisible(True)
        self.progress_gauge.setVisible(False)
        self.progress_gauge_label.setVisible(False)
        self.system_note_text_area.setText("The standard solution value is within the normal range.")
        self.system_note_sign_label.setText("NORMAL")
        self.setCircleColour(self.system_note_circle, "green")

        self.setEnableButtons(True)
    
    # Sample Data Row
        sampledata = [
            self.check,
            self.date,
            self.projectName,
            self.sampleNo,
            self.sampleID,
            self.replication,
            result,
            self.rawSample_liquid,
            self.samplePotential,
            self.cl_criteria
        ]
        header_sample = [
            "Check", "Date", "ProjectName", "SampleNo", "SampleID", "Replication",
            "Chloride in Soil (mg/kg)", "Chloride in Liquid (mg/L)", "Potential (mV)", "Cl Criteria (mg/kg)"
        ]

        # Measurement Conditions
        measurementdata = [
            self.date,
            self.projectName,
            self.sampleNo,
            self.sampleID,
            self.replication,
            self.guidelineType,
            self.mainParameter,
            self.subParameter,
            self.cl_criteria,
            self.moisture,
            self.buffer,
            self.stabilizationTime,
            self.baselineType
        ]
        header_measurement = [
            "Date", "ProjectName", "SampleNo", "SampleID", "Replication", "Guideline Type",
            "MainParameter", "SubParameter", "Cl Criteria (mg/kg)", "Moisture(%)", "Buffer Range (%)",
            "Stabilization Time (s)", "Baseline"
        ]

        # STD Values
        stddata = [
            self.date,
            self.projectName,
            self.sampleNo,
            self.sampleID,
            self.replication,
            self.STDValues[0][0],
            self.STDValues[0][1],
            self.STDValues[0][2],
            self.STDValues[0][3],
            self.STDcheck,
            self.stdpotential
        ]
        header_std = [
            "Date", "ProjectName", "SampleNo", "SampleID", "Replication",
            "STD 10ppm", "STD 100ppm", "STD 1000ppm", "STD 5000ppm",
            "STD check (100ppm)", "STD check potential (mV)"
        ]
        append_or_create_excel(self.rawFileName, "AISCT_SAL", [sampledata], header_sample)
        append_or_create_excel(self.rawFileName, "Measurement Conditions", [measurementdata], header_measurement)
        append_or_create_excel(self.rawFileName, "STD value", [stddata], header_std)

    def recalculateButtonPushed(self):
        self.setEnableButtons(False)

        # Reset
        self.system_note_text_area.setText("")
        self.setCircleColour(self.system_note_circle, "grey")
        self.system_note_sign_label.setText("")
        self.average_potential_field.setValue(0)
        self.cl_conc_extract_field.setText("")
        self.cl_conc_sample_field.setText("")
        self.setCircleColour(self.chloride_measurement_circle, "grey")

        # Fill defaults if missing
        if not self.borehole_id_field.text():
            self.borehole_id_field.setText("N/A")
        if not self.borehole_no_field.text():
            self.borehole_no_field.setText("N/A")
        if not self.sample_id_edit_field.text():
            self.sample_id_edit_field.setText("N/A")

        borehole_id = self.borehole_id_field.text()
        borehole_no = self.borehole_no_field.text()
        top_depth = str(self.top_depth_field.value())
        bottom_depth = str(self.bottom_depth_field.value())

        if self.auto_sample_naming_checkbox.isChecked():
            self.sampleID = f"{borehole_id}-{borehole_no}_{top_depth}-{bottom_depth}"
        else:
            self.sampleID = self.sample_id_edit_field.text()

        confirm = QMessageBox.question(self, "Sample Info", f"Sample ID: {self.sampleID}\nConfirm this info?", QMessageBox.Yes | QMessageBox.Retry)
        if confirm == QMessageBox.Retry:
            self.setEnableButtons(True)
            return

        self.date = datetime.now()
        self.projectName = self.project_name_field.text()
        self.sampleNo = self.sample_no_spinner.value()
        self.replication = self.replication_spinner.value()
        self.moisture = self.moisture_dropdown.currentText()
        self.buffer = self.buffer_dropdown.currentText()
        self.guidelineType = self.guideline_type_dropdown.currentText()
        self.stabilizationTime = self.stabilization_time_field.value()
        self.baselineType = self.baseline_dropdown.currentText()

        self.mainParameter = self.main_parameter_field.text() if self.guidelineType == "Manual" else self.main_parameter_dropdown.currentText()
        self.subParameter = self.sub_parameter_field.text() if self.guidelineType == "Manual" else self.sub_parameter_dropdown.currentText()

        moisture_map = {"Dry (0)": 0, "Damp (1-25)": 0.125, "Moist (26-50)": 0.375, "Wet (51-75)": 0.625, "Saturated (76-99)": 0.875}
        buffer_map = {"20%": 0.2, "30%": 0.3, "40%": 0.4, "50%": 0.5}
        self.moisture = moisture_map.get(self.moisture, 0.0)
        self.buffer = buffer_map.get(self.buffer, 0.2)

        self.cl_criteria = float(self.cl_criteria_field.text())
        if self.cl_criteria < 50:
            choice = QMessageBox.question(self, "Guideline Warning", "Current criteria < 50. Reset?", QMessageBox.Yes | QMessageBox.Ignore)
            if choice == QMessageBox.Yes:
                self.setEnableButtons(True)
                return

        self.rawSample = self.ionEquation(self.samplePotential)
        self.average_potential_field.setValue(self.samplePotential)

        if self.sample_type_dropdown.currentText() == "Soil":
            self.rawSample_liquid = (self.rawSample - self.baseline) if self.baselineType == "Yes" else self.rawSample
        else:
            self.rawSample_liquid = (self.rawSample - self.baseline/2)*2 if self.baselineType == "Yes" else self.rawSample

        if self.rawSample_liquid <= self.lower_val:
            self.cl_conc_extract_field.setText("N.D.")
        else:
            self.cl_conc_extract_field.setText(str(self.rawSample_liquid))

        self.rawSample_soil = self.rawSample_liquid * self.liquidSoilFactor / (1 - self.moisture) if self.sample_type_dropdown.currentText() == "Soil" else self.rawSample_liquid

        value = self.rawSample_soil
        if value <= self.lower_val:
            result = "N.D."; color = "green"
        elif value <= self.cl_criteria * (1 - self.buffer):
            result = "M.C."; color = "green"
        elif value <= self.cl_criteria:
            result = "M.C. (within Buffer)"; color = "yellow"
        elif value <= self.cl_criteria * (1 + self.buffer):
            result = f"{value:.2f} (within Buffer)"; color = "#EDA500"
        elif value <= self.higher_val:
            result = f"{value:.2f}"; color = "red"
        else:
            result = "Exceeded Max."; color = "red"

        self.cl_conc_sample_field.setText(result)
        self.setCircleColour(self.chloride_measurement_circle, color)

        sampledata = [self.check, self.date, self.projectName, self.sampleNo, self.sampleID, self.replication, result, self.rawSample_liquid, self.samplePotential, self.cl_criteria]
        measurementdata = [self.date, self.projectName, self.sampleNo, self.sampleID, self.replication, self.guidelineType, self.mainParameter, self.subParameter, self.cl_criteria, self.moisture, self.buffer, self.stabilizationTime, self.baselineType]
        stddata = [self.date, self.projectName, self.sampleNo, self.sampleID, self.replication, self.STDValues[0][0], self.STDValues[0][1], self.STDValues[0][2], self.STDValues[0][3], self.STDcheck, self.stdpotential]

        header_sample = ["Check", "Date", "ProjectName", "SampleNo", "SampleID", "Replication", "Chloride in Soil (mg/kg)", "Chloride in Liquid (mg/L)", "Potential (mV)", "Cl Criteria (mg/kg)"]
        header_measurement = ["Date", "ProjectName", "SampleNo", "SampleID", "Replication", "Guideline Type", "MainParameter", "SubParameter", "Cl Criteria (mg/kg)", "Moisture(%)", "Buffer Range (%)", "Stabilization Time (s)", "Baseline"]
        header_std = ["Date", "ProjectName", "SampleNo", "SampleID", "Replication", "STD 10ppm", "STD 100ppm", "STD 1000ppm", "STD 5000ppm", "STD check (100ppm)", "STD check potential (mV)"]

        append_or_create_excel(self.rawFileName, "AISCT_SAL", [sampledata], header_sample)
        append_or_create_excel(self.rawFileName, "Measurement Conditions", [measurementdata], header_measurement)
        append_or_create_excel(self.rawFileName, "STD value", [stddata], header_std)

        self.system_note_text_area.setVisible(True)
        self.system_note_text_area.setText("The standard solution value is within the normal range.")
        self.system_note_sign_label.setText("NORMAL")
        self.setCircleColour(self.system_note_circle, "green")
        self.setEnableButtons(True)

    def autoFileNamingCheckBoxValueChanged(self):
        is_checked = self.auto_file_naming_checkbox.isChecked()
        self.file_name_field.setEnabled(not is_checked)
        self.file_name_label.setEnabled(not is_checked)
        self.file_name_field.setText("")
   
    def exportDataButtonPushed(self):
        self.setEnableButtons(False)

        self.system_note_text_area.setText("")
        self.setCircleColour(self.system_note_circle, "grey")
        self.system_note_sign_label.setText("")

        self.ionTableData = self.table_model.getDataAsDataFrame()

        header_sample = ["Date", "ProjectName", "SampleNo", "SampleID", "Replication",
                        "Chloride in Soil (mg/kg)", "Chlorie in Liquid (mg/L)", "Potential (mV)", "Cl Criteria (mg/kg)"]
        header_measurement = ["Date", "ProjectName", "SampleNo", "SampleID", "Replication",
                            "Guideline Type", "MainParameter", "SubParameter", "Cl Criteria (mg/kg)",
                            "Moisture(%)", "Buffer Range (%)", "Stabilization Time (s)", "Baseline"]
        header_std = ["Date", "ProjectName", "SampleNo", "SampleID", "Replication",
                    "STD 10ppm", "STD 100ppm", "STD 1000ppm", "STD 5000ppm",
                    "STD check (100ppm)", "STD check potential (mV)"]

        if not self.auto_file_naming_checkbox.isChecked():
            self.filename = self.file_name_field.text() + ".xlsx"
        else:
            self.filename = f"{self.project_name_field.text()}_SAL_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx"

        df_sample = self.ionTableData.copy()
        df_sample = df_sample[df_sample.iloc[:, 0] != 0]
        df_sample = df_sample.iloc[:, 1:]

        if df_sample.empty:
            QMessageBox.warning(self, "Export Warning", "No rows selected for export.")
            return

        df_sample.columns = header_sample
        df_measurement = pd.DataFrame(self.measurementData, columns=header_measurement)
        df_std = pd.DataFrame(self.stdData, columns=header_std)

        df_measurement = df_measurement.loc[df_sample.index]
        df_std = df_std.loc[df_sample.index]

        with pd.ExcelWriter(self.filename, engine='openpyxl') as writer:
            df_sample.to_excel(writer, sheet_name='AISCT_SAL', index=False)
            df_measurement.to_excel(writer, sheet_name='Measurement Conditions', index=False)
            df_std.to_excel(writer, sheet_name='STD value', index=False)

        self.system_note_text_area.setText("The predicted values have been successfully exported.")
        self.system_note_sign_label.setText("EXPORTED")
        self.setCircleColour(self.system_note_circle, "green")

        self.setEnableButtons(True)

    def AISCTSALUI_Close(self):
        if os.path.isfile(self.rawFileName):
            choice = QMessageBox.question(
                self, "File Back-up",
                "Do you want to Backup the files or Delete them?\nYou can also Cancel and move the file yourself.",
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )

            if choice == QMessageBox.No:  # Delete
                confirm = QMessageBox.warning(self, "Confirm Delete", "Do you really want to delete the files?",
                                            QMessageBox.Ok | QMessageBox.Cancel)
                if confirm == QMessageBox.Ok:
                    os.remove(self.rawFileName)
                    try:
                        os.remove(self.filename)
                    except:
                        pass
            elif choice == QMessageBox.Yes:  # Backup
                f = QProgressDialog("Backup the data", None, 0, 0, self)
                f.setWindowTitle("Backup Session")
                f.setCancelButton(None)
                f.setWindowModality(Qt.WindowModal)
                f.show()
                QApplication.processEvents()

                currDate = f"{self.project_name_field.text()}_SAL_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"
                os.makedirs(currDate, exist_ok=True)
                shutil.move(self.rawFileName, os.path.join(currDate, os.path.basename(self.rawFileName)))
                try:
                    shutil.move(self.filename, os.path.join(currDate, os.path.basename(self.filename)))
                except:
                    pass

                os.makedirs("AISCT-DATA", exist_ok=True)
                shutil.move(currDate, os.path.join("AISCT-DATA", currDate))
                f.close()

        close_confirm = QMessageBox.question(
        self, "Close request", "Do you want to close the app?",
        QMessageBox.Ok | QMessageBox.Cancel
    )
        if close_confirm == QMessageBox.Ok:
            try:
                self.cl_close()
            except:
                pass
            self.close()  # ✅ only closes when OK is clicked
        else:
            pass  # Do nothing, stay open
        
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            "Close request",
            "Do you want to close the app?",
            QMessageBox.Ok | QMessageBox.Cancel
        )

        if reply == QMessageBox.Ok:
            try:
                self.cl_close()
            except Exception:
                pass
            event.accept()
        else:
            event.ignore()  # <-- This prevents the window from closing

if __name__ == "__main__": 
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()

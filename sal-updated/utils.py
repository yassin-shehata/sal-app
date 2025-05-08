import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QProgressDialog
from PySide6.QtCore import QTimer


class Timer(QProgressDialog):
    def __init__(self, duration,title="Light Warmup Timer"):
        """initialises timer window

        Args:
            duration (int): timer duration in seconds
            title (str, optional): timer window title. Defaults to "Light Warmup Timer".
        """
        super().__init__()

        # initialising attributes 
        self.duration = duration
        self.remaining = duration
        self.timer = QTimer(self)

        # setting dialog properties
        self.setWindowTitle(title)
        self.setLabelText(f"{self.remaining//60:02}:{self.remaining%60:02}")
        self.setRange(0, self.duration) # set range of timer 
        self.setAutoReset(0)
        self.setValue(0) # set initial value to zero 
        self.setCancelButtonText("Cancel Timer") # make cancel button 
        self.timer.timeout.connect(self.update_timer) # connect the timer to the update function 
        self.timer.start(1000)  # start the timer with the interval to update every second (in ms)
        self.show() # show the dialog 

    def update_timer(self):
        """updates the timer 
        """
        self.setValue(self.value() + 1) # increment the value 
        self.remaining = self.duration - self.value() # update the remaining time value 
        self.setLabelText(f"{self.remaining//60:02}:{self.remaining%60:02}") # update the displayed text 

        if self.value() >= self.duration: # checks if the timer has completed 
            self.timer.stop() # stop the timer 
            self.setLabelText("Light source was warmed up!") # change the text 
            self.setCancelButtonText("Continue") # change the button from cancel to continue 
            

    def cancelEvent(self):
        """handles user closing the window
        """
        if self.remaining > 0: # if the user is closing the timer early, 
            # create a popup dialog asking the user to confirm stopping the timer early 
            dialog = QMessageBox(self) 
            dialog.setWindowTitle("Confirm Cancel") 
            dialog.setText("The timer has not completed yet. Are you sure you want to cancel early?")
            dialog.setIcon(QMessageBox.Question)
            yes_button = dialog.addButton("Yes", QMessageBox.YesRole)
            no_button = dialog.addButton("No", QMessageBox.NoRole)
            dialog.exec()
            
            if dialog.clickedButton() == yes_button: 
                self.timer.stop()
                self.done(1)  
        else: # otherwise, the close event was called when the timer completed normally
            self.done(1) # so just close the window. 


# --- testing code --- # 
if __name__ == "__main__":
    class MainWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("timer test ")
            self.setGeometry(100, 100, 300, 200)
            self.main()

        def showMessage(self, title, message):
            """
            displays dialog for showing an error message 
            """
            msg = QMessageBox(self)
            if title == "Error":
                msg.setIcon(QMessageBox.Critical)
            else: 
                msg.setIcon(QMessageBox.Information)

            msg.setText(message)
            msg.setWindowTitle(title)
            msg.exec()

        def main(self):
            dialog = QMessageBox(self)
            dialog.setWindowTitle("Light Source Stabilization")
            dialog.setText("You must warm up the light for 30 minutes.\nIf you already did it, skip this step to get started.")
            start_button = dialog.addButton("Warm Up", QMessageBox.AcceptRole)
            skip_button = dialog.addButton("Skip", QMessageBox.RejectRole)

            dialog.exec()

            if dialog.clickedButton() == start_button:  
                self.timer_dialog = Timer(10)  
                self.timer_dialog.canceled.connect(self.timer_dialog.cancelEvent) 

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

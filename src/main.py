from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QSystemTrayIcon

# Create the icon
icon = QIcon("icon.ico")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

app.exec()

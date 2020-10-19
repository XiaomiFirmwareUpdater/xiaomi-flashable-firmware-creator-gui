"""Custom QMessageBox classes."""
from pathlib import Path

from PyQt5.QtWidgets import QMessageBox, QPushButton


class MessageBox(QMessageBox):
    """Custom QMessage class to allow setting localized buttons text."""

    def __init__(self, title, message, ok_text, box_type="Warning", parent=None):
        self.title = title
        self.message = message
        self.ok_text = ok_text
        self.box_type = box_type
        super().__init__(parent)
        if self.box_type == "Warning":
            self.setIcon(QMessageBox.Warning)
        elif self.box_type == "Critical":
            self.setIcon(QMessageBox.Critical)
        else:
            self.setIcon(QMessageBox.Information)
        self.setWindowTitle(self.title)
        self.setText(self.message)
        self.setModal(True)
        self.set_buttons()

    def set_buttons(self):
        """Set QMessageBox buttons."""
        self.setStandardButtons(QMessageBox.Ok)
        ok_button = self.button(QMessageBox.Ok)
        ok_button.setText(self.ok_text)


class OutputMessageBox(MessageBox):
    """Custom MessageBox with multiple buttons."""

    filepath: Path
    browse_text: str

    def __init__(self, title, message, ok_text, browse_text, filepath, box_type="", parent=None):
        self.browse_text = browse_text
        self.filepath = filepath
        super().__init__(title, message, ok_text, box_type, parent)

    def set_buttons(self):
        """Set QMessageBox buttons."""
        self.addButton(QPushButton(self.ok_text), QMessageBox.YesRole)
        self.addButton(QPushButton(self.browse_text), QMessageBox.ActionRole)

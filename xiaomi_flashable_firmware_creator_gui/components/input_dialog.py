"""Custom QInputDialog class"""
from PyQt5.QtWidgets import QInputDialog


class InputDialog(QInputDialog):
    """Custom QInputDialog class to allow setting localized buttons text."""

    def __init__(self, title, message, ok_text, cancel_text, parent=None):
        super().__init__(parent)
        self.setInputMode(QInputDialog.TextInput)
        self.setFixedSize(300, 100)
        self.setOption(QInputDialog.UsePlainTextEditForTextInput)
        self.setWindowTitle(title)
        self.setLabelText(message)
        self.setOkButtonText(ok_text)
        self.setCancelButtonText(cancel_text)
        self.setModal(True)

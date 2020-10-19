"""Drag and Drop space class."""

from pathlib import Path

from PyQt5.QtCore import QMimeDatabase
from PyQt5.QtWidgets import QGroupBox


class DropSpace(QGroupBox):
    """
    A modified Groupbox to allow drag and drop.
    """
    status_box = None
    parent = None
    _translate = None

    def __init__(self, parent, status_box, tr):
        """Initialize the DropSpace class."""
        super().__init__(parent)
        DropSpace.status_box = status_box
        DropSpace.parent = parent
        DropSpace._translate = tr
        self.setAcceptDrops(True)

    @classmethod
    def dragEnterEvent(cls, file):
        """
        Override default dragEnterEvent
        Allows dragging zip files only
        """
        file_type = QMimeDatabase().mimeTypeForFile(
            file.mimeData().urls()[0].toLocalFile()).name()
        if file_type == 'application/zip':
            file.accept()
        else:
            file.ignore()

    @classmethod
    def dropEvent(cls, file):
        """
        Override default dropEvent.
        Update selected filename.
        """
        filepath = file.mimeData().urls()[0].toLocalFile()
        cls.filepath = Path(filepath).absolute()
        cls.filename = cls.filepath.name
        cls.status_box.setText(cls._translate("Status Box", f"File {cls.filename} is selected"))

"""Layout altering functions."""
from PyQt5.QtCore import Qt


def adjust_layout_direction(self, lang: str):
    """
    Change Layout Direction based on languages
    """
    rtl_languages = ['ar', 'az', 'dv', 'fa', 'he', 'ur']
    if lang in rtl_languages:
        self.setLayoutDirection(Qt.RightToLeft)
        self.statusBar().setLayoutDirection(Qt.RightToLeft)
    else:
        self.setLayoutDirection(Qt.LeftToRight)
        self.statusBar().setLayoutDirection(Qt.LeftToRight)

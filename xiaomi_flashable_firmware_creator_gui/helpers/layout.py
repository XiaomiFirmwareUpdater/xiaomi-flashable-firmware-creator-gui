"""Layout altering functions."""
from PyQt5.QtCore import Qt


def adjust_layout_direction(window, lang: str):
    """
    Change Layout Direction based on languages
    """
    rtl_languages = ['ar', 'az', 'dv', 'fa', 'he', 'ur']
    if lang in rtl_languages:
        window.setLayoutDirection(Qt.RightToLeft)
        if hasattr(window, 'statusBar'):
            window.statusBar().setLayoutDirection(Qt.RightToLeft)
    else:
        window.setLayoutDirection(Qt.LeftToRight)
        if hasattr(window, 'statusBar'):
            window.statusBar().setLayoutDirection(Qt.LeftToRight)

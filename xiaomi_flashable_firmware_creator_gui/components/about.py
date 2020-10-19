# -*- coding: utf-8 -*-
"""Xiaomi Flashable Firmware Creator GUI - About Class"""
from PyQt5.QtCore import QSize, QRect, Qt, QMetaObject, QCoreApplication
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QDialog, QLabel, QTabWidget, QWidget, \
    QTextBrowser, QDialogButtonBox, QSizePolicy, QApplication

from xiaomi_flashable_firmware_creator_gui.helpers.layout import adjust_layout_direction


class AboutBox(QDialog):
    """
    About Window class
    """

    def __init__(self, lang):
        super().__init__()
        self.lang = lang
        self._translate = QCoreApplication.translate
        # Init
        self.label_header = QLabel(self)
        self.tabs = QTabWidget(self)
        self.tab_about = QWidget()
        self.tab_sources = QWidget()
        self.tab_authors = QWidget()
        self.tab_thanks = QWidget()
        self.sources_text = QTextBrowser(self.tab_sources)
        self.about_text = QTextBrowser(self.tab_about)
        self.authors_text = QTextBrowser(self.tab_authors)
        self.thanks_text = QTextBrowser(self.tab_thanks)
        self.button_box = QDialogButtonBox(self)

    def setup_ui(self):
        """
        setup window ui
        """
        self.setObjectName("about_box")
        self.resize(600, 345)
        size_policy = QSizePolicy(
            QSizePolicy.Fixed, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(QSize(600, 345))
        self.setMaximumSize(QSize(600, 345))
        icon = QIcon()
        icon.addPixmap(QPixmap("icon.png"), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        self.label_header.setGeometry(QRect(0, 0, 571, 41))
        size_policy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.label_header.sizePolicy().hasHeightForWidth())
        self.label_header.setSizePolicy(size_policy)
        font = QFont()
        font.setPointSize(14)
        self.label_header.setFont(font)
        self.label_header.setIndent(10)
        self.label_header.setObjectName("label_header")
        self.tabs.setGeometry(QRect(10, 40, 580, 250))
        self.tabs.setObjectName("tabs")
        self.tab_about.setObjectName("tab_about")
        self.about_text.setGeometry(QRect(0, 0, 580, 220))
        size_policy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.about_text.sizePolicy().hasHeightForWidth())
        self.about_text.setSizePolicy(size_policy)
        self.about_text.setAcceptDrops(False)
        self.about_text.setReadOnly(True)
        self.about_text.setOpenExternalLinks(True)
        self.about_text.setObjectName("about_text")
        self.tabs.addTab(self.tab_about, "")
        self.tab_sources.setObjectName("tab_sources")
        self.sources_text.setGeometry(QRect(0, 0, 580, 220))
        size_policy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sources_text.sizePolicy().hasHeightForWidth())
        self.sources_text.setSizePolicy(size_policy)
        self.sources_text.setAcceptDrops(False)
        self.sources_text.setReadOnly(True)
        self.sources_text.setOpenExternalLinks(True)
        self.sources_text.setObjectName("sources_text")
        self.tabs.addTab(self.tab_sources, "")
        self.tab_authors.setObjectName("tab_authors")
        self.authors_text.setGeometry(QRect(0, 0, 580, 220))
        size_policy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.authors_text.sizePolicy().hasHeightForWidth())
        self.authors_text.setSizePolicy(size_policy)
        self.authors_text.setAcceptDrops(False)
        self.authors_text.setReadOnly(True)
        self.authors_text.setOpenExternalLinks(True)
        self.authors_text.setObjectName("authors_text")
        self.tabs.addTab(self.tab_authors, "")
        self.tab_thanks.setObjectName("tab_thanks")
        self.thanks_text.setGeometry(QRect(0, 0, 580, 220))
        size_policy = QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.thanks_text.sizePolicy().hasHeightForWidth())
        self.thanks_text.setSizePolicy(size_policy)
        self.thanks_text.setAcceptDrops(False)
        self.thanks_text.setReadOnly(True)
        self.thanks_text.setOpenExternalLinks(True)
        self.thanks_text.setObjectName("thanks_text")
        self.tabs.addTab(self.tab_thanks, "")
        self.button_box.setGeometry(QRect(490, 300, 104, 37))
        self.button_box.setOrientation(Qt.Horizontal)
        self.button_box.setStandardButtons(
            QDialogButtonBox.Cancel)
        cancel_button = self.button_box.button(QDialogButtonBox.Cancel)
        cancel_button.setText(self._translate("About Box", "Cancel"))
        self.button_box.setObjectName("button_box")
        self.button_box.rejected.connect(self.reject)
        self.button_box.accepted.connect(self.accept)
        adjust_layout_direction(self, self.lang)
        self.retranslate_ui()
        self.tabs.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        """
        Items strings
        """
        self.setWindowTitle(self._translate("About Box", "About "))
        self.label_header.setText(
            self._translate("About Box", "Xiaomi Flashable Firmware Creator"))
        self.about_text.setHtml(self._translate("About Box",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                        "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n "
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" />"
                                        "<style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'Arial\'; "
                                        "font-size:11pt; font-weight:400; "
                                        "font-style:normal;\">\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; "
                                        "margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                                        "text-indent:0px;\">"
                                        "<a href=\"https://github.com/XiaomiFirmwareUpdater/"
                                        "xiaomi-flashable-firmware-creator.py/\">"
                                        "<span style=\" text-decoration: underline; "
                                        "color:#009dff;\">"
                                        "Xiaomi Flashable Firmware Creator</span></a> "
                                        "is a Python 3 tool that generates flashable "
                                        "firmware-update "
                                        "packages, extracted from official MIUI ROMS. "
                                        "By <a href=\"https://xiaomifirmwareupdater.com\">"
                                        "<span style=\" text-decoration: underline; "
                                        "color:#009dff;\">"
                                        "XiaomiFirmwareUpdater.</span></a></p>\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; "
                                        "margin-left:0px; "
                                        "margin-right:0px; -qt-block-indent:0; "
                                        "text-indent:0px;\">"
                                        "It supports creating untouched firmware, "
                                        "non-arb firmware, "
                                        "firmware + vendor flashable zip, and "
                                        "firmware-less ROMs.</p>\n"
                                        "<p style=\" margin-top:12px; margin-bottom:12px; "
                                        "margin-left:0px; "
                                        "margin-right:0px; -qt-block-indent:0; "
                                        "text-indent:0px;\">"
                                        "<a href=\"https://xiaomifirmwareupdater.com\">"
                                        "<span style=\" text-decoration: underline; "
                                        "color:#009dff;\">"
                                        "Xiaomi Firmware Updater</span></a> is a community "
                                        "project, started "
                                        "in January 2018, aims to provide firmware packages "
                                        "for all Xiaomi "
                                        "devices, in order to allow custom ROM users to update "
                                        "their devices’ "
                                        "firmware easily through custom recovery instead of "
                                        "having to flash "
                                        "full ROM every time they want to update."
                                        "</p></body></html>"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_about),
                             self._translate("About Box", "About"))
        self.sources_text.setHtml(self._translate("About Box",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                          "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" />"
                                          "<style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Arial\'; "
                                          "font-size:11pt; font-weight:400; "
                                          "font-style:normal;\">\n"
                                          "<p style=\" margin-top:0px; margin-bottom:0px; "
                                          "margin-left:0px; "
                                          "margin-right:0px; -qt-block-indent:0; "
                                          "text-indent:0px;\">"
                                          "Xiaomi Flashable Firmware Creator is a free and "
                                          "open source software, "
                                          "licensed under the GPL-3.0 "
                                          "(GNU GENERAL PUBLIC LICENSE) license.</p>\n"
                                          "<p style=\" margin-top:12px; margin-bottom:12px; "
                                          "margin-left:0px; "
                                          "margin-right:0px; -qt-block-indent:0; "
                                          "text-indent:0px;\">"
                                          "It uses the following libraries:</p>\n"
                                          "<ul style=\"margin-top: 0px; margin-bottom: 0px; "
                                          "margin-left: 0px; "
                                          "margin-right: 0px; -qt-list-indent: 1;\">"
                                          "<li style=\"\" "
                                          "style=\" margin-top:0px; margin-bottom:0px; "
                                          "margin-left:0px; "
                                          "margin-right:0px; -qt-block-indent:0; "
                                          "text-indent:0px;\">"
                                          "PyQt 5.15.0 (built against 5.15.0)</li></ul>"
                                          "</body></html>"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_sources),
                             self._translate("About Box", "Sources"))
        self.authors_text.setHtml(self._translate("About Box",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                          "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" />"
                                          "<style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'Arial\'; "
                                          "font-size:11pt; font-weight:400; "
                                          "font-style:normal;\">\n"
                                          "<ul style=\"margin-top: 0px; margin-bottom: "
                                          "0px; margin-left: "
                                          "0px; margin-right: 0px; -qt-list-indent: 1;\">"
                                          "<li style=\"\" style=\" margin-top:0px; "
                                          "margin-bottom:0px; "
                                          "margin-left:0px; margin-right:0px; "
                                          "-qt-block-indent:0; "
                                          "text-indent:0px;\">"
                                          "<a href=\"https://github.com/yshalsager\">"
                                          "<span style=\" text-decoration: underline; "
                                          "color:#009dff;\">"
                                          "yshalsager</span></a>  - Lead Developer</li><"
                                          "/ul></body></html>"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_authors),
                             self._translate("About Box", "Authors"))
        self.thanks_text.setHtml(self._translate("About Box",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" "
                                         "\"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" "
                                         "/><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Arial\'; "
                                         "font-size:11pt; font-weight:400; "
                                         "font-style:normal;\">\n"
                                         "<ul style=\"margin-top: 0px; margin-bottom: 0px; "
                                         "margin-left: 0px; "
                                         "margin-right: 0px; -qt-list-indent: 1;\">"
                                         "<li style=\"\" style=\" margin-top:0px; "
                                         "margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; "
                                         "-qt-block-indent:0; "
                                         "text-indent:0px;\">"
                                         "<a href=\"https://github.com/ardadem\">"
                                         "<span style=\" text-decoration: underline; "
                                         "color:#009dff;\">ardadem</span></a>"
                                         " for shell script version</li>\n"
                                         "<li style=\"\" style=\" margin-top:0px; "
                                         "margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; "
                                         "-qt-block-indent:0; "
                                         "text-indent:0px;\">"
                                         "<a href=\"https://github.com/hh2333\">"
                                         "<span style=\" text-decoration: "
                                         "underline; color:#009dff;\">TH779</span>"
                                         "</a> and <a href=\"https://github.com/PIPIPIG233666\">"
                                         "<span style=\" text-decoration: "
                                         "underline; color:#009dff;\">PIPIPIG233666</span>"
                                         "</a> for Simplified Chinese translation</li>"
                                         "<li style=\"\" style=\" margin-top:0px; "
                                         "margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; "
                                         "-qt-block-indent:0; "
                                         "text-indent:0px;\">"
                                         "<a href=\"https://github.com/zstanecic\">"
                                         "<span style=\" text-decoration: "
                                         "underline; color:#009dff;\">Zvonimir Stanecic</span>"
                                         "</a> for Croatian translation</li>"
                                         "<li style=\"\" style=\" margin-top:0px; "
                                         "margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; "
                                         "-qt-block-indent:0; "
                                         "text-indent:0px;\">"
                                         "<a href=\"https://github.com/0n3-70uch\">"
                                         "<span style=\" text-decoration: "
                                         "underline; color:#009dff;\">Fabian Briese</span>"
                                         "</a> for German translation</li>"
                                         "<li style=\"\" style=\" margin-top:0px; "
                                         "margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; "
                                         "-qt-block-indent:0; "
                                         "text-indent:0px;\">"
                                         "<a href=\"https://t.me/foxone\">"
                                         "<span style=\" text-decoration: "
                                         "underline; color:#009dff;\">Ed</span>"
                                         "</a> for Italian translation</li>"
                                         "<li style=\"\" style=\" margin-top:0px; "
                                         "margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; "
                                         "-qt-block-indent:0; "
                                         "text-indent:0px;\">"
                                         "<a href=\"https://github.com/kacskrz\">"
                                         "<span style=\" text-decoration: "
                                         "underline; color:#009dff;\">Orjon</span>"
                                         "</a> for Polish translation</li>"
                                         "<li style=\"\" style=\" margin-top:0px; "
                                         "margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; "
                                         "-qt-block-indent:0; "
                                         "text-indent:0px;\">"
                                         "<a href=\"https://github.com/DeicPro\">"
                                         "<span style=\" text-decoration: "
                                         "underline; color:#009dff;\">Pablo</span>"
                                         "</a> and Thorin for Spanish translation</li>"
                                         "<li style=\"\" style=\" margin-top:0px; "
                                         "margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; "
                                         "-qt-block-indent:0; "
                                         "text-indent:0px;\">"
                                         "<a href=\"https://t.me/Bodzey\">"
                                         "<span style=\" text-decoration: "
                                         "underline; color:#009dff;\">Bohdan Cherniak</span>"
                                         "</a> for Russian translation</li>"
                                         "<li style=\"\" style=\" margin-top:0px; "
                                         "margin-bottom:0px; "
                                         "margin-left:0px; margin-right:0px; "
                                         "-qt-block-indent:0; "
                                         "text-indent:0px;\">"
                                         "<a href=\"https://github.com/EnesSastim\">"
                                         "<span style=\" text-decoration: "
                                         "underline; color:#009dff;\">Enes Sastim</span>"
                                         "</a> and <a href=\"https://github.com/trzpro\">"
                                         "<span style=\" text-decoration: "
                                         "underline; color:#009dff;\">Emir Bardakçı</span>"
                                         "</a> for Turkish translation</li></ul>\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; "
                                         "margin-left:0px; "
                                         "margin-right:0px; -qt-block-indent:0; "
                                         "text-indent:0px;\"><br/>"
                                         "And all people who have contributed "
                                         "and I have forgotten to mention."
                                         "</p></body></html>"))
        self.tabs.setTabText(self.tabs.indexOf(self.tab_thanks),
                             self._translate("About Box", "Thanks To"))


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    about = AboutBox('en_US')
    about.setup_ui()
    about.show()
    sys.exit(app.exec_())

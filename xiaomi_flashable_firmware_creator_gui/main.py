#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
"""Xiaomi Flashable Firmware Creator GUI"""

import logging
import sys
from pathlib import Path

from PyQt5.QtCore import QUrl, QSize, QRect, QMetaObject, Qt, QTranslator
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QGroupBox, QMainWindow, QWidget, QRadioButton, \
    QLabel, QFrame, QPushButton, QMenuBar, \
    QTextEdit, QProgressBar, QMenu, QStatusBar, QAction, \
    QSizePolicy, qApp, QApplication, QDesktopWidget, \
    QFileDialog, QDialog

from xiaomi_flashable_firmware_creator.firmware_creator import FlashableFirmwareCreator
from xiaomi_flashable_firmware_creator_gui import current_dir
from xiaomi_flashable_firmware_creator_gui.components.about import AboutBox
from xiaomi_flashable_firmware_creator_gui.components.drop_space import DropSpace
from xiaomi_flashable_firmware_creator_gui.components.input_dialog import InputDialog
from xiaomi_flashable_firmware_creator_gui.components.message_box import MessageBox, \
    OutputMessageBox
from xiaomi_flashable_firmware_creator_gui.helpers.layout import adjust_layout_direction
from xiaomi_flashable_firmware_creator_gui.helpers.misc import browse_file_directory
from xiaomi_flashable_firmware_creator_gui.helpers.settings import load_settings, update_settings

logging.basicConfig(filename=f'{current_dir}/data/last_run.log', filemode='w',
                    format='(%(asctime)s) - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.INFO)


class MainWindowUi(QMainWindow):
    """Main Window"""

    def __init__(self, lang, translator):
        super().__init__()
        # Init
        self.lang = lang
        self._translateanslator = translator
        self._translate = QApplication.translate
        self.window_body = QWidget(self)
        self.process_type = QGroupBox(self.window_body)
        self.btn_fw = QRadioButton(self.process_type)
        self.btn_nonarb = QRadioButton(self.process_type)
        self.btn_vendor = QRadioButton(self.process_type)
        self.btn_fwless = QRadioButton(self.process_type)
        self.frame = QFrame(self.window_body)
        self.btn_select = QPushButton(self.frame)
        self.btn_url = QPushButton(self.frame)
        self.btn_create = QPushButton(self.frame)
        self.menubar = QMenuBar(self)
        self.status_box = QTextEdit(self.window_body)
        self.groupbox_drop = DropSpace(self.window_body, self.status_box, self._translate)
        self.label_drop = QLabel(self.groupbox_drop)
        self.progress_bar = QProgressBar(self.window_body)
        self.menu_file = QMenu(self.menubar)
        self.statusbar = QStatusBar(self)
        self.menu_language = QMenu(self.menubar)
        self.menu_help = QMenu(self.menubar)
        self.action_open_zip = QAction(self)
        self.action_open_remote_zip = QAction(self)
        self.action_quit = QAction(self)
        # languages
        self.action_language_sq = QAction(self)
        self.action_language_ar = QAction(self)
        self.action_language_ca = QAction(self)
        self.action_language_zh_CN = QAction(self)
        self.action_language_hr = QAction(self)
        self.action_language_cs = QAction(self)
        self.action_language_nl = QAction(self)
        self.action_language_en = QAction(self)
        self.action_language_fr = QAction(self)
        self.action_language_de = QAction(self)
        self.action_language_el = QAction(self)
        self.action_language_hi = QAction(self)
        self.action_language_id = QAction(self)
        self.action_language_it = QAction(self)
        self.action_language_fa = QAction(self)
        self.action_language_ms = QAction(self)
        self.action_language_pl = QAction(self)
        self.action_language_pt_BR = QAction(self)
        self.action_language_ro = QAction(self)
        self.action_language_ru = QAction(self)
        self.action_language_sl = QAction(self)
        self.action_language_es_ES = QAction(self)
        self.action_language_tr = QAction(self)
        self.action_language_uk = QAction(self)
        self.action_language_vi = QAction(self)
        self.action_donate = QAction(self)
        self.action_about = QAction(self)
        self.action_report_bug = QAction(self)
        self.action_website = QAction(self)
        # vars
        self.filepath = None
        self.filename = ''
        # setup
        self.setup_ui()
        self.setWindowIcon(QIcon(f'{current_dir}/icon.png'))
        self.center()
        adjust_layout_direction(self, lang)
        self.show()

    def setup_ui(self):
        """
        setup window ui
        """
        # Main Window
        self.setObjectName("main_window")
        self.setEnabled(True)
        self.resize(600, 400)
        size_policy = QSizePolicy(QSizePolicy.Fixed,
                                  QSizePolicy.Fixed)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(size_policy)
        self.setMinimumSize(QSize(600, 400))
        self.setMaximumSize(QSize(600, 400))
        self.window_body.setObjectName("window_body")
        self.setCentralWidget(self.window_body)
        # GroupBox: process_type
        self.process_choose()
        # GroupBox: Drop files
        self.file_dropper()
        # Frame: Status
        self.status_frame()
        # Menubar
        self.menu_bar()
        # UI Strings
        self.re_translate_ui()
        QMetaObject.connectSlotsByName(self)

    def process_choose(self):
        """
        GroupBox: process_type
        """
        self.process_type.setGeometry(QRect(10, 20, 250, 140))
        self.process_type.setObjectName("process_type")
        self.btn_fw.setGeometry(QRect(10, 20, 160, 30))
        self.btn_fw.setObjectName("btn_fw")
        self.btn_nonarb.setGeometry(QRect(10, 50, 160, 30))
        self.btn_nonarb.setObjectName("btn_nonarb")
        self.btn_vendor.setGeometry(QRect(10, 80, 160, 30))
        self.btn_vendor.setObjectName("btn_vendor")
        self.btn_fwless.setGeometry(QRect(10, 110, 160, 30))
        self.btn_fwless.setObjectName("btn_fwless")
        # Actions
        self.btn_fw.setChecked(True)

    def file_dropper(self):
        """
        GroupBox: Drop files
        """
        self.groupbox_drop.setGeometry(QRect(270, 20, 320, 140))
        self.groupbox_drop.setObjectName("groupbox_drop")
        self.groupbox_drop.setAcceptDrops(True)
        self.label_drop.setGeometry(QRect(0, 30, 320, 111))
        # self.label_drop.setFrameShape(QFrame.Box)
        # self.label_drop.setFrameShadow(QFrame.Sunken)
        # self.label_drop.setLineWidth(2)
        self.label_drop.setAlignment(Qt.AlignCenter)
        self.label_drop.setObjectName("label_drop")

    def status_frame(self):
        """
        Frame: Status
        """
        self.frame.setGeometry(QRect(10, 170, 580, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.btn_select.setGeometry(QRect(125, 20, 105, 35))
        self.btn_select.setObjectName("btn_select")
        self.btn_select.setStatusTip("action_open_zip_tip")
        self.btn_url.setGeometry(QRect(240, 20, 105, 35))
        self.btn_url.setObjectName("btn_url")
        self.btn_url.setStatusTip("action_zip_url_tip")
        self.btn_create.setGeometry(QRect(355, 20, 105, 35))
        self.btn_create.setObjectName("btn_create")
        self.btn_create.setStatusTip("btn_create_tip")
        self.status_box.setGeometry(QRect(10, 250, 580, 40))
        self.status_box.setObjectName("status_box")
        # self.status_box.setFrameShape(QFrame.Box)
        # self.status_box.setFrameShadow(QFrame.Sunken)
        self.status_box.setReadOnly(True)
        self.status_box.setOverwriteMode(True)
        self.status_box.setObjectName("status_box")
        self.progress_bar.setGeometry(QRect(10, 300, 580, 40))
        self.progress_bar.setObjectName("progress_bar")
        self.progress_bar.setValue(0)

        # Action
        self.btn_select.clicked.connect(self.select_file)
        self.btn_url.clicked.connect(self.enter_url)
        self.btn_create.clicked.connect(self.create_zip)

    def menu_bar(self):
        """
        Menubar
        """
        self.menubar.setGeometry(QRect(0, 0, 600, 32))
        self.menubar.setObjectName("menubar")
        self.menu_file.setObjectName("menu_file")
        self.menu_language.setObjectName("menu_language")
        self.menu_help.setObjectName("menu_help")
        self.setMenuBar(self.menubar)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.action_open_zip.setObjectName("action_open_zip")
        self.action_open_zip.setStatusTip("action_open_zip_tip")
        self.action_open_remote_zip.setObjectName("action_open_remote_zip")
        self.action_open_remote_zip.setStatusTip("action_open_remote_zip")
        self.action_quit.setObjectName("action_quit")
        self.action_quit.setStatusTip("action_quit_tip")
        self.action_language_sq.setObjectName("action_language_sq")
        self.action_language_ar.setObjectName("action_language_ar")
        self.action_language_ca.setObjectName("action_language_ca")
        self.action_language_zh_CN.setObjectName("action_language_zh_CN")
        self.action_language_hr.setObjectName("action_language_hr")
        self.action_language_cs.setObjectName("action_language_cs")
        self.action_language_nl.setObjectName("action_language_nl")
        self.action_language_en.setObjectName("action_language_en")
        self.action_language_fr.setObjectName("action_language_fr")
        self.action_language_de.setObjectName("action_language_de")
        self.action_language_el.setObjectName("action_language_el")
        self.action_language_hi.setObjectName("action_language_hi")
        self.action_language_id.setObjectName("action_language_id")
        self.action_language_it.setObjectName("action_language_it")
        self.action_language_ms.setObjectName("action_language_ms")
        self.action_language_fa.setObjectName("action_language_fa")
        self.action_language_pl.setObjectName("action_language_pl")
        self.action_language_pt_BR.setObjectName("action_language_pt_BR")
        self.action_language_ro.setObjectName("action_language_ro")
        self.action_language_ru.setObjectName("action_language_ru")
        self.action_language_sl.setObjectName("action_language_sl")
        self.action_language_es_ES.setObjectName("action_language_es_ES")
        self.action_language_tr.setObjectName("action_language_tr")
        self.action_language_uk.setObjectName("action_language_uk")
        self.action_language_vi.setObjectName("action_language_vi")
        self.action_report_bug.setObjectName("action_report_bug")
        self.action_report_bug.setStatusTip("action_report_bug_tip")
        self.action_donate.setObjectName("action_donate")
        self.action_donate.setStatusTip("action_donate_tip")
        self.action_about.setObjectName("action_about")
        self.action_about.setStatusTip("action_about_tip")
        self.action_website.setObjectName("action_website")
        self.action_website.setStatusTip("action_website_tip")
        self.menu_file.addActions([self.action_open_zip, self.action_open_remote_zip,
                                   self.action_quit])
        self.menu_language.addActions(
            [self.action_language_sq, self.action_language_ar, self.action_language_ca,
             self.action_language_zh_CN, self.action_language_hr, self.action_language_cs,
             self.action_language_nl, self.action_language_en, self.action_language_fr,
             self.action_language_de, self.action_language_el, self.action_language_hi,
             self.action_language_id, self.action_language_it, self.action_language_ms,
             self.action_language_fa, self.action_language_pl, self.action_language_pt_BR,
             self.action_language_ro, self.action_language_ru, self.action_language_sl,
             self.action_language_es_ES, self.action_language_tr, self.action_language_uk,
             self.action_language_vi])
        self.menu_help.addActions([self.action_report_bug, self.action_donate,
                                   self.action_about, self.action_website])
        self.menubar.addActions([self.menu_file.menuAction(), self.menu_language.menuAction(),
                                 self.menu_help.menuAction()])
        # Shortcuts
        self.action_open_zip.setShortcut('Ctrl+O')
        self.action_open_remote_zip.setShortcut('Ctrl+R')
        self.action_quit.setShortcut('Ctrl+Q')
        # Actions
        self.action_open_zip.triggered.connect(self.select_file)
        self.action_open_remote_zip.triggered.connect(self.enter_url)
        self.action_quit.triggered.connect(qApp.quit)
        self.action_language_sq.triggered.connect(
            lambda: self.change_language("sq"))
        self.action_language_ar.triggered.connect(
            lambda: self.change_language("ar"))
        self.action_language_ca.triggered.connect(
            lambda: self.change_language("ca"))
        self.action_language_zh_CN.triggered.connect(
            lambda: self.change_language("zh-CN"))
        self.action_language_hr.triggered.connect(
            lambda: self.change_language("hr"))
        self.action_language_cs.triggered.connect(
            lambda: self.change_language("cs"))
        self.action_language_nl.triggered.connect(
            lambda: self.change_language("nl"))
        self.action_language_en.triggered.connect(
            lambda: self.change_language("en_US"))
        self.action_language_fr.triggered.connect(
            lambda: self.change_language("fr"))
        self.action_language_de.triggered.connect(
            lambda: self.change_language("de"))
        self.action_language_el.triggered.connect(
            lambda: self.change_language("el"))
        self.action_language_hi.triggered.connect(
            lambda: self.change_language("hi"))
        self.action_language_id.triggered.connect(
            lambda: self.change_language("id"))
        self.action_language_it.triggered.connect(
            lambda: self.change_language("it"))
        self.action_language_ms.triggered.connect(
            lambda: self.change_language("ms"))
        self.action_language_fa.triggered.connect(
            lambda: self.change_language("fa"))
        self.action_language_pl.triggered.connect(
            lambda: self.change_language("pl"))
        self.action_language_pt_BR.triggered.connect(
            lambda: self.change_language("pt-BR"))
        self.action_language_ro.triggered.connect(
            lambda: self.change_language("ro"))
        self.action_language_ru.triggered.connect(
            lambda: self.change_language("ru"))
        self.action_language_sl.triggered.connect(
            lambda: self.change_language("sl"))
        self.action_language_es_ES.triggered.connect(
            lambda: self.change_language("es-ES"))
        self.action_language_tr.triggered.connect(
            lambda: self.change_language("tr"))
        self.action_language_uk.triggered.connect(
            lambda: self.change_language("uk"))
        self.action_language_vi.triggered.connect(
            lambda: self.change_language("vi"))
        self.action_about.triggered.connect(self.open_about)
        self.action_report_bug.triggered.connect(
            lambda: self.open_link('https://github.com/XiaomiFirmwareUpdater/'
                                   'xiaomi-flashable-firmware-creator-gui/issues'))
        self.action_donate.triggered.connect(
            lambda: self.open_link('https://xiaomifirmwareupdater.com/donate'))
        self.action_website.triggered.connect(
            lambda: self.open_link('https://xiaomifirmwareupdater.com'))

    def re_translate_ui(self):
        """
        Items strings
        """
        self.setWindowTitle(self._translate("Title",
                                    "Xiaomi Flashable Firmware Creator"))
        self.process_type.setTitle(self._translate("Radio Buttons", "Process"))
        self.btn_fw.setText(self._translate("Radio Buttons", "Firmware"))
        self.btn_nonarb.setText(self._translate("Radio Buttons", "Non-ARB Firmware"))
        self.btn_vendor.setText(self._translate("Radio Buttons", "Firmware + Vendor"))
        self.btn_fwless.setText(self._translate("Radio Buttons", "Firmware-less ROM"))
        self.groupbox_drop.setTitle(self._translate("Drop space", "Drop a file"))
        self.label_drop.setText(self._translate("Drop space",
                                        "<html><head/><body>"
                                        "<p align=\"center\">"
                                        "<span style=\" font-style:italic;\">"
                                        "Drop a rom zip file here"
                                        "</span></p></body></html>"))
        self.btn_select.setText(self._translate("Main Buttons", "Select file"))
        self.btn_select.setStatusTip(self._translate("Main Buttons", "Select MIUI Zip file"))
        self.btn_url.setText(self._translate("Main Buttons", "Enter URL"))
        self.btn_url.setStatusTip(self._translate("Main Buttons", "Enter a URL of a Zip file"))
        self.btn_create.setText(self._translate("Main Buttons", "Create"))
        self.btn_create.setStatusTip(self._translate("Main Buttons", "Create the selected output zip"))
        self.menu_file.setTitle(self._translate("Menu bar", "File"))
        self.menu_language.setTitle(self._translate("Menu bar", "Language"))
        self.menu_help.setTitle(self._translate("Menu bar", "Help"))
        self.action_open_zip.setText(self._translate("Menu bar", "Open ZIP"))
        self.action_open_zip.setStatusTip(self._translate("Menu bar", "Select MIUI Zip file"))
        self.action_open_remote_zip.setText(self._translate("Menu bar", "Enter URL"))
        self.action_open_remote_zip.setStatusTip(self._translate("Menu bar", "Enter a URL of a Zip file"))
        self.action_quit.setText(self._translate("Menu bar", "Quit"))
        self.action_quit.setStatusTip(self._translate("Menu bar", "Exits the application"))
        self.action_language_sq.setText(self._translate("Menu bar", "Albanian"))
        self.action_language_ar.setText(self._translate("Menu bar", "Arabic"))
        self.action_language_ca.setText(self._translate("Menu bar", "Catalan"))
        self.action_language_zh_CN.setText(self._translate("Menu bar", "Chinese Simplified"))
        self.action_language_hr.setText(self._translate("Menu bar", "Croatian"))
        self.action_language_cs.setText(self._translate("Menu bar", "Czech"))
        self.action_language_nl.setText(self._translate("Menu bar", "Dutch"))
        self.action_language_en.setText(self._translate("Menu bar", "English"))
        self.action_language_fr.setText(self._translate("Menu bar", "French"))
        self.action_language_de.setText(self._translate("Menu bar", "German"))
        self.action_language_el.setText(self._translate("Menu bar", "Greek"))
        self.action_language_hi.setText(self._translate("Menu bar", "Hindi"))
        self.action_language_id.setText(self._translate("Menu bar", "Indonesian"))
        self.action_language_it.setText(self._translate("Menu bar", "Italian"))
        self.action_language_ms.setText(self._translate("Menu bar", "Malay"))
        self.action_language_fa.setText(self._translate("Menu bar", "Persian"))
        self.action_language_pl.setText(self._translate("Menu bar", "Polish"))
        self.action_language_pt_BR.setText(self._translate("Menu bar", "Portuguese, Brazilian"))
        self.action_language_ro.setText(self._translate("Menu bar", "Romanian"))
        self.action_language_ru.setText(self._translate("Menu bar", "Russian"))
        self.action_language_sl.setText(self._translate("Menu bar", "Slovenian"))
        self.action_language_es_ES.setText(self._translate("Menu bar", "Spanish"))
        self.action_language_tr.setText(self._translate("Menu bar", "Turkish"))
        self.action_language_uk.setText(self._translate("Menu bar", "Ukrainian"))
        self.action_language_vi.setText(self._translate("Menu bar", "Vietnamese"))
        self.action_report_bug.setText(self._translate("Menu bar", "Report Bug"))
        self.action_report_bug.setStatusTip(self._translate("Menu bar", "Submit an issue "
                                                                "in case anything is wrong"))
        self.action_donate.setText(self._translate("Menu bar", "Donate"))
        self.action_donate.setStatusTip(self._translate("Menu bar", "Show us some love"))
        self.action_about.setText(self._translate("Menu bar", "About"))
        self.action_about.setStatusTip(self._translate("Menu bar", "About this tool"))
        self.action_website.setText(self._translate("Menu bar", "Website"))
        self.action_website.setStatusTip(self._translate("Menu bar", "Visit tool website"))
        self.statusBar().showMessage(self._translate("Status Box", "Ready"))

    def center(self):
        """
        Dynamically center the window in screen
        """
        # https://gist.github.com/saleph/163d73e0933044d0e2c4
        # geometry of the main window
        window = self.frameGeometry()
        # center point of screen
        center_point = QDesktopWidget().availableGeometry().center()
        # move rectangle's center point to screen's center point
        window.moveCenter(center_point)
        # top left of rectangle becomes top left of window centering it
        self.move(window.topLeft())

    def change_language(self, lang: str):
        """
        Update strings language and settings
        """
        update_settings(dict({'language': lang}))
        adjust_layout_direction(self, lang)
        self._translateanslator.load(f'{current_dir}/i18n/{lang}.qm')
        self.re_translate_ui()
        logging.info(f'Language is switched to {lang}')

    def select_file(self):
        """
        Opens select file Dialog
        """
        dialog = QFileDialog()
        filepath = dialog.getOpenFileName(
            self,
            self._translate('Select Files Dialog', 'Select MIUI zip'),
            '', self._translate('Select Files Dialog', 'MIUI zip files') + ' (*.zip)')[0]
        if not filepath:
            self.statusBar().showMessage(self._translate("Status Box", "Please select a file!"))
            self.status_box.setText(self._translate("Status Box", "Please select a file!"))
            return
        self.filepath = Path(filepath).absolute()
        self.filename = self.filepath.name
        self.status_box.setText(self._translate("Status Box", f"File {self.filename} is selected"))
        self.statusBar().showMessage(self._translate("Status Box", f"File {self.filename} is selected"))
        logging.info(f'File {self.filename} is selected')

    def enter_url(self):
        """
        Enter URL Dialog
        """
        dialog = InputDialog(self._translate('Enter URL Dialog', 'Remote Zip URL'),
                             self._translate('Enter URL Dialog', 'Enter a MIUI zip direct link:'),
                             self._translate('Enter URL Dialog', 'Set URL'),
                             self._translate('Enter URL Dialog', 'Cancel'),
                             parent=self.window_body)
        if dialog.exec_() == QDialog.Accepted:
            url = dialog.textValue()
            if "http" not in url or "ota.d.miui.com" not in url:
                message_box = MessageBox(self._translate('Popup Message', 'Error'),
                                         self._translate('Popup Message', 'Not a valid URL.'),
                                         self._translate('Popup Message', 'OK'), box_type="Warning",
                                         parent=self.window_body)
                message_box.exec_()
                # if button_clicked == QMessageBox.Ok:
                #     pass
                return
            self.filepath = url
            self.filename = url.split("/")[-1]
            self.status_box.setText(
                self._translate("Status Box", f"Remote file {self.filename} is selected."))
            logging.info(f'Remote file {self.filename} is selected')

    def create_zip(self):
        """
        creates output zip file
        """
        checked_radiobutton = None
        process = None
        if not self.filepath:
            error_box = MessageBox(self._translate('Popup Message', 'Error'),
                                   self._translate('Popup Message', 'You must select a ROM zip first!'),
                                   self._translate('Popup Message', 'OK'), box_type="Critical",
                                   parent=self.window_body)
            error_box.exec_()
            logging.info(f'No Zip error shown')
            return

        for button in self.process_type.findChildren(QRadioButton):
            if button.isChecked():
                checked_radiobutton = button.text()
                logging.info(f'Selected process ({button.text()})')
        if checked_radiobutton == 'Firmware':
            process = 'firmware'
        if checked_radiobutton == 'Non-ARB Firmware':
            process = 'nonarb'
        if checked_radiobutton == 'Firmware + Vendor':
            process = 'vendor'
        if checked_radiobutton == 'Firmware-less ROM':
            process = 'firmwareless'
        self.status_box.setText(self._translate("Status Box", f"Starting {process} job"))
        out_dir = Path(".").absolute() if isinstance(self.filepath, str) else self.filepath.parent
        firmware_creator = FlashableFirmwareCreator(str(self.filepath),
                                                    process, out_dir)
        self.progress_bar.setValue(1)
        logging.info(f'Starting extract job')
        self.progress_bar.setValue(5)
        self.status_box.setText(
            self._translate("Status Box", f"Unzipping MIUI ROM..."))
        self.progress_bar.setValue(20)
        logging.info(f'Unzipping {self.filename}')
        extracted = False
        try:
            firmware_creator.extract()
            extracted = True
        except RuntimeError as err:
            if str(err) == "Nothing found to extract!":
                message_box = MessageBox(self._translate('Popup Message', 'Error'),
                                         self._translate('Popup Message', 'Unsupported operation for MTK!'),
                                         self._translate('Popup Message', 'OK'), box_type="Warning",
                                         parent=self.window_body)
                message_box.exec_()
                self.status_box.setText(
                    self._translate("Status Box", "Error: Unsupported operation for MTK!"))
                logging.warning(f'Unsupported operation for MTK')
                firmware_creator.close()
                self.progress_bar.setValue(100)
            else:
                raise err
        if extracted:
            self.progress_bar.setValue(45)
            self.status_box.setText(
                self._translate("Status Box", "Generating updater-script..."))
            self.progress_bar.setValue(55)
            logging.info(f'Creating updater-script')
            firmware_creator.generate_updater_script()
            self.status_box.setText(self._translate("Status Box", "Creating zip.."))
            self.progress_bar.setValue(75)
            logging.info(f'Creating output zip')
            new_zip = firmware_creator.make_zip()
            firmware_creator.cleanup()
            firmware_creator.close()
            self.progress_bar.setValue(100)
            message_box = OutputMessageBox(
                self._translate('Popup Message', 'Done'),
                self._translate('Popup Message', f'All Done! Output zip is {new_zip}'),
                self._translate('Popup Message', 'OK'), self._translate('Popup Message', 'Show in folder'),
                self.filepath, parent=self.window_body)
            clicked = message_box.exec_()
            if clicked:
                browse_file_directory(self.filepath)
            logging.info(f'Done')
            self.status_box.setText(self._translate("Status Box", "Ready"))
            self.statusBar().showMessage(self._translate("Status Box", "Ready"))

    @staticmethod
    def open_link(link):
        """
        Opens link in browser
        """
        QDesktopServices.openUrl(QUrl(link))
        logging.info(f'{link} opened')

    def open_about(self):
        """
        Opens About box
        """
        about_box = AboutBox(self.lang)
        about_box.setup_ui()
        about_box.exec_()


def main():
    """Main."""
    app = QApplication(sys.argv)
    settings = load_settings()
    lang = settings['language']
    logging.info(f'Language {lang} loaded')
    translator = QTranslator(app)
    translator.load(f'{current_dir}/i18n/{lang}.qm')
    app.installTranslator(translator)
    _ = MainWindowUi(lang, translator)
    sys.exit(app.exec_())

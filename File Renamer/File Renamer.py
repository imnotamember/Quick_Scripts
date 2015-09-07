__author__ = 'Joshua Zosky'

import sys
import os
import shutil
from PyQt4.QtGui import QApplication, QDialog, QFileDialog, QTableWidgetItem
from PyQt4.QtCore import QDir
from rf import Ui_Dialog


class RenameFilesDialog(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.console_output = "Welcome to the File Renamer."
        self.show()

        # Connect up the buttons.
        self.ui.OpenBrowse.clicked.connect(self.show_open_dialog)
        self.ui.OrderNum.clicked.connect(self.order_numerically)
        self.ui.SaveBrowse.clicked.connect(self.show_save_dialog)
        self.ui.Deploy.clicked.connect(self.deploy_files)
        self.ui.Console.setText(self.console_output)


    @staticmethod
    def where_to(text_box_contents):

        # if text_box_contents is None:
        #     return '/home'

        if QDir().exists(text_box_contents) is True:
            return str(text_box_contents)
        else:
            return '/home'

    def show_open_dialog(self):

        location = self.where_to(self.ui.OpenText.text())
        fnames = QFileDialog.getOpenFileNames(self, 'Open files', location)

        if fnames.isEmpty() is True:
            return

        file_directory = os.path.split(str(fnames[0]))
        self.ui.OpenText.setText(file_directory[0])

        row_count = len(fnames)
        self.ui.FileTable.setRowCount(row_count)
        counter = 0
        self.console_output = 'Loading:\n%s' % self.console_output
        for name in fnames:
            self.console_output = '%s\n%s' % (name, self.console_output)
            self.ui.Console.setText(self.console_output)
            name = str(name)
            folder_name, file_name = os.path.split(name)
            folder_name = QTableWidgetItem(folder_name)
            file_name = QTableWidgetItem(file_name)
            self.ui.FileTable.setItem(counter, 0, folder_name)
            self.ui.FileTable.setItem(counter, 1, file_name)
            counter += 1


    def show_save_dialog(self):

        location = self.where_to(self.ui.SaveText.text())
        folder = QFileDialog.getExistingDirectory(self, "Select Directory to Save New Files", location)

        if folder.isEmpty() is True:
            return

        self.console_output = "Current folder to save to is: %s\n%s" % (str(folder), self.console_output)
        self.ui.Console.setText(self.console_output)
        self.ui.SaveText.setText(folder)

        for row in range(self.ui.FileTable.rowCount()):
            folder_name = QTableWidgetItem(self.ui.SaveText.text())
            self.ui.FileTable.setItem(row, 2, folder_name)


    def deploy_files(self):

        row_count = self.ui.FileTable.rowCount()
        self.console_output = 'Saving:\n%s' % self.console_output
        for row in range(row_count):
            old_file = os.path.join(str(self.ui.FileTable.item(row, 0).text()),
                                str(self.ui.FileTable.item(row, 1).text()))
            new_file = os.path.join(str(self.ui.FileTable.item(row, 2).text()),
                                    str(self.ui.FileTable.item(row, 3).text()))
            self.console_output = '%s ===> %s\n%s' % (old_file, new_file, self.console_output)
            self.ui.Console.setText(self.console_output)
            shutil.copyfile(old_file, new_file)

    def order_numerically(self):

        if self.ui.FileTable.item(0,0) is None:
            return

        prefix = str(self.ui.Prefix.text())
        suffix = str(self.ui.Suffix.text())
        row_count = self.ui.FileTable.rowCount()
        for count in range(row_count):
            og_file_name = str(self.ui.FileTable.item(count, 1).text())
            og_file_name, og_extension = os.path.splitext(og_file_name)
            if count < 10:
                new_filename = prefix + '0' + str(count) + suffix + og_extension
            else:
                new_filename = prefix + str(count) + suffix + og_extension
            folder_name = QTableWidgetItem(self.ui.SaveText.text())
            file_name = QTableWidgetItem(new_filename)
            self.ui.FileTable.setItem(count, 2, folder_name)
            self.ui.FileTable.setItem(count, 3, file_name)

app = QApplication(sys.argv)
rfd = RenameFilesDialog()
sys.exit(app.exec_())
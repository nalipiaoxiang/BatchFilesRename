from PyQt5.Qt import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog
import os

from resource.batchFilesRename_ui import Ui_Main


class PaneBatchFilesRename(QWidget, Ui_Main):
    def __init__(self, parent=None, *args, **kwargs):
        super(PaneBatchFilesRename, self).__init__(parent, *args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    # 信号
    # 槽函数
    # 添加目标路径
    def add_files_path(self):
        # 使用前先清空展示文件列表
        self.files_list_text_edit.clear()
        # 获取路径
        files_directory = QFileDialog.getExistingDirectory(self, '选择一个py文件', './')
        # 展示路径
        self.directory_line_edit.setText(files_directory)
        # 根据路径获取文件
        files_name = [files_directory + os.sep + name for name in os.listdir(files_directory) if os.path.isfile(files_directory + os.sep + name)]
        # 展示文件列表
        for name in files_name:
            self.files_list_text_edit.appendPlainText(name)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    paneBatchFilesRename = PaneBatchFilesRename()
    paneBatchFilesRename.show()
    sys.exit(app.exec_())

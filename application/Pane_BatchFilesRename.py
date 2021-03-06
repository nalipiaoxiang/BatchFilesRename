from PyQt5.Qt import Qt
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon, QPixmap, QDesktopServices
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox
import os

from resource.batchFilesRename_ui import Ui_Main


class PaneBatchFilesRename(QWidget, Ui_Main):
    def __init__(self, parent=None, *args, **kwargs):
        super(PaneBatchFilesRename, self).__init__(parent, *args, **kwargs)
        # 初始化数据
        self.files_name = []
        self.new_files_name = []
        self.files_directory = ''

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setupUi(self)

    # 信号
    # 槽函数
    # 添加目标路径
    def add_files_path(self):
        # 使用前先清空展示文件列表
        self.files_list_text_edit.clear()
        self.files_name.clear()
        self.new_files_name.clear()
        # 获取路径
        files_directory = QFileDialog.getExistingDirectory(self, '选择一个py文件', './')
        self.files_directory = files_directory
        # 展示路径
        self.directory_line_edit.setText(files_directory)
        # 根据路径获取文件
        self.files_name = [files_directory + os.sep + name for name in os.listdir(files_directory) if
                           os.path.isfile(files_directory + os.sep + name)]
        # 展示文件列表
        for name in self.files_name:
            self.files_list_text_edit.appendPlainText(name)

    # 预览处理结果
    def preview_files_list(self):
        # 判断选中的文件夹中是否有文件
        if len(self.files_name) == 0:
            message_box = QMessageBox(self)
            message_box.setWindowIcon(QIcon(':/main/images/message-exclamatory-mark.PNG'))
            message_box.setIcon(QMessageBox.Information)
            message_box.setWindowTitle('注意:')
            message_box.setText('<h1>当前文件夹下不存在文件,请从新添加</h1>')
            message_box.setDetailedText('当前文件夹下不存在文件,请从新添加')
            message_box.show()
            return None
        # 获取重命名方式
        if self.default_radio_button.isChecked():
            # 默认
            # 获取文件列表
            for i, element in enumerate(self.files_name):
                new_file_name = self.files_directory + os.sep + str(i+1) + os.path.splitext(element)[-1]
                self.new_files_name.append(new_file_name)
                self.files_list_preview_text_edit.appendPlainText(new_file_name)
            return None
        if self.custom_radio_button.isChecked():
            # 自定义
            QMessageBox.warning(self, '警告!', '<h1>该功能还未实现,敬请期待!</h1>', QMessageBox.Cancel | QMessageBox.Cancel)
            return None

    # 执行重命名
    def apply(self):
        if len(self.files_name) == 0 or len(self.new_files_name)==0:
            message_box = QMessageBox(self)
            message_box.setWindowIcon(QIcon(':/main/images/message-exclamatory-mark.PNG'))
            message_box.setIcon(QMessageBox.Information)
            message_box.setWindowTitle('注意:')
            message_box.setText('<h1>请先执行预览功能,然后应用</h1>')
            message_box.setDetailedText('请先执行预览功能,然后应用')
            message_box.show()
            return None
        # 执行重命名
        # 二次警告
        msg = QMessageBox.warning(self, '警告!', '<h1>确认执行重命名!</h1>', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if msg == QMessageBox.No:
            return None
        # 获取重命名方式
        if self.default_radio_button.isChecked():
            # 默认
            if len(self.files_name) == len(self.new_files_name):
                for i in range(0,len(self.files_name)):
                    os.rename(self.files_name[i], self.new_files_name[i])
                    self.rename_progressBar.setValue(int((100/len(self.files_name))*(i+1)))
                self.files_list_preview_text_edit.appendPlainText('执行完成!')
        if self.custom_radio_button.isChecked():
            # 自定义
            QMessageBox.warning(self, '警告!', '<h1>该功能还未实现,敬请期待!</h1>', QMessageBox.Cancel | QMessageBox.Cancel)
            return None

    # 关于
    def about(self):
        # 关于
        QMessageBox.about(self, '批量重命名工具', '<h1>批量重命名工具!点击确定查看源代码</h1>')
        QDesktopServices.openUrl(QUrl('https://github.com/nalipiaoxiang/BatchFilesRename'))



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    paneBatchFilesRename = PaneBatchFilesRename()
    paneBatchFilesRename.show()
    sys.exit(app.exec_())

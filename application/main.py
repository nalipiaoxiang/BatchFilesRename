from PyQt5.QtWidgets import QApplication
from Pane_BatchFilesRename import PaneBatchFilesRename

if __name__ == '__main__':
    import sys
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("paneBatchFilesRename")
    app = QApplication(sys.argv)
    paneBatchFilesRename = PaneBatchFilesRename()
    paneBatchFilesRename.setWindowTitle('简单的批量重命名工具')
    paneBatchFilesRename.show()
    sys.exit(app.exec_())
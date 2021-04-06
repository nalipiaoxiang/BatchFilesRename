from PyQt5.QtWidgets import QApplication

from application.Pane_BatchFilesRename import PaneBatchFilesRename

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    paneBatchFilesRename = PaneBatchFilesRename()
    paneBatchFilesRename.show()
    sys.exit(app.exec_())
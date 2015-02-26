from PyQt4 import QtGui, QtCore

from specview.ui.qt.menubars import MainMainBar
from specview.ui.qt.docks import (DataDockWidget, InfoDockWidget,
                                  ConsoleDockWidget,ModelDockWidget)


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Basic app info
        self.menu_bar = MainMainBar()
        self.setMenuBar(self.menu_bar)
        self.setWindowTitle('IFUpy')
        tb = QtGui.QToolBar()
        self.addToolBar(tb)
        tb.hide()

        # File open dialog
        self.file_dialog = QtGui.QFileDialog(self)

        # Set the MDI area as the central widget
        self.mdiarea = QtGui.QMdiArea(self)
        self.mdiarea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiarea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.mdiarea.setActivationOrder(QtGui.QMdiArea.CreationOrder)
        self.mdiarea.cascadeSubWindows()

        # Set center widget as a top-level, layout-ed widget
        main_layout = QtGui.QVBoxLayout()
        main_layout.addWidget(self.mdiarea)
        main_layout.setContentsMargins(0, 0, 0, 0)
        # self.setCentralWidget(main_widget)
        self.setCentralWidget(self.mdiarea)
        self.setCorner(QtCore.Qt.BottomRightCorner,
                       QtCore.Qt.RightDockWidgetArea)

        # Setup data dock
        self.data_dock = DataDockWidget(self)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.data_dock)

        # Setup info view dock
        self.info_dock = InfoDockWidget(self)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.info_dock)
        self.info_dock.hide()

        # Setup info view dock
        self.model_editor_dock = ModelDockWidget(self)
        self.addDockWidget(QtCore.Qt.RightDockWidgetArea, self.model_editor_dock)
        self.model_editor_dock.setFloating(True)
        self.model_editor_dock.hide()

        # Setup console dock
        self.console_dock = ConsoleDockWidget(self)
        self.addDockWidget(QtCore.Qt.BottomDockWidgetArea, self.console_dock)

        self._setup_menu_bar()

    def _setup_menu_bar(self):
        self.menu_bar.docks_menu.addAction(
            self.data_dock.toggleViewAction())
        self.menu_bar.docks_menu.addAction(
            self.info_dock.toggleViewAction())
        self.menu_bar.docks_menu.addAction(
            self.console_dock.toggleViewAction())

    def set_toolbar(self, toolbar=None, hide_all=False):
        if toolbar is not None:
            self.addToolBar(toolbar)

        for child in self.children():
            if isinstance(child, QtGui.QToolBar):
                if child == toolbar:
                    child.show()
                elif child.isVisible():
                    child.hide()

                if hide_all:
                    child.hide()
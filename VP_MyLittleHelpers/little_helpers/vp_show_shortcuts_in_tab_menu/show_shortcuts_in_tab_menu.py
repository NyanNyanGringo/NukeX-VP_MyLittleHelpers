import nuke

from PySide2.QtWidgets import QApplication, QLineEdit, QAction
from PySide2.QtCore import QObject, QEvent, QTimer, Qt, QSortFilterProxyModel

from little_helpers.vp_little_helpers import qtHelper


class CustomProxyModel(QSortFilterProxyModel):
    def __init__(self, nodes_shortcuts: dict, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nodes_shortcuts = nodes_shortcuts

    def data(self, index, role):
        try:
            original_data = super().data(index, role)
        except RuntimeError:  # advoid "Can't find converter for 'QMap<QString,int>'"
            return ""

        if role == Qt.DisplayRole:

            shortcut = self.nodes_shortcuts.get(original_data)
            if shortcut:
                return f"{original_data} {shortcut}"

        return original_data


class EventFilter(QObject):
    def __init__(self, node_graph_widget=None, show_hotkeys: bool = True, action: QAction = None):
        """
        param action: QAction from nuke.menu("Nuke") connected to turn on/off ShowShortcutsInTabMenu instrument.
        """
        super().__init__(node_graph_widget)
        self.node_graph_widget = node_graph_widget
        self.show_hotkeys = show_hotkeys
        self.action = action

    def eventFilter(self, obj, event):
        if event.type() == QEvent.ShortcutOverride and obj.hasFocus() and event.key() == Qt.Key_Tab:
            QTimer.singleShot(100, self.change_widget_behaviour)
        return super().eventFilter(obj, event)

    def change_widget_behaviour(self):
        widget = QApplication.focusWidget()

        if isinstance(widget, QLineEdit):
            view = widget.completer().popup()
            delegate = view.itemDelegate()

            proxy_model = CustomProxyModel(nodes_shortcuts=self.get_nodes_shortcuts())
            proxy_model.setSourceModel(widget.completer().model())
            widget.completer().setModel(proxy_model)
            widget.completer().model()  # update model

            view.setItemDelegate(None)
            view.setItemDelegate(delegate)

            widget.update()
            widget.repaint()
            view.update()
            view.repaint()

            widget.completer().complete()

    def get_nodes_shortcuts(self,
                            _menu_nodes=nuke.menu("Nodes"),
                            _header_name: str = None,
                            _only_items_with_shortcuts: bool = True) -> dict:
        """
        Iterate through all items in nuke.menu("Nodes") and create dictionary
        like {"menu_item_name [head_menu_name]": "action_shortcut"}.
        """

        # after installing Event Filter to NodeGraph QLineEdit we can't return
        # QSortFilterProxyModel to original state. When user disable showing
        # hotkeys in Tab menu - don't uninstall Event Filter but don't show
        # any hotkeys.
        if not self.action.isChecked():
            return {}

        nodes_hotkeys = {}

        for item in _menu_nodes.items():

            if item.__class__.__name__ == "Menu":

                current_header_name = item.name() if _header_name is None else f"{_header_name} -> {item.name()}"
                sub_hotkeys = self.get_nodes_shortcuts(_menu_nodes=item,
                                                       _header_name=current_header_name,
                                                       _only_items_with_shortcuts=_only_items_with_shortcuts)
                nodes_hotkeys.update(sub_hotkeys)

            else:

                shortcut = item.action().shortcut().toString() or ""

                if _only_items_with_shortcuts and not shortcut:
                    continue

                key = f"{item.name()} [{_header_name}]" if _header_name else item.name()
                nodes_hotkeys[key] = shortcut

        return nodes_hotkeys


def start(action):
    node_graph_widget = qtHelper.get_current_dag()
    _filter = EventFilter(node_graph_widget=node_graph_widget,
                          show_hotkeys=True, action=action)

    if action.isChecked():
        node_graph_widget.installEventFilter(_filter)

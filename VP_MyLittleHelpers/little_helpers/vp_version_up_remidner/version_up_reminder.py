from PySide2 import QtWidgets, QtCore, QtGui
import nuke
import nukescripts
import random

from little_helpers.vp_little_helpers import qtHelper


class TransparentWidget(QtWidgets.QWidget):
    def __init__(self, text, position='top-left', parent=None):
        super(TransparentWidget, self).__init__(parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.ToolTip)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setAttribute(QtCore.Qt.WA_NoSystemBackground)

        # Установка полупрозрачного фона
        self.setStyleSheet("background-color: rgba(120, 80, 40, 180);")

        # Надпись по центру с увеличенным шрифтом
        self.label = QtWidgets.QLabel(text, self)
        self.label.setStyleSheet("color: white; font-size: 14px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        # Создание кнопки
        self.button = QtWidgets.QPushButton("Save New Comp Version | Alt + Shift + S", self)
        self.button.setStyleSheet("font-size: 14px; padding: 6px; background-color: rgba(120, 80, 40, 180);")
        self.button.clicked.connect(self.animate_button_to_green)

        # Установка макета
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)  # Сохранение self.label как атрибут класса
        layout.addWidget(self.button)
        layout.setContentsMargins(5, 5, 5, 5)  # Уменьшенные отступы
        layout.setSpacing(5)  # Уменьшенное расстояние между текстом и кнопкой
        self.setLayout(layout)

        # Таймер для автоматического закрытия виджета через 5 секунд
        self.close_timer = QtCore.QTimer(self)
        self.close_timer.setSingleShot(True)
        self.close_timer.timeout.connect(self.fade_out)

        # Анимация появления (снизу вверх)
        self.animation = QtCore.QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(1000)  # Длительность анимации появления
        self.animation.finished.connect(self.start_fade_out_timer)

        # Анимация прозрачности
        self.opacity_effect = QtWidgets.QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.opacity_effect)
        self.opacity_animation = QtCore.QPropertyAnimation(self.opacity_effect, b"opacity")
        self.opacity_animation.setDuration(1000)

        # Установка позиции
        self.position = position

    def start_fade_out_timer(self):
        self.close_timer.start(7500)  # Задержка перед затуханием

    def fade_out(self):
        self.opacity_animation.setStartValue(1)
        self.opacity_animation.setEndValue(0)
        self.opacity_animation.start()
        self.opacity_animation.finished.connect(self.close)

    def animate_button_to_green(self):
        # Запускаем анимацию изменения цвета кнопки
        for i in range(0, 60, 5):  # Плавный переход
            new_style = f"font-size: 14px; padding: 6px; background-color: rgba({120 - i}, {80 + i}, 40, 180);"
            QtCore.QCoreApplication.processEvents()  # Обновляем UI на каждом шаге
            self.setStyleSheet(new_style)
            self.button.setStyleSheet(new_style)
            QtCore.QThread.msleep(40)  # Небольшая задержка для плавности
        self.label.setText("Completed ✅")
        self.button.hide()
        self.save_new_version()

    def save_new_version(self):
        nukescripts.script_and_write_nodes_version_up()

    def showEvent(self, event):
        screen = QtWidgets.QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        widget_geometry = self.geometry()

        # Определение начальной позиции (снизу вне экрана)
        if self.position == 'center':
            x = (screen_geometry.width() - widget_geometry.width()) // 2
            y = (screen_geometry.height() - widget_geometry.height()) // 2
        elif self.position == 'top-left':
            x = 0 + screen_geometry.width() / 100
            y = 0 + screen_geometry.height() / 15
        elif self.position == 'top-right':
            x = screen_geometry.width() - widget_geometry.width()
            y = 0
        elif self.position == 'bottom-left':
            x = 0
            y = screen_geometry.height() - widget_geometry.height()
        elif self.position == 'bottom-right':
            x = screen_geometry.width() - widget_geometry.width()
            y = screen_geometry.height() - widget_geometry.height()

        start_rect = QtCore.QRect(x, screen_geometry.height(), widget_geometry.width(), widget_geometry.height())
        end_rect = QtCore.QRect(x, y, widget_geometry.width(), widget_geometry.height())
        self.setGeometry(start_rect)

        # Запуск анимаций
        self.animation.setStartValue(start_rect)
        self.animation.setEndValue(end_rect)
        self.animation.start()

        self.opacity_animation.setStartValue(0)
        self.opacity_animation.setEndValue(1)
        self.opacity_animation.start()


def show_transparent_widget(position='top-left'):
    phrases = [
        "Dear Sir, kindly remember to... upgrade the Script Version! :)",
        "Hey, don’t forget to... bump up the Script Version! ;)",
        "Yo, boss! Time to... power up that Script Version! ^_^",
        "My esteemed Lord, do ensure the Script Version is elevated :3",
        "Please proceed with updating the Script Version, My Lord :|",
        "My Lord, time to boost that Script Version :D",
        "My Lord, it’s crucial not to overlook the Script Version upgrade :S",
        "You’ve got this, My Lord! Level up that Script Version :]",
        "O wise one, the time to ascend the Script Version has come :o",
        "My Lord, upgrade the Script Version immediately >:(",
        "My Lord, don’t let that Script Version stay behind! :P",
        "Keep going, My Lord! Remember to enhance the Script Version :)",
        "My Lord, it is imperative to update the Script Version :|",
        "Oh Mighty Lord, a Script Version upgrade beckons! :>",
        "Don’t forget to up that Script Version, My Lord ;)",
        "My Lord, the Script Version needs your immediate attention! :O",
        "My Lord, the Script awaits its rise to a higher Version ^_^",
        "Let’s take that Script Version to the next level, My Lord! :]",
        "My Lord, it’s time to dial up that Script Version B-)",
        "My Lord, don’t let the Script Version stay stuck in the past! XD"
    ]

    # Случайный выбор фразы
    selected_phrase = random.choice(phrases)

    # Получение главного окна Nuke как родителя
    parent = QtWidgets.QApplication.activeWindow()

    # Создание и отображение виджета с заданной позицией и текстом
    widget = TransparentWidget(text=selected_phrase, position=position, parent=parent)
    widget.resize(300, 100)  # Уменьшение размеров для лучшей видимости
    widget.show()


ON_SCRIPT_LOAD_CALLBACK = lambda: nuke.executeInMainThread(show_transparent_widget)


def start():
    if qtHelper.check_action_is_checked(config_key="version_up_reminder"):
        nuke.addOnScriptLoad(ON_SCRIPT_LOAD_CALLBACK)
    else:
        nuke.removeOnScriptLoad(ON_SCRIPT_LOAD_CALLBACK)

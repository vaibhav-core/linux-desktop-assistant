import signal
import sys
import math
import random

from PySide6.QtCore import QPointF, QRectF, Qt, QTimer
from PySide6.QtGui import (
    QColor,
    QConicalGradient,
    QPainter,
    QPen,
    QRadialGradient,
)
from PySide6.QtWidgets import QApplication, QWidget


class JarvisWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(
            Qt.FramelessWindowHint |
            Qt.WindowStaysOnTopHint |
            Qt.Tool
        )

        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_ShowWithoutActivating)

        self.resize(180, 180)

        screen = QApplication.primaryScreen().availableGeometry()

        x = screen.right() - self.width() - 30
        y = screen.bottom() - self.height() - 30

        self.move(x, y)

        self.elapsed = 0.0
        self.particles = [
            (random.uniform(0, math.tau), random.uniform(0.72, 1.15), random.uniform(0.6, 1.8))
            for _ in range(28)
        ]

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.animate)
        self.timer.start(16)

    def animate(self):

        self.elapsed += 0.016

        self.update()

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        center = QPointF(self.width() / 2, self.height() / 2)
        pulse = 1.0 + 0.045 * math.sin(self.elapsed * 1.7)
        radius = min(self.width(), self.height()) * 0.255 * pulse

        painter.setPen(Qt.PenStyle.NoPen)
        for scale, alpha in ((2.35, 10), (1.9, 16), (1.55, 25), (1.3, 36)):
            glow = QRadialGradient(center, radius * scale)
            glow.setColorAt(0.0, QColor(28, 220, 255, alpha))
            glow.setColorAt(0.48, QColor(13, 140, 220, alpha // 2))
            glow.setColorAt(1.0, QColor(0, 40, 100, 0))
            painter.setBrush(glow)
            painter.drawEllipse(center, radius * scale, radius * scale)

        painter.save()
        painter.translate(center)
        painter.rotate(math.degrees(self.elapsed * 24.0))
        for index, (angle, orbit, size) in enumerate(self.particles):
            travel = angle + self.elapsed * (0.22 + index % 3 * 0.08)
            distance = radius * (orbit + 0.05 * math.sin(self.elapsed * 2.0 + index))
            particle = QPointF(math.cos(travel) * distance, math.sin(travel) * distance)
            alpha = int(35 + 35 * (0.5 + 0.5 * math.sin(self.elapsed * 2.5 + index)))
            painter.setBrush(QColor(96, 232, 255, alpha))
            painter.drawEllipse(particle, size, size)
        painter.restore()

        core = QRadialGradient(center - QPointF(radius * 0.28, radius * 0.32), radius * 1.2)
        core.setColorAt(0.0, QColor(225, 255, 255, 245))
        core.setColorAt(0.13, QColor(94, 239, 255, 235))
        core.setColorAt(0.52, QColor(9, 151, 220, 220))
        core.setColorAt(0.82, QColor(4, 62, 150, 210))
        core.setColorAt(1.0, QColor(0, 13, 52, 180))
        painter.setBrush(core)
        painter.drawEllipse(center, radius, radius)

        painter.save()
        painter.translate(center)
        painter.rotate(math.degrees(-self.elapsed * 40.0))
        arc_gradient = QConicalGradient(QPointF(0, 0), 0)
        arc_gradient.setColorAt(0.0, QColor(173, 255, 255, 0))
        arc_gradient.setColorAt(0.18, QColor(173, 255, 255, 190))
        arc_gradient.setColorAt(0.33, QColor(36, 179, 255, 30))
        arc_gradient.setColorAt(0.62, QColor(0, 75, 185, 0))
        arc_gradient.setColorAt(0.84, QColor(92, 224, 255, 135))
        arc_gradient.setColorAt(1.0, QColor(173, 255, 255, 0))
        painter.setBrush(Qt.BrushStyle.NoBrush)
        painter.setPen(QPen(arc_gradient, max(1.0, radius * 0.035)))
        painter.drawEllipse(QRectF(-radius * 1.07, -radius * 1.07, radius * 2.14, radius * 2.14))
        painter.restore()

        highlight = QRadialGradient(center - QPointF(radius * 0.34, radius * 0.38), radius * 0.42)
        highlight.setColorAt(0.0, QColor(255, 255, 255, 150))
        highlight.setColorAt(0.32, QColor(168, 255, 255, 48))
        highlight.setColorAt(1.0, QColor(168, 255, 255, 0))
        painter.setBrush(highlight)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(center - QPointF(radius * 0.34, radius * 0.38), radius * 0.42, radius * 0.42)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    signal.signal(signal.SIGINT, signal.SIG_DFL)

    window = JarvisWindow()
    window.show()

    sys.exit(app.exec())
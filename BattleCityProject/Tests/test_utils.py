# test_utils.py
import pygame
from unittest.mock import Mock, MagicMock
import os
import sys


def setup_test_environment():
    """Настройка тестового окружения без лишнего вывода"""

    # Подавляем вывод PyGame
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')

    try:
        # Мокаем pygame.display и другие модули
        pygame.display.set_mode = Mock(return_value=Mock())
        pygame.display.update = Mock()
        pygame.mixer.music.load = Mock()
        pygame.mixer.music.play = Mock()
        pygame.mixer.music.stop = Mock()
        pygame.mixer.music.set_volume = Mock()
        pygame.mixer.Sound = Mock(return_value=Mock())
        pygame.mixer.Channel = Mock(return_value=Mock())

        # Создаем заглушки для изображений
        mock_image = MagicMock()
        mock_image.get_rect = Mock(return_value=Mock(width=32, height=32))

        # Тихая заглушка для загрузки изображений
        def silent_image_load(path):
            return mock_image

        pygame.image.load = silent_image_load
        pygame.transform.scale = Mock(return_value=mock_image)

        # Мокаем шрифты
        mock_font = Mock()
        mock_font.render = Mock(return_value=Mock())
        pygame.font.Font = Mock(return_value=mock_font)
        pygame.font.SysFont = Mock(return_value=mock_font)

        # Мокаем threading.Timer
        import threading
        def mock_timer(interval, function):
            mock_timer_obj = Mock()
            mock_timer_obj.start = Mock()
            return mock_timer_obj

        threading.Timer = mock_timer

        return mock_image

    finally:
        # Восстанавливаем stdout
        sys.stdout.close()
        sys.stdout = original_stdout


def create_mock_surface(width=800, height=512):
    """Создает mock поверхность для экрана"""
    mock_surface = Mock()
    mock_surface.blit = Mock()
    mock_surface.fill = Mock()
    mock_surface.get_rect = Mock(return_value=Mock(width=width, height=height))
    mock_surface.get_width = Mock(return_value=width)
    mock_surface.get_height = Mock(return_value=height)
    return mock_surface


def suppress_pygame_output():
    """Подавляет вывод PyGame"""
    import os
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
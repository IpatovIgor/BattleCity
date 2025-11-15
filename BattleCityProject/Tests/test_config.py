# test_config.py
import os
import sys


def setup_test_paths():
    """Настройка путей для тестов"""

    # Подавляем вывод PyGame
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)  # C:\GAMES\tanki\BattleCity\BattleCityProject
    code_dir = os.path.join(parent_dir, "Code")

    # Проверяем существование папки Code
    if not os.path.exists(code_dir):
        print(f"❌ Папка Code не найдена: {code_dir}")
        return False

    # Добавляем путь к Code в sys.path
    sys.path.insert(0, code_dir)

    # Проверяем, что файлы доступны
    required_files = ["BulletClass.py", "PlayerClass.py", "BrickClass.py"]
    for file in required_files:
        file_path = os.path.join(code_dir, file)
        if not os.path.exists(file_path):
            print(f"❌ Отсутствует: {file}")
            return False

    # Устанавливаем переменные окружения для тестов
    os.environ['TEST_MODE'] = 'True'

    return True


# Автоматически настраиваем пути при импорте
PATHS_SETUP = setup_test_paths()
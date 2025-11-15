# run_all_tests.py
import unittest
import sys
import os


def run_all_tests():
    """Запуск всех тестов с чистым выводом"""

    # Подавляем вывод PyGame
    os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'

    print("=" * 50)
    print("ЗАПУСК ТЕСТОВ")
    print("=" * 50)

    # Добавляем текущую директорию в путь
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, current_dir)

    # Импортируем конфигурацию
    try:
        from test_config import PATHS_SETUP
        if not PATHS_SETUP:
            print("❌ Не удалось настроить пути для тестов!")
            return False
    except ImportError as e:
        print(f"❌ Ошибка импорта test_config: {e}")
        return False

    # Находим все тестовые файлы
    test_files = ['test_bullet.py', 'test_brick.py', 'test_player.py']

    # Загружаем и запускаем тесты из каждого файла
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()

    for test_file in test_files:
        if os.path.exists(os.path.join(current_dir, test_file)):
            print(f"📋 Загрузка тестов из: {test_file}")
            try:
                # Импортируем модуль и добавляем его тесты в suite
                module_name = test_file[:-3]  # убираем .py
                module = __import__(module_name)
                suite = test_loader.loadTestsFromModule(module)
                test_suite.addTest(suite)
            except Exception as e:
                print(f"❌ Ошибка загрузки {test_file}: {e}")
        else:
            print(f"❌ Файл не найден: {test_file}")

    if test_suite.countTestCases() == 0:
        print("❌ Нет тестов для запуска!")
        return False

    # Запускаем тесты
    print(f"\n🚀 Запуск {test_suite.countTestCases()} тестов...\n")
    test_runner = unittest.TextTestRunner(verbosity=1)  # Уменьшаем verbosity до 1
    result = test_runner.run(test_suite)

    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ ТЕСТОВ")
    print("=" * 50)

    # Красивая статистика
    print(f"✅ Пройдено: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"❌ Провалено: {len(result.failures)}")
    print(f"⚠️  Ошибок: {len(result.errors)}")

    if result.wasSuccessful():
        print("\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!")
    else:
        print("\n💥 НЕКОТОРЫЕ ТЕСТЫ НЕ ПРОЙДЕНЫ")

    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_all_tests()
    sys.exit(0 if success else 1)

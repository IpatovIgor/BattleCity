# explore_structure.py
import os


def explore_structure():
    print("Исследование структуры проекта...")
    current_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"Текущая папка: {current_dir}")

    # Поднимаемся на уровень выше (в BattleCityProject)
    parent_dir = os.path.dirname(current_dir)
    print(f"Родительская папка: {parent_dir}")

    print("\nСодержимое родительской папки:")
    for item in os.listdir(parent_dir):
        item_path = os.path.join(parent_dir, item)
        if os.path.isdir(item_path):
            print(f"📁 {item}")
            # Показываем содержимое важных папок
            if item in ['Code', 'Tests', 'Images', 'Music']:
                subitems = os.listdir(item_path)[:10]  # первые 10 элементов
                for subitem in subitems:
                    print(f"   📄 {subitem}")
        else:
            print(f"📄 {item}")

    # Ищем файлы игровых классов
    print(f"\nПоиск игровых файлов в {parent_dir}:")
    game_files = []
    for root, dirs, files in os.walk(parent_dir):
        for file in files:
            if file in ['BulletClass.py', 'PlayerClass.py', 'BrickClass.py']:
                full_path = os.path.join(root, file)
                game_files.append(full_path)
                print(f"✓ Найден: {file} -> {full_path}")

    return parent_dir, game_files


if __name__ == "__main__":
    parent_dir, game_files = explore_structure()
    if game_files:
        print(f"\n✅ Игровые файлы найдены! Используйте путь: {parent_dir}")
    else:
        print(f"\n❌ Игровые файлы не найдены!")
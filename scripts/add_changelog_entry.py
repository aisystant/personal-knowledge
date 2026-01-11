"""
Добавляет запись в историю изменений чанка.
Использование:
  python scripts/add_changelog_entry.py --file path/to/chunk.md --message "Исправлены опечатки"
"""

import os
import argparse
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description='Add changelog entry to a chunk')
    parser.add_argument('--file', type=str, required=True, help='Path to chunk file')
    parser.add_argument('--message', type=str, required=True, help='Changelog message')
    args = parser.parse_args()

    # TODO: Реализовать
    # 1. Чтение файла
    # 2. Поиск секции "История изменений"
    # 3. Добавление новой записи с текущей датой и временем
    # 4. Обновление поля updated в frontmatter
    # 5. Сохранение файла

    print(f"Adding changelog entry to: {args.file}")
    print(f"Message: {args.message}")
    print("TODO: Implementation required")


if __name__ == '__main__':
    main()

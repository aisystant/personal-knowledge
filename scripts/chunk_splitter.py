"""
Разбивает большие файлы на чанки по 10 000 символов.
Использование:
  python scripts/chunk_splitter.py --file path/to/file.md
"""

import os
import argparse


def main():
    parser = argparse.ArgumentParser(description='Split large files into chunks')
    parser.add_argument('--file', type=str, required=True, help='Path to file to split')
    args = parser.parse_args()

    # TODO: Реализовать
    # 1. Чтение файла
    # 2. Семантическая разбивка (по параграфам, не посередине предложения)
    # 3. Создание связанных чанков (part 1/N, part 2/N...)
    # 4. Обновление related_chunks в метаданных

    print(f"Splitting file: {args.file}")
    print("TODO: Implementation required")


if __name__ == '__main__':
    main()

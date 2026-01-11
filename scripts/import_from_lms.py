"""
Импортирует комментарии под ДЗ стажеров из LMS.
Использование:
  python scripts/import_from_lms.py --student-id all
"""

import os
import argparse
from datetime import datetime


def main():
    parser = argparse.ArgumentParser(description='Import homework reviews from LMS')
    parser.add_argument('--student-id', type=str, default='all', help='Student ID or "all"')
    args = parser.parse_args()

    # TODO: Реализовать
    # 1. Подключение к API LMS
    # 2. Получение списка комментариев под ДЗ
    # 3. Создание чанков с метаданными
    # 4. Сохранение в папку lms/homework-reviews/

    print(f"Importing from LMS...")
    print(f"Student ID: {args.student_id}")
    print("TODO: Implementation required")


if __name__ == '__main__':
    main()

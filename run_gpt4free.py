#!/usr/bin/env python3
# Файл запуска GPT4Free
# Расположение: /gpt4free/run_gpt4free.py
# Автор: Ваше имя
# Дата создания: 2024-01-15

import sys
import os

# Добавляем корневую директорию проекта в путь
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from g4f.gui.run import run_gui_args
from g4f.cli import get_api_parser

def main():
    """
    Основная функция запуска GPT4Free с поддержкой различных режимов.
    
    Режимы запуска:
    1. GUI (по умолчанию)
    2. API
    3. Отладка
    """
    parser = get_api_parser()
    
    # Если аргументы не переданы, запускаем GUI
    if len(sys.argv) == 1:
        sys.argv.append('--gui')
    
    args = parser.parse_args()
    
    # Установка значений по умолчанию
    if not hasattr(args, 'host'):
        args.host = '0.0.0.0'
    if not hasattr(args, 'port') or args.port is None:
        args.port = 8080
    
    try:
        run_gui_args(args)
    except Exception as e:
        print(f"Ошибка при запуске: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

import os
import sys
from pathlib import Path
from colorama import init, Fore

# Ініціалізація colorama для підтримки кольорового виведення
init(autoreset=True)

def list_directory_structure(path: Path, indent: str = ''):
    """Рекурсивно виводить структуру директорії з кольоровим виділенням"""
    if not path.exists():
        print(Fore.RED + f"Помилка: Шлях {path} не існує.")
        return
    if not path.is_dir():
        print(Fore.RED + f"Помилка: {path} не є директорією.")
        return
    
    for item in path.iterdir():
        if item.is_dir():
            print(Fore.BLUE + indent + f"📂 {item.name}")
            list_directory_structure(item, indent + '  ')  # Рекурсивно виводимо вміст директорії
        else:
            print(Fore.GREEN + indent + f"📜 {item.name}")

def main():
    """Основна функція для запуску скрипта"""
    if len(sys.argv) != 2:
        print(Fore.RED + "Помилка: потрібно вказати шлях до директорії.")
        sys.exit(1)

    directory_path = Path(sys.argv[1])

    # Перевірка, чи існує директорія, перед запуском функції виведення
    if not directory_path.exists() or not directory_path.is_dir():
        print(Fore.RED + f"Помилка: {directory_path} не є правильною директорією.")
        sys.exit(1)

    list_directory_structure(directory_path)

if __name__ == "__main__":
    main()

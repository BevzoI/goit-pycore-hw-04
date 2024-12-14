import pprint
from os import path

def get_cats_info(file_path: str):
    # Перевірка на наявність файлу
    if not path.exists(file_path):
        return False
    
    # Список ключів для кожного кота
    keys_list = ['id', 'name', 'age']
    result = []
    
    try:
        
        with open(file=file_path, mode='r', encoding='utf-8') as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue  
                
                
                cat_list = line.split(',')
                
                
                if len(cat_list) != 3:
                    print(f"Невірний формат рядка: {line}")
                    continue  
                
                
                cat_dict = dict(zip(keys_list, cat_list))
                
                
                try:
                    cat_dict['age'] = int(cat_dict['age'])
                except ValueError:
                    print(f"Невірний вік для кота {cat_dict['name']}: {cat_dict['age']}")
                    continue  
                
                result.append(cat_dict)
    
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return False
    
    return result

cats_info = get_cats_info("task_02_file.txt")
if cats_info:
    pprint.pprint(cats_info)
else:
    print("Не вдалося отримати інформацію про котів.")

import requests
import os


def get_character_data(character_id):
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Ошибка при получении данных: {response.status_code}")

def write_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"id - {data['id']}\n")
        file.write(f"name - {data['name']}\n")
        file.write(f"status - {data['status']}\n")

def read_and_filter_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if 'i' not in line.lower():
                print(line.strip())

def main():
    try:
                               
        character_data = get_character_data(72)
        
        temp_filename = "temp_rick.txt"
        write_to_file(character_data, temp_filename)

        new_filename = "cool.txt"
        os.rename(temp_filename, new_filename)
        print(f"Переименован в {new_filename}")
        print("\nСтроки без символа 'i':")
        read_and_filter_file(new_filename)
        
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        if os.path.exists(new_filename):
            os.remove(new_filename)
            print(f"\nФайл {new_filename} успешно удален")

if __name__ == "__main__":
    main()
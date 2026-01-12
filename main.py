import requests
import os


def get_character_data(character_id: int) -> dict:
    """
    Fetches character data from the Rick and Morty API.

    Args:
        character_id: The ID of the character to fetch.

    Returns:
        A dictionary containing character data.

    Raises:
        Exception: If the HTTP request fails or returns non-200 status.
    """
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Ошибка при получении данных: {response.status_code}")


def write_to_file(data: dict, filename: str) -> None:
    """
    Writes character data to a text file.

    Args:
        data: Dictionary containing character data.
        filename: Name of the file to write to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"id - {data['id']}\n")
        file.write(f"name - {data['name']}\n")
        file.write(f"status - {data['status']}\n")


def read_and_filter_file(filename: str) -> None:
    """
    Reads a file and prints lines that don't contain the letter 'i'.

    Args:
        filename: Name of the file to read.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if 'i' not in line.lower():
                print(line.strip())


def main() -> None:
    """Main function to execute the character data processing workflow."""
    new_filename = "cool.txt"
    
    try:
        character_data = get_character_data(72)
        
        temp_filename = "temp_rick.txt"
        write_to_file(character_data, temp_filename)

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

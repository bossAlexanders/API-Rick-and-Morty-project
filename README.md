1. API Integration
Connects to the public Rick and Morty API (https://rickandmortyapi.com)

Fetches detailed character information by ID

Includes robust error handling for HTTP requests

2. Data Processing Pipeline
Fetch: Retrieves character data (ID, name, status)

Write: Saves formatted data to temporary files

Filter: Reads and displays lines excluding those containing 'i'

Cleanup: Automatically removes generated files

3. File Operations
Creates temporary text files with structured data

Renames files during processing

Implements proper file cleanup using try-finally pattern

Technical Implementation
Core Functions:
get_character_data(): API client function with error handling

write_to_file(): File writer with UTF-8 encoding support

read_and_filter_file(): Content filter and display function

main(): Orchestrates the complete workflow

Code Quality Features:
PEP8 compliant formatting

Type hints for better code clarity

Comprehensive docstrings in English

Proper exception handling

Context managers for file operations

Workflow Example
Fetch character #72 from API

Write data to temp_rick.txt

Rename to cool.txt

Filter and display lines without 'i'

Automatically delete the file

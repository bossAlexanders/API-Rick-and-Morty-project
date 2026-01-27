# Rick and Morty API Integration — Data Processing Pipeline

## Overview
This project demonstrates an end-to-end data processing workflow using the public  
**Rick and Morty API**: https://rickandmortyapi.com

The script fetches character data by ID, writes it to temporary files, processes the data,
and ensures proper cleanup.

---

## API Integration
- Connects to the public Rick and Morty API
- Fetches detailed character information by **ID**
- Retrieves the following fields:
  - `id`
  - `name`
  - `status`
- Includes robust HTTP error handling

---

## Data Processing Pipeline

### 1. Fetch
- Retrieves character data from the API

### 2. Write
- Saves formatted character data to a temporary text file

### 3. Rename
- Renames the temporary file during processing

### 4. Filter
- Reads file contents
- Displays only lines **excluding** those containing the letter **`i`**

### 5. Cleanup
- Automatically deletes all generated files
- Uses a `try–finally` pattern to guarantee cleanup

---

## File Operations
- Creates temporary UTF-8 encoded text files
- Writes structured data in a readable format
- Renames files as part of the workflow
- Ensures safe cleanup with context managers

---

## Technical Implementation

### Core Functions
- **`get_character_data()`**
  - API client function
  - Handles network and HTTP errors

- **`write_to_file()`**
  - Writes formatted data to a file
  - Supports UTF-8 encoding

- **`read_and_filter_file()`**
  - Reads file content
  - Filters out lines containing the letter `i`

- **`main()`**
  - Orchestrates the complete workflow

---

## Code Quality Features
- PEP 8–compliant formatting
- Type hints for improved readability
- Comprehensive docstrings (English)
- Proper exception handling
- Context managers for all file operations

---

## Example Workflow
1. Fetch character **#72** from the API
2. Write data to `temp_rick.txt`
3. Rename file to `cool.txt`
4. Display lines without the letter `i`
5. Automatically delete the file

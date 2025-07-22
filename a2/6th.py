import logging

# Configure logging
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return None
    except IOError:
        logging.error(f"IO error occurred while reading the file: {file_path}")
        return None

# Example usage
file_path = 'example.txt'
file_content = read_file(file_path)

if file_content:
    print("File content:")
    print(file_content)
else:
    print("An error occurred. Check the error_log.txt file for details.")

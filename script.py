
import os

def delete_files_by_extension(directory, extensions):
    # """
    # Deletes files in the specified directory with the specified extensions.
    
    # Args:
    #     directory (str): The path to the directory where files will be deleted.
    #     extensions (list): List of file extensions to be deleted (e.g., ['.png', '.jpg']).
    # """
    if not os.path.isdir(directory):
        print(f"The directory '{directory}' does not exist.")
        return
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Deleted: {file_path}")

if __name__ == "__main__":
    # Example usage
    directory = "C:/Users/USER/Pictures"
    extensions = ['.png', '.jpg', '.jpeg']  # Add more extensions if needed
    
    delete_files_by_extension(directory, extensions)

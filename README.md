# Downloads Folder Sorter

This Python script is designed to help you keep your Downloads folder organized by sorting files into sub-folders based on their file extensions. Over time, your Downloads folder can become cluttered with various files, and this script aims to bring order to the chaos.

## Features

- **File Sorting:** The script iterates through the files in your Downloads folder and organizes them into sub-folders based on their file extensions.
  
- **Customizable Categories:** The categories and their associated file extensions are defined in the `config.json` file. You can customize the categories to suit your specific needs.

## How to Use

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/downloads-folder-sorter.git
   ```

2. **Navigate to the Project Directory:**
   ```bash
   cd downloads-folder-sorter
   ```

3. **Configure Categories:**
   Edit the `config.json` file to define your own categories and file extensions.

   Example:
   ```json
   [
       {
           "name": "Documents",
           "extensions": [".pdf", ".doc", ".docx", ".txt"]
       },
       {
           "name": "Images",
           "extensions": [".png", ".jpg", ".jpeg", ".gif"]
       },
       // Add more categories as needed
   ]
   ```

4. **Run the Script:**
   ```bash
   python sorter.py
   ```

5. **Check Your Downloads Folder:**
   The script will organize the files in your Downloads folder based on the categories you defined.

## Configuration

- **config.json:**
  The `config.json` file contains an array of categories, each with a name and a list of associated file extensions. Customize this file to create your own categories.

```json
[
    {
        "name": "Documents",
        "extensions": [".pdf", ".doc", ".docx", ".txt"]
    },
    {
        "name": "Images",
        "extensions": [".png", ".jpg", ".jpeg", ".gif"]
    },
    // Add more categories as needed
]
```

## Important Note

- This script is specifically designed for Windows environments and assumes that the user's Downloads folder is located at `C:\Users\Username\Downloads`. If your Downloads folder is in a different location, please update the `home_directory` and `download_path` variables accordingly in the script.

Feel free to customize the script to fit your specific use case, and enjoy a more organized Downloads folder!

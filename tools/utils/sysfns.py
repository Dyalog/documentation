import os
from bs4 import BeautifulSoup

def process_markdown_file(file_path):
    """
    Process a markdown file to add a hidden div with search keywords
    based on the command found in the h1 tag using BeautifulSoup
    """
    # Read the file content
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Check if hidden div already exists
    if "<!-- Hidden search keywords -->" in content:
        print(f"Hidden search keywords div already exists in {file_path}. Skipping.")
        return False
    
    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(content, 'html.parser')
    
    # Find the h1 tag with class "heading"
    h1_tag = soup.find('h1', class_='heading')
    if not h1_tag:
        print(f"No h1 tag with class 'heading' found in {file_path}. Skipping.")
        return False
    
    # Find the span with class "command"
    command_span = h1_tag.find('span', class_='command')
    if not command_span:
        print(f"No span with class 'command' found in h1 tag in {file_path}. Skipping.")
        return False
    
    # Get the text from the command span
    command_text = command_span.get_text().strip()
    
    # Check if the command contains the ⎕ symbol
    if '⎕' not in command_text:
        print(f"No ⎕ symbol found in command span in {file_path}. Skipping.")
        return False
    
    # Extract the command with ⎕ symbol using BeautifulSoup text extraction
    # Look for words that start with ⎕ followed by uppercase letters
    command_parts = command_text.split()
    full_command = None
    
    for part in command_parts:
        if '⎕' in part:
            # Find the part that contains ⎕
            start_idx = part.find('⎕')
            # Extract from ⎕ until end of word or non-alpha character
            command_chunk = ''
            i = start_idx
            while i < len(part) and (part[i] == '⎕' or part[i].isalpha()):
                command_chunk += part[i]
                i += 1
            
            if command_chunk.startswith('⎕'):
                full_command = command_chunk
                break
    
    if not full_command:
        print(f"Could not extract command with ⎕ in {file_path}. Skipping.")
        return False
    
    # Prepare the hidden div content
    if len(full_command) == 2:  # ⎕ plus one letter (like ⎕A)
        hidden_div = f"""<!-- Hidden search keywords -->
<div style="display: none;">
  {full_command}
</div>

"""
    else:
        # Get command without ⎕
        command_without_symbol = full_command[1:]
        hidden_div = f"""<!-- Hidden search keywords -->
<div style="display: none;">
  {full_command} {command_without_symbol}
</div>

"""
    
    # Add the hidden div to the beginning of the file
    new_content = hidden_div + content
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)
    
    print(f"Added hidden div with keywords to {file_path}: {full_command}")
    return True

def process_directory(directory_path):
    """
    Process all markdown files in the given directory
    """
    # Check if directory exists
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f"Error: {directory_path} is not a valid directory.")
        return
    
    # Counter for statistics
    total_files = 0
    processed_files = 0
    skipped_files = 0
    error_files = 0
    
    # Process each file in the directory
    for filename in os.listdir(directory_path):
        # Check if it's a markdown file
        if filename.lower().endswith('.md'):
            total_files += 1
            file_path = os.path.join(directory_path, filename)
            
            # Skip if it's a directory
            if os.path.isdir(file_path):
                continue
            
            # Process the file
            try:
                if process_markdown_file(file_path):
                    processed_files += 1
                else:
                    skipped_files += 1
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")
                error_files += 1
    
    # Print summary
    print(f"\nSummary:")
    print(f"Total markdown files found: {total_files}")
    print(f"Files processed: {processed_files}")
    print(f"Files skipped: {skipped_files}")
    print(f"Files with errors: {error_files}")

def main():
    directory_path = "language-reference-guide/docs/system-functions"
    process_directory(directory_path)
    print("Processing complete.")

if __name__ == "__main__":
    main()
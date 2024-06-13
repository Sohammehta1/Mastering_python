import json
import os
import sys

AGGREGATE_FILE = 'aggregator.txt'
INDEX_FILE = 'index.json'

def return_index():
    '''Returns the json object containing information about all the files'''
    if not os.path.exists(INDEX_FILE):
        return {}
    
    with open(INDEX_FILE, 'r') as f:
        try:
            data = json.load(f)
            return data if data else {}
        except json.JSONDecodeError:
            return {}

def save_index(indices):
    with open(INDEX_FILE, 'w') as f:
        json.dump(indices, f, indent=4)

def add_file(filePath):
    '''Adds Given file at given filePath'''
    indices = return_index()
    fileName = os.path.basename(filePath)

    base_name, ext = os.path.splitext(fileName)
    counter = 1
    while fileName in indices:
        fileName = f"{base_name}({counter}){ext}"
        counter += 1

    start = os.path.getsize(AGGREGATE_FILE) if os.path.exists(AGGREGATE_FILE) else 0
    fileSize = os.path.getsize(filePath)

    with open(AGGREGATE_FILE, 'a', encoding='utf-8') as agg_file:
        with open(filePath, 'r', encoding='utf-8') as src_file:
            content = src_file.read()
            agg_file.write(content)

    indices[fileName] = {"start": start, "fsize": fileSize, 'fpath': filePath, 'ref':False}
    save_index(indices)

    os.remove(filePath)
    print(f"Content from {filePath} appended successfully.")

def remove_file(fileName):
    '''
    Removes file from aggregator file and creates new cut_'original_name' '''
    indices = return_index()
    if fileName not in indices:
        print(f"Error! {fileName} not found in the aggregator.")
        return
    
    file_info = indices.get(fileName)
    
    if not file_info:
        print(f"Error! File information for {fileName} not found.")
        return
    
    start = file_info["start"]
    fileSize = file_info["fsize"]

    with open(AGGREGATE_FILE, 'r+b') as f:
        content = f.read()
        new_content = content[:start] + content[start + fileSize:]
        f.seek(0)
        f.write(new_content)
        f.truncate()

    with open(f'cut_{fileName}', 'w', encoding='utf-8') as cut_file:
        cut_file.write(content[start:start + fileSize].decode('utf-8'))

    del indices[fileName]
    for key, value in indices.items():
        if value["start"] > start:
            value["start"] -= fileSize
    save_index(indices)
    print(f"Content of {fileName} removed successfully.")

def list_files():
    '''
    List all the file names'''
    indices = return_index()
    if not indices:
        print("The aggregator file is empty!")
    else:
        print("Following are the files in the aggregator:")
        for i, key in enumerate(indices.keys(), 1):
            print(f"{i}. {key}")

def copy_file(fileName):
    '''
    Creates a copy of the file (keeps original file)'''
    indices = return_index()
    if fileName not in indices:
        print(f"No such file named '{fileName}' in the aggregator.")
        return
    file_info = indices.get(fileName)
    start = file_info["start"]
    fileSize = file_info["fsize"]

    with open(AGGREGATE_FILE, 'r+b') as f:
        content = f.read()
        copy_content = content[start:start + fileSize].decode('utf-8')

    copyName = f'copy_{fileName}'
    with open(copyName, 'w', encoding='utf-8') as f:
        f.write(copy_content)

    print(f"Content of {fileName} copied successfully.")

def rename_file(fileName, newName):
    indices = return_index()
    if fileName not in indices:
        print("File not found in the aggregator.")
        return
    loc = ''
    if indices[fileName]['ref']==True:
        temp = indices[fileName]['fpath'].split('/')
        temp[-1] = newName
        loc += '/'.join(temp)
        os.rename(indices[fileName]['fpath'],loc)
    indices[newName] = indices.pop(fileName)
    indices[newName]['fpath'] = loc
    save_index(indices)
    
    print(f"File {fileName} renamed to {newName} in index.")

def display_file(fileName):
    indices = return_index()
    if fileName not in indices:
        print(f"No file '{fileName}' found in the aggregator.")
        return
    file_info = indices.get(fileName)
    start = file_info["start"]
    fileSize = file_info["fsize"]

    with open(AGGREGATE_FILE, 'r', encoding='utf-8') as f:
        f.seek(start)
        content = f.read(fileSize)
        print("Required file is displayed below:")
        print(content)

def move_file(fileName, newLocation):
    indices = return_index()
    if fileName not in indices:
        print(f"Error! {fileName} not found in the aggregator.")
        return
    file_info = indices.get(fileName)
    start = file_info["start"]
    fileSize = file_info["fsize"]

    with open(AGGREGATE_FILE, 'r+b') as f:
        content = f.read()
        move_content = (content[start:start + fileSize]).decode('utf-8')
        new_content = content[:start] + content[start + fileSize:]
        f.seek(0)
        f.write(new_content)
        f.truncate()
        

    new_filepath = os.path.join(newLocation, fileName)
    with open(new_filepath, 'w') as f:
        f.write(move_content)
    file_info['fpath'] = new_filepath
    file_info['ref'] = True
    indices[fileName] = file_info

    save_index(indices)
    print(f"'{fileName}' moved successfully to {newLocation}.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python aggregator.py <command> <arguments>")
        return

    command = sys.argv[1]
    if command == 'add' and len(sys.argv) == 3:
        add_file(sys.argv[2])
    elif command == 'cut' and len(sys.argv) == 3:
        remove_file(sys.argv[2])
    elif command == 'list':
        list_files()
    elif command == 'copy' and len(sys.argv) == 3:
        copy_file(sys.argv[2])
    elif command == 'rename' and len(sys.argv) == 4:
        rename_file(sys.argv[2], sys.argv[3])
    elif command == 'move' and len(sys.argv) == 4:
        move_file(sys.argv[2], sys.argv[3])
    elif command == 'display' and len(sys.argv) == 3:
        display_file(sys.argv[2])
    else:
        print("Invalid command or arguments.")

if __name__ == '__main__':
    main()

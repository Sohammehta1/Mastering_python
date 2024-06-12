import json
import os

AGGREGATE_FILE = 'aggregator.txt'
INDEX_FILE = 'index.json'

def return_index():
    '''
    Will return a dictionary of fileName-line mapping.
    '''
    if not os.path.exists(INDEX_FILE):
        return {}
    
    with open(INDEX_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def add_file(filePath):
    '''
    Appends the file to the aggregate file and to the index.
    If file name exists then adds number to the fileName (e.g., fileName(1)).
    '''
    indices = return_index()
    fileName = os.path.basename(filePath)

    # Ensure unique file name in the index
    base_name, ext = os.path.splitext(fileName)
    counter = 1
    while fileName in indices:
        fileName = f"{base_name}({counter}){ext}"
        counter += 1

    with open(AGGREGATE_FILE, 'a') as f:
        s = os.path.getsize(AGGREGATE_FILE)
        # The current file will start from byte s 
        fileSize = os.path.getsize(filePath)
        indices[fileName] = [s, fileSize]

        src_content = ''
        with open(filePath, 'r') as fN:
            src_content = fN.read()
        f.write(src_content)

        with open(INDEX_FILE, 'w') as i:  # updating the index function
            json.dump(indices, i)
    
    print(f"Content from {filePath} appended successfully.")

def remove_file(fileName):
    '''
    Removes the file in concern if at all it exists in the aggregator file.
    '''
    indices = return_index()
    if len(indices) == 0:
        print("Error! No such file exists in the aggregator.")
        return

    agg_size = os.path.getsize(AGGREGATE_FILE)

    if fileName in indices:
        starting_point, fileSize = indices[fileName]
        end = starting_point + fileSize

        if starting_point < 0 or end > agg_size or starting_point >= end:
            print("Invalid start or end positions")
            return

        with open(AGGREGATE_FILE, 'r+b') as f:
            content = f.read()
            new_content = content[:starting_point] + content[end:]  # This is the new content without the current file
            f.seek(0)
            f.write(new_content)
            f.truncate()

        # Update indices
        del indices[fileName]
        for key, (start, size) in indices.items():
            if start > starting_point:  # Adjust start positions for all files after the removed file
                indices[key] = [start - fileSize, size]

        with open(INDEX_FILE, 'w') as i:
            json.dump(indices, i)

        print(f"Content of {fileName} removed successfully.")
    else:
        print(f"Error! {fileName} not found in the aggregator.")

# Example usage:
#add_file('/home/soham/Desktop/Aggregate_me/financial_aid_supervisedLearning.txt')
remove_file('financial_aid_supervisedLearning.txt')

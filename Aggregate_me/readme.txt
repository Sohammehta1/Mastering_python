"Aggregate me" is a file aggregator which is able to do opertions like add, remove.... on the  aggregator file.
The aggregator has following COMMANDS:

1 Add a new file (add file.txt)
    Adds file.txt to aggregator.txt and deletes the original file.txt.

2 Remove a file (cut file.txt)
    Removes file.txt from aggregator.txt and creates a separate file cut_file.txt with the same content as the original file.txt.

3 List all files (list)
    Lists all the files present in aggregator.txt.

4 Create a copy of a file (copy file.txt)
    Keeps file.txt in aggregator.txt and creates a copy of the original file.txt as copy_file.txt.

5 Rename a file (rename old_file.txt new_file.txt)
    Renames old_file.txt to new_file.txt within aggregator.txt.

6 Move a file (move file.txt new_location)
    Moves file.txt to a new location (new_location), keeping a reference in aggregator.txt.

7 Display content of a file (display file.txt)
    Displays the content of file.txt from aggregator.txt.
I 
All this can be done from the command line.
Once you have added the main.py to the system path you can use this utility from anywhere.
I have built this on Ubuntu, so I'm not sure if it'll work on windows the same way it works here, if at all it does work.
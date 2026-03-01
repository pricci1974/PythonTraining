#This function adds a record to the Data.txt file
def writeEntry(type, genre, title, year, author = " ", seasons = " "):
    filePath = "Data.txt"
    if type in "tvshow":
        toWrite = f"{type}, {genre}, {year}, {title}, {seasons}"
    if type in "movie":
        toWrite = f"{type}, {genre}, {year}, {title}"
    if type in "music":
        toWrite = f"{type}, {genre}, {year}, {title}, {author}"

    try:
        with open(filePath, 'a') as file:
            file.write(toWrite + '\n')
    except:
        print("Yeah, no")
    
#This function deletes an entry based on the title    
def deleteEntry(title):
    file_path = 'Data.txt'
    search_string = title
        
    try:
        with open(file_path, 'r') as f:
            lines = [line for line in f if search_string not in line]

        with open(file_path, 'r') as f:
            lines2 = [line for line in f]

        if len(lines) == len(lines2):
            print("Nothing Found!!")
            input("Press ENTER to continue")
            return

        with open(file_path, 'w') as f:
            f.writelines(lines)
            input("Library updated. Press ENTER to continue\n")
    except:
        print("error")
    
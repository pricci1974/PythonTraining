#This program stores and retrieves video recording library entries
#The types are movies, TV shows, and music videos

from M6ReadFile import DataFile as RF
from M6WriteFile import deleteEntry as DE

userInput = 0
print("Welcome to the video library")

while (int(userInput != 4)):
    tf = RF()
    tf.readLibrary()

    print("\nHere are your TV Shows:")
    for var in tf.tvList:
        var.printVideo()

    print("\nYour Movies:")
    for var in tf.movieList:
            var.printVideo()

    print("\nFinally, your Music Videos:")
    for var in tf.musicList:
        var.printVideo()

    print("\nPress 1 for TV Shows, 2 for Movies, 3 for Music Videos\n")
    try:
        userInput = int(input("or 4 to exit: "))
    except:
        print("Please enter 1, 2, 3, or 4")
        try:
            userInput = int(input("or 4 to exit: "))
        except:
            print("Incorrect")
            quit()
    if (int(userInput == 1)):
        print("\nHere are your TV Shows:")
        for var in tf.tvList:
            var.printVideo()
        
        subMenuInput = int(input("\nPress 1 to add a show or 2 to delete one: "))   
        if (int(subMenuInput == 1)):
            tf.addEntry("tvshow")     
        if (int(subMenuInput == 2)):
            toDelete = input("What is the title you wish to delete? ")
            DE(toDelete)

    if (int(userInput == 2)):
        print("\nHere are your Movies:")
        for var in tf.movieList:
            var.printVideo()
        
        subMenuInput = int(input("\nPress 1 to add a movie or 2 to delete one: "))   
        if (int(subMenuInput == 1)):
            tf.addEntry("movie")     
        if (int(subMenuInput == 2)):
            toDelete = input("What is the title you wish to delete? ")
            DE(toDelete)

    if (int(userInput == 3)):
        print("\nHere are your Music Videos:")
        for var in tf.musicList:
            var.printVideo()
        
        subMenuInput = int(input("\nPress 1 to add a Music Video or 2 to delete one: "))   
        if (int(subMenuInput == 1)):
            tf.addEntry("music")     
        if (int(subMenuInput == 2)):
            toDelete = input("What is the title you wish to delete? ")
            DE(toDelete)

print("Goodbye")            

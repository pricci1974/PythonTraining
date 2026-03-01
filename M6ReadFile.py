import M6Video
from M6WriteFile import writeEntry as WE

#This class is used to handle reading the files and preparing to add entries
class DataFile:
    
    def __init__(self):
        self.dataFile = "Data.txt" #only file used for storage --must be in same directory as program
        self.tvList = []
        self.musicList = []
        self.movieList = []

    # Reads the Data file and builds lists of entries based on the
    # entry type
    def readLibrary(self):
        try:
            with open(self.dataFile, 'r') as file:
                for line in file:
                    for word in line.split(','):
                        if "tvshow" in word:
                            tvEntry = line.split(',')
                            self.tvList.append(M6Video.TVShow(tvEntry))
                        if "music" in word:
                            mEntry = line.split(',')
                            self.musicList.append(M6Video.Music(mEntry))
                        if "movie" in word:
                            movEntry = line.split(',')
                            self.movieList.append(M6Video.Video(movEntry))           
    
            print()
            myListTV = len(list(self.tvList))
            myListMusic = len(list(self.musicList))
            myListMovie = len(list(self.movieList))

            print(f"You have the following entries in your library: \n\n",
                  f"TV Shows: {myListTV}\n Movies: {myListMovie}", 
                  f"\n Music Videos: {myListMusic}")   
        except Exception as error:
            print("Could not open file.\nPlease create Data.txt file in same",
                  "directory as program.")     
            print(error)


    def addEntry(self, type):
        
        if (type in "tvshow"):
            tvTitle = input("What is the name of the show? ")
            tvGenre = input("What is the genre? ")
            tvYear = input("What is the year? ")
            tvSeason = input("How many seasons? ")

            if not tvTitle.strip() or not tvGenre.strip() or not tvYear.strip() or not tvSeason.strip():
                input("Incorrect input\n Press ENTER to return")
                return
            print(f"You added: {tvTitle}")
            WE(type=type, title=tvTitle, genre=tvGenre, year=tvYear, seasons=tvSeason)
            input("Press ENTER to contunue\n")
        
        if (type in "movie"):
            movTitle = input("What is the name of the movie? ")
            movGenre = input("What is the genre? ")
            movYear = input("What is the year? ")

            if not movTitle.strip() or not movGenre.strip() or not movYear.strip():
                input("Incorrect input\n Press ENTER to return")
                return
            print(f"You added: {movTitle}")
            WE(type=type, title=movTitle, genre=movGenre, year=movYear)
            input("Press ENTER to contunue\n")

        if (type in "music"):
            musTitle = input("What is the name of the song? ")
            musGenre = input("What is the genre? ")
            musYear = input("What is the year? ")
            musArtist = input("Who is the Artist/Group? ")

            if not musTitle.strip() or not musGenre.strip() or not musYear.strip() or not musArtist.strip():
                input("Incorrect input\n Press ENTER to return")
                return
            print(f"You added: {musTitle}")
            WE(type=type, title=musTitle, genre=musGenre, year=musYear, author=musArtist)
            input("Press ENTER to contunue\n")


#OO Classes
#Each class has its own print function
class Video:
    def __init__(self, video_list):
        self.__list_type = video_list[0] #private
        self.genra = video_list[1]
        self.year = video_list[2]
        self.title = video_list[3]

    #This getter is needed to return the type
    def getType(self):
        return self.__list_type
    
    def printVideo(self):
        print(f" {self.title.strip()} is a{self.genra} movie from{self.year}.")

        
class Music(Video):
    def __init__(self, video_list):
        super().__init__(video_list)
        self.artist = video_list[4] #unique to Music
        
    def printVideo(self):
        print(f"{self.title} from the{self.genra} genre, released in{self.year} by {self.artist.strip()}.")

class TVShow(Video):
    def __init__(self, video_list):
        super().__init__(video_list)
        self.seasons = video_list[4] #unique to TV Shows
        
    def printVideo(self):
        print(f"{self.title} is a{self.genra} show from{self.year} with {self.seasons.strip()} seasons.")

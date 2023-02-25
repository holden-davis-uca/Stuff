#Holden Davis
#CSCI 3360 - CRN 11203
#Dr. Chen - Fall 2021

import imdb

loadfile = open("data.sql", "w")
    

print("\n\n<!---STARTING---!>\n\n")

ia = imdb.IMDb()

topmovies = ia.get_top250_movies()
toptv = ia.get_top250_tv()
people = []
actors = []
directors = []
producers = []
writers = []

def doperson(person, persontype, MEDIA_ID):
    person = ia.get_person(person.personID)
    PERSON_ID = "nm" + person.personID
    name = person.data['name']
    if name not in people:
        people.append(name)
        #print(person.data['name'])
        try:
            BDate = person.data['birth date']
        except KeyError:
            BDate = "null"
        Name = person.data['name'].split()
        FName = Name[0]
        LName = Name[1]
        try:
            Biography = person.data['mini biography'][0][:1500]
            Biography = Biography.replace("'", "")
            Biography = Biography.replace("&", "")
        except KeyError:
            Biography = "null"
        try:
            Birth = person.data['birth notes'].split()
            try:
                City = Birth[0]
                State = Birth[1]
                Country = Birth[2]
            except IndexError: 
                City = "null"
                State = "null"
                Country = "null"
        except KeyError:
            City = "null"
            State = "null"
            Country = "null"
        
        #Person Insertion
        loadfile.write("INSERT INTO Person VALUES ('" + str(PERSON_ID) +"', '"+ str(BDate) +"', '"+ str(FName) +"', '"+ str(LName) + "', '"+ str(Biography) +"', '"+ str(City) + "', '"+ str(State) +"', '"+ str(Country) +"');\n")
        #print("INSERT INTO Person VALUES ('" + str(PERSON_ID) +"', '"+ str(BDate) +"', '"+ str(FName) +"', '"+ str(LName) + "', '"+ str(Biography) +"', '"+ str(City) + "', '"+ str(State) +"', '"+ str(Country) +"');\n")
        #Actor, write actor and acts tables
        if persontype == "a":
            if name not in actors:
                actors.append(name)
                loadfile.write("INSERT INTO Actor VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
                #print("INSERT INTO Actor VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
            loadfile.write("INSERT INTO Acts VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            #print("INSERT INTO Acts VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            
        #Producer, write producer and produces tables
        if persontype == "p":
            if name not in producers:
                producers.append(name)
                loadfile.write("INSERT INTO Producer VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
                #print("INSERT INTO Producer VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
            loadfile.write("INSERT INTO Produces VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            #print("INSERT INTO Produces VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            
        #Director, write director and directs tables
        if persontype == "d":
            if name not in directors:
                directors.append(name)
                loadfile.write("INSERT INTO Director VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
                #print("INSERT INTO Director VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
            loadfile.write("INSERT INTO Directs VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            #print("INSERT INTO Directs VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            
        #Writer, write writer and writes tables
        if persontype == "w":
            if name not in writers:
                writers.append(name)
                loadfile.write("INSERT INTO Writer VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
                #print("INSERT INTO Writer VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
            loadfile.write("INSERT INTO Writes VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            #print("INSERT INTO Writes VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
    else:
        #Actor, write actor and acts tables
        if persontype == "a":
            if name not in actors:
                actors.append(name)
                loadfile.write("INSERT INTO Actor VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
                #print("INSERT INTO Actor VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
            loadfile.write("INSERT INTO Acts VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            #print("INSERT INTO Acts VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            
        #Producer, write producer and produces tables
        if persontype == "p":
            if name not in producers:
                producers.append(name)
                loadfile.write("INSERT INTO Producer VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
                #print("INSERT INTO Producer VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
            loadfile.write("INSERT INTO Produces VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            #print("INSERT INTO Produces VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            
        #Director, write director and directs tables
        if persontype == "d":
            if name not in directors:
                directors.append(name)
                loadfile.write("INSERT INTO Director VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
                #print("INSERT INTO Director VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
            loadfile.write("INSERT INTO Directs VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            #print("INSERT INTO Directs VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            
        #Writer, write writer and writes tables
        if persontype == "w":
            if name not in writers:
                writers.append(name)
                loadfile.write("INSERT INTO Writer VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
                #print("INSERT INTO Writer VALUES ('" + str(PERSON_ID) +"', '"+ str(PERSON_ID) +"');\n")
            loadfile.write("INSERT INTO Writes VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
            #print("INSERT INTO Writes VALUES ('" + str(PERSON_ID) + "', '"+ str(MEDIA_ID) +"');\n")
    

def domovies():
    for i in topmovies[0:25]:
        
        #Build media from a movie to insert into Media table
        movie = ia.get_movie(i.movieID)
        MEDIA_ID = "tt" + movie.movieID
        MPAA_Rating = movie.data['certificates'][0]
        Name = movie.data['localized title']
        Name = Name.replace("'", "")
        Popularity = movie.data['rating']
        Summary = movie.data['plot outline'][:1500]
        Summary = Summary.replace("'", "")
        Summary = Summary.replace("&", "")
        Genre = movie.data['genres'][0]
        Date = movie.data['original air date']
        
        #Generic Media Insertion
        loadfile.write("INSERT INTO Media VALUES ('" + str(MEDIA_ID) +"', '"+ str(MPAA_Rating) +"', '"+ str(Name) +"', '"+ str(Popularity) +"', '"+ str(Summary) +"', '"+ str(Genre) +"', '"+ str(Date)+ "');\n")
        #print("INSERT INTO Media VALUES ('" + str(MEDIA_ID) +"', '"+ str(MPAA_Rating) +"', '"+ str(Name) +"', '"+ str(Popularity) +"', '"+ str(Summary) +"', '"+ str(Genre) +"', '"+ str(Date)+ "');\n")
        
        #Build movie from a movie to insert into Movie table
        MOVIE_ID = "tt" + movie.movieID
        Runtime = movie.data['runtimes'][0]
        Budget = movie.data['box office']['Budget']
        MEDIA_ID = "tt" + movie.movieID
        
        #Movie Insertion
        loadfile.write("INSERT INTO Movie VALUES ('" + str(MOVIE_ID) +"', '"+ str(Runtime) +"', '"+ str(Budget) +"', '"+ str(MEDIA_ID) + "');\n")
        #print("INSERT INTO Movie VALUES ('" + str(MOVIE_ID) +"', '"+ str(Runtime) +"', '"+ str(Budget) +"', '"+ str(MEDIA_ID) + "');\n")
        
        actor = movie.data['cast'][0]
        doperson(actor, "a", MEDIA_ID)
        
        producer = movie.data['producers'][0]
        doperson(producer, "p", MEDIA_ID)
        
        director = movie.data['director'][0]
        doperson(director, "d", MEDIA_ID)
        
        writer = movie.data['writer'][0]
        doperson(writer, "w", MEDIA_ID)   
        
def dotv():
    for i in toptv[0:25]:
        
        #Build media from a tv to insert into Media table
        tv = ia.get_movie(i.movieID)
        MEDIA_ID = "tt" + tv.movieID
        MPAA_Rating = tv.data['certificates'][0]
        Name = tv.data['localized title']
        Name = Name.replace("'", "")
        Popularity = tv.data['rating'] 
        Summary = tv.data['plot'][0][:1500]
        Summary = Summary.replace("'", "")
        Genre = tv.data['genres'][0]
        Date = tv.data['year']
        
        #Generic Media Insertion
        loadfile.write("INSERT INTO Media VALUES ('" + str(MEDIA_ID) +"', '"+ str(MPAA_Rating) +"', '"+ str(Name) +"', '"+ str(Popularity) +"', '"+ str(Summary) +"', '"+ str(Genre) +"', '"+ str(Date)+ "');\n")
        #print("INSERT INTO Media VALUES ('" + str(MEDIA_ID) +"', '"+ str(MPAA_Rating) +"', '"+ str(Name) +"', '"+ str(Popularity) +"', '"+ str(Summary) +"', '"+ str(Genre) +"', '"+ str(Date)+ "');\n")
        
        #Build series from a tv series to insert into Series table
        SERIES_ID = "tt" + tv.movieID
        try:
            Average_Runtime = tv.data['runtimes'][0]
        except KeyError:
            Average_Runtime = 'null'
        MEDIA_ID = "tt" + tv.movieID  
        
        #Series Insertion
        loadfile.write("INSERT INTO Series VALUES ('" + str(SERIES_ID) +"', '"+ str(Average_Runtime) +"', '"+ str(MEDIA_ID) + "');\n")
        #print("INSERT INTO Series VALUES ('" + str(SERIES_ID) +"', '"+ str(Average_Runtime) +"', '"+ str(MEDIA_ID) + "');\n")
        
        #Update tv series to include episodes
        ia.update(tv, 'episodes')
        
        for seasonindex in tv['episodes'].keys():
            for episodeindex in tv['episodes'][seasonindex].keys():
                episode = ia.get_movie(tv['episodes'][seasonindex][episodeindex].movieID)
                EPISODE_ID = "tt" + episode.movieID
                Release = episode.data['original air date']
                Season_Number = seasonindex
                Episode_Number = episodeindex
                try:
                    Runtime = episode.data['runtimes'][0]
                except KeyError:
                    Runtime = 'null'
                Name = episode.data['localized title']
                Name = Name.replace("'", "")
                Summary = episode.data['plot'][0][:1500]
                Summary = Summary.replace("'", "")
                SERIES_ID = "tt" + tv.movieID
                
                #Episode Insertion
                loadfile.write("INSERT INTO Episode VALUES ('" + str(EPISODE_ID) +"', '"+ str(Name) +"', '"+ str(Release) +"', '"+ str(Season_Number) +"', '"+ str(Episode_Number) +"', '"+ str(Runtime) +"', '"+ str(Summary) +"', '"+ str(SERIES_ID) + "');\n")
                #print("INSERT INTO Episode VALUES ('" + str(EPISODE_ID) +"', '"+ str(Name) +"', '"+ str(Release) +"', '"+ str(Season_Number) +"', '"+ str(Episode_Number) +"', '"+ str(Runtime) +"', '"+ str(Summary) +"', '"+ str(SERIES_ID) + "');\n")
                
                #Restriction to only do the first episode of the first season for simplicity's sake
                if seasonindex == 1 and episodeindex == 1:
                    break
            #Restriction to only do the first episode of the first season for simplicity's sake
            if seasonindex == 1 and episodeindex == 1:
                break
               
print("Doing movies")
domovies()
print("Did movies")
print("Doing TV")
dotv()
print("Did TV")
        
loadfile.close()


print("\n\n<!---STOPPING---!>\n\n")

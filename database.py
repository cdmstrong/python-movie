#!/usr/bin/env python3
import psycopg2

#####################################################
##  Database Connection
#####################################################

'''
Connect to the database using the connection string
'''
def openConnection():
    # connection parameters - ENTER YOUR LOGIN AND PASSWORD HERE
    userid = "postgres"
    database = "movie"
    passwd = "root"
    myHost = "43.153.94.194"

    # Create a connection to the database
    conn = None
    try:
        # Parses the config file and connects using the connect string
        conn = psycopg2.connect(database=database,
                                    user=userid,
                                    password=passwd,
                                    host=myHost)
        print('connect success')
    except psycopg2.Error as sqle:
        print("psycopg2.Error : " + sqle.pgerror)
    
    # return the connection to use
    return conn
conn = openConnection()
'''
Validate staff based on login and password
'''
def checkStaffCredentials(login, password):
    cur = conn.cursor()

    # 
    cur.execute("Select * from Staff where login= %s and password = %s;", (login, password))

    # 提交更改
    conn.commit()
    rows = cur.fetchall()
    cur.close()
    if len(rows) == 0:
        return None
    return rows[0]


'''
List all the associated movies in the database by staff
'''
def findMoviesByStaff(login):
    cur = conn.cursor()
    # 
    cur.execute("Select * from Movie where ManagedBy= %s ORDER BY Description ASC, title DESC;;",(login,))
    # 提交更改
    conn.commit()
    rows = cur.fetchall()
    list = []
    for i in rows:
        id, Title, ReleaseDate, PrimaryGenre, SecondaryGenre, AvgRating, ManagedBy, Description = i
        list.append({
            "movie_id": id,
            "title": Title,
            "releasedate":ReleaseDate,
            "avgrating": AvgRating,
            "staff": ManagedBy,
            "genre": PrimaryGenre,
            "description":Description
        })
    cur.close()
    if len(list) == 0:
        return None
    return list


'''
Find a list of movies based on the searchString provided as parameter
See assignment description for search specification
'''
def findMoviesByCriteria(searchString):
    cur = conn.cursor()
    # 插入一条新记录
    cur.execute("""SELECT * FROM movie JOIN Genre on movie.PrimaryGenre = Genre.GenreID WHERE ReleaseDate >= CURRENT_DATE - INTERVAL '20 years' AND 
                ( title LIKE %s OR Description LIKE %s or ManagedBy LIKE %s or Genre.GenreName LIKE %s)
                ORDER BY CASE WHEN Description = '' THEN 1 ELSE 0 END DESC, 
                ReleaseDate DESC,
                Title ASC;""", ('%' + searchString + '%','%' + searchString + '%', '%' + searchString + '%', '%' + searchString + '%'))
    # 提交更改
    conn.commit()
    rows = cur.fetchall()
    list = []
    print(rows)
    for i in rows:
        id, Title, ReleaseDate, PrimaryGenre, SecondaryGenre, AvgRating, ManagedBy, Description, _, _ = i
        list.append({
            "movie_id": id,
            "title": Title,
            "releasedate":ReleaseDate,
            "avgrating": AvgRating,
            "staff": ManagedBy,
            "genre": PrimaryGenre,
            "description":Description
        })
    cur.close()
    if len(list) == 0:
        return None
    return list


'''
Add a new movie
'''
def addMovie(title, releasedate, genre1, genre2, staff, description):
    print('addmovie')
    print(description)
    if not genre2:
        genre2 = 1
    cur = conn.cursor()
    # 插入一条新记录
    cur.execute("INSERT INTO movie (Title, ReleaseDate, PrimaryGenre, SecondaryGenre, AvgRating, ManagedBy, Description) VALUES (%s, %s, %s, %s, %s, %s, %s);", (title, releasedate, genre1, genre2, 0, staff, description))
    # 提交更改
    conn.commit()
    cur.close()
    return True


'''
Update an existing movie
'''
def updateMovie(movieid, title, releasedate, avgrating, genre1, genre2, staff, description):
    if genre2 == "":
        genre2 = None
    cur = conn.cursor()
    # 插入一条新记录
    cur.execute("UPDATE  movie set Title = %s, ReleaseDate = %s, PrimaryGenre = %s, SecondaryGenre = %s, AvgRating = %s, ManagedBy = %s, Description = %s where id = %s;", (title, releasedate, genre1, genre2, avgrating, staff, description, movieid))
    # 提交更改
    conn.commit()
    cur.close()
    return True
    
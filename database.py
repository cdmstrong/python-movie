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
    userid = "root"
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

    return ['jdavis', '0123', 'Jamie', 'Davis', '0422349845', 'jdavis@mrc.com.au', '8 Grenfell Way Petersham NSW', 110915.20]


'''
List all the associated movies in the database by staff
'''
def findMoviesByStaff(login):

    return


'''
Find a list of movies based on the searchString provided as parameter
See assignment description for search specification
'''
def findMoviesByCriteria(searchString):

    return


'''
Add a new movie
'''
def addMovie(title, releasedate, genre1, genre2, staff, description):
    print('addmovie')
    
    return True


'''
Update an existing movie
'''
def updateMovie(movieid, title, releasedate, avgrating, genre1, genre2, staff, description):

    return

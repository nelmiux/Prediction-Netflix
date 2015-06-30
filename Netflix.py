#!/usr/bin/env python3

import os
import urllib.request
import re
import io
import ctypes
import math
import json
import time

# ------------
# netflix_avg_movie
# ------------

def netflix_avg_movie (movie_id, data) :
    '''
        param: movie_id
        description: The variable data has the access to the cache.
                     (keys,values) = (movies ID,movie's average)
        return: The overall average of the movie corresponding to the movie_id
    '''
    assert movie_id != {}
    avg = data[movie_id]

    assert 1.0 <= avg <= 5.0
    return avg


# ------------
# netflix_avg_user
# ------------
    
def netflix_avg_user (user_id, data) :
    '''
        param: user_id
        description: The variable data has the access to the cache.
                     (keys,values) = (user ID,user's average)
        return: The overall average of the user corresponding tot he user_id
    '''
    assert user_id != {}
      
    avg = data[user_id][0]

    assert 1.0 <= avg <= 5.0

    return avg

# ------------
# netflix_rating
# ------------

def netflix_rating (movie_id, user_id, data):
    '''
        param: movie_id, user_id
        description: The variable data has the access to the cache.
                     (movie: {user: rate}) 
        return the average of the movie 
    '''
    assert user_id != {}
   
    #optains tuple with the user_id and their corresponding ratings
    d = data[movie_id]
    rating = 0
    #loop through the values in d and obtain the rating of the user_id
    for user,rate in d.items() :
        if user_id in user :
            rating = rate

    assert 0 <= rating <= 5.0
    return rating

# ------------
# netflix_read_movie_id
# ------------

#return the movie_id from the line obtain from the input file
def netflix_read_movie_id (line) :
    assert line != {}
    l = line.rstrip()
    l = l.rstrip(':')
    return l

# ------------
# netflix_read_user_id
# ------------

#return the user_id from the line obtain from the input file
def netflix_read_user_id(line) :
    assert line != {}
    return line.rstrip()


def sqre_diff(a, p) :
    """
    returns ( a - p ) squared
    """
    return (a - p) ** 2

def netflix_write (s, w) :
    """
    writes the object s to the writer w.
    It appends a new line also.
    """
    
    w.write(str(s) + "\n")


def netflix_predict(userAvg,  movieAvg, userDecAvg) :
    """
        Currently experimenting with implementation #1
        Trying different combinations of numerators and
        denominators.
    """
    assert ( 0 < userAvg <= 5)
    assert ( 0 < movieAvg <= 5)
    assert ( 0 <= userDecAvg <= 5)    
    if (userAvg == 0) :
        return movieAvg
    if (userDecAvg == 0) :
        return round(userAvg * 0.521 + movieAvg * 0.52 - 0.14, 1)
    return round(userDecAvg * 0.7 + movieAvg * 0.3, 1)  

def rmse (sqrDiff, count) :
    """
    rmse calculates the root mean square error.
    It is given the running sum of square differences
    and the count to divide by. The square root is then 
    returned.
    """
    assert count > 0 
    return round(math.sqrt(sqrDiff / count), 2)

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """
    start_time = time.time()
    sqrDiff=0
    c=0
    movie_id = ""
    movieDecade = 0
    userDecAvg = 0

    solutionsCache = open("pam2599-probe_solutions.json", "r")
    solutionsDict = json.loads(solutionsCache.read())
    userAvg  = open("ezo55-Average_Viewer_Rating_Cache.json")
    userAvgDict   = json.loads(userAvg.read())
    movieAvg = open("BRG564-Average_Movie_Rating_Cache.json", "r")
    movieAvgDict = json.loads(movieAvg.read())
    userDec = open("drc2582-customer_decade_dict.json", "r")
    userDecDict = json.loads(userDec.read())
    movieDec = open("pra359-Movie_Decades_Cache.json", "r")
    movieDecDict = json.loads(movieDec.read())

    #loop through the file and obtain the total average
    lines = r.readlines()
    for l in lines :
        if ':' not in l :
            user_id = netflix_read_user_id(l)
            try :
                userDecAvg = userDecDict[user_id][str(movieDecade)]['total'] / userDecDict[user_id][str(movieDecade)]['count']
            except KeyError :
                userDecAvg = 0
            prediction = netflix_predict(userAvgDict[user_id],movieAvgDict[movie_id], userDecAvg)
            actual_rating = netflix_rating(movie_id, user_id, solutionsDict)
            sqrDiff += sqre_diff(actual_rating,prediction)
            c += 1
            netflix_write(prediction, w)
        else :
           #obtains the movie ID from the file 
           #and calls the corresponding cache to get 
           #the movie's average
            movie_id = netflix_read_movie_id(l)
            movieDecade = movieDecDict[movie_id]
            netflix_write(str(movie_id) + ':', w)
            
    solutionsCache.close()
    userAvg.close()
    movieAvg.close()
    userDec.close()
    movieDec.close()

    netflix_write("RMSE: " + str(rmse(sqrDiff,c)), w)
    print("--- %s seconds ---" % (time.time() - start_time))
    return rmse

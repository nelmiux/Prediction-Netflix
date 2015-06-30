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
# netflix_sqre_diff
# ------------

def netflix_sqre_diff(a, p) :
    """
    returns ( a - p ) squared
    """
    return (a - p) ** 2

# ------------
# netflix_write
# ------------

def netflix_write (s, w) :
    """
    writes the object s to the writer w.
    It appends a new line too.
    """
    
    w.write(str(s) + "\n")

# ------------
# netflix_predict
# ------------

def netflix_predict(userAvg,  movieAvg, userDecAvg) :
    """
    predict the user rating using a linear progression
    """
    assert ( 0 < userAvg <= 5)
    assert ( 0 < movieAvg <= 5)
<<<<<<< HEAD
    assert ( 0 <= userDecAvg <= 5)    
    if (userDecAvg == 0) :
        return round(userAvg * 0.521 + movieAvg * 0.52 - 0.14, 1)
=======
    assert ( 0 <= userDecAvg <= 5) 
>>>>>>> origin/master
    return round(userDecAvg * 0.7 + movieAvg * 0.3, 1) 

# ------------
# netflix_rmse
# ------------

def netflix_rmse (sqrDiff, count) :
    """
    rmse calculates the root mean square error.
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
    userAvg  = open("ezo55-Average_Viewer_Rating_Cache.json", "r")
    userAvgDict   = json.loads(userAvg.read())
    movieAvg = open("BRG564-Average_Movie_Rating_Cache.json", "r")
    movieAvgDict = json.loads(movieAvg.read())
    userDec = open("drc2582-customer_decade_dict.json", "r")
    userDecDict = json.loads(userDec.read())
    movieDec = open("pra359-Movie_Decades_Cache.json", "r")
    movieDecDict = json.loads(movieDec.read())

    #loop through the file and obtain the total average
    l = r.readline().strip()
    while (l) :
        if ':' not in l :
            user_id = l
            try :
                userDecAvg = userDecDict[user_id][str(movieDecade)]['total'] / userDecDict[user_id][str(movieDecade)]['count']
            except KeyError:
                userDecAvg = 0
            prediction = netflix_predict(userAvgDict[user_id],movieAvgDict[movie_id], userDecAvg)
            actual_rating = solutionsDict[movie_id][user_id]
            sqrDiff += netflix_sqre_diff(actual_rating,prediction)
            c += 1
            netflix_write(prediction, w)
        else :
           #obtains the movie ID from the file 
           #and calls the corresponding cache to get 
           #the movie's average
            movie_id = l[:-1]
            movieDecade = movieDecDict[movie_id]
            netflix_write(str(movie_id) + ':', w)
        l = r.readline().strip()
            
    solutionsCache.close()
    userAvg.close()
    movieAvg.close()
    userDec.close()
    movieDec.close()
    rmse = netflix_rmse(sqrDiff,c)
    netflix_write("RMSE: " + str(rmse), w)
    #print("--- %s seconds ---" % (time.time() - start_time))
    return rmse

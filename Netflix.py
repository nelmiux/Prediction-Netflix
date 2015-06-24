#!/usr/bin/env python3

import os
import urllib.request
import re
import io
import ctypes
import math
import json

total_avg = 3.7

# ------------
# netflix_avg_movie
# ------------

def netflix_avg_movie (movie_id) :
    '''
        param: movie_id
        description: The variable data has the access to the cache.
                     (keys,values) = (movies ID,movie's average)
        return: The overall average of the movie corresponding to the movie_id
    '''
    assert movie_id != {}

    url = "http://www.cs.utexas.edu/~ebanner/netflix-tests/BRG564-Average_Movie_Rating_Cache.json"
    r = urllib.request.urlopen(url)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))

    avg = data[movie_id]

    assert 1.0 <= avg <= 5.0
    return avg


# ------------
# netflix_avg_user
# ------------
    
<<<<<<< HEAD
def netflix_avg_user (user_id) :
    '''
        param: user_id
        description: The variable data has the access to the cache.
                     (keys,values) = (user ID,user's average)
        return: The overall average of the user corresponding tot he user_id
    '''
    assert user_id != {}
    url = "http://www.cs.utexas.edu/~ebanner/netflix-tests/ezo55-Average_Viewer_Rating_And_True_Variance_Cache.json"
    r = urllib.request.urlopen(url)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
    
    avg = data[user_id][0]
=======
def netflix_avg_user (user_id, rating, d, d1) :
    uavg = 0
    if ((len(d) == 0) or (user_id not in d)) :
        d[user_id] = [rating, 1, rating]
        d1[user_id] = rating
        uavg = rating
    else :
        t0 = d[user_id][0]
        sum_user = int(t0) + int(rating)
        t1 = d[user_id][1]
        count_movies = int(t1) + 1
        uavg = sum_user / float(count_movies)  
        d[user_id][0] = sum_user
        d[user_id][1] = count_movies
        d[user_id][2] = uavg
        d1[user_id] = uavg
    return uavg
>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc

    assert 1.0 <= avg <= 5.0
    return avg

# ------------
# netflix_rating
# ------------

def netflix_rating (movie_id, user_id):
    '''
        param: movie_id, user_id
        description: The variable data has the access to the cache.
                     (movie: {user: rate}) 
        return the average of the movie 
    '''
    assert user_id != {}

    url = "http://www.cs.utexas.edu/~ebanner/netflix-tests/pam2599-probe_solutions.json"
    r = urllib.request.urlopen(url)
    data = json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))

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
    return line[:-2]

# ------------
# netflix_read_user_id
# ------------

#return the user_id from the line obtain from the input file
def netflix_read_user_id(line) :
<<<<<<< HEAD
    assert line != {}
    return line[:-1]

=======
    return line[:-14]

def netflix_read_rating(line) :
    return line[-13:-12]

>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc
# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
<<<<<<< HEAD
    """
    r a reader
    w a writer
    """
    
=======
    
    d = dict()
    d1 = dict()
>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc
    movie_id = -1
    tavg = 0 
    tsum = 0
<<<<<<< HEAD
    count = 0
    dt = dict()

    #loop through the file and obtain the total average
    for l in r :
        if (l[len(l)-2] != ':') :
            user_id = netflix_read_user_id(l)
            uavg = netflix_avg_user (user_id)
            dt.update({user_id:uavg})
            tavg = tavg + uavg
            count = count + 1

    tavg = tavg/count
    assert 1.0 <= tavg <= 5.0

    #move the counter to the start of the file
    r.seek(0)


    for s in r :
      
=======
    tsum2 = 0
    tcount = 0
    s = r.readline()
    while s != '\n' and s != '' : 
        l = s.split()
>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc
        if (s[len(s)-2] == ':') :
           #obtains the movie ID from the file 
           #and calls the corresponding cache to get 
           #the movie's average
            movie_id = netflix_read_movie_id(s)
<<<<<<< HEAD
            w.write(str(movie_id) + ':\n')
            mavg = netflix_avg_movie (movie_id)
        else :
            #obtains the user ID from the file. 
            #Calls the corresponding cache to get 
            #the user's average
            user_id = netflix_read_user_id(s)
            uavg = dt[user_id]
            actual_rating = netflix_rating(movie_id, user_id)
            #our prediction for the user's rating
            prediction = (uavg * 0.521) + (mavg * 0.52) - 0.14
            temp = prediction
            temp = round(temp,1)
            w.write(str(temp) + '\n')

            #means square error calculation
            value = float(actual_rating - prediction)
            tsum += math.pow(value, 2)
    
   
    #rmse calculation 
    t7 = tsum / (float(count))
    rmse = math.sqrt(t7)
    rmse = round(rmse, 2)
    assert rmse > 0
    w.write('RMSE = ' + str(rmse) + '\n')
    return rmse
=======
            t = netflix_avg_movie (movie_id)
            with open("data.txt",'a+') as f: 
                f.write(s)
            s = r.readline()
        else :
            movie_file = netflix_read_movie_files (movie_id)
            user_id = netflix_read_user_id(s)
            t2 = movie_file.readline()
            t2 = movie_file.readline()
            while t2 != '\n' and t2 != '' : 
                if (user_id) in t2 :
                    rating = int(netflix_read_rating(t2))
                    uavg = netflix_avg_user (user_id, rating, d, d1)
                    predicted = ((t + uavg ) / float(2))
                    tcount = tcount + 1
                    f1 = open("result.txt",'a+')
                    t5 = float(rating - predicted)
                    t6 = abs(t5)
                    f1.write(str(user_id) + ',' + str(predicted) + '\n')
                    math.pow(t6, 2)
                    tsum += t6
                    tsum2 += predicted
                    with open("data.txt",'a+') as f: 
                        f.write(t2)
                    f1.close()
                t2 = movie_file.readline()
            movie_file.close()
        s = r.readline()
    f1 = open("result.txt",'a+')
    t1 = r.readline()
    t7 = tsum / (float(tcount))
    rmse = math.sqrt(t7)
    rmse = round(t7, 2)
    f1.write('RMSE = ' + str(rmse))
    f1.close()
    b = (movie_id != -1)
    return b
>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc

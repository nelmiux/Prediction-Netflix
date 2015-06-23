#!/usr/bin/env python3

import os
import urllib.request
import re
from collections import defaultdict
import io
import ctypes
import math
# ------------
# netflix_rating_list
# ------------

def netflix_avg_movie (movie_id) :
    movie_file = netflix_read_movie_files (movie_id)
    sum_movie = 0
    count_users = 0
    t2 = movie_file.readline()
    t2 = movie_file.readline()
    while t2 != '\n' and t2 != '' : 
        sum_movie += float(t2[-13:-12])
        count_users += 1
        t2 = movie_file.readline() 
    assert (count_users != 0)
    avg =  sum_movie / float(count_users)
    movie_file.close()
    return avg
    
def netflix_avg_user (user_id, rating, d, d1) :
    uavg = 0
    if ((len(d) == 0) or (user_id not in d)) :
        d[user_id] = [rating, 1, rating]
        d1[user_id] = rating
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


# ------------
# netflix_read
# ------------

def netflix_read_movie_files (movie_id) :
    """

    """
    file_name = 'mv_' + (('0' * (7 - len(str(movie_id)))) + str(movie_id)) + '.txt'
    # movie_file = open("/media/sf_Work/GitHub/private/cs373-netflix/" + file_name)
    movie_file = open("/u/downing/cs/netflix/training_set/" + file_name)
    # movie_file = urllib.request.urlopen('http://www.cs.utexas.edu/users/downing/netflix/training_set/' + file_name)

    return movie_file

# ------------
# netflix_read
# ------------

def netflix_read_movie_id (line) :
    """

    """
    return line[:-2]

def netflix_read_user_id(line) :
    return line[:-1]

def netflix_read_rating(line) :
    return line[-13:-12]

def netflix_write_data_file (line) :
    with open("data.txt",'a+') as f: 
        f.write(line)
    return f

# ------------
# netflix_eval
# ------------

def netflix_eval (l) :
    """
 
    """
    

# -------------
# netflix_print
# -------------

def netflix_print (user_id, predicted) :
    """
    
    """
    f = open("result.txt",'a+')
    return f

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """
    d = dict()
    d1 = dict()
    movie_id = -1
    tsum = 0
    tcount = 0
    tsum2 = 0
    for s in r :
        if (s[len(s)-2] == ':') :
            movie_id = netflix_read_movie_id(s)
            t = netflix_avg_movie (movie_id)
            netflix_write_data_file (s)
        else :
            user_id = netflix_read_user_id(s)
            movie_file = netflix_read_movie_files (movie_id)
            t2 = movie_file.readline()
            t2 = movie_file.readline()
            while t2 != '\n' and t2 != '' : 
                if (user_id) in t2 :
                    rating = int(netflix_read_rating(t2))
                    uavg = netflix_avg_user (user_id, rating, d, d1)
                    predicted = (t + uavg / float(2))
                    tcount = tcount + 1
                    print(tcount)
                    f1 = netflix_print(user_id, predicted)
                    t5 = float(rating - predicted)
                    t6 = abs(t5)
                    f1.write(str(user_id) + ',' + str(predicted) + '\n')
                    math.pow(t6, 2)
                    tsum += t6
                    tsum2 += predicted
                    netflix_write_data_file (t2)
                t2 = movie_file.readline()
            movie_file.close()
    t1 = r.readline()
    t7 = tsum / (float(tcount))
    rmse = 1 / float(1.0)
    rmse = math.sqrt(t7)
    f1.write('         ' + str(rmse))
    print(str(rmse))

#!/usr/bin/env python3

import os
import urllib.request
import re
import io
import ctypes
import math

total_avg = 3.7

# ------------
# netflix_avg_movie
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

# ------------
# netflix_avg_user
# ------------
    
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


# ------------
# netflix_read_movie_files
# ------------

def netflix_read_movie_files (movie_id) :
    """

    """
    file_name = 'mv_' + (('0' * (7 - len(str(movie_id)))) + str(movie_id)) + '.txt'
    # movie_file = open("/media/sf_Work/GitHub/private/cs373-netflix/" + file_name)
    movie_file = open("/u/downing/cs/netflix/training_set/" + file_name)
    # movie_file = urllib.request.urlopen('http://www.cs.utexas.edu/users/downing/netflix/training_set/' + file_name)

    return movie_file


def netflix_read_movie_id (line) :
    return line[:-2]

def netflix_read_user_id(line) :
    return line[:-14]

def netflix_read_rating(line) :
    return line[-13:-12]

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    
    d = dict()
    d1 = dict()
    movie_id = -1
    tsum = 0
    tsum2 = 0
    tcount = 0
    s = r.readline()
    while s != '\n' and s != '' : 
        l = s.split()
        if (s[len(s)-2] == ':') :
            movie_id = netflix_read_movie_id(s)
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
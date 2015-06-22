#!/usr/bin/env python3

import os
import urllib.request
import re
from collections import defaultdict
import io
import ctypes

# ------------
# netflix_rating_list
# ------------

def netflix_avg_movie (movie_file) :
    sum_movie = 0
    count_users = 0
    # path = "/u/downing/cs/netflix/training_set/"
    # movie_file = urllib.request.urlopen('http://www.cs.utexas.edu/users/downing/netflix/training_set/' + file_name)
    t2 = movie_file.readline()
    t2 = movie_file.readline()
    while t2 != '\n' and t2 != '' : 
        sum_movie += float(t2[-13:-12])
        count_users += 1
        t2 = movie_file.readline() 
    assert (count_users != 0)
    avg =  sum_movie / float(count_users)
    return avg

def netflix_user_data (d, user_id, rating) :
    """
    This make a dictionary to be used after to compute the users per movie avg
    it will return the dictionary of the relation sum of all user's rating per 
    movie and number of movies
    """
    if (user_id) in d :
        # index = d.keys().index(user_id)
        sum_user = 0
        count_movies = int(d[user_id][1]) + 1
        sum_user = int(d[user_id][0]) + int(rating)
        avg = sum_user / float(count_movies)
        d[user_id][0] = sum_user
        d[user_id][1] = count_movies
        d[user_id][2] = avg
    else :
        d.update({user_id: [int(rating), 1, 0]})
    return d

# ------------
# netflix_read
# ------------

def netflix_read_movie_files (movie_id) :
    """

    """
    file_name = 'mv_' + (('0' * (7 - len(str(movie_id)))) + str(movie_id)) + '.txt'
    # movie_file = open("/media/sf_Work/GitHub/private/cs373-netflix/" + file_name)
    # movie_file = open("/u/downing/cs/netflix/training_set/" + file_name)
    libc = ctypes.cdll.LoadLibrary('libc.so.6')
    res_init = libc.__res_init
    res_init()
    movie_file = urllib.request.urlopen('http://www.cs.utexas.edu/users/downing/netflix/training_set/' + file_name)

    return movie_file.read().decode('utf-8')

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
    with open("data.txt","a+") as f: 
        f.write(line)
    return f

    """
    t1 = r.readline()
    sum_movie = 0
    movie_id = -1
    count_movie = 0
    l1 = []
    while t1 != '\n' and t1 != '' : 
        if (t1[len(t1) - 2] == ':') :               
            movie_id = t1[:-2]
            file_name = 'mv_' + (('0' * (7 - len(str(movie_id)))) + str(movie_id)) + '.txt'
            movie_file = open("/media/sf_Work/GitHub/private/cs373-netflix/" + file_name)
            t4 = netflix_avg_movie (movie_file)
            avg_movies = []
            avg_movies = [movie_id, t4]
            with open("data.txt","a+") as f:
                f.write(movie_id + ':\n')
            movie_file.close()
            l1 = []
        else :
            user_id = t1[:-1]
            movie_file = open("/media/sf_Work/GitHub/private/cs373-netflix/" + file_name)
            t2 = movie_file.readline()
            t2 = movie_file.readline()
            while t2 != '\n' and t2 != '' : 
                if (user_id) in t2 :
                    rating = t2[-13:-12]
                    with open("data.txt","a+") as f:
                        f.write(t2)
                t2 = movie_file.readline()
            movie_file.close()
            l1.append(int(t1[:-1]))
            d1[movie_id] = l1
        t1 = r.readline()
    movie_file.close()
    print(avg_movies)

    return d1
    """
    

# ------------
# netflix_eval
# ------------

def netflix_eval (l) :
    """
 
    """
    

# -------------
# netflix_print
# -------------

def netflix_print (w, l, k) :
    """
    
    """
    try :
        assert ((type(l) is dict) and (type(k) is int))
        assert (k > 0)
        assert (w is not None)
        w.write(str(i) + " " + str(l) + " " + str(k) + "\n")
    except (AssertionError, OverflowError, MemoryError) :
        w.write("")

# -------------
# netflix_solve
# -------------

def netflix_solve (r, w) :
    """
    r a reader
    w a writer
    """
    movie_id = -1
    d = defaultdict(list)
    t1 = r.readline()
    while t1 != '\n' and t1 != '' :
        if (t1[len(t1) - 2] == ':') :               
            movie_id = netflix_read_movie_id(t1)
            movie_file = netflix_read_movie_files (movie_id)
            t4 = netflix_avg_movie (movie_file)
            netflix_write_data_file (t1)
            movie_file.close()
        else :
            user_id = netflix_read_user_id(t1)
            movie_file = netflix_read_movie_files (movie_id)
            t2 = movie_file.readline()
            t2 = movie_file.readline()
            while t2 != '\n' and t2 != '' : 
                if (user_id) in t2 :
                    netflix_write_data_file (t2)
                t2 = movie_file.readline()
            movie_file.close()
        t1 = r.readline()
    f = io.StringIO(open('data.txt').read())
    for s in f :
        if (s[len(s) - 2] == ':') :
            movie_id = netflix_read_movie_id(t1)
        else :
            user_id = s[:-14]
            rating = netflix_read_rating(s)
            print(netflix_user_data (d, user_id, rating).items())

    os.remove('data.txt')
    

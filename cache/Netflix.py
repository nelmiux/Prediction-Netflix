#!/usr/bin/env python3

import sys

def netflix_avg_movie (movie_file) :
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
    return avg

def read_write (d) :
    for i in range(1, 17771) :
        file_name = 'mv_' + (('0' * (7 - len(str(i)))) + str(i)) + '.txt'
        f = open("/u/downing/cs/netflix/training_set/" + file_name)
        mavg = netflix_avg_movie (f)
        f.close()
        f = open("/u/downing/cs/netflix/training_set/" + file_name)
        for s in f :
            if (s[len(s) - 2] != ':') :
                user_id = s[:-14]
                rating = s[-13:-12]
                if ((len(d) == 0) or (user_id not in d)) :
                     d[user_id] = [rating, 1, 0.0]
                     d1[user_id] = 0
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

        with open("Avg_Movie_Ratings.txt","w+") as f: 
            f.write(str(i) + ',' + str(mavg) + '\n')
                    
        with open("Avg_User_Ratings.txt","w+") as f:
            keys = d1.keys()

            for each in keys:
                f.write (str(each) + ',' + str(d1.get(each)))
                
if __name__ == "__main__" :
    d = dict()
    d1 = dict()
    read_write (d)


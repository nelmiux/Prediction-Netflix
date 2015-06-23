#!/usr/bin/env python3


# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

import io
from unittest import main, TestCase

from Netflix import  netflix_solve ,netflix_print, netflix_eval,netflix_write_data_file,netflix_read_rating,netflix_read_user_id,netflix_read_movie_id ,netflix_avg_movie, netflix_avg_user,netflix_read_movie_files  

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

    # ------------
    # netflix_avg
    # ------------

    def test_movie_avg_1(self) :
        s = "1454193,5,1997-02-07\n"
        avg = netflix_avg_movie(s)
        self.assertEqual(s,5)

    def test_movie_avg_2(self) :
        s = "1488844,3,2005-09-06\n822109,5,2005-05-13\n885013,4,2005-10-19\n30878,4,2005-12-26\n"
        avg = netflix_avg_movie(s)
        self.assertEqual(s,4)

    def test_movie_avg_3(self) :
        s = "1116080,5,2005-08-08\n255443,2,2005-05-23\n2460625,3,2005-03-21\n1621184,5,2005-06-26\n2404795,4,2005-09-21\n"
        avg = netflix_avg_movie(s)
        self.assertEqual(s,3.8)

    def test_movie_avg_4(self) :
        s = "1361273,5,2006-06-06\n2917453,5,2003-04-10\n1826419,5,2000-12-09\n"
        avg = netflix_avg_movie(s)
        self.assertEqual(s,5)

    def test_movie_avg_5(self) :
        s = ""
        self.expectedFailure(netflix_avg_movie(s))

    #--------
    # user
    #--------

   
    
    def test_user_avg_1(self) :
        dic = dict()
        initial_len = len(dic)
        dic1 = dict()
        user_id = '1010112'
        rating = 5
        user_avg = netflix_avg_user(user_id,rating,dic,dic1)
        self.assertEqual(user_avg, 2)
        self.assertEqual(dic[user_id][0], 5)
        self.assertEqual(dic[user_id][1], 1)
        self.assertEqual(dic[user_id][2], 5)
        self.assertEqual(len(dic), initial_len+1)

    def test_user_avg_2(self) :
        dic = {'1010112' :[5,1,5],'156078': [3,1,3]}
        dic1 = {'156078': 3}
        user_id = '156078'
        rating = 2
        avg = netflix_avg_user(user_id,rating,dic,dic1)
        self.assertEqual(dic[user_id][0], 5)
        self.assertEqual(dic[user_id][1], 2)
        self.assertEqual(dic[user_id][2], 2.5)

    def test_user_avg_3(self) :
        dic = {'156078': [5,2,2.5], '2558337' :[22,6,4.3333333], '1936287' : [1,1,1],'1122423' : [34,10,3.4], '8163045' : [20,7,2.85714286]}
        dic1 = {'156078': 2.5, '2558337' :4.3333333, '1936287' : 1 ,'1122423' : 3.4, '8163045' : 2.85714286}
        user_id = '1122423'
        rating = 4
        avg = netflix_avg_user(user_id,rating,dic,dic1)
        self.assertEqual(dic[user_id][0], 38)
        self.assertEqual(dic[user_id][1], 11)
        self.assertEqual(dic[user_id][2], 3.45454545)

    # ----
    # read
    # ----
    '''
    def test_read_1 (self) :
        r = io.StringIO("1:\n1\n2\n3\n4:\n9\n12\n15\n32\n")
        l = netflix_read (r)
        self.assertEqual(l, {'1': [1, 2, 3], '4': [9, 12, 15, 32]})

    def test_read_1 (self) :
        r = io.StringIO("5:\n12\n9\n41\n7:\n4\n97\n1\n6\n12\n14\n15:\n7\n8\n10\n11\n24:\n1\n60:\n2\n3\n")
        l = netflix_read (r)
        self.assertEqual(l, {'5': [12, 9, 41], '7': [4, 97, 1, 6, 12, 14],'15': [7, 8, 10, 11], '24': [1] ,'60': [2, 3] })

    def test_read_1 (self) :
        r = io.StringIO("60:\n77\n")
        l = netflix_read (r)
        self.assertEqual(l, {'60': [77]})

    def test_read_1 (self) :
        r = io.StringIO("1:\n")
        l = netflix_read (r)
        self.assertEqual(l, {'1': []})


    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = netflix_eval()
        self.assertEqual(v, 1)
  
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        t = netflix_print()
        self.assertEqual(w.getvalue(), t)

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "")

    def test_solve (self) :
        r = StringIO("")
        w = StringIO()
        netflix_solve(r, w)
        self.assertTrue(w.getvalue() < 1.0)

    def test_solve (self) :
        r = StringIO("")
        w = StringIO()
        netflix_solve(r, w)
        self.assertTrue(w.getvalue() < 0.95)
    '''

# ----
# main
# ----

if __name__ == "__main__" :
    main()

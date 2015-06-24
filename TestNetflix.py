#!/usr/bin/env python3


# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import  netflix_avg_movie, netflix_avg_user, netflix_read_movie_id, netflix_read_user_id, netflix_rating, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

    # ------------
    #  test_netflix_avg_movie
    # ------------

    def test_netflix_avg_movie_1(self) :
        s = "1"
        r_avg = 3.749542961608775
        avg = netflix_avg_movie(s)
        self.assertEqual(avg,r_avg)
    
    def test_netflix_avg_movie_2(self) :
        s = "2"
        r_avg = 3.5586206896551724
        avg = netflix_avg_movie(s)
        self.assertEqual(avg,r_avg)

    def test_netflix_avg_movie_3(self) :
        s = "17770"
        r_avg = 2.816503800217155
        avg = netflix_avg_movie(s)
        self.assertEqual(avg,r_avg)

    def test_netflix_avg_movie_4(self) :
        s = "8274"
        r_avg = 3.887323943661972
        avg = netflix_avg_movie(s)
        self.assertEqual(avg,r_avg)

    #--------
    # test_netflix_avg_user
    #--------

    def test_netflix_avg_user_1(self) :
        user_id = '378466'
        rating = 4.4515539305301646
        user_avg = netflix_avg_user(user_id)
        self.assertEqual(user_avg, rating)

    def test_netflix_avg_user_2(self) :
        user_id = '1197733'
        rating = 3.5
        user_avg = netflix_avg_user(user_id)
        self.assertEqual(user_avg, rating)

    def test_netflix_avg_user_3(self) :
        user_id = '585188'
        rating = 3.9285714285714284
        user_avg = netflix_avg_user(user_id)
        self.assertEqual(user_avg, rating)

    #--------------------
    # test_read_movie_id
    #-------------------

    def test_read_movie_id_1 (self) :
        line = str("17757:\n")
        ans  = "17757"
        result = netflix_read_movie_id (line) 
        self.assertEqual(result,ans)

    def test_read_movie_id_2 (self) :
        line = "12:\n"
        ans  = "12"
        result = netflix_read_movie_id (line) 
        self.assertEqual(result,ans)

    def test_read_movie_id_3 (self) :
        line = "9732:\n"
        ans  = "9732"
        result = netflix_read_movie_id (line) 
        self.assertEqual(result,ans)

    def test_read_movie_id_4 (self) :
        line = "73:\n"
        ans  = "73"
        result = netflix_read_movie_id (line) 
        self.assertEqual(result,ans)

    def test_read_movie_id_5 (self) :
        line = "19378:\n"
        ans  = "19378"
        result = netflix_read_movie_id (line) 
        self.assertEqual(result,ans)


    #--------------------
    # netflix_read_user_id 
    #-------------------

    def test_netflix_read_user_id_1(self) :
        line = "716091\n"
        ans  = "716091"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)

    def test_netflix_read_user_id_2(self) :
        line = "1242432\n"
        ans  = "1242432"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)

    def test_netflix_read_user_id_3(self) :
        line = "1646405\n"
        ans  = "1646405"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)
    
    def test_netflix_read_user_id_4(self) :
        line = "2565022\n"
        ans  = "2565022"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)

    def test_netflix_read_user_id_5(self) :
        line = "2095153\n"
        ans  = "2095153"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)

    #--------------------
    # netflix_rating
    #-------------------

    def test_netflix_rating_1(self) :
        movie_id = "4446"
        user_id = "1657689"
        result = netflix_rating(movie_id, user_id)
        ans = 3
        self.assertEqual(result,ans)

    def test_netflix_rating_2(self) :
        movie_id = "8082"
        user_id = "2639376"
        result = netflix_rating(movie_id, user_id)
        ans = 5
        self.assertEqual(result,ans)

    def test_netflix_rating_3(self) :
        movie_id = "16429"
        user_id = "1002523"
        result = netflix_rating(movie_id, user_id)
        ans = 3
        self.assertEqual(result,ans)

    #--------------------
    # netflix_solve
    #-------------------

    def test_netflix_solve (self) :
        w = StringIO()
        r = StringIO("1:\n1283744\n10:\n1952305\n1531863\n1000:\n2326571\n")
        result = netflix_solve (r, w)
        self.assertTrue(result < 1.0)

# ----
# main
# ----

if __name__ == "__main__" :
    main()
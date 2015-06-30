#!/usr/bin/env python3


# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import  netflix_read_movie_id, netflix_read_user_id, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

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
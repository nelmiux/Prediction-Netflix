#!/usr/bin/env python3


# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

<<<<<<< HEAD
from Netflix import  netflix_avg_movie, netflix_avg_user, netflix_read_movie_id, netflix_read_user_id, netflix_rating, netflix_solve
=======
from Netflix import  netflix_solve, netflix_read_rating,  netflix_read_movie_id, netflix_avg_movie, netflix_avg_user, netflix_read_movie_files, netflix_read_user_id  
>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc

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

<<<<<<< HEAD
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

=======
    def test_user_avg_1(self) :
        dic = dict()
        initial_len = len(dic)
        dic1 = dict()
        user_id = '1010112'
        rating = 5
        user_avg = netflix_avg_user(user_id,rating,dic,dic1)
        self.assertEqual(user_avg, rating)
        self.assertEqual(dic[user_id][0], rating)
        self.assertEqual(dic[user_id][1], 1)
        self.assertEqual(dic[user_id][2], rating)
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

    def test_user_avg_4(self) :
        dic = {'156078': [5,2,2.5], '2558337' :[22,6,4.3333333], '1936287' : [1,1,1],'1122423' : [34,10,3.4], '8163045' : [20,7,2.85714286]}
        dic1 = {'156078': 2.5, '2558337' :4.3333333, '1936287' : 1 ,'1122423' : 3.4, '8163045' : 2.85714286}
        user_id = '1122423'
        rating = 4
        avg = netflix_avg_user(user_id,rating,dic,dic1)
        self.assertEqual(dic[user_id][1], 11)

    def test_user_avg_5(self) :
        dic = {'156078': [5,2,2.5], '2558337' :[22,6,4.3333333], '1936287' : [1,1,1],'1122423' : [34,10,3.4], '8163045' : [20,7,2.85714286]}
        dic1 = {'156078': 2.5, '2558337' :4.3333333, '1936287' : 1 ,'1122423' : 3.4, '8163045' : 2.85714286}
        user_id = '1122423'
        rating = 4
        avg = netflix_avg_user(user_id,rating,dic,dic1)
        self.assertEqual(dic[user_id][2], (38/11))

    def test_user_avg_6(self) :
        dic = {'156078': [5,2,2.5], '2558337' :[22,6,4.3333333], '1936287' : [1,1,1],'1122423' : [34,10,3.4], '8163045' : [20,7,2.85714286]}
        dic1 = {'156078': 2.5, '2558337' :4.3333333, '1936287' : 1 ,'1122423' : 3.4, '8163045' : 2.85714286}
        user_id = '1122423'
        rating = 4
        avg = netflix_avg_user(user_id,rating,dic,dic1)
        not_change = "156078"
        self.assertEqual(dic[not_change][2], 2.5)
  
>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc
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

    def test_read_user_id_1(self) :
<<<<<<< HEAD
        line = "716091\n"
=======
        line = "716091,4,2000-01-08\n"
>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc
        ans  = "716091"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)

    def test_read_user_id_2(self) :
<<<<<<< HEAD
        line = "1242432\n"
=======
        line = "1242432,3,2005-03-05\n"
>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc
        ans  = "1242432"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)

    def test_read_user_id_3(self) :
<<<<<<< HEAD
        line = "1646405\n"
=======
        line = "1646405,3,2005-07-18\n"
>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc
        ans  = "1646405"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)
    
    def test_read_user_id_4(self) :
<<<<<<< HEAD
        line = "2565022\n"
=======
        line = "2565022,3,2004-11-19\n"
>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc
        ans  = "2565022"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)

    def test_read_user_id_5(self) :
<<<<<<< HEAD
        line = "2095153\n"
=======
        line = "2095153,3,2004-11-07\n"
>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc
        ans  = "2095153"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)

    #--------------------
<<<<<<< HEAD
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
=======
    # netflix_read_rating
    #-------------------

    def test_read_rating_1(self) :
        line = "716091,4,2000-01-08\n"
        ans  = "4"
        result = netflix_read_rating(line) 
        self.assertEqual(result,ans)

    def test_read_rating_2(self) :
        line = "1242432,3,2005-03-05\n"
        ans  = "3"
        result = netflix_read_rating (line) 
        self.assertEqual(result,ans)

    def test_read_rating_3(self) :
        line = "1646405,5,2005-07-18\n"
        ans  = "5"
        result = netflix_read_rating (line) 
        self.assertEqual(result,ans)

    def test_read_rating_4(self) :
        line = "169989,1,2005-06-16\n"
        ans  = "1"
        result = netflix_read_rating (line) 
        self.assertEqual(result,ans)

    def test_read_rating_5(self) :
        line = "2103032,2,2004-03-12\n"
        ans  = "2"
        result = netflix_read_rating (line) 
        self.assertEqual(result,ans)

    #--------------------
    # test_netflix_solve
>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc
    #-------------------

    def test_netflix_solve (self) :
        w = StringIO()
<<<<<<< HEAD
        r = StringIO("1:\n1283744\n10:\n1952305\n1531863\n1000:\n2326571\n")
        result = netflix_solve (r, w)
        self.assertTrue(result < 1.0)
=======
        r = StringIO("2915:\n1293710\n1374201\n2179492\n837304\n205:\n1595943\n1502149\n1974369\n1418772\n")
        result = netflix_solve (r, w)
        self.assertEqual(result,1)
>>>>>>> 5768cc84a21ec0eb27e0f3610d32d4c20a9a0cbc

# ----
# main
# ----

if __name__ == "__main__" :
    main()
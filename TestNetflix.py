#!/usr/bin/env python3


# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import  netflix_solve, netflix_read_rating,  netflix_read_movie_id, netflix_avg_movie, netflix_avg_user, netflix_read_movie_files, netflix_read_user_id  

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

    # ------------
    #  test_movie_avg
    # ------------

    def test_movie_avg_1(self) :
        s = "0000001"
        r_avg = ((28)+(31*2)+(136*3)+(207*4)+(145*5))/547;
        avg = netflix_avg_movie(s)
        print(avg)
        self.assertEqual(avg,r_avg)
    
    def test_movie_avg_2(self) :
        s = "0000036"
        r_avg = ((109)+(148*2)+(387*3)+(205*4)+(90*5))/939;
        avg = netflix_avg_movie(s)
        self.assertEqual(avg,r_avg)

    def test_movie_avg_3(self) :
        s = "0008686"
        r_avg = ((27)+(28*2)+(70*3)+(23*4)+(6*5))/154;
        avg = netflix_avg_movie(s)
        self.assertEqual(avg,r_avg)

    def test_movie_avg_4(self) :
        s = "0013581"
        r_avg = ((75)+(56*2)+(253*3)+(404*4)+(317*5))/1105;
        avg = netflix_avg_movie(s)
        self.assertEqual(avg,r_avg)

    #--------
    # test_user_avg
    #--------

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
        line = "716091,4,2000-01-08\n"
        ans  = "716091"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)

    def test_read_user_id_2(self) :
        line = "1242432,3,2005-03-05\n"
        ans  = "1242432"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)

    def test_read_user_id_3(self) :
        line = "1646405,3,2005-07-18\n"
        ans  = "1646405"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)
    
    def test_read_user_id_4(self) :
        line = "2565022,3,2004-11-19\n"
        ans  = "2565022"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)

    def test_read_user_id_5(self) :
        line = "2095153,3,2004-11-07\n"
        ans  = "2095153"
        result = netflix_read_user_id (line) 
        self.assertEqual(result,ans)

    #--------------------
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
    #-------------------

    def test_netflix_solve (self) :
        w = StringIO()
        r = StringIO("2915:\n1293710\n1374201\n2179492\n837304\n205:\n1595943\n1502149\n1974369\n1418772\n")
        result = netflix_solve (r, w)
        self.assertEqual(result,1)

# ----
# main
# ----

if __name__ == "__main__" :
    main()
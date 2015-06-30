#!/usr/bin/env python3


# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_sqre_diff,netflix_write, netflix_predict ,netflix_rmse, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :

    #--------------------
    # test_netflix_sqre_diff
    #-------------------
    def test_netflix_sqre_diff_1 (self) :
        a = 4
        p = 1.1538461538461542
        ans = 8.10059171597632934674556213017764
        result = netflix_sqre_diff(a , p) 
        self.assertEqual(result,ans)

    def test_netflix_sqre_diff_2 (self) :
        a = 3
        p = 2.8500000000000001
        ans = 0.022499999999999975
        result = netflix_sqre_diff(a , p) 
        self.assertEqual(result,ans)

    def test_netflix_sqre_diff_3 (self) :
        a = 1
        p = 3.810810810810811
        ans = 7.900657414170928747991234477721
        result = netflix_sqre_diff(a , p) 
        self.assertEqual(result,ans)

    def test_netflix_sqre_diff_4 (self) :
        a = 5
        p = 4.197270412
        ans = 0.6443747914506498
        result = netflix_sqre_diff(a , p) 
        self.assertEqual(result,ans)

    #--------------------
    # test_netflix_predict
    #-------------------
    def test_netflix_predicte_1 (self) :
        userAvg = 3.1739130434782608 
        movieAvg = 3.239269406392694
        userDecAvg = 3.130434782608696 
        ans = 3.2
        result = netflix_predict(userAvg,  movieAvg, userDecAvg) 
        self.assertEqual(result,ans)

    def test_netflix_predict_2 (self) :
        userAvg = 5.0
        movieAvg = 3.3172147001934236
        userDecAvg = 5.0 
        ans = 4.5
        result = netflix_predict(userAvg,  movieAvg, userDecAvg) 
        self.assertEqual(result,ans)

    def test_netflix_predict_3 (self) :
        userAvg = 3.3333333333333335
        movieAvg = 3.749542961608775
        userDecAvg = 2.2857142857142856 
        ans = 2.7
        result = netflix_predict(userAvg,  movieAvg, userDecAvg) 
        self.assertEqual(result,ans)

    def test_netflix_predict_4 (self) :
        userAvg = 1.83827405
        movieAvg = 2.9217495472
        userDecAvg = 2.81740283 
        ans = 2.8
        result = netflix_predict(userAvg,  movieAvg, userDecAvg) 
        self.assertEqual(result,ans)

    def test_netflix_predict_5 (self) :
        userAvg = 1.83827405
        movieAvg = 2.9217495472
        userDecAvg = 0
        ans = 2.3
        result = netflix_predict(userAvg,  movieAvg, userDecAvg) 
        self.assertEqual(result,ans)
    #--------------------
    # test_netflix_rmse 
    #-------------------
    
    def test_netflix_rmse_1 (self) :
        sqrDiff = 82.27000000000002
        count   = 92
        ans     = 0.95
        result  = netflix_rmse (sqrDiff, count)  
        self.assertEqual(result,ans)

    def test_netflix_rmse_2 (self) :
        sqrDiff = 35.18937
        count   = 40
        ans     = 0.94
        result  = netflix_rmse (sqrDiff, count)  
        self.assertEqual(result,ans)

    def test_netflix_rmse_3 (self) :
        sqrDiff =  100.394782
        count   =   110
        ans     = 0.96
        result  = netflix_rmse (sqrDiff, count)  
        self.assertEqual(result,ans)


    def test_netflix_rmse_4 (self) :
        sqrDiff =  10.2784137
        count   =   9
        ans     = 1.07
        result  = netflix_rmse (sqrDiff, count)  
        self.assertEqual(result,ans)

    #-------------------
    # test_netflix_write
    #------------------
    def test_netflix_write_1(self) :
        w = StringIO()
        r = 0.96
        result = netflix_write(r, w)

    #--------------------
    # netflix_solve
    #-------------------

    def test_netflix_solve_1 (self) :
        w = StringIO()
        r = StringIO("1:\n1283744\n10:\n1952305\n1531863\n1000:\n2326571\n")
        ans = 0.5
        result = netflix_solve (r, w)
        self.assertEqual(result,ans)

    def test_netflix_solve_2 (self) :
        w = StringIO()
        r = StringIO("1:\n30878\n1774623\n10001:\n90355\n10040:\n1207062\n")
        ans = 0.91
        result = netflix_solve (r, w)
        self.assertEqual(result,ans)

    def test_netflix_solve_3 (self) :
        w = StringIO()
        r = StringIO("12150:\n1752432\n10:\n1952305\n12154:\n2604008\n")
        ans = 0.74
        result = netflix_solve (r, w)
        self.assertEqual(result,ans)

    
# ----
# main
# ----

if __name__ == "__main__" :
    main()

#!/usr/bin/env python3


# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s    = ""
        netflix_read()
        self.assertEqual()
        self.assertEqual()


    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = netflix_eval()
        self.assertEqual()
  
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        netflix_print()
        self.assertEqual(w.getvalue(), "")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

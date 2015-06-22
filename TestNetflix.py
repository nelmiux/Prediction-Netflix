#!/usr/bin/env python3


# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

import io
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
        r = io.StringIO("1:\n1\n2\n3\n4:\n9\n12\n15\n32\n")
        l = netflix_read (r)
        self.assertEqual(l, {'1': [1, 2, 3], '4': [9, 12, 15, 32]})

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

# ----
# main
# ----

if __name__ == "__main__" :
    main()

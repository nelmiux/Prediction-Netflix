# CS373-netflix

## Status
![Build Status](https://magnum.travis-ci.com/nelmiux/cs373-netflix.svg?token=d7DyZsL5MGsgRrcqFYN1&branch=master)

Netflix	index
/media/sf_Work/GitHub/private/cs373-netflix/Netflix.py

 
## Modules
      	  	
ctypes  io  json  math  os  re  time  urllib

 
## Functions
      	  	
netflix_predict(userAvg, movieAvg, userDecAvg)
    predict the user rating using a linear progression

netflix_rmse(sqrDiff, count)
    rmse calculates the root mean square error.

netflix_solve(r, w)
    r a reader
    w a writer

netflix_sqre_diff(a, p)
    returns ( a - p ) squared

netflix_write(s, w)
    writes the object s to the writer w.
    It appends a new line too.

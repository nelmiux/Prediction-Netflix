FILES :=                              \
    .travis.yml                       \
    netflix-tests/EID-RunNetflix.in   \
    netflix-tests/EID-RunNetflix.out  \
    netflix-tests/EID-TestNetflix.py  \
    netflix-tests/EID-TestNetflix.out \
    Netflix.html                      \
    Netflix.log                       \
    Netflix.py                        \
    RunNetflix.py                     \
    RunNetflix.in                     \
    RunNetflix.out                    \
    TestNetflix.py                    \
    TestNetflix.out

all:

check:
	@for i in $(FILES);                                         \
    do                                                          \
        [ -e $$i ] && echo "$$i found" || echo "$$i NOT FOUND"; \
    done

clean:
	rm -f  .coverage
	rm -f  *.pyc
	rm -f  Netflix.html
	rm -f  Netflix.log
	rm -f  RunNetflix.out
	rm -f  TestNetflix.out
	rm -rf __pycache__

config:
	git config -l

test: 
	python3 Netflix.py

netflix-tests:
	git clone https://github.com/cs373-summer-2015/netflix-tests.git

Netflix.html: Netflix.py
	pydoc3 -w Netflix

Netflix.log:
	git log > Netflix.log

RunNetflix.out: RunNetflix.py
	cat RunNetflix.in
	/usr/bin/env python3 Netflix.py

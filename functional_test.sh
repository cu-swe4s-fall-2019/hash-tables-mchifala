test -e ssshtest || wget https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run test_overall python analyze_hash.py words.txt 10000 h_mult linear_probing 9999 func_test.png
assert_no_stderr
assert_exit_code 0
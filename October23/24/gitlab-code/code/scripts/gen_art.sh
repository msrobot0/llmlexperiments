#!/bin/bash

code_file=$1

python3 -c "
from art import *
art = text2art(open('$code_file').read(), 'block')
print(art)
" > ascii_art.txt

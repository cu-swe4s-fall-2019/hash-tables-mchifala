import sys
from math import sqrt
from math import floor

def h_ascii(key, n):
    asci_sum = 0
    for char in key:
        asci_sum += ord(char)
        
    try:
        return asci_sum % n
    
    except ZeroDivisionError as inst:
        print("Run-Time Error:", type(inst))
        print("Cannot perform integer division or modulo by zero")
        sys.exit(1)

def h_rolling(key, n):
    p = 53
    m = 2**64
    
    asci_sum = 0
    for c,char in enumerate(key):
        asci_sum += ord(char) * p ** c
    
    try:
        asci_sum = asci_sum % m
        
    except ZeroDivisionError as inst:
        print("Run-Time Error:", type(inst))
        print("Cannot perform integer division or modulo by zero")
        sys.exit(1)
    
    try:
        return asci_sum % n
    
    except ZeroDivisionError as inst:
        print("Run-Time Error:", type(inst))
        print("Cannot perform integer division or modulo by zero")
        sys.exit(1)
        
def h_mult(key, n):
    # Per page 264 of Cormen's Introduction to Algorithms 
    A = (sqrt(5)-1)/2
    asci_sum = 0
    for char in key:
        asci_sum += ord(char)
        
    return floor(n*((asci_sum*A)%1))
    
    
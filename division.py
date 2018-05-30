#!/usr/bin/env python
import argparse
import io 

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        'Divide one number by another')
    parser.add_argument('numerator', type=float, help='Numerator')
    parser.add_argument('divisor', type=float, help='Divisor')
    
    args = parser.parse_args()
    try:
<<<<<<< HEAD
        print(args.numerator / args.divisor)
=======
        print(args.numeratorawv7ie72367qwgasdouasdfasffaFS / args.divisor)
>>>>>>> 8028bce2560baba0b8284ff79a0a84d7119dd1ee
    except:
        raise io.RumTimeError

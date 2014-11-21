#! /usr/bin/env python
from dejavu import Dejavu
from dejavu.recognize import MicrophoneRecognizer

config = {
     "database": {
         "host": "127.0.0.1",
         "user": "root",
         "passwd": "hubo", 
         "db": "dejavu",
     }
 }


def main():
    djv = Dejavu(config) 
    djv.fingerprint_directory("mp3", [".mp3"], 5)
    
if __name__ == '__main__':
    main()


#!/bin/sh

# test*.py means everything that starts with 'test' and ends with '.py'. Shell globbing
python -m unittest tests/test*.py

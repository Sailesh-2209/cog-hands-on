# -*- coding: utf-8 -*-

import re
import os


DATA_DIR = 'data'

def get_content(file_path):
    text = ''
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        text = ''.join(lines)
    return text

def parse_currency(text):
    matches = re.findall("([$\u20b9\u00a3][0-9]+\.?[0-9]*)", text)
    print("Matches for currency: ", end=" ")
    print(matches)
    print()

def parse_dates(text):
    matches = re.findall("(\d{2}/\d{2}/\d{2,4})", text)
    print("Matches for date: ", end=" ")
    print(matches)
    print()

def parse_ordinals(text):
    ordinal_nums = re.findall("(\d+(?:st|nd|rd|th))", text)
    ordinals = re.findall(r"first|second|third|(?:four|fif|six|seven|eigh|nin|ten)th", text)
    matches = ordinal_nums + ordinals
    print("Matches for ordinals: ", end=" ")
    print(matches)
    print()

def parse_vowels(text):
    matches = re.findall(r"\b[aeiouAEIOU][a-zA-Z]{3}\b", text)
    print("Matches for words of length 4 starting with vowels: ", end=" ")
    print(matches)
    print()

def parse(text):
    parse_currency(text)
    parse_dates(text)
    parse_ordinals(text)
    parse_vowels(text)

def main():
    file_name = input("Enter the file name: ")
    file_path = os.path.join(DATA_DIR, file_name)
    text = get_content(file_path)
    print("File content: ")
    print(text)
    print()
    parse(text)

if __name__ == "__main__":
    main()


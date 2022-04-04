# -*- coding: utf-8 -*-

import random
import time
import datetime
from num2words import num2words

def generate_currencies():
    currencies = ['$', '\u20b9', '\u00a3']
    values = [round(random.uniform(1, 200), 2) for _ in range(100)]
    combine = []
    flag = False
    for value in values:
        for currency in currencies:
            s = str(currency) + (str(value) if flag else str(int(value)))
            flag = not flag
            combine.append(s)
    vals = [random.choice(combine) for _ in range(30)]
    return vals

def generate_dates():
    format_options = ["%d/%m/%Y", "%d/%m/%y", "%m/%d/%Y", "%m/%d/%y"]
    dates = []
    for _ in range(30):
        year = random.randint(1900, 2022)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        datetime_obj = datetime.datetime(year, month, day)
        date = datetime_obj.strftime(random.choice(format_options))
        dates.append(date)
    return dates

def generate_ordinals():
    to = ["ordinal", "ordinal_num"]
    ordinals = []
    for _ in range(30):
        num = random.randint(1, 200)
        ordinal = num2words(num, to=random.choice(to))
        ordinals.append(ordinal)
    return ordinals

def generate_text(values):
    filename = input("Enter basefile name: ")
    text = ''
    with open(filename) as f:
        file_text = f.readlines();
        for para in file_text:
            lines = para.split(". ")
            for line in lines:
                words = line.split(" ")
                it = random.randint(0, 3)
                for _ in range(it):
                    bp = random.randint(1, len(words))
                    words.insert(bp, random.choice(values))
                newline = ' '.join(words)
                newline += '. '
                text += newline
    return text

def write_to_file(text):
    filename = input("Enter destination file name: ")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)

def main():
    currency_values = generate_currencies()
    date_values = generate_dates()
    ordinal_values = generate_ordinals()
    values = currency_values + date_values + ordinal_values
    text = generate_text(values)
    write_to_file(text)
    # print(text)

if __name__ == "__main__":
    main()


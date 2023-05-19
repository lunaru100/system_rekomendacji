from collections import Counter
from typing import List
from Student import Student

import csv

studenci :List[Student] = []
with open('rekomendacje.csv') as file:
    reader = csv.reader(file)
    for line in reader:
        studenci.append(Student(line[0], line[2:], line[1].split(", ")))


popular = Counter(manga 
                  for student in studenci
                  for manga in student.mangas)

print(f'Proponujemy {", ".join([key[0] for key in popular.most_common(3)])}, jako najbardziej popularne mangi')

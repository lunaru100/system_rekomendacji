from collections import Counter
from typing import List
from Student import Student

import csv

def most_popular(student :Student, studenci: List[Student], max_results = 5):
    popular = Counter(manga 
                    for student in studenci
                    for manga in student.mangas)
    suggestions = [manga[0] for manga in popular.most_common() if manga not in student.mangas]
    return suggestions[:max_results]

def filtrowanie_kolaboratywne_uzytkownicy():
    pass


def filtrowanie_kolaboratywne_zainteresowania():
    pass

def faktoryzacja_macierzy():
    pass

studenci :List[Student] = []
with open('rekomendacje.csv') as file:
    reader = csv.reader(file)
    for line in reader:
        studenci.append(Student(line[0], line[2:], line[1].split(", ")))


print(f'Dla studenta 1  proponujemy s{", ".join([key for key in most_popular(studenci[0], studenci)])}, jako najbardziej popularne mangi')

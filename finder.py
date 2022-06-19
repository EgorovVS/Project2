import data_input
import csv
from encodings import utf_8

def search_for_name():
        result =''
        with open('library.csv', encoding='utf_8') as lib:
                read_data = csv.reader(lib, delimiter="|")
                name = data_input.name_input().split()
                for line in read_data:
                        if name == line[0:3]:
                            pre_res = line[3]
                            result+= pre_res+'\n'
                        if name == line[0:2]:
                            pre_res = str(line[0:])
                            result += pre_res + '\n'
                        if name == line[0:1]:
                            pre_res = str(line[0:])
                            result += pre_res + '\n'
                return result

def card_for_name():
       result ='*'*10+'\n'
       with open('library.csv', encoding='utf_8') as lib:
                read_data = csv.reader(lib, delimiter="|")
                name = data_input.name_input().split()
                for line in read_data:
                        i = 0
                        if line[0:3] == name:
                            while i < len(line):
                                pre = line[i]
                                result += pre + '\n'
                                i += 1

                        if name == line[0:2]:
                            pre_res = str(line[0:])
                            result += pre_res + '\n'

                        if name == line[0:1]:
                            pre_res = str(line[0:])
                            result += pre_res + '\n'

                result+='*'*10+'\n'
       return result

def card_for_number():
       result ='*'*10+'\n'
       with open('library.csv', encoding='utf_8') as lib:
                read_data = csv.reader(lib, delimiter="|")
                number = data_input.number_input().split()
                for line in read_data:
                        i = 0
                        if line == []:
                                continue
                        if line[3] == number[0]:
                                while i < len(line):
                                        pre = line[i]
                                        result += pre+'\n'
                                        i+=1
                                result+='*'*10+'\n'
                return result
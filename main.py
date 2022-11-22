from pprint import pprint
import csv
import re

def replace_nums(contacts_list):
    pattern_num = r"(\+7|8)?\s*\(*(\d{3})\)*[-\s]*(\d{3})[-\s]?(\d{2})-?(\d{2})(\s?)\(?(доб.)?\s?(\d{4})?\)?"
    substitution = r"+7(\2)\3-\4-\5\6\7\8"
    for entry in contacts_list:
        entry[5] = re.sub(pattern_num, substitution, entry[5])
    return

def fix_names(contacts_list):
    pattern_name = r"\s"
    for entry in contacts_list:
        result1 = re.findall(pattern_name, entry[0])
        if len(result1) == 2:
            fio = re.split(pattern_name, entry[0])
            entry[0],entry[1],entry[2] = fio[0],fio[1],fio[2]
        if len(result1) == 1:
            fio = re.split(pattern_name, entry[0])
            entry[0], entry[1]= fio[0], fio[1]
        result2 = re.findall(pattern_name, entry[1])
        if len(result2) == 1:
            fio = re.split(pattern_name, entry[1])
            entry[1], entry[2]= fio[0], fio[1]
    return

def unite_entries(contacts_list):
    for entry in contacts_list:
        for entry2 in contacts_list:
            if entry[0] in entry2[0]:
                for i in range(7):
                    if entry[i] == '':
                        entry[i] = entry2[i]
    new_contacts_list = []
    for entry in contacts_list:
        if entry not in new_contacts_list and len(entry) == 7:
            new_contacts_list.append(entry)
    return new_contacts_list

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    replace_nums(contacts_list)
    fix_names(contacts_list)
    new = unite_entries(contacts_list)

with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new)

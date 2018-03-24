import csv

def readCSV1(file_name):
    result = []
    with open(file_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            result.append(row.values()[0])

    return result

def readCSV(file_name):
    contents = open(file_name).read().split("\n")
    return contents



ip_list = []
lines = readCSV("IP_test.csv")
total_cnt = 0
for i, line in enumerate(lines):
    if i==0:
        continue
    ip_list.append(line.strip())
    if i % 100 == 0 or i==len(lines)-1 :
        ip_stream = " ".join(ip_list)
        ip_list = []
        print(ip_stream)
        print("\n")
        total_cnt += 1
        if total_cnt == 20:
            break
        # print(ip_stream)
        # print("\n")


# print(lines[len(lines)-1])
import csv

with open('./data/file.csv', 'r') as file:
    csv_reader = csv.reader(file)
    data = {}
    for row in csv_reader:
        email, name = row

        occurrence_number = email.find('@')
        if occurrence_number == -1:
            continue

        domain = email[occurrence_number + 1:]
        if data.get(domain):
            data[domain].append((email, name))
        else:
            data[domain] = [(email, name)]

    result = []
    for key in data.keys():
        users = data[key]
        if not result:
            while users:
                result.append([users.pop()])
        else:
            for i in result:
                if users:
                    i.append(users.pop())

            while users:
                result.append([users.pop()])

    chunck = []
    for i in result:
        chunck.append(tuple(row for row in i))

    print(tuple(r for r in chunck))

import csv

__all__ = (
    'get_unique_chunks_by_mail_domain_csv_file',
)


def _get_data_from_csv_file(file_path):
    data = {}

    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)

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
    return data


def get_unique_chunks_by_mail_domain_csv_file(file_path):
    data = _get_data_from_csv_file(file_path)

    result = []
    for key in data.keys():
        users_info = data[key]
        if not result:
            while users_info:
                result.append([users_info.pop()])
        else:
            for i in result:
                if users_info:
                    i.append(users_info.pop())

            while users_info:
                result.append([users_info.pop()])

    chunk = []
    for i in result:
        chunk.append(tuple(row for row in i))

    return tuple(r for r in chunk)

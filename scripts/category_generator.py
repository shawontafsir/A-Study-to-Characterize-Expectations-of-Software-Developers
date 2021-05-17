#! /usr/bin/python
import json


def get_unique_topics(file):
    temp_headers = json.load(open("data/category_wise_labels.json", "r"))
    headers = {}
    for key, value in temp_headers.items():
        headers[key] = value
    d = headers["What are your expectations from your organization?"]
    result = []

    with open(file, 'r') as f:
        lines = f.readlines()

    for line in lines:
        s = []
        for topic in line.strip().split(', '):
            for k, v in d.items():
                if topic and topic in v and k not in s:
                    s.append(k)

        result.append(', '.join(s))

    return result


if __name__ == "__main__":
    file = '/home/khalid/Programs/khalid/python/SE_expectation_python/file.txt'
    result = get_unique_topics(file)
    for r in range(len(result)):
        print(result[r])

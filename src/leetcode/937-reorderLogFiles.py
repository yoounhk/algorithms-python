from typing import List


def reorderLogFiles(logs: List[str]) -> List[str]:

    digits = []
    letters = []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        elif log.split()[1].isalpha():
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

from typing import Counter, List
import re


def mostCommonWord(paragraph: str, banned: List[str]) -> str:

    words = []

    for i in range(0, len(banned)):
        banned[i] = banned[i].lower()

    for word in re.split('[^a-zA-Z]', paragraph):
        _word = re.sub('[^a-zA-Z]', '', word).lower()
        if _word in banned:
            pass
        elif _word:
            words.append(_word)
    frequency = Counter(words)
    max_k = ""
    max_v = 0
    for k, v in frequency.items():
        if v > max_v:
            max_k = k
            max_v = v
    return max_k

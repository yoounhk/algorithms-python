import collections
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    _dict = collections.defaultdict(list)
    for word in strs:
        _dict[''.join(sorted(word))].append(word)
    return _dict.values()


groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])

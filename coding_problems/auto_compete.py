# Implement an autocomplete system. 
# That is, given a query string s and a set of all possible query strings, 
# return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

import re

strings = ['dog', 'deer', 'deal']

def auto_complete(list_,partial):
    results = []
    partial = partial.lower()
    for i in list_:
        i = i.lower()
        if i.startswith(partial):
            results.append(i)
    return results

print(auto_complete(strings, 'de'))
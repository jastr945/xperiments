import collections
import re


def unique_chars(s):
    """Determines if a string has all unique characters"""
    cnt = collections.Counter(s)
    results_list = []
    for c in s:
        lettercount = cnt[c]
        if lettercount > 1:
            results_list.append('False')
        else:
            results_list.append('True')
    if 'False' in results_list:
        return False
    else:
        return True

print(unique_chars('addb'))


def permutation(str1, str2):
    """Determines if one string is a permutation of another"""
    results_list = []
    if len(str1)==len(str2):
        for letter in str1:
            if letter in str2:
                results_list.append("True")
            else:
                results_list.append("False")
        if "False" in results_list:
            return False
        else:
            return True
    else:
        return False


print(permutation("aabb", "bbaa"))
print(permutation("aabb", "bbaaa"))
print(permutation("asabb", "bbaas"))
print(permutation("asbb", "bbaa"))


def replace_spaces(my_string, true_length):
    """Replaces all spaces in a string with %20; discards any additional spaces at the end given the true length of a string"""
    real_str = my_string[:true_length]
    result = re.sub(" ", "%20", real_str)
    return result

print(replace_spaces("aa bb cc     ", 8))

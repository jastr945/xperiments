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


def compressed(my_string):
    """aabcccccaaa becomes a2b1c5a3. If the result is nor shorter, return the original string."""
    final_str = ""
    check_list = []
    for i in my_string:
        if len(check_list) > 1 and i==check_list[-2]:
            check_list[-1]+=1
        else:
            check_list.append(i)
            check_list.append(1)
    for i in check_list:
        final_str+=str(i)
    if final_str > my_string:
        return my_string
    else:
        return final_str

print(compressed("aabcccccaaa"))


def all_unique(str1):
    """Identify if a string has all unique characters"""
    for i in str1:
        if str1.count(i) > 1:
            return False
    else:
        return True

print(all_unique("hangs"))
print(all_unique("ahhngs"))

def all_unique2(str2):
    """Identify if a string has all unique characters"""
    return str1==set(str1)

print(all_unique("hangs"))
print(all_unique("ahhngs"))


def is_substring(str1, str2):
    """Finds out if one string is a substring of another"""
    return str1.find(str2) > 0

def if_rotation(str1, str2):
    """Checks if one string is rotation of another using is_substring method"""
    if len(str1)!=len(str2):
        return False
    double = str1 + str1
    return is_substring(double, str2)

print(if_rotation("waterbottle", "bottlewater"))

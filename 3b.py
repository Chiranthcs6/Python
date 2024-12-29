import difflib

def calc_simi(str1,str2):
    seq_matcher= difflib.SequenceMatcher(None,str1,str2)
    similarity_ratio=seq_matcher.ratio()
    return similarity_ratio

str1=input("Enter the string one: ")
str2=input("Enter the string two: ")

similarity=calc_simi(str1,str2)
print("Similarity",similarity)
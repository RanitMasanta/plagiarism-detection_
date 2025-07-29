from difflib import SequenceMatcher
with open ('demo.txt')as one, open('demo2.txt') as two:
    data_file1=one.read()
    data_file2=two.read()
    matches=SequenceMatcher(None,data_file1,data_file2).ratio()
    print(f"The plagiarized content is {matches*100}%")

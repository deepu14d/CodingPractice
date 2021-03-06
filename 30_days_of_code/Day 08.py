""" This is Day 8 (Dictionaries and Maps) Challenge in 30 days of code by HackerRank  """

""" Task - 
Given n names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each name queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for name is not found, print Not found instead.

 """


# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(input())
name_numbers = [input().split() for i in range(n)]
phone_book = {k: v for k, v in name_numbers}
while True:
    try:
        name = input()
        if name in phone_book:
            print(f'{name}={phone_book[name]}')
        else:
            print('Not found')
    except:
        break

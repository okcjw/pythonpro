import string 
def Frequency_analytic(s):
    noise=string.whitespace + string.punctuation
    words = {}
    for c in s:
        if c in noise: 
            continue
        words [c] = words.get(c, 0) + 1
    
    for key, value in sorted(words.items()):
        print(key, value)
    
if __name__ == "__main__":
    msg=input('input your message : ')
    Frequency_analytic(msg)

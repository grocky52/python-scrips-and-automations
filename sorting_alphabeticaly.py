def sortinput(inputstr):
    words = [w.lower() for w in inputstr] #make alist because sort works with a list
    words.sort() #used to sort only list alphabetically and dont modify like sorted which works on list dict and set
    for w in words:
        print(w)

if __name__ == '__main__':
    inputstr = input('enter your sentence here     ')
    sortinput(inputstr)

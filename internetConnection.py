import requests as rq

def checkconnection():
    link = input('enter a link')
    print("trying to connect")

    try:
        rq.get(link)
        print(f'connection to the {link} was successful')
        return True
    except:
        rq.ConnectionError()
        print(f'connection to {link} wasnt possible')
        return False

checkconnection()

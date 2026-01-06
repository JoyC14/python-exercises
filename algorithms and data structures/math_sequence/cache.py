def hitormiss(list):
    cache = []
    for requests_num in list:
        if requests_num in cache:
            print("hit")
        else:
            print("miss")
            if len(cache) < 8:
                cache.append(requests_num)
            else:
                cache.remove(cache[0])
                cache.append(requests_num)
    return cache

def main():
    requests = []
    while True:
        requests_num = input("enter a number")
        if requests_num.isnumeric() is True and requests_num!= "0":
            requests.append(int(requests_num))
        elif requests_num == "Q" or requests_num == "q":
            break
        elif requests_num == "0":
            print(hitormiss(requests))

main()                
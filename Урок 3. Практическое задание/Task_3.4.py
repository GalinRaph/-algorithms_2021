import hashlib

url = input('url')

kash = {'10dd6e016c6ddd709c730ea8db557c20a6e5a2558d5b73178bc68797bbb22e19': 'gb.ru'}


def chek_url(u):
    hash_u = hashlib.sha256(u.encode()).hexdigest()
    if hash_u in kash.keys():
        return True
    else:
        return {hash_u: u}


chek_url(url)

try:
    kash.update(chek_url(url))
except TypeError:
    print("Такой объект уже есть в кэше")

print(kash)
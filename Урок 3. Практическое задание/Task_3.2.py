import hashlib
from uuid import uuid4

password = input("Введите пароль")

salt = uuid4().hex


def hash_pass(data, sal):
    res = hashlib.sha256(sal.encode() + data.encode()).hexdigest()
    pass_2 = input("Введите пароль повторно")
    res_2 = hashlib.sha256(sal.encode() + pass_2.encode()).hexdigest()
    if res_2 == res:
        return res, print(res)
    else:
        return print("Неверный пароль")


hash_password = hash_pass(password, salt)


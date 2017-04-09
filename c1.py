import requests
from bs4 import BeautifulSoup
import random
import re


def qiushibaike():
    content = requests.get('http://www.qiushibaike.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'content'}):
        print(div.text.strip())


def demo_string():
    stra = 'hello worlD'
    print(stra.capitalize())
    print(stra.replace('worlD', 'pengkun'))
    strb = '  \n\rhello hahaha  \r\n'
    print(1, strb.lstrip())
    print(2, strb.rstrip())
    strc = 'hello w '
    print(3, strc.startswith('he'))
    print(4, strc.endswith('456'))
    print(stra + strb + strc)
    print(7, '-'.join(['a', 'b', 'c']))
    print(7, '-'.join([strb, stra, 's']))
    print(8, strc.split(' '))


def demo_operation():
    print(1 + 2, 5 / 2, 5 * 2, 5 - 2)
    x = 3
    print(type(x))


def demo_buildinfunction():
    print(1, max(2, 1), min(5, 3))
    print(len('xxxxxxx'))
    print(abs(-5))
    print(4, range(1, 10, 3))
    print(5, dir(list))
    print(chr(97), ord('a'))


def demo_controlflow():
    scpre = 65
    if scpre > 99:
        print(1, 'A')
    elif scpre > 50:
        print(2, 'a')
    while scpre < 100:
        print(scpre)
        scpre += 10

    for i in range(1, 10):
        if i == 1:
            pass  # do_special
            # print(3,1)
        if i < 5:
            continue
        print(i)


def demo_dict():
    dicta = {1: 1, 2: 4, 3: 9}
    print(dicta)
    print(dicta.keys(), dicta.values())
    print(1 in dicta)
    for key, value in dicta.items():
        print(key, value)
    dictb = {'+': add, '-': sub}
    print(dictb.get('-')(15, 3))
    dictb['*'] = 'x'
    print(dictb)
    dictb.pop('*')
    print(dictb)
    del dictb['-']
    print(dictb)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def demo_list():
    lista = [1, 2, 3]
    print(lista)
    listb = ['1', 1, 'a', 1.1]
    lista.extend(listb)
    print(lista)
    print(len(listb))
    print('c' in listb)
    lista = listb + lista
    print(lista)
    lista.insert(0, 'eqweqwqqe')
    print(lista)
    print(lista.pop(1))
    print(lista)
    lista.reverse()
    print(lista)
    print(lista[0])
    # lista.sort()
    print(lista)
    pupplea = (1, 2, 3)
    print(pupplea)


def demo_set():
    set1 = {1, 2, 3}
    set2 = {1, 2, 3}
    print(set1)
    print(type(set1))
    set1.add(4)
    set1.add(4)
    print(set1)
    print(set1 | set2)
    print(set1 - set2)
    print(set1 & set2)
    print(set1 ^ set2)
    # print(set2 + set1)
    # print(set1.add(4))


class User:
    type = 'USER'

    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)


class Guest(User):
    def __init__(self, name, uid):
        self.name = name
        self.uid = uid

    def __repr__(self):
        return "im guest" + self.name + ' ' + str(self.uid)


class Admin(User):
    type = 'ADMIN'

    def __init__(self, name, uid, group):
        User.__init__(self, name, uid)
        self.group = group

    def __repr__(self):
        return 'im ' + self.name + ' ' + str(self.uid)


def create_user(type):
    if type == 'USER':
        return User('u2', 2)
    elif type == 'ADMIN':
        return Admin('a1', 102, 'g2')
    else:
        return Guest('gu1', 201)
        # raise ValueError('error')


def demo_exception():
    try:
        print(2 / 1)
        print(2 / 0)
        raise Exception("Raise Exception", "pk")
    except Exception as e:
        print('error:', e)
    finally:
        print('clean up')


def demo_random():
    random.seed(1)
    # x=prex*100007%xxxx
    # prex =x 幂等性
    print(random.random())
    print(int(random.random() * 100))
    print(random.randint(0, 200))
    print(random.choice(range(0, 10, 2)))
    print(random.sample(range(0, 10, 2), 3))
    a = [1, 2, 3, 4, 5]
    random.shuffle(a)
    print(a)


def demo_re():
    str = 'abc123def12gh12'
    p1 = re.compile('\d+')
    p2 = re.compile('\d')
    print(p1.findall(str))
    print(p2.findall(str))

    str1 = 'a@163.com,b@gmail.com,c@qq.com,d@163.com,z@qq.com'
    p3 = re.compile('[\w]+@[163|qq]+\.com')
    p4 = re.compile('[\w]+@[^qq]+\.com')
    print(p3.findall(str1))
    print(p4.findall(str1))

    str3 = '<html><h>title</h><body>xxxx</body></html>'
    p5 = re.compile('<h>[^<]+</h>')
    print(p5.findall(str3))
    p6=re.compile('<h>([^<]+)</h>')
    print(p6.findall(str3))
    str4='xx2016-06-11yy'
    p7=re.compile('\d{4}-\d\d-\d\d')
    print(p7.findall(str4))


if __name__ == '__main__':
    user1 = User('u1', 1)
    print(user1)
    admin1 = Admin('a1', 101, 'g1')
    print(admin1)
    print(create_user('USERX'))
    # demo_string()
    print('hello world')
    # comment
    # demo_operation()
    # demo_buildinfunction()
    # demo_controlflow()
    # demo_list()
    # demo_dict()
    # demo_set()
    # demo_exception()
    # demo_random()
    demo_re()

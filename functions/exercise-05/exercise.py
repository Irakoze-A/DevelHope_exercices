import random

def random_list_summer(n=15):
    liste = [random.randint(-100,100) for i in range(n)]
    print(liste)
    print(sum(liste))
random_list_summer()
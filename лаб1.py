import math
def task1():

    city = "Lviv"
    print(city)

def task2():

    is_citizen = True
    is_voter = False

    print("Значення is_citizen:", is_citizen)
    print("Значення is_voter:", is_voter)

def task3():
    is_raining = True
    is_snowing = False

    print("Результат логічного 'не' для is_raining:", not is_raining)
    print("Результат логічного 'не' для is_snowing:", not is_snowing)

def task4_math():
    y=7.315
    z=3.127
    f= 16 * (y**2) + math.e**(y*z) + math.pow((z + 1.51), 1/3) + math.log(y*z)
    print("Результат прикладу:", f)

if __name__ == '__main__':
    print("Task 1 : ")
    task1()
    print("Task 2 : ")
    task2()
    print("Task 3 : ")
    task3()
    print("Task 4 : ")
    task4_math()


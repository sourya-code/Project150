
from tkinter import *
import random

root= Tk()
root.title("Country Capitals")
root.geometry("500x500")

enter_name = Entry(root)
enter_name.place(relx = 0.5, rely = 0.1, anchor= CENTER)

enter_name1 = Entry(root)
enter_name1.place(relx = 0.5, rely = 0.2, anchor= CENTER)

country_list = Label(root)
city_list = Label(root)
lucky_country = Label(root)
lucky_city = Label(root)


list1 = []
list2 = []

def addcountry():
    country_name = enter_name.get()
    list1.append(country_name)
    country_list["text"] = "Country Name : " + str(list1)
    city_name = enter_name1.get()
    list2.append(city_name)
    city_list["text"] = "City Name : " + str(list2)
    

def random_number1():
    length = len(list1)
    random_no = random.randint(0, length)
    generated_random_number1 = list1[random_no]
    lucky_country["text"] = "Random Country : " + str(generated_random_number1)
    
def random_number():
    length = len(list2)
    random_no = random.randint(0, length)
    generated_random_number = list2[random_no]
    lucky_city["text"] = "Random City : " + str(generated_random_number)
    
btn = Button(root, text="Display Country and City Name", command= addcountry)
btn.place(relx = 0.5, rely = 0.3, anchor= CENTER)

country_list.place(relx = 0.5, rely = 0.4, anchor= CENTER)
city_list.place(relx = 0.5, rely = 0.5, anchor= CENTER)

btn1 = Button(root, text="Display City Name Randomly", command= random_number)
btn1.place(relx = 0.5, rely = 0.6, anchor= CENTER)

btn2 = Button(root, text="Display Country Name Randomly", command= random_number1)
btn2.place(relx = 0.5, rely = 0.7, anchor= CENTER)

lucky_country.place(relx = 0.5, rely = 0.8, anchor= CENTER)
lucky_city.place(relx = 0.5, rely = 0.9, anchor= CENTER)

root.mainloop()
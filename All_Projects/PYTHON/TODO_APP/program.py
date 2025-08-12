import tkinter as tk
from tkinter import messagebox
import mysql.connector
cn = mysql.connector.connect(
        database="TODOApp",
        user="root",
        password="ranjana@2024",
        host="localhost",
        port="3306"
    )
c = cn.cursor()


mwin = tk.Tk()
mwin.geometry("400x300+200+200")  
mwin.title("To-Do List Application")
def add():
  awin = tk.Tk()
  awin.geometry("300x200")
  awin.title("Add Task")
  l1 = tk.Label(awin, text = "task_description", font = ("Arial",14))
  l2 = tk.Label(awin, text = "Date", font = ("Arial",14))
  l3 = tk.Label(awin, text = "status", font = ("Arial",14))
  e1 = tk.Entry(awin, width = 10, font = ("Arial",14))
  e2 = tk.Entry(awin, width = 10, font = ("Arial",14))
  e3 = tk.Entry(awin, width = 10, font = ("Arial",14))
  
  
  
  
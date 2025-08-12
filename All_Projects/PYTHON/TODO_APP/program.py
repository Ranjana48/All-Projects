import tkinter as tk
import mysql.connector as mysql
import tkinter.messagebox
cn = mysql.connect(
        database="TODOApp",
        user="root",
        password="ranjana@2024",
        host="localhost",
        port="3306"
    )
c = cn.cursor()


mwin = tk.Tk()
mwin.geometry("300x300+200+200")  
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
  
  def addTask():
    sql = "INSERT INTO todo (task_description, status, date_date) VALUES (%s, %s, %s)"
    desc = e1.gwt()
    d = e2.get()
    ts = e3.get()
    
    try:
      c.execute(sql, params = (desc, ts, d)) 
      tk.messagebox.showinfo(title = "info", message = "Task Created")
      e1.delete(0,tk.END)
      e2.delete(0,tk.End)
      e3.delete(0,tk.END)
      cn.commit()
    except:
      tk.messagebox.showerror(title="error", message = " Error in Creating Task")
      def close():
        awin.destroy()
        b1 = tk.Button(awin, text = "Add", font = ("Arial", 14),commanad = addTask)
        b2 = tk.Button(awin, text = "Close", font = ("Arial", 14), command = close)
        l1.grid(row = 1, column=1)
        l2.grid(row = 2, column = 1)
        l3.grid(row =3, column =1)
        e1.grid(row = 1, column =2)
        e2.grid(row=2, column =2)
        e3.grid(row=3, column =2)
        b1.grid(row =4,column =1)
        b2.grid(row=4, column =2)
        
        def view():
          vwin = tk.Tk()
          vwin.title("ViewTasks")
          vwin.geometry("500x500")
          cmd = "select * from todo"
          c.execute(cmd)
          rows = c.fetchall()
          for row in rows:
            output = '\t'.join(list(map(str, row)))
            t1 = tk.Label(vwin,text = output, font =   ("Arial", 14))
            t1.pack(side=tkinter.TOP, fill=tkinter.BOTH)
            
            def close():
              vwin.destroy()
              b1 = tk.Button(vwin, text = "Close", font=("Arial", 14), command = close)
              b1.pack(side=tkinter.TOP, fill=tkinter.BOTH)
              
              def delete():
                dwin = tk.Tk()
                dwin.title("Delete Task")
                dwin.geometry("200x200")
                l1 = tk.Label(dwin, text ="TaskID", font =("Arial", 14))
                e1 = tk.Entery(dwin, width = 10, font=("Arial", 14))
                
                def deletetask():
                  sql = "delete from todo where taskid = %s"
                  taskid = e1.get()
                  c.execute(sql, params=(taskid,))
                  k = c.rowcount
                  if k>0:
                    tk.messagebox.showinfo(title="info",message="task deleted")
                    cn.commit()
                  else:
                    tk.messagebox.showerror(tittle="error",message="invalid taskid")
                    def close():
                      dwin.destroy()
                      b1 = tk.Button(dwin, text="Delete", font = ("Arial", 14), command = deletetask)
                      b2 = tk.Button(dwin, text = "close", font =("Arial", 14), command = close)
                      l1.grid(row=1,column=1)
                      e1.grid(row=1,column=2)
                      b1.grid(row=2,column=1)
                      b2.grid(row=2,column=2)
                      def update():
                        uwin = tk.Tk()
                        uwin.title("Update Task")
                        uwin.geometry("200x200")
                        l1 = tk.Label(uwin, text ="TaskId", font = ("Arial", 14))
                        l2 = tk.Label(uwin, text ="Status", font =("Arial", 14))
                        e1 = tk.Entry(uwin, width =10, font = ("Arial", 14))
                        e2 = tk.Entry(uwin, width = 10, font = ("Arial", 14))
                        def updatetask():
                          sql = "update todo set status = %s where taskid = %s"
                          taskid = e1.get()
                          status = e2.get()
                          c.execute(sql, params = (status, taskid))
                          k = c.rowcount
                          if k>0:
                            tk.messagebox.showinfo(title = "info", message = " Task Updated")
                            cn.commit()
                          else:
                            tk.messagebox.showinfo(title = "error", message = "invalid TaskId")
                            def close():
                              uwin.destroy()
                              b1 = tk.Button(uwin,text = "close", font = ("Arial", 14), command = updatetask)
                              b2 = tk. Button(uwin, text ="close", font = ("Arial", 14), command = close)
                              l1.grid(row=1,column=1)
                              l2.grid(row=2,column=1)
                              e1.grid(row=1,column=2)

                              e2.grid(row=2,column=2)
                              b1.grid(row=3,column=1)
                              b2.grid(row=3,column=2)
                              
                              def close():
                               mwin.destroy()
                               b1 = tk.Button(mwin, text = "Add Task", font = ("Arial", 14), command = add)
                               b2 = tk.Button(mwin, text = "view Task", font = ("Arial", 14), command=view)
                               b3 = tk.Button(mwin, text = "Update Task", font = ("Arial", 14), command=update)
                               b4 = tk.Button(mwin, text = "delete Task", font = ("Arial", 14), command=delete)
                               b5 = tk.Button(mwin, text = "Exit", font = ("Arial", 14), command=close)
                               b1.pack(side=tk.TOP, fill=tk.BOTH)
                               b2.pack(side=tk.TOP, fill=tk.BOTH)
                               b3.pack(side=tk.TOP, fill=tk.BOTH)
                               b4.pack(side=tk.TOP, fill=tk.BOTH)
                               b5.pack(side=tk.TOP, fill=tk.BOTH)
                               
                               
                               
                               
                               

                        
                      
                      
                      
                
                
                
                
              
            
            
        
        
      
       
        
  
  
  
  
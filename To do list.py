from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add__task():  
    task_string = task_field.get()  
    if len(task_string) == 0:  
        messagebox.showinfo('Error', 'Field is Empty.')  
    else:    
        tasks.append(task_string)   
        the_cursor.execute('insert into tasks values (?)', (task_string ,))    
        list__update()    
        task_field.delete(0, 'end')  
    
def list__update():    
    clear__list()    
    for task in tasks:    
        task_listbox.insert('end', task)  
  
def delete__task():  
    try:  
        the_value = task_listbox.get(task_listbox.curselection())    
        if the_value in tasks:  
            tasks.remove(the_value)    
            list__update()   
            the_cursor.execute('delete from tasks where title = ?', (the_value,))  
    except:   
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')        
  
def delete_all_tasks_():  
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')  
    if message_box == True:    
        while(len(tasks) != 0):    
            tasks.pop()    
        the_cursor.execute('delete from tasks')   
        list__update()  
   
def clear__list():   
    task_listbox.delete(0, 'end')  
  
def close():    
    print(tasks)   
    guiWindow.destroy()  
    
def retrieve_database():    
    while(len(tasks) != 0):    
        tasks.pop()    
    for row in the_cursor.execute('select title from tasks'):    
        tasks.append(row[0])  
   
if __name__ == "__main__":   
    guiWindow = Tk()   
    guiWindow.title("To-Do List ")  
    guiWindow.geometry("665x400+550+250")   
    guiWindow.resizable(0, 0)  
    guiWindow.configure(bg = "#B5E5CF")  
   
    the_connection = sql.connect('listOfTasks.db')   
    the_cursor = the_connection.cursor()   
    the_cursor.execute('create table if not exists tasks (title text)')  
    
    tasks = []  
        
    functions_frame = Frame(guiWindow, bg = "#8EE5EE") 
    
    functions_frame.pack(side = "top", expand = True, fill = "both")  
 
    task_label = Label( functions_frame,text = "TO-DO-LIST \n Enter the Task Name:",  
        font = ("arial", "14", "bold"),  
        background = "#8EE5EF", 
        foreground="#FF1493",
    )    
    task_label.place(x = 20, y = 30)  
        
    task_field = Entry(  
        functions_frame,  
        font = ("Arial", "14"),  
        width = 43,  
        foreground="black",
        background = "white",  
    )    
    task_field.place(x = 181, y = 31)  
    
    add_button =Button(  
        functions_frame,  
        text = "Add (+)",  
        width = 16,
        bg='#1C86EE',font=("arial", "15", "bold"),
        command = add__task,
        
    )  
    del_button = Button(  
        functions_frame,  
        text = "Remove (-)",  
        width = 16,
        bg='#1C86EE', font=("arial", "14", "bold"),
        command = delete__task,  
    )  
    del_all_button = Button(  
        functions_frame,  
        text = "Delete All",  
        width = 16,
        font=("arial", "14", "bold"),
        bg='#1C86EE',
        command = delete_all_tasks_
    )
    
    exit_button = Button(  
        functions_frame,  
        text = "Exit",  
        width = 51,
        bg='#1C86EE',  font=("arial", "14", "bold"),
        command = close  
    )    
    add_button.place(x = 19, y = 81,)  
    del_button.place(x = 241, y = 81)  
    del_all_button.place(x = 461, y = 81)  
    exit_button.place(x = 11, y = 331)  
    
    task_listbox = Listbox(  
        functions_frame,  
        width = 71,  
        height =10,  
        font="bold",
        selectmode = 'SINGLE',  
        background = "WHITE",
        foreground="BLACK",    
        selectbackground = "#FF8C00",  
        selectforeground="BLACK"
    )    
    task_listbox.place(x = 18, y = 141)  
    
    retrieve_database()  
    list__update()    
    guiWindow.mainloop()    
    the_connection.commit()  
    the_cursor.close()
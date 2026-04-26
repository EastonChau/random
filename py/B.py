import tkinter as tk
from datetime import datetime

def splash():
    root = tk.Tk()
    root.focus_force()
    root.geometry(f"{800}x{500}")
    root.title("splash screen")
    root.configure(bg="#0700DC")

    def current():
        current_time = datetime.now()
        time_format = current_time.strftime("%Y-%m-%d %H:%M:%S")
        date_label.config(text="Now is " + time_format)
        date_label.after(500, current)

    date_label = tk.Label(root, text = 'wait..', font = ("Arial",50), fg= "white", bg="#0700DC")
    date_label.pack(pady=50)
    pName = tk.Label(root, text = 'Welcome!\nWork Hard, Live Big!', font = ("Arial",60), fg= "white", bg="#0700DC")
    pName.pack(pady = 5)
    create_label = tk.Label(root, text = 'Created by Easton Chau👍 ', font = ("Arial",24), fg= "white", bg="#0700DC")
    create_label.pack(pady = 0)
    current()

    root.after(7777, root.destroy)
    root.mainloop()

def fullscreen():
    root = tk.Tk()
    root.focus_force()
    root.geometry(f"{1280}x{720}")
    root.configure(bg = "blue")
    return root

def fram(root):
    frame = tk.Frame(root)
    frame.pack(expand=True)
    frame.configure(bg = "blue")
    return frame

#data from users
salary = float (0) # annual
percent = float (0) # decimal, not %, of salary saved
cost = float (0)
salary_raise = float(0) # annual

#other data
salary_month = float (0)
saved = float (0)
investment_rate = float (0.03/12)
down_payment = float (0)

def main():
    root = fullscreen()  
    frame = fram(root)

    def cal(n):
        global saved
        global down_payment
        global investment_rate
        global salary_month
        global percent
        global salary_raise
        
        if (n%12 == 0) & (n != 0):
            salary_month = ((salary_month*12)*(1+salary_raise))/12

        investment_earned = saved*investment_rate
        salarySaved = salary_month * percent
        saved += investment_earned + salarySaved
        
        down_payment -= investment_earned + salarySaved
        
        print(f"year: {(n)}")
        print(f"investment_earned :{investment_earned}")
        print(f"salary_month :{salary_month}")
        print(f"percent :{percent}")
        print(f"salarySaved :{salarySaved}")
        print(f"down_payment :{down_payment}")
        print(f"salary_raise :{salary_raise}")
        print(f"===============================")

        if down_payment > 0:
            return cal(n+1)
        else:
            return (n + 1)
    
    def write_input():
        global saved
        saved = 0
        global salary
        salary = float (entrySalary.get())
        global percent
        percent = float (entryPercent.get())
        global cost 
        cost = float (entryCost.get())
        global down_payment
        down_payment = 0.2 * cost
        global salary_month
        salary_month = salary/12
        
        global salary_raise
        salary_raise = float (entryRaise.get())

        labelResult.config(text = f"It will take you {cal(0)} months to save for the down payment on your dream home.")


    #Input Section
    labelSalary = tk.Label(frame, text = "Annual Salary:", fg = "white", bg = "blue",font = ("Arial", 33))
    labelSalary.grid(row=0,column=0, padx=5,pady = 5, sticky='e')
    entrySalary = tk.Entry(frame, width = 30,font = ("Arial", 33))
    entrySalary.grid(row=0, column=1, padx=5,pady=5, sticky='w')
    entrySalary.insert(0, "360000")

    labelPercent = tk.Label(frame, text = "Monthly Savings Percentage:", fg = "white", bg = "blue",font = ("Arial", 33))
    labelPercent.grid(row=1,column=0, padx=5,pady = 5, sticky='e')
    entryPercent = tk.Entry(frame, width = 30,font = ("Arial", 33))
    entryPercent.grid(row=1, column=1, padx=5,pady=5, sticky='w')
    entryPercent.insert(0, "0.2")

    labelCost = tk.Label(frame, text = "Home Cost:", fg = "white", bg = "blue",font = ("Arial", 33))
    labelCost.grid(row=2,column=0, padx=5,pady = 5, sticky='e')
    entryCost = tk.Entry(frame, width = 30,font = ("Arial", 33))
    entryCost.grid(row=2, column=1, padx=5,pady=5, sticky='w')  
    entryCost.insert(0, "8000000")

    labelRaise = tk.Label(frame, text = "Annual Raise:", fg = "white", bg = "blue",font = ("Arial", 33))
    labelRaise.grid(row=3,column=0, padx=5,pady = 5, sticky='e')
    entryRaise = tk.Entry(frame, width = 30,font = ("Arial", 33))
    entryRaise.grid(row=3, column=1, padx=5,pady=5, sticky='w')  
    entryRaise.insert(0, "0.03")

    buttonSubmit = tk.Button(frame, text = "Calculate", font = ("Arial", 33, 'bold'), command = write_input)
    buttonSubmit.grid(row=4,column=0, columnspan=2, padx=10,pady = 10, sticky='ew')
    
    #result
    labelResult = tk.Label(frame, text = "It will take you ? months to save for the down payment on your dream home.", fg = "white", bg = "blue",font = ("Arial", 33))
    labelResult.grid(row=5,column=0, columnspan=2, padx=10,pady = 10, sticky='ew')

    root.mainloop()

splash()

main()
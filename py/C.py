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
salary_raise = 500 #0.05

#other data
salary_month = 0
investment_rate = 300/12 #0.03
down_payment = 1600000
epsilon = 100

def main():
    root = fullscreen()
    frame = fram(root)
    
    def notPossible():
        saved = 0
        salary_m = salary_month

        print(f"start saved: {saved}")
        for i in range(36):
            
            if (i%12==0) and (i!=0):
                salary_m = ((salary_m*12)*(1+(salary_raise/10000)))/12
           
            saved += salary_m + (investment_rate*saved/10000)
            
            print(f"i: {i} saved: {saved}")
            print(f"i: {i} saved: {saved}")
            if ((i+1)%12==0) and (i!=0):
                print(f"year: {(i+1)/12}")
                print(saved)
                print("-------")
        
        print(saved)
        print(salary_m)

        if saved < (down_payment-epsilon):
            return ("It is not possible to pay the down payment in three years.")
        else:
            return cal()

    def cal():
        maxR = 10000
        minR = 0
        guess = 5000
        s = 0
        saved = 0
        
        print(f"starting salary month: {salary_month}")
        print(f"max min: {maxR}:{minR}")

        x = 0
        while ((saved < down_payment - epsilon) or (saved > down_payment + epsilon)) and (x<100):
            saved = 0
            salary_m = salary_month
            salary_saved = 0

            print(f"==========================")
            print(f"max min: {maxR}:{minR}")

            print("while 0")

            for i in range(36):
                if (i%12==0) & (i!=0):
                    salary_m = ((salary_m*12)*(1+(salary_raise/10000)))/12
                    salary_saved = (salary_m * guess)/10000
                else:
                    salary_saved = (salary_m * guess)/10000
                    
                saved += salary_saved + (investment_rate*saved/10000)
                
                print(f"---------")
                print(f"i: {i}")
                print(f"saved: {saved}")
                print(f"---------")
                    
            if saved > (down_payment + epsilon):
                maxR = guess
            elif saved < (down_payment - epsilon):
                minR = guess
                
            guess = (maxR+minR)//2
            print(f"saved: {saved}")
            print(f"guess: {guess}")
            s += 1
            x += 1

            print(f"==========================")

        return f"Best savings rate: {guess/10000}\nSteps in bisection search {s}"

    
    def write_input():
        global salary_month
        salary_month = float(entrySalary.get())/12
        labelResult.config(text = notPossible())

    #Input Section
    labelSalary = tk.Label(frame, text = "Starting Salary:", fg = "white", bg = "blue",font = ("Arial", 33))
    labelSalary.grid(row=0,column=0, padx=5,pady = 5, sticky='e')
    entrySalary = tk.Entry(frame, width = 30,font = ("Arial", 33))
    entrySalary.grid(row=0, column=1, padx=5,pady=5, sticky='w')
    entrySalary.insert(0, "300000")

    buttonSubmit = tk.Button(frame, text = "Calculate", font = ("Arial", 33, 'bold'), command = write_input)
    buttonSubmit.grid(row=4,column=0, columnspan=2, padx=10,pady = 10, sticky='ew')
    
    #result
    labelResult = tk.Label(frame, text = "It will take you ? months to save for the down payment on your dream home.", fg = "white", bg = "blue",font = ("Arial", 33))
    labelResult.grid(row=5,column=0, columnspan=2, padx=10,pady = 10, sticky='ew')

    root.mainloop()

splash()

main()
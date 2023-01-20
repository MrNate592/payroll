import tkinter as tk
import time,tempfile
from tkinter import messagebox,ttk
import dbinfo 

# Define class 
class payrollsystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee Payroll Management System")   # Title
        
        # Define window size and colour
        self.root.geometry("1400x800")    
        self.root.config(bg="#222e50")
        title=tk.Label(self.root,text="Employee Payroll Management System",font=("Arial bold",30,"bold"),bg="#292826",fg="#f0f1f2",anchor="w",padx=10)
        title.place(x=0,y=0,relwidth=1)

        # Top row of buttons
        allemp_button=tk.Button(self.root,text="All Employees",command=self.employee_frame,font=("Arial bold",13),bg="#05ab79",fg="#f0f1f2",activebackground="#f0c808")
        allemp_button.place(x=1050,y=10,height=30,width=140)

        

        logout=tk.Button(self.root,text="Log Out",command=self.logout,font=("Arial bold",13),bg="#05ab79",fg="#f0f1f2",activebackground="#f0c808")
        logout.place(x=1200,y=10,height=30,width=140)

        
        # Styles for window to show all employees  table
        style = ttk.Style()
        style.theme_use('alt')
        style.configure('TCombobox', background = 'gray',foreground="#f0f1f2")
        style.map('TCombobox', fieldbackground=[('readonly','#292826')])
        style.configure("Treeview",background="#292826",foreground="#f0f1f2",fieldbackground="#292826")
        style.map('Treeview',background=[('selected',"#292826")],foreground=[('selected','#f0c808')])
        

        # Variables 
        self.var_emp_id=tk.StringVar()
        self.var_department=tk.StringVar()
        self.var_name=tk.StringVar()
        self.var_gender=tk.StringVar()
        self.var_salaryid=tk.StringVar()
        self.var_address=tk.StringVar()
        self.var_bank=tk.StringVar()
        self.var_bankid=tk.StringVar()
        self.var_dob=tk.StringVar()
        self.var_accountno= tk.StringVar()
        self.var_n_salary=tk.StringVar()
        self.var_lb1_values=tk.StringVar()
        self.var_date=tk.StringVar()
        self.var_wage_rate=tk.StringVar()
        self.var_tax=tk.StringVar()
        self.var_b_salary=tk.StringVar()
        self.var_medical=tk.StringVar()
        self.var_nis=tk.StringVar()
        self.var_hours=tk.StringVar()
        self.var_taxid=tk.StringVar()
        self.var_paydate=tk.StringVar()

        # Create first frame
        Frame1=tk.Frame(self.root,bd=3,relief=tk.RIDGE,bg="#292826")
        Frame1.place(x=10,y=70,width=750,height=650)
        
        t1=tk.Label(Frame1,text="Employee Details",justify='center',font=("Arial bold",22),bg="#3b3e42",fg="#f0c808",anchor="w",padx=10)
        t1.place(x=0,y=0,relwidth=1)
        
        t2=tk.Label(Frame1,text="Employee ID*",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        t2.place(x=10,y=65)
        
        self.txt_code=tk.Entry(Frame1,font=("Arial bold",13),textvariable=self.var_emp_id,bg="#292826",fg="#f0f1f2")
        self.txt_code.place(x=250,y=69,width=200)

        button_search=tk.Button(Frame1,text="Search",command=self.search,font=("Arial bold",18),bg="#05ab79",fg="#f0f1f2",activebackground="#eb9c5c")
        button_search.place(x=480,y=65,height=30)

        # Frame 1 - Row 1---------------------------------------------------------------------------

        department=tk.Label(Frame1,text="Department",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        department.place(x=10,y=117)
        department=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_department,bg="#292826",fg="#f0f1f2")
        department.place(x=170,y=120,width=200)
        
        bank=tk.Label(Frame1,text="Bank",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        bank.place(x=400,y=120)
        bank=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_bank,bg="#292826",fg="#faf3dd")
        bank.place(x=520,y=120,width=200)
        
        # Frame 1 - Row 2---------------------------------------------------------------------------

        name=tk.Label(Frame1,text="Name",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        name.place(x=10,y=170)
        name=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_name,bg="#292826",fg="#f0f1f2")
        name.place(x=170,y=170,width=200)
        
        bankid=tk.Label(Frame1,text="Bank ID#",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        bankid.place(x=400,y=170)
        bankid=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_bankid,bg="#292826",fg="#f0f1f2")
        bankid.place(x=520,y=170,width=200)
        
        # Frame 1 - Row 3---------------------------------------------------------------------------

        dob=tk.Label(Frame1,text="DOB",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        dob.place(x=10,y=220)
        dob=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_dob,bg="#292826",fg="#f0f1f2")
        dob.place(x=170,y=220,width=200)

        accountnumber=tk.Label(Frame1,text="Account#",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        accountnumber.place(x=400,y=220)
        accountnumber=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_accountno,bg="#292826",fg="#f0f1f2")
        accountnumber.place(x=520,y=220,width=200)
        
        # Frame 1 - Row 4--------------------------------------------------------------------------- 
        
        gender=tk.Label(Frame1,text="Gender",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        gender.place(x=10,y=270)
        
        gender=ttk.Combobox(Frame1,textvariable=self.var_gender,font=('Arial bold',13,'bold'),state="readonly")
        gender['values']=("Select","Male","Female","Other")
        gender.current(0)
        gender.place(x=170,y=270,width=200)

        salaryid=tk.Label(Frame1,text="Salary ID",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        salaryid.place(x=400,y=270)
        salaryid=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_salaryid,bg="#292826",fg="#f0f1f2")
        salaryid.place(x=520,y=270,width=200)
        
        # Frame 1 - Row 5---------------------------------------------------------------------------

        address=tk.Label(Frame1,text="Address",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        address.place(x=10,y=330)
        address=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_address,bg="#292826",fg="#f0f1f2")
        address.place(x=170,y=330,width=500)

        taxid=tk.Label(Frame1,text="Tax ID",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        taxid.place(x=10,y=380)
        taxid=tk.Entry(Frame1,font=("times  new roman",13),textvariable=self.var_taxid,bg="#292826",fg="#f0f1f2")
        taxid.place(x=170,y=380,width=500)

        
        ##Frame 2---------------------------------------------------------------------------

        Frame2=tk.Frame(self.root,bd=3,relief=tk.RIDGE,bg="#292826")
        Frame2.place(x=770,y=70,width=580,height=330)
        
        title3=tk.Label(Frame2,text="Employee Salary Details",font=("Arial bold",20),bg="#3b3e42",fg="#f0c808",anchor="w",padx=10)
        title3.place(x=0,y=0,relwidth=1)
        
        date=tk.Label(Frame2,text="Date",font=("Arial bold",17),bg="#292826",fg="#f0c808")
        date.place(x=10,y=60)
        date=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_date,bg="#292826",fg="#f0f1f2")
        date.place(x=160,y=64,width=100)
        
        hours=tk.Label(Frame2,text="Hours Worked",font=("Arial bold",17),bg="#292826",fg="#f0c808")
        hours.place(x=280,y=60)
        hours=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_hours,bg="#292826",fg="#f0f1f2")
        hours.place(x=460,y=64,width=100)
   
        # Frame 2 - Row 1--------------------------------------------------------------------------- 

        wagerate=tk.Label(Frame2,text="Wage Rate",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        wagerate.place(x=10,y=120)
        wagerate=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_wage_rate,bg="#292826",fg="#f0f1f2")
        wagerate.place(x=160,y=125,width=100)
        
        b_salary=tk.Label(Frame2,text="Basic Salary",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        b_salary.place(x=280,y=120)
        b_salary=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_b_salary,bg="#292826",fg="#f0f1f2")
        b_salary.place(x=440,y=125,width=120)
        
        # Frame 2 - Row 2--------------------------------------------------------------------------- 

        medical=tk.Label(Frame2,text="Medical",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        medical.place(x=10,y=180)
        medical=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_medical,bg="#292826",fg="#f0f1f2")
        medical.place(x=160,y=185,width=100)
        
        tax=tk.Label(Frame2,text="Income Tax",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        tax.place(x=280,y=180)
        tax=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_tax,bg="#292826",fg="#f0f1f2")
        tax.place(x=440,y=185,width=120)
        
        # Frame 2 - Row 3--------------------------------------------------------------------------- 

        nis=tk.Label(Frame2,text="NIS",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        nis.place(x=10,y=220)
        nis=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_nis,bg="#292826",fg="#f0f1f2")
        nis.place(x=160,y=225,width=100)
        
        netsalary=tk.Label(Frame2,text="Net Salary*",font=("Arial bold",18),bg="#292826",fg="#f0c808")
        netsalary.place(x=280,y=220)
        netsalary=tk.Entry(Frame2,font=("times  new roman",13),textvariable=self.var_n_salary,bg="#292826",fg="#f0f1f2")
        netsalary.place(x=440,y=225,width=120)
        
        #Buttons
        button_calculate=tk.Button(Frame2,text="Calculate",command=self.calculate,font=("Arial bold",18),bg="#014421",fg="#f0f1f2",activebackground="#f0c808")
        button_calculate.place(x=20,y=275,height=30,width=120)
        
        button_clear=tk.Button(Frame2,text="Clear",command=self.clear,font=("Arial bold",18),bg="#f18805",fg="#f0f1f2",activebackground="#f0c808")
        button_clear.place(x=150,y=275,height=30,width=120)
        
        self.button_update=tk.Button(Frame2,text="Update",state=tk.NORMAL,command=self.update,font=("Arial bold",18),bg="#1c448e",fg="#f0f1f2",activebackground="#f0c808")
        self.button_update.place(x=280,y=275,height=30,width=120)
        
        self.button_delete=tk.Button(Frame2,text="Delete",state=tk.NORMAL,command=self.delete,font=("Arial bold",18),bg="#d7263d",fg="#f0f1f2",activebackground="#f0c808")
        self.button_delete.place(x=410,y=275,height=30,width=120)
        
        #Frame3
        Frame3=tk.Frame(self.root,bd=3,relief=tk.RIDGE,bg="#292826")
        Frame3.place(x=770,y=410,width=580,height=310)
        
        #alculator Frame
        self.var_txt=tk.StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
            
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
            
        def clear_calc():
            self.var_txt.set('')
            self.var_operator=''
        
        cal_frame=tk.Frame(Frame3,bg="#292826",bd=2,relief=tk.RIDGE)
        cal_frame.place(x=5,y=5,width=247,height=295)
        
        txt_result=tk.Entry(cal_frame,bg='#292826',fg="#f0f1f2",textvariable=self.var_txt,font=("Arial bold",20,"bold"),justify=tk.RIGHT)
        txt_result.place(x=0,y=0,relwidth=1,height=50)
        
        #Row 1
        btn_7=tk.Button(cal_frame,text='7',command=lambda:btn_click(7),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_7.place(x=0,y=52,w=60,h=60)
        btn_8=tk.Button(cal_frame,text='8',command=lambda:btn_click(8),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_8.place(x=61,y=52,w=60,h=60)
        btn_9=tk.Button(cal_frame,text='9',command=lambda:btn_click(9),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_9.place(x=122,y=52,w=60,h=60)
        btn_divide=tk.Button(cal_frame,text='/',command=lambda:btn_click("/"),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_divide.place(x=183,y=52,w=60,h=60)
        
        #Row 2
        btn_4=tk.Button(cal_frame,text='4',command=lambda:btn_click(4),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_4.place(x=0,y=112,w=60,h=60)
        btn_5=tk.Button(cal_frame,text='5',command=lambda:btn_click(5),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_5.place(x=61,y=112,w=60,h=60)
        btn_6=tk.Button(cal_frame,text='6',command=lambda:btn_click(6),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_6.place(x=122,y=112,w=60,h=60)
        btn_multiply=tk.Button(cal_frame,text='*',command=lambda:btn_click("*"),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_multiply.place(x=183,y=112,w=60,h=60)
        
        #Row 3
        btn_1=tk.Button(cal_frame,text='1',command=lambda:btn_click(1),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_1.place(x=0,y=172,w=60,h=60)
        btn_2=tk.Button(cal_frame,text='2',command=lambda:btn_click(2),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_2.place(x=61,y=172,w=60,h=60)
        btn_3=tk.Button(cal_frame,text='3',command=lambda:btn_click(3),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_3.place(x=122,y=172,w=60,h=60)
        btn_minus=tk.Button(cal_frame,text='-',command=lambda:btn_click("-"),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_minus.place(x=183,y=172,w=60,h=60)
        
        #Row 4
        btn_0=tk.Button(cal_frame,text='0',command=lambda:btn_click(0),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_0.place(x=0,y=233,w=60,h=60)
        btn_clear=tk.Button(cal_frame,text='C',command=clear_calc,font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_clear.place(x=61,y=233,w=60,h=60)
        btn_plus=tk.Button(cal_frame,text='+',command=lambda:btn_click("+"),font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_plus.place(x=122,y=233,w=60,h=60)
        btn_equalto=tk.Button(cal_frame,text='=',command=result,font=("Arial bold",15,"bold"),bg="#292826",fg="#f0c808",activebackground="#f0c808")
        btn_equalto.place(x=183,y=233,w=60,h=60)
        
        # Payslip
        sal_frame=tk.Frame(Frame3,bg="#292826",bd=2,relief=tk.RIDGE)
        sal_frame.place(x=260,y=5,width=310,height=295)

        title_sal=tk.Label(sal_frame,text="Payslip",font=("Arial bold",18),bg="#3b3e42",fg="#f0c808",anchor="w",padx=10)
        title_sal.place(x=0,y=0,relwidth=1)
        
        sal_frame2=tk.Frame(sal_frame,bg="#292826",bd=2,relief=tk.RIDGE)
        sal_frame2.place(x=0,y=30,relwidth=1,height=230)
        self.sample=f'''Company Name: Technocrats\nCourse: CSE1202
        
─────────────────────────
  Employee ID\t\t:               
  Salary Date\t\t:   Mon-YYYY     
  Generated on\t\t:  DD-MM-YYYY  
  Account # \t\t:                
─────────────────────────
  Hours Worked\t\t:              
  Wage Rate   \t\t:  GYD.-----   
  Medical     \t\t:  GYD.-----   
  Income Tax  \t\t:  GYD.-----   
  NIS         \t\t:  GYD.-----   
─────────────────────────                              
  Basic Salary\t\t:  GYD.-----   
  Net Salary  \t\t:  GYD.-----    
─────────────────────────
'''
        scroll_y=tk.Scrollbar(sal_frame2,orient=tk.VERTICAL)
        scroll_y.pack(fill=tk.Y,side=tk.RIGHT)
        
        self.txt_salary_receipt=tk.Text(sal_frame2,font=("Arial bold",11),bg="#292826",fg="#f0f1f2",yscrollcommand=scroll_y.set)
        self.txt_salary_receipt.pack(fill=tk.BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_receipt.yview)
        self.txt_salary_receipt.insert(tk.END,self.sample)
        
        self.button_print=tk.Button(sal_frame,text="Print",command=self.print,state=tk.NORMAL,font=("Arial bold",18),bg="#292826",fg="#f0f1f2",activebackground="#f0c808")
        self.button_print.place(x=180,y=262,height=30,width=110)
        
        self.check_connection()
    
    #Functions

    #Function to search database
    def search(self):
        try:
            con=dbinfo.connect()
            cur=con.cursor()
            cur.execute("select * from user_information where UserID=%s",(self.var_emp_id.get()))
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Employee ID,Please try with another ID",parent=self.root)
            else:
                self.var_emp_id.set(row[1]) 
                self.var_department.set(row[7]) 
                self.var_name.set(row[4]) 
                self.var_gender.set(row[6]) 
                self.var_bank.set(row[11]) 
                self.var_address.set(row[5]) 
                self.var_b_salary.set(row[19]) 
                self.var_dob.set(row[8]) 
                self.var_date.set(row[15])
                self.var_wage_rate.set(row[16])
                self.var_tax.set(row[18])
                self.var_bankid.set(row[12])
                self.var_accountno.set(row[13])
                self.var_salaryid.set(row[14])
                self.var_medical.set(row[17])
                self.var_nis.set(row[9])
                self.var_n_salary.set(row[20])
                self.var_hours.set(row[10])
                self.var_taxid.set(row[9])
                self.var_paydate.set(row[8])
            
                new_sample=f'''Company Name: Technocrats\n
Course: CSE1202
─────────────────────────
  Employee ID\t\t: {self.var_emp_id.get()}
  Salary Date\t\t:  {self.var_date.get()}
  Generated on\t\t:  {str(time.strftime("%d-%m-%Y"))}
  Acccount  \t\t:   {self.var_accountno.get()}
 ─────────────────────────
 
  Hours worked\t\t: {self.var_hours.get()}hours
  Wage Rate   \t\t:  GYD.{self.var_wage_rate.get()}
  Medical     \t\t:  GYD.{self.var_medical.get()}
  Income Tax  \t\t:  GYD.{self.var_tax.get()}
  NIS         \t\t:  GYD.{self.var_nis.get()}
  Basic Salary\t\t: GYD{self.var_b_salary.get()}
  Net Salary\t\t  : GYD.{self.var_n_salary.get()}
 ─────────────────────────
 '''         

                self.txt_salary_receipt.delete('1.0',tk.END)
                self.txt_salary_receipt.insert(tk.END,new_sample)
                self.button_update.config(state=tk.NORMAL)
                self.button_delete.config(state=tk.NORMAL)
                self.txt_code.config(state='readonly')
                self.button_print.config(state=tk.NORMAL)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to: {str(ex)}')
    

    # Function to clear all the entry boxes
    def clear(self):
        self.button_update.config(state=tk.NORMAL)
        self.button_delete.config(state=tk.NORMAL)
        self.button_print.config(state=tk.NORMAL)
        self.txt_code.config(state=tk.NORMAL)
        self.var_emp_id.set('')
        self.var_department.set('')
        self.var_name.set('')
        self.var_gender.set('')
        self.var_salaryid.set('')
        self.var_address.set('')
        self.var_bank.set('')
        self.var_bankid.set('')
        self.var_dob.set('')
        self.var_accountno.set ('')
        self.var_n_salary.set('')
        self.var_lb1_values.set('')
        self.var_date.set('')
        self.var_wage_rate.set('')
        self.var_tax.set('')
        self.var_b_salary.set('')
        self.var_medical.set('')
        self.var_nis.set('')
        self.var_hours.set('')
        self.var_taxid.set('')
        self.txt_salary_receipt.delete('1.0',tk.END)
        
    # Function to delete a user
    def delete(self):
        if self.var_emp_id.get()=='':
            messagebox.showerror("Error","Employee ID is required")
        else:
            try:
                con=dbinfo.connect()
                cur=con.cursor()
                cur.execute("select * from user_information where UserID=%s",(self.var_emp_id.get()))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID,Please try with another ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you want to Delete??")
                    if op==True:
                        cur.execute("delete from user_information where ID=%s",(self.var_emp_id.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee Record Deleted Successfully",parent=self.root)
                        self.clear()
                    pass
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
        
  
    # Function to update employees information
    def update(self):
        if self.var_emp_id.get()=='' or self.var_n_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee details are required")
        else:
            try:
                con=dbinfo.connect()
                cur=con.cursor()
                cur.execute("select * from user_information where UserID=%s",(self.var_emp_id.get()))
                row=cur.fetchone()
                
                department =  self.var_department.get()
                self.lb1_values = tk.Variable(value=department)
               

                emp =  self.var_emp_id.get()
                self.lb2_values = tk.Variable(value=emp)
                

                gender = self.var_gender.get()
                self.lb123_values = tk.Variable(value=gender)

                salary = self.txt_salary_receipt.get('1.0',tk.END)
                self.ll_values = tk.Variable(value = salary)
             

                name =  self.var_name.get()
                self.lb3_values = tk.Variable(value=name)

                dob =  self.var_dob.get()
                self.lb4_values = tk.Variable(value=dob)

                address =  self.var_address.get()
                self.lb5_values = tk.Variable(value=address)

                taxid =  self.var_taxid.get()
                self.lb6_values = tk.Variable(value=taxid)

                bank =  self.var_bank.get()
                self.lb7_values = tk.Variable(value=bank)

                bankid =  self.var_bankid.get()
                self.lb8_values = tk.Variable(value=bankid)

                accountno =  self.var_accountno.get()
                self.lb2_values = tk.Variable(value=accountno)


                salaryid =  self.var_salaryid.get()
                self.lb9_values = tk.Variable(value=salaryid)

                paydate =  self.var_paydate.get()
                self.lb10_values = tk.Variable(value=paydate)

                wage_rate =  self.var_wage_rate.get()
                self.lb11_values = tk.Variable(value=wage_rate)

                tax =  self.var_tax.get()
                self.lb12_values = tk.Variable(value=tax)

                nis =  self.var_nis.get()
                self.lb13_values = tk.Variable(value=nis)

                b_salary =  self.var_b_salary.get()
                self.lb14_values = tk.Variable(value=b_salary)

                n_salary =  self.var_n_salary.get()
                self.lb15_values = tk.Variable(value=n_salary)

                hours =  self.var_hours.get()
                self.lb17_values = tk.Variable(value=hours)

                medical = self.var_medical.get()
                self.lb19_values = tk.Variable(value = medical)

                if row==None:
                    messagebox.showerror("Error","This employee id is invalid,try again with valid id",parent=self.root)
                else:
                    sql = ("UPDATE `user_information` SET `Department`=%s,`Name`=%s,`DOB`=%s,`Address`=%s,`Gender`=%s,`NIS`=%s,`Bank`=%s,`BankID`=%s,`AccountNumber`=%s,`SalaryID`=%s,`Paydate`=%s,`WageRate`=%s,`Medical`=%s,`Tax`=%s,`BasicSalary`=%s, `NetSalary`= %s,`SalaryReceipt`=%s, `Hours`=%s WHERE UserID = %s") #,(self.var_department.get()))#self.var_name.get(),self.var_age.get(),self.var_gender.get(),self.var_email.get(),self.var_hr_location.get(),self.var_dob.get(),self.var_doj.get(),self.var_experience.get(),self.var_proofid.get(),self.var_contact.get(),self.var_status.get(),self.txt_address.get('1.0',tk.END),self.var_month.get(),self.var_year.get(),self.var_b_salary.get(),self.var_t_days.get(),self.var_absents.get(),self.var_medical.get(),self.var_pf.get(),self.var_conveyance.get(),self.var_n_salary.get(),self.var_emp_id.get()+".txt",self.var_emp_id.get()))
                    data = (department,name,dob,address,gender,taxid, bank, bankid, accountno,salaryid,paydate,wage_rate,medical,tax,b_salary,n_salary,salary,hours,emp)

                    cur.execute(sql,data)
                    con.commit()
                    con.close()
                    file=open('receipts/'+str(emp)+".txt",'w')
                    file.close
                    messagebox.showinfo("Success","Record Updated Successfully")
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to: {str(ex)}')
            
    # Function to calculate salary
    def calculate(self):
        if self.var_date.get()=='' or self.var_b_salary.get()=='':
            messagebox.showerror('Error','All Fields are required')
        else:
            wagerate_cal1=float(self.var_b_salary.get())/(52)
            hours = self.var_hours.get()
            wagerate_cal2 = float(wagerate_cal1/float(hours))
            
            incometax = float(self.var_b_salary.get())*float(0.30)
            nis = float(self.var_b_salary.get())*(0.048)
            deduct = float(self.var_b_salary.get())-float(incometax+nis)

            self.var_n_salary.set(str(wagerate_cal1))
            self.var_wage_rate.set(str(wagerate_cal2))
            self.var_tax.set(str(incometax))
            self.var_nis.set(str(nis))
            self.var_n_salary.set(str(deduct))
            
            #####Update Receipt####
            new_sample=f'''Company Name: Technocrats\nCourse: CSE1202
─────────────────────────
  Employee ID\t\t: {self.var_emp_id.get()}
  Salary Date\t\t:  {self.var_date.get()}
  Generated on\t\t:  {str(time.strftime("%d-%m-%Y"))}
  Acccount # \t\t:   {self.var_accountno.get()}
─────────────────────────
 
  Hours worked\t\t: {self.var_hours.get()}hours
  Wage Rate   \t\t:  GYD.{self.var_wage_rate.get()}
  Medical     \t\t:  GYD.{self.var_medical.get()}
  Income Tax  \t\t:  GYD.{self.var_tax.get()}
  NIS         \t\t:  GYD.{self.var_nis.get()}
  Basic Salary\t\t: GYD{self.var_b_salary.get()}
  Net Salary\t\t  : GYD.{self.var_n_salary.get()}
─────────────────────────
# '''         

            self.txt_salary_receipt.delete('1.0',tk.END)
            self.txt_salary_receipt.insert(tk.END,new_sample)

    # Functon to check database connection  
    def check_connection(self):
        try:
            con=dbinfo.connect()
            cur=con.cursor()
            cur.execute("select * from user_information")
            self.row=cur.fetchall()
        except Exception as ex:
            messagebox.showerror("Error",f'Cause: {str(ex)}')

    # Functon to show all employee details in table
    def show(self):
        try:
            con=dbinfo.connect()
            cur=con.cursor()
            cur.execute("select * from user_information")
            row=cur.fetchall()
            self.employee_tree.delete(*self.employee_tree.get_children())
            for x in row:
                self.employee_tree.insert('',tk.END,values=x)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error",f'Cause: {str(ex)}')
            
    # Functon to logout  
    def logout(self):
        messagebox.showinfo("Success","Logged Out Successfully",parent=self.root)
        self.root.destroy()
        import main
    
    # Employees table frame
    def employee_frame(self):
        self.root2=tk.Toplevel(self.root)
        self.root2.title("All Employee Details")
        self.root2.geometry("1080x700")
        self.root2.config(bg="#ffffff")
        title=tk.Label(self.root2,text="All Employee Details",font=("Arial bold",30,"bold"),bg="#b4c5e4",fg="#011936",anchor="w",padx=10)
        title.pack(side=tk.TOP,fill=tk.X)
        self.root2.focus_force()
        
        scrolly=tk.Scrollbar(self.root2,orient=tk.VERTICAL,bg="#99edc3")
        scrollx=tk.Scrollbar(self.root2,orient=tk.HORIZONTAL,bg="#99edc3")
        scrollx.pack(side=tk.BOTTOM,fill=tk.X)
        scrolly.pack(side=tk.RIGHT,fill=tk.Y)
        
        self.employee_tree=ttk.Treeview(self.root2,columns=('id', 'userid','username','password','name','address', 'gender', 'department','dob', 'tax_id','hours', 'bank', 'bank_id', 'accountno', 'salary_id', 'pay_date', 'wage_rate', 'medical','tax','basic_salary', 'net_salary', 'salary_receipt'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('id',text='ID')
        self.employee_tree.heading('userid',text='UserID')
        self.employee_tree.heading('username',text='Username')
        self.employee_tree.heading('password',text='Password')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('department',text='Department')
        self.employee_tree.heading('dob',text='DOB')
        self.employee_tree.heading('tax_id',text='NIS')
        self.employee_tree.heading('hours',text='Hours')
        self.employee_tree.heading('bank',text='Bank')
        self.employee_tree.heading('bank_id',text='BankID')
        self.employee_tree.heading('accountno',text='Account#')
        self.employee_tree.heading('salary_id',text='Salary ID')
        self.employee_tree.heading('pay_date',text='Pay Date')
        self.employee_tree.heading('wage_rate',text='Wage Rate')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('tax',text='Income Tax')
        self.employee_tree.heading('basic_salary',text='Basic Salary')
        self.employee_tree.heading('net_salary',text='Net Salary')
        self.employee_tree.heading('salary_receipt',text='Salary Receipt')
        self.employee_tree['show']='headings'
        
        self.employee_tree.column('id',width=50)
        self.employee_tree.column('userid',width=100)
        self.employee_tree.column('username',width=100)
        self.employee_tree.column('password',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('address',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('department',width=100)

        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('tax_id',width=100)
        self.employee_tree.column('hours',width=100)

        self.employee_tree.column('bank',width=100)
        self.employee_tree.column('bank_id',width=100)
        self.employee_tree.column('accountno',width=100)
        self.employee_tree.column('salary_id',width=100)
        self.employee_tree.column('pay_date',width=100)
        self.employee_tree.column('wage_rate',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('tax',width=100)
        self.employee_tree.column('basic_salary',width=100)

        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_receipt',width=500)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.employee_tree.pack(fill=tk.BOTH,expand=1)
        self.show()
    
        self.root2.mainloop()
        
    # Function to print salary slip
    def print(self):
        file=tempfile.mktemp(".txt")
        
        textContent = self.txt_salary_receipt.get('1.0',tk.END)
        filename=self.var_emp_id.get()
        myfile = open(filename, "w+",encoding="utf-8")
        myfile.write(textContent)
        # to test
        print("File saved as", filename)
        self.txt_salary_receipt.insert(tk.END,self.sample)

    
root=tk.Tk()
obj=payrollsystem(root)
root.mainloop()

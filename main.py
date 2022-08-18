from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pyautogui
import string
import random
import sqlite3
from PIL import ImageTk,Image


admin_info = {'admin':'password'}

connector = sqlite3.connect('Report.db')
cursor = connector.cursor()

cursor.execute(""" 
CREATE TABLE if not exists report
    (name text,
    report_name text,
    description text
)""")

connector.commit()

def exit_1():
    window0.destroy()
    
def exit_2():
    window_report.destroy()

def exit_3():
    win001.destroy()

def pass_statement():
    pass

def quit_1():
    exit()

def bib():
    messagebox.showinfo("Bibliography", """
                        Information was taken from: 
                        https://www.unicef.org/end-violence/how-to-stop-cyberbullying 
                        https://us.norton.com/internetsecurity-how-to-how-to-recognize-and-protect-yourself-from-cybercrime.html#
                        https://support.google.com/google-ads/answer/2375413?hl=en
                        https://www.csa.gov.sg/gosafeonline/go-safe-for-me/homeinternetusers/5-simple-ways-you-can-fight-spam-and-protect-yourself
                        """)


def Admin_Login():
    global window0
    window0 = Toplevel()
    window0.geometry('400x400')
    window0.resizable(False, False)
    window0.title("Admin Sign In")
    label1 = Label(window0, text = "Admin Sign In", relief = "solid", width = 20, font = ("arial",19 ,"bold"), fg = 'white', bg = 'black').pack(fill = BOTH, padx = 2, pady = 2)
    label2 = Label(window0, text = "Username", width = 20, font = ("arial",12 ,"bold"), fg = 'black').place(x = 5, y = 125)
    label3 = Label(window0, text = "Password", width = 20, font = ("arial",12 ,"bold"), fg = 'black').place(x = 5, y = 185)
    entry0 = Entry(window0, textvar = usr).place(x = 180, y = 125)
    entry1 = Entry(window0, textvar = pwd, show='*').place(x = 180, y = 185)
    button2 = Button(window0, text = 'Login', command = passwords_1, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'white').place(x=125, y=250)
    button3 = Button(window0, text = 'Close', command = exit_1, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'white').place(x=200, y=250)
    
    window0.mainloop()

def admin_page():
    a = cursor.execute("SELECT rowid, * FROM report")
    connector.commit()
    global win001
    win001 = Tk()
    win001.geometry('1080x1080')
    win001.title("View Books")
    but = Button(win001, text = "Exit", command = exit_3, bg = 'red', fg = 'black').place(x=1800, y=1000)
    
    i = 0
    for record in a: 
        for j in range(len(record)):
            e = Entry(win001, width=(len(str(record[j]))), fg='black') 
            e.grid(row=i, column=j)
            e.insert(END, record[j])
        i += 1
    win001.attributes('-fullscreen', True)
    win001.mainloop()

# User page to view all options
def user_pg():
    global window_user
    root.destroy()
    window_user = Tk()
    
    menu = Menu(window_user)
    window_user.config(menu = menu)

    sub_menu = Menu(menu)
    menu.add_cascade(label = "Options", menu = sub_menu)
    sub_menu.add_command(label = "Bibliography", command = bib)
    
    bg = ImageTk.PhotoImage(Image.open('bg.png'))
    l_bg = Label(window_user, image = bg).place(x = 0, y = 0)
    
    
    window_user.title('User Page')
    report_but = Button(window_user, text="Report a \nCybercrime", command=report, height=10,width=45,relief = RAISED, font = ("arial", 20, "bold"), fg = 'white', bg = 'purple').place(x=40, y=100)
    password_checker = Button(window_user, text = 'Password \nChecker', command = password_check, height=10,width=45,relief = RAISED, font = ("arial", 20, "bold"), fg = 'white', bg = 'purple').place(x=960, y=100)
    password_generator = Button(window_user, text = 'Password \nGenerator', command = password_gen, height=10,width=45,relief = RAISED, font = ("arial", 20, "bold"), fg = 'white', bg = 'purple').place(x=40, y=520)
    tips_but = Button(window_user, text = 'Tips to Follow When Browsing the Internet', command = tips, height=10,width=45,relief = RAISED, font = ("arial", 20, "bold"), fg = 'white', bg = 'purple').place(x=960, y=520)
    
    quit_but = Button(window_user, text='Close', command=quit_1, relief = RAISED, font = ("arial", 12, "bold"), fg = 'black', bg = 'red').place(x=1800, y=950)
    window_user.attributes('-fullscreen', True)
    window_user.mainloop()

# Password to access the admin page

def passwords_1():
    global username
    global password
    
    username = usr.get()
    password = pwd.get()
    if str(username) in admin_info:
        if admin_info[username] == password:
            window0.destroy()
            messagebox.showinfo("Information","Successfully Signed In!")
            admin_page()
        else:
            messagebox.showerror("Error", "Wrong Password")
    else:
        messagebox.showerror("Error", "Wrong Username")

# THINGS INSIDE THE PORTAL

# Report to admin
def report():
    global name, r_name, description_1, description_2, description_3, description_4, description_5, window_report
    window_report = Toplevel()
    window_report.title("Report")
    window_report.geometry("500x550")
    window_report.resizable(False, False)
    
    bg_r = ImageTk.PhotoImage(Image.open('report_img.jpg'))
    l_bg_r = Label(window_report, image = bg_r).place(x = 0, y = 0)
    
    
    l_1 = Label(window_report, text = "File Your Report", bg = "black", fg = "white", font = ("arial",20 ,"bold")).pack(padx=10, pady=10, fill = BOTH)
    l_name = Label(window_report, text = 'Enter your name:', fg = 'black').place(x = 70, y = 100)
    l_r_name = Label(window_report, text = "Enter the problem type: ").place(x = 35, y = 160)
    
    l_2 = Label(window_report, text = "Describe your problem below...", fg = 'black').place(x = 10, y = 200)
    l_3 = Label(window_report, text = "Line 1", fg = 'black').place(x = 10, y = 230)
    l_4 = Label(window_report, text = "Line 2", fg = 'black').place(x = 10, y = 280)
    l_5 = Label(window_report, text = "Line 3", fg = 'black').place(x = 10, y = 330)
    l_6 = Label(window_report, text = "Line 4", fg = 'black').place(x = 10, y = 380)
    l_7 = Label(window_report, text = "Line 5", fg = 'black').place(x = 10, y = 430)
    
    b_1 = Button(window_report, text = 'Submit', command=get_report).place(x = 120, y = 500)
    b_2 = Button(window_report, text = 'Exit', command=exit_2, width=6).place(x = 300, y = 500)
    
    name = StringVar()
    r_name = StringVar()
    description_1 = StringVar()
    description_2 = StringVar()
    description_3 = StringVar()
    description_4 = StringVar()
    description_5 = StringVar()
    
    e_name = Entry(window_report, textvariable=name).place(x = 200, y = 100)
    
    list_of_r_name = ['Cyberbullying', 'Cybercrime', 'Malware', 'Internet Attacks', 'Other']
    droplist = OptionMenu(window_report, r_name, *list_of_r_name)
    r_name.set("Select Below")
    droplist.config(width = 15)
    droplist.place(x = 200, y = 150)
    
    
    e_description_1 = Entry(window_report, textvariable=description_1, width = 60).place(x = 10, y = 252)
    e_description_2 = Entry(window_report, textvariable=description_2, width = 60).place(x = 10, y = 302)
    e_description_3 = Entry(window_report, textvariable=description_3, width = 60).place(x = 10, y = 352)
    e_description_4 = Entry(window_report, textvariable=description_4, width = 60).place(x = 10, y = 402)
    e_description_5 = Entry(window_report, textvariable=description_5, width = 60).place(x = 10, y = 452)
    
    
    
    window_report.mainloop()

def get_report():
    flag = False
    f_name = name.get()
    f_r_name = r_name.get()
    f_description_1 = description_1.get()
    f_description_2 = description_2.get()
    f_description_3 = description_3.get()
    f_description_4 = description_4.get()
    f_description_5 = description_5.get()
    if f_name == '':
        messagebox.showerror("Attention!", "Please Enter Your Name.")
    else:
        flag = True
    if f_r_name == 'Select Below':
        flag = False
        messagebox.showerror("Attention!", "Please select an option")
    else:
        flag = True
        a = str(f_description_1 + ' | ' +  f_description_2 + ' | ' +  f_description_3 + ' | ' +  f_description_4 + ' | ' +  f_description_5)
    
    if flag == True:
        cursor.execute("""
    Insert INTO report values (?,?,?) 
    """,(f_name, f_r_name, a))
        connector.commit()
        messagebox.showinfo("Information", "Report Sent to the Admin!")
        window_report.destroy()
    
    connector.close()


# Password Checker
def password_check():
    password = pyautogui.password("Enter a Password you want to test: ", "Enter your password...")
    spcl = list("!@#$%^&*()_-+=~`{[}]|\:;\'<,>.?/\"")
    try:
        if len(password) < 4:
            messagebox.showerror("Attention!", "Password too short, try making it longer.")
            return
        
        if password.isascii():
            if any(i.isupper() for i in password) or any(i.islower() for i in password):
                if any(i in spcl for i in password) and ((any(i.isupper() for i in password) or any(i.islower() for i in password)) or (any(i.isdigit() for i in password))):
                        messagebox.showinfo("Information", "Password is Highly Secure!")
                elif any(i.isdigit() for i in password):
                    messagebox.showinfo("Information", "Password is Secure.")
                else:
                    messagebox.showinfo("Information", "Password is Okay...")
            else:
                messagebox.showerror("Attention!", "Password could be more secure!")
        else:
            messagebox.showerror("Attention!", "Please enter a valid password.")    
    except:
        pass

# Password Generator
def password_gen():
    while True:
        strength_of_password = pyautogui.confirm("\nHow strong do you want your password to be?", "Select an Option Below", buttons=[ "digits", "simple", "mediocre", "hard", "extreme"])
        if strength_of_password != None:
            while True:
                length_of_password = int(pyautogui.prompt("How long do you want the password to be? \n(number of characters)", "Enter:"))
                if length_of_password < 4:
                    messagebox.showerror("Attention!","The password must be greater than or equal to 4 characters... Try Again!")
                else:
                    break      
            if strength_of_password == 'digits':
                combined = string.digits
                break
            elif strength_of_password == 'simple':
                combined = string.ascii_lowercase
                break
            elif strength_of_password == 'mediocre':
                combined = string.ascii_lowercase + string.digits
                break
            elif strength_of_password == 'hard':
                combined = string.ascii_uppercase + string.ascii_lowercase + string.digits
                break
            elif strength_of_password == 'extreme':
                combined = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
                break
            else:
                messagebox.showerror("Attention!", "Please enter a valid choice...")
        else:
            break
    password = "".join(random.sample(combined, length_of_password))
    messagebox.showinfo("Information", "Your password is: " + password + "\nWrite it down somewhere so you don't forget.")

# Tips
def tips():
    # the four main internet abuses below
    choice = pyautogui.confirm("Hey there \nWhat kind of tips are you interested in?", "What do you say?",buttons=['Cyberbullying', 'Cybercrime', 'Malware', 'Spamming'])
    if choice == 'Cyberbullying':
        pyautogui.confirm("""
Can you tell the difference between a joke and bullying? 
It is hard to tell if someone is joking or if they are seriously trying to hurt you, especially online. 
But if you feel hurt or think others are laughing at you instead of with you, then the jokes have gone too far. 
If you feel bad and it doesn’t stop, then it’s worth getting help. 
Stopping cyberbullying is not just about calling out bullies, it’s also about recognizing that everyone deserves respect online and in real life.
""", "Tip 1", buttons=['Next'])
        
        pyautogui.confirm("""
What are the effects of cyberbullying?
When bullying happens online it would often seem like there is no escape.
It can affect a person in different ways:
1. Mentally – feeling upset, embarrassed, stupid, even afraid or angry
2. Emotionally – feeling ashamed or losing interest in the things you love doing
3. Physically – tiredness (loss of sleep), or experiencing symptoms like stomach aches and headaches
The feeling of being laughed at or harassed by others, can prevent people from speaking up or trying to deal with the problem.
Cyberbullying can affect us in many ways. But these can be overcome and people can regain their confidence and health.
""", "Tip 2", buttons = ['Next'])
        
        pyautogui.confirm("""
How can cyberbullying affect my mental health?
When you experience cyberbullying you might start to feel ashamed, nervous, anxious and insecure about what people say or think about you.
Feeling lonely, overwhelmed, frequent headaches, nausea or stomachaches are common.
You can lose your motivation to do the things that you usually enjoy doing and feel isolated from the people you love and trust.
Skipping school is another common effect of cyberbullying and can affect the mental health of young people.
Who sometimes turn to substances like alcohol and drugs or violent behavior to deal with their psychological and physical pain.
Talking to a friend, family member or school counsellor you trust can be a first step to getting help.
""", "Tip 3", buttons = ['Next'])
        
        pyautogui.confirm("""
Who should I talk to if someone is bullying me online? 
Why is reporting important?
If you think you’re being bullied, the first step is to seek help from someone you trust such as your parents, a close family member or another trusted adult.
If the bullying is happening on a social platform, consider blocking the bully and formally reporting their behaviour on the platform itself.
For bullying to stop, it needs to be identified and reporting it is key.
It can be helpful to collect evidence such as text messages and screen shots of social media posts to show what has been going on.
If you are in immediate danger, then you should contact the police or emergency services in your country.
Also, you can report through this application that would be viewed by the team and it's response would be shared as soon as possible.
""", "Tip 4", buttons = ['Next'])

        
        pyautogui.confirm("""
How do I prevent my personal information from being used to manipulate or humiliate me on social media?
Think twice before posting or sharing anything on digital platforms.
Don’t give out personal details such as your address, telephone number or the name of your school.
Read the privacy settings of social media apps.
Some of the most common ones are:
1. You can decide who can see your profile, send you direct messages or comment on your posts by adjusting your account privacy settings. 
2. You can report hurtful comments, messages, photos and videos and request they be removed.
3. Besides unfriending, you can completely block people to stop them from seeing your profile or contacting you.
4. You can delete posts and stories on your profile or hide them from specific people.
""", "Tip 5", buttons = ['Quit'])

    elif choice == 'Cybercrime':
        pyautogui.confirm("""
What is cybercrime?
Cybercrime is any crime that takes place online or primarily online. 
Cybercriminals often commit crimes by targeting computer networks or devices.
Cybercrime can range from security breaches to identity theft.
""", "Tip 1",buttons = ['Next'])
        
        pyautogui.confirm("""
How to protect yourself against cybercrime
Use a full-service internet security suite.
They provide real-time protection against existing and emerging malware including ransomware and viruses, 
and helps protect your private and financial information when you go online.
""", "Tip 2",buttons = ['Next'])
        
        pyautogui.confirm("""
Use strong passwords
Don’t repeat your passwords on different sites, and change your passwords regularly.
Make them complex. That means using a combination of at least 10 letters, numbers, and symbols.
""", "Tip 3",buttons = ['Next'])
        
        pyautogui.confirm("""
Take measures to help protect yourself against identity theft
Identity theft occurs when someone wrongfully obtains your personal data in a way that involves fraud or deception, typically for economic gain.
You might be tricked into giving personal information over the internet, for instance, or a thief might steal your mail to access account information.
That’s why it’s important to guard your personal data.
A VPN (Virtual Private Network) can also help to protect the data you send and receive online, especially when accessing the internet on public Wi-Fi.
""", "Tip 4",buttons = ['Next'])
        
        pyautogui.confirm("""
Know what to do if you become a victim
If you believe that you’ve become a victim of a cybercrime, you need to alert the local police or a higher authority.
This is important even if the crime seems minor.
Your report may assist authorities in their investigations or may help to catch criminals from taking advantage of other people in the future.
""", "Tip 5",buttons = ['Quit'])

    elif choice == 'Malware':
        pyautogui.confirm("""
What's malware?
"Malware" is any kind of software that's designed to harm a computer. 
Malware can steal sensitive information from your computer, gradually slow down your computer, or even send fake emails from your email account without your knowledge.
Here are some common types of malware you might have heard about:
1. Virus: A harmful computer program that can copy itself and infect a computer.
2. Worm: A malicious computer program that sends copies of itself to other computers via a network.
3. Spyware: Malware that collects information from people without their knowledge.
4. Adware: Software that automatically plays, displays, or downloads advertisements on a computer.
5. Trojan horse: Harms your computer or steals your information after it's installed.
""", "Tip 1", buttons = ['Next'])
        
        pyautogui.confirm("""
How malware spreads?
Malware can get onto your computer in a number of different ways. Here are some common examples:
1. Downloading free software from the Internet that secretly contains malware
2. Downloading legitimate software that's secretly bundled with malware
3. Visiting a website that's infected with malware
4. Clicking a fake error message or pop-up window that starts a malware download
5. Opening an email attachment that contains malware
""", "Tip 2", buttons = ['Next'])
        
        pyautogui.confirm("""
How to protect yourself from malware?
1. Keep your computer and software updated
2. Think twice before clicking links or downloading anything
3. Be careful about opening email attachments or images
4. Don't trust pop-up windows that ask you to download software
5. Use antivirus software (most important)
""", "Tip 3", buttons = ['Quit'])
        
    elif choice == 'Spamming':
        pyautogui.confirm("""
What is spamming?
Spamming is the use of electronic messaging systems like e-mails and other digital delivery systems and broadcast media to send unwanted bulk messages indiscriminately.
Simple Ways You Can Fight Spam and Protect Yourself are:
1. Never give out or post your email address publicly.
Posting your email address publicly allows others to send spam emails to you, or worse, hack your account if you are using a weak password.
2. Think before you click any link.
Make sure that you scrutinize the content of spam emails before opening any attachments (even if it looks like an innocent text or image file) or clicking on hyperlinks. 
3. Do not reply to spam messages
Never respond to spam messages because through this, the spammer will know that the email address is active and increases the chance of your email to be constantly targeted by the spammer.
4. Download spam filtering tools and anti-virus software
Spam filtering tools and anti-virus software can help to scan the emails that you received for malware. 
5. Avoid using your personal or business email address when registering in websites
Many spammers watch these groups or emailing lists to harvest new email addresses.
""", "Tip", buttons = ['Quit'])
        pass


if __name__ == '__main__':
    root = Tk()
    root.geometry('553x300')
    root.title("Main Window")
    root.resizable(False,False)
    
    menu = Menu(root)
    root.config(menu = menu)

    sub_menu = Menu(menu)
    menu.add_cascade(label = "Options", menu = sub_menu)
    sub_menu.add_command(label = "Bibliography", command = bib)
    
    
    img = ImageTk.PhotoImage(file= r"C:\Users\moin6\PycharmProjects\Projects\something.jpg")
    Label_BG = Label(root, image=img).place(x=0, y=0, relwidth=1, relheight=1)
    
    usr = StringVar()
    pwd = StringVar()
    
    label0 = Label(root, text = "Cyber Safety Portal", relief = "solid", width = 25, font = ("arial",25 ,"bold"), fg = 'white', bg = 'black').pack(fill = BOTH, padx = 0, pady = 0)
    Button0 = Button(root, text = "Admin", relief = "solid", width = 8, font = ("arial",27 ,"bold"), bg = 'white', fg = 'black', command=Admin_Login).place(x = 310, y = 75)
    Button1 = Button(root, text = "User", relief = "solid", width = 8, font = ("arial",27 ,"bold"), bg = 'white', fg = 'black', command=user_pg).place(x = 310, y = 187)
    
    root.mainloop()

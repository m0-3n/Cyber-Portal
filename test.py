from unicodedata import name
import pyautogui
from tkinter import font, messagebox
from tkinter import *
import sqlite3

    
# def tips():
    
    
    
    
    
    
    
    
    
    
#     name = pyautogui.prompt(
#         "What is you name?", "Enter your name below...")
#     # the four main internet abuses below
#     choice = pyautogui.confirm("Hey there " + name + ".\nWhat kind of tips are you interested in?", "What do you say?",buttons=['Cyberbullying', 'Cybercrime', 'Malware', 'Spamming'])
#     if choice == 'Cyberbullying':
#         pyautogui.confirm("""
# Can you tell the difference between a joke and bullying? 
# It is hard to tell if someone is joking or if they are seriously trying to hurt you, especially online. 
# But if you feel hurt or think others are laughing at you instead of with you, then the jokes have gone too far. 
# If you feel bad and it doesn’t stop, then it’s worth getting help. 
# Stopping cyberbullying is not just about calling out bullies, it’s also about recognizing that everyone deserves respect online and in real life.
# """, "Tip 1", buttons=['Next'])
        
#         pyautogui.confirm("""
# What are the effects of cyberbullying?
# When bullying happens online it would often seem like there is no escape.
# It can affect a person in different ways:
# 1. Mentally – feeling upset, embarrassed, stupid, even afraid or angry
# 2. Emotionally – feeling ashamed or losing interest in the things you love doing
# 3. Physically – tiredness (loss of sleep), or experiencing symptoms like stomach aches and headaches
# The feeling of being laughed at or harassed by others, can prevent people from speaking up or trying to deal with the problem.
# Cyberbullying can affect us in many ways. But these can be overcome and people can regain their confidence and health.
# """, "Tip 2", buttons = ['Next'])
        
#         pyautogui.confirm("""
# How can cyberbullying affect my mental health?
# When you experience cyberbullying you might start to feel ashamed, nervous, anxious and insecure about what people say or think about you.
# Feeling lonely, overwhelmed, frequent headaches, nausea or stomachaches are common.
# You can lose your motivation to do the things that you usually enjoy doing and feel isolated from the people you love and trust.
# Skipping school is another common effect of cyberbullying and can affect the mental health of young people.
# Who sometimes turn to substances like alcohol and drugs or violent behavior to deal with their psychological and physical pain.
# Talking to a friend, family member or school counsellor you trust can be a first step to getting help.
# """, "Tip 3", buttons = ['Next'])
        
#         pyautogui.confirm("""
# Who should I talk to if someone is bullying me online? 
# Why is reporting important?
# If you think you’re being bullied, the first step is to seek help from someone you trust such as your parents, a close family member or another trusted adult.
# If the bullying is happening on a social platform, consider blocking the bully and formally reporting their behaviour on the platform itself.
# For bullying to stop, it needs to be identified and reporting it is key.
# It can be helpful to collect evidence such as text messages and screen shots of social media posts to show what has been going on.
# If you are in immediate danger, then you should contact the police or emergency services in your country.
# Also, you can report through this application that would be viewed by the team and it's response would be shared as soon as possible.
# """, "Tip 4", buttons = ['Next'])

        
#         pyautogui.confirm("""
# How do I prevent my personal information from being used to manipulate or humiliate me on social media?
# Think twice before posting or sharing anything on digital platforms.
# Don’t give out personal details such as your address, telephone number or the name of your school.
# Read the privacy settings of social media apps.
# Some of the most common ones are:
# 1. You can decide who can see your profile, send you direct messages or comment on your posts by adjusting your account privacy settings. 
# 2. You can report hurtful comments, messages, photos and videos and request they be removed.
# 3. Besides unfriending, you can completely block people to stop them from seeing your profile or contacting you.
# 4. You can delete posts and stories on your profile or hide them from specific people.
# """, "Tip 5", buttons = ['Quit'])

#     elif choice == 'Cybercrime':
#         pyautogui.confirm("""
# What is cybercrime?
# Cybercrime is any crime that takes place online or primarily online. 
# Cybercriminals often commit crimes by targeting computer networks or devices.
# Cybercrime can range from security breaches to identity theft.
# """, "Tip 1",buttons = ['Next'])
        
#         pyautogui.confirm("""
# How to protect yourself against cybercrime
# Use a full-service internet security suite.
# They provide real-time protection against existing and emerging malware including ransomware and viruses, 
# and helps protect your private and financial information when you go online.
# """, "Tip 2",buttons = ['Next'])
        
#         pyautogui.confirm("""
# Use strong passwords
# Don’t repeat your passwords on different sites, and change your passwords regularly.
# Make them complex. That means using a combination of at least 10 letters, numbers, and symbols.
# """, "Tip 3",buttons = ['Next'])
        
#         pyautogui.confirm("""
# Take measures to help protect yourself against identity theft
# Identity theft occurs when someone wrongfully obtains your personal data in a way that involves fraud or deception, typically for economic gain.
# You might be tricked into giving personal information over the internet, for instance, or a thief might steal your mail to access account information.
# That’s why it’s important to guard your personal data.
# A VPN (Virtual Private Network) can also help to protect the data you send and receive online, especially when accessing the internet on public Wi-Fi.
# """, "Tip 4",buttons = ['Next'])
        
#         pyautogui.confirm("""
# Know what to do if you become a victim
# If you believe that you’ve become a victim of a cybercrime, you need to alert the local police or a higher authority.
# This is important even if the crime seems minor.
# Your report may assist authorities in their investigations or may help to catch criminals from taking advantage of other people in the future.
# """, "Tip 5",buttons = ['Quit'])

#     elif choice == 'Malware':
#         pyautogui.confirm("""
# What's malware?
# "Malware" is any kind of software that's designed to harm a computer. 
# Malware can steal sensitive information from your computer, gradually slow down your computer, or even send fake emails from your email account without your knowledge.
# Here are some common types of malware you might have heard about:
# 1. Virus: A harmful computer program that can copy itself and infect a computer.
# 2. Worm: A malicious computer program that sends copies of itself to other computers via a network.
# 3. Spyware: Malware that collects information from people without their knowledge.
# 4. Adware: Software that automatically plays, displays, or downloads advertisements on a computer.
# 5. Trojan horse: Harms your computer or steals your information after it's installed.
# """, "Tip 1", buttons = ['Next'])
        
#         pyautogui.confirm("""
# How malware spreads?
# Malware can get onto your computer in a number of different ways. Here are some common examples:
# 1. Downloading free software from the Internet that secretly contains malware
# 2. Downloading legitimate software that's secretly bundled with malware
# 3. Visiting a website that's infected with malware
# 4. Clicking a fake error message or pop-up window that starts a malware download
# 5. Opening an email attachment that contains malware
# """, "Tip 2", buttons = ['Next'])
        
#         pyautogui.confirm("""
# How to protect yourself from malware?
# 1. Keep your computer and software updated
# 2. Think twice before clicking links or downloading anything
# 3. Be careful about opening email attachments or images
# 4. Don't trust pop-up windows that ask you to download software
# 5. Use antivirus software (most important)
# """, "Tip 3", buttons = ['Quit'])
        
#     elif choice == 'Spamming':
#         pyautogui.confirm("""
# What is spamming?
# Spamming is the use of electronic messaging systems like e-mails and other digital delivery systems and broadcast media to send unwanted bulk messages indiscriminately.
# Simple Ways You Can Fight Spam and Protect Yourself are:
# 1. Never give out or post your email address publicly.
# Posting your email address publicly allows others to send spam emails to you, or worse, hack your account if you are using a weak password.
# 2. Think before you click any link.
# Make sure that you scrutinize the content of spam emails before opening any attachments (even if it looks like an innocent text or image file) or clicking on hyperlinks. 
# 3. Do not reply to spam messages
# Never respond to spam messages because through this, the spammer will know that the email address is active and increases the chance of your email to be constantly targeted by the spammer.
# 4. Download spam filtering tools and anti-virus software
# Spam filtering tools and anti-virus software can help to scan the emails that you received for malware. 
# 5. Avoid using your personal or business email address when registering in websites
# Many spammers watch these groups or emailing lists to harvest new email addresses.
# """, "Tip", buttons = ['Quit'])
#         pass

# tips()

# DB

connector = sqlite3.connect('Report.db')
cursor = connector.cursor()

cursor.execute(""" 
CREATE TABLE if not exists report
    (name text,
    report_name text,
    description text
)""")

connector.commit()


def report():
    global hmm_name, r_name, window_report, text_1
    window_report = Tk()
    window_report.title("Report")
    window_report.geometry("500x550")
    window_report.resizable(False, False)
    
    
    l_1 = Label(window_report, text = "File Your Report", bg = "black", fg = "white", font = ("arial",20 ,"bold")).pack(padx=10, pady=10, fill = BOTH)
    l_name = Label(window_report, text = 'Enter your name:', fg = 'black').place(x = 70, y = 100)
    l_r_name = Label(window_report, text = "Enter the problem type: ").place(x = 35, y = 160)
    
    l_2 = Label(window_report, text = "Describe your problem here...", fg = 'black').place(x = 10, y = 200)


    
    b_1 = Button(window_report, text = 'Submit', command=get_report()).place(x = 120, y = 500)
    b_2 = Button(window_report, text = 'Exit', command=exit_1, width=6).place(x = 300, y = 500)
    
    hmm_name = StringVar()
    r_name = StringVar()
    
    

    
    e_name = Entry(window_report, textvariable=hmm_name).place(x = 200, y = 100)
    
    list_of_r_name = ['Cyberbullying', 'Cybercrime', 'Malware', 'Internet Attacks', 'Other']
    droplist = OptionMenu(window_report, r_name, *list_of_r_name)
    r_name.set("Select Below")
    droplist.config(width = 15)
    droplist.place(x = 200, y = 150)   
    
    text_1 = Text(window_report,height=13, width=47).place(x = 10, y = 230)
    
    
    window_report.mainloop()

def exit_1():
    exit()



def get_report():
    
    def get_txt():
        global txt_inp
        txt_inp = text_1.get(1.0, "end-1c")
        return txt_inp
    
    
    flag = False
    f_name = hmm_name.get()
    f_r_name = r_name.get()
    
    
    if f_name == '':
        messagebox.showerror("Attention!", "Please Enter Your Name.")
    else:
        flag = True
        print(f_name)
    if f_r_name == 'Select Below':
        flag = False
        messagebox.showerror("Attention!", "Please select an option")
    else:
        flag = True
        print(f_r_name)
        
    a = get_txt()
    
    if flag == True:
        cursor.execute("""
    Insert INTO report values (?,?,?) 
    """,(f_name, f_r_name, a))
        connector.commit()
        messagebox.showinfo("Information", "Report Sent to the Admin!")
        window_report.destroy()


report()
connector.close()
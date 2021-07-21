
from tkinter import *  
from pytube import YouTube 
from tkinter import filedialog 
import  smtplib 
import stdiomask 





def browseFiles(): # To get path where the file need to be Download by Browsing
    global path
    path = filedialog.askdirectory()    
    path=path.replace('/','\\\\') # The Path should be in format " c:\\Users\\examples\\ "" 
    return path

def browseFiles_location(): # To allocate the path 
        location = path
        return location


def mail():
    
    sender='Sender_mail@gmail.com' # Sender mail
    receivers = 'Reciever_mail@gmail.com' # Receiver mail
    password = stdiomask.getpass() # It will hide password ny using " * " 
    message= """Hi. Very are trying to download video through link. """ # Message need to send to receiver

    server =smtplib.SMTP('smtp.gmail.com',587) 

    server.starttls()

    server.login(sender,password) # Login to mail

    print("Login Success")

    server.sendmail(sender,receivers,message) # Send mail

    print("EMail has sent to mail.")



def Downloader():
    try :
        link1 =YouTube(str(link.get()))
        video = link1.streams.first()
        video.download(browseFiles_location())
        mail()
        
        Label(root, text = 'DOWNLOADED', font = 'calibri 20').place(x= 400 , y = 510)  
    except:
        print("Some Error in given Link")





root = Tk()
root.geometry('800x600') # Sizing the Frame
root.resizable(0,0)
root.title("YouTube Video Downloader")

Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()

Label(root , text = 'Choose directory' , font = 'arial 20 bold').place(x =120, y=190)

button_explore = Button(text = "Choose directory" , command = browseFiles)

link = StringVar()  # Variable to store Link

Label(root, text = 'Paste your Link Here:', font = 'calibri 25 bold').place(x= 250 , y = 50)

link_enter = Entry(root, width = 90,textvariable = link).place(x = 120, y = 110)


Button(root,text = 'DOWNLOAD', font = 'calibri 15 bold' ,bg = 'firebrick1', padx = 2, command = Downloader).place(x=300 ,y =350)

button_exit = Button(text = "Exit" , command = exit)

button_exit.place(x= 250,y=500)

button_explore.place(x = 120, y= 240)

root.mainloop()
import tkinter as tk
from PIL import Image, ImageTk
from image_editor import output_image
#import quote_maths
from sendtoclient import sendfunc

window=tk.Tk()
window.geometry("500x500")
window.title("RARE AIR Quote Generator")

minimumguaranteedhoursinput=tk.StringVar()
ferrytimeinput=tk.StringVar()
clientnameinput=tk.StringVar()
clientemailinput=tk.StringVar()
agentinput=tk.StringVar()
averagesectorlengthinput=tk.StringVar()
basedathomeinput=tk.StringVar()
ferrytimeinput=tk.StringVar()
flightnumbersinput=tk.StringVar()
configurationinput=tk.StringVar()

def generate():
    mgh=float(minimumguaranteedhoursinput.get())
    ferrytime=float(ferrytimeinput.get())
    clientname=str(clientnameinput.get())
    clientemail=str(clientemailinput.get())
    agent=str(agentinput.get())
    averagesectorlength=str(averagesectorlengthinput.get())
    basedathome=str(basedathomeinput.get())
    ferytime=str(ferrytimeinput.get())
    flightnumbers=str(flightnumbersinput.get())
    configuration=str(configurationinput.get())

    flightcycleratio=averagesectorlength/60.
    
    output_image("Cessna C208B",agent,clientname,mgh)
    sendfunc(clientname,clientemail)
    
window.grid_columnconfigure((0,1), weight=1)#This command is crucial to get even column spacing
window.grid_rowconfigure((0,10),weight=1)

#This section creates the RARE heading
n=0.3#This is the rescale factor for the RARE logo
image=Image.open("../Resources/logo.png")
[imageWidth,imageHeight]=image.size
image=image.resize((int(n*imageWidth),int(n*imageHeight)),Image.ANTIALIAS)
logo=ImageTk.PhotoImage(image)
header=tk.Label(window,image=logo)
header.grid(row=0,column=0,columnspan=2)

prompt1=tk.Label(window,text="Please enter client name: ")
prompt1.grid(row=1,column=0)

entry1=tk.Entry(window,textvariable=clientnameinput)
entry1.grid(row=1,column=1)

prompt2=tk.Label(window,text="Please enter client email address: ")
prompt2.grid(row=2,column=0)

entry2=tk.Entry(window, textvariable=clientemailinput)
entry2.grid(row=2,column=1)

prompt3=tk.Label(window,text="Enter Minimum Guaranteed Hours:")
prompt3.grid(row=3,column=0)

entry3=tk.Entry(window,textvariable=minimumguaranteedhoursinput)
entry3.grid(row=3,column=1)

prompt4=tk.Label(window,text="Enter Estimated Ferry Time (hrs):")
prompt4.grid(row=4,column=0)

entry4=tk.Entry(window,textvariable=ferrytimeinput)
entry4.grid(row=4,column=1)

prompt5=tk.Label(window,text="Enter Average Sector Length (hrs, rounded to the nearest 0.1:",wraplength=200,justify='center')
prompt5.grid(row=5,column=0)

entry5=tk.Entry(window,textvariable=averagesectorlengthinput)
entry5.grid(row=5,column=1)

prompt6=tk.Label(window,text="Aircraft Based At Home: ")
prompt6.grid(row=6,column=0)

basedathomeinput.set("Yes")
entry6=tk.OptionMenu(window,basedathomeinput,"Yes","No")
entry6.grid(row=6,column=1)

prompt7=tk.Label(window, text="Are Flight Numbers Needed: ")
prompt7.grid(row=7,column=0)

flightnumbersinput.set("Yes")
entry7=tk.OptionMenu(window,basedathomeinput,"Yes","No")
entry7.grid(row=7,column=1)

prompt8=tk.Label(window, text="What is your name:")
prompt8.grid(row=8,column=0)

entry8=tk.Entry(window,textvariable=agentinput)
entry8.grid(row=8,column=1)

prompt9=tk.Label(window, text="Aircraft configuration: ")
prompt9.grid(row=9,column=0)

configurationinput.set("9 VIP")
entry9=tk.OptionMenu(window,configurationinput,"9 VIP","12 or Cargo", "Cargo Only", "19", "19 or Cargo","VIP")
entry9.grid(row=9,column=1)


outputButton=tk.Button(window, text="Calculate", command=generate)
outputButton.grid(row=10,column=0,columnspan=2)

window.mainloop()

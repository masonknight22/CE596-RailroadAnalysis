from tkinter import * #download all of tkinter
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import askopenfile
import os

main = Tk()
main.title("Input Values for Railroad Bridge Analysis")
main.geometry('700x700')

# Create a Main Frame
main_frame=Frame(main)
main_frame.pack(fill=BOTH, expand=1)
# Create A Canvas
my_canvas=Canvas(main_frame)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)
# Add a Scrollbar to the Canvas
my_scrollbar=ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
# Create ANOTHER frame in the Canvas
root=Frame(my_canvas, bg="#ECECEC")
# Add that new frame in a window in the canvas
my_canvas.create_window((0,0), window=root, anchor="nw")

#####y### SPAN INFORMATION
frame1=LabelFrame(root, text="Span Information", font='Helvetica 22 bold', padx=110, pady=30, bg="#FFFFFF", bd=0,
    highlightthickness=0)
frame1.grid(row=0,column=0,padx=10,pady=10)

startspan_label=Label(frame1,text="Start Span", bg="#FFFFFF").grid(row=0,column=0)
StartSpan=Entry(frame1, width=4, borderwidth=0)
StartSpan.grid(row=0,column=1)
StartSpan.insert(0, 50)

endspan_label=Label(frame1,text="End Span", bg="#FFFFFF").grid(row=1,column=0)
EndSpan=Entry(frame1, width=4, borderwidth=0)
EndSpan.grid(row=1,column=1)
EndSpan.insert(0, 50)

spanincrement_label=Label(frame1,text="Span Increment", bg="#FFFFFF").grid(row=2,column=0)
SpanIncrement=Entry(frame1, width=3, borderwidth=0)
SpanIncrement.grid(row=2,column=1)
SpanIncrement.insert(0,15)

## Moment/Stress Calcalculation Intervals
Blank_label=Label(frame1,text="  ").grid(row=4,column=0)
Moment_Stress_label=Label(frame1,text="Moment/Stress Calculation Interval Locations", bg="#FFFFFF", font=('TkDefaultFont', 10)).grid(row=5,column=0)

startmoment_label=Label(frame1,text="Start Location", bg="#FFFFFF").grid(row=6,column=0)
StartMoment=Entry(frame1, width=5, borderwidth=0)
StartMoment.grid(row=6,column=1)
StartMoment.insert(0, 0.05)

finishmoment_label=Label(frame1,text="End Location", bg="#FFFFFF").grid(row=7,column=0)
FinishMoment=Entry(frame1, width=5, borderwidth=0)
FinishMoment.grid(row=7,column=1)
FinishMoment.insert(0, 0.5)

intervalmoment_label=Label(frame1,text="Interval", bg="#FFFFFF").grid(row=8,column=0)
IntervalMoment=Entry(frame1, width=5, borderwidth=0)
IntervalMoment.grid(row=8,column=1)
IntervalMoment.insert(0, 0.05)

stepmoment_label=Label(frame1,text="Step Size", bg="#FFFFFF").grid(row=9,column=0)
StepMoment=Entry(frame1, width=5, borderwidth=0, bg="#FFFFFF")
StepMoment.grid(row=9,column=1)
StepMoment.insert(0, 0.01)

blank_label=Label(frame1,text="  ", bg="#FFFFFF").grid(row=4,column=0)
blank=Entry(frame1, width=5, borderwidth=0)



LLType_label=Label(frame1,text="LL Type", bg="#FFFFFF").grid(row=3,column=0)
LL=StringVar()
lltype_label=Label(root)

lltypes=["Custom",  "Alternate" , "CooperE"]
LL.set(lltypes[0])
##LL_Type=LL.get()
##LLtype_Button=Button(frame1,text="Save LL Type Changes",command=LL_type_command).grid(row=3,column=2)

#Drop Down Box
drop_LLtype=OptionMenu(frame1,LL,*lltypes)
drop_LLtype.grid(row=3,column=1)
    
#SpanInfoButton=Button(frame1,text="Save Span Changes",command=SpanInfo).grid(row=10,column=1)
#########

########### OUTPUT LOCATION
frame2=LabelFrame(root, text='Output Location',font='Helvetica 22 bold',padx=125, pady=30, bg="#FFFFFF", bd=0,
    highlightthickness=0)
frame2.grid(row=1,column=0,padx=10,pady=10)

outputlocation_label=Label(frame2,text="Output Location", bg="#FFFFFF").grid(row=3,column=0)
outputlocation=Entry(frame2, width=25, borderwidth=0)
outputlocation.grid(row=3,column=1)
outputlocation.insert(0, "/Users/myriamsarment/Dropbox (Team Connor)/Allegheny/IDEAS Fatigue Train/PROGRAM - from Myriam/Code Folders/April6thCode/Output/")

#OutputButton=Button(frame2,text="Save Output Changes",command=OutLoc).grid(row=4,column=1)
###########

########### DEAD LOADS RELATED FRAME
frame3=LabelFrame(root, text='Dead Loads',font='Helvetica 22 bold',padx=10, pady=10, bg="#FFFFFF", bd=0,
    highlightthickness=0)
frame3.grid(row=2,column=0,padx=10,pady=10)

GirderType_label=Label(frame3,text="Girder Type", bg="#FFFFFF").grid(row=0,column=0)
DeckType_label=Label(frame3,text="Deck Type", bg="#FFFFFF").grid(row=2,column=0)
girder=StringVar()
deck=StringVar()

girdertype_label=Label(root)
decktype_label=Label(root)

#Girder type drop downs
girdertypes=["Deck Plate Girder","Through Plate Girder","Beam Span"]
decktypes=["Open Timber Deck", "Ballasted Timber Deck", 
          "Ballasted Concrete Deck", "Ballasted Steel Deck"]
girder.set(girdertypes[0])
deck.set(decktypes[0])

#Drop Down Box
drop_girder=OptionMenu(frame3,girder,*girdertypes)
drop_girder.grid(row=0,column=1)
drop_deck=OptionMenu(frame3,deck,*decktypes)
drop_deck.grid(row=2,column=1)
#aButton=Button(frame3,text="Show selection", command=dead_load).grid(row=6,column=1)
###########

########### For COOPER LOADING FRAME
frame4=LabelFrame(root, text='Cooper Loads',font='Helvetica 22 bold',padx=10, pady=10, bg="#FFFFFF", bd=0,
    highlightthickness=0)
frame4.grid(row=3,column=0,padx=10,pady=10)

CooperType_label=Label(frame4,text="Cooper Type", bg="#FFFFFF").grid(row=0,column=0)
CooperYear_label=Label(frame4,text="Cooper Year", bg="#FFFFFF").grid(row=2,column=0)
GirderConnection_label=Label(frame4,text="Girder Connection", bg="#FFFFFF").grid(row=4,column=0)

cooperT=IntVar()
cooperY=StringVar()
girderconnect=StringVar()

coopertype_label=Label(root)
cooperyear_label=Label(root)
girderconnection_label=Label(root)

#Drop down options
coopertypes=["40","50","55","60","65","72","80"]
cooperyears=["Unknown", "1906","1920", "1935","1948","1968"]
    # Unknown, 1906 (E40 min; E50,55 common), 1920 (E60 min),
    #1935 (E72 min; E65 common), 1948 (E72 min; E65 common), 
    #1968 (E80 min)
girderconnections=["Welded", "Riveted"]

cooperT.set(coopertypes[0])
cooperY.set(cooperyears[5])
girderconnect.set(girderconnections[0])

#Drop Down Box
drop_coopertype=OptionMenu(frame4,cooperT,*coopertypes)
drop_coopertype.grid(row=0,column=1)
drop_cooperyear=OptionMenu(frame4,cooperY,*cooperyears)
drop_cooperyear.grid(row=2,column=1)
drop_girderconnection=OptionMenu(frame4,girderconnect,*girderconnections)
drop_girderconnection.grid(row=4,column=1)
#bButton=Button(frame4,text="Show selection", command=cooper_load).grid(row=6,column=1)

##############

############## For Impact Related FRAME
frame5=LabelFrame(root, text='Impact Value',font='Helvetica 22 bold',padx=10, pady=10, bg="#FFFFFF", bd=0,
    highlightthickness=0)
frame5.grid(row=4,column=0,padx=10,pady=10)

DesignImpact_label=Label(frame5,text="Design Impact and Year", bg="#FFFFFF").grid(row=0,column=0)
DesignImpact=StringVar()

designimpact_label=Label(root)

#DesignImpactYear drop down options
DesignImpactYearTypes=["Unknown", "All 1906 Impact", 
                       "All 1920 Impact", "1935 Hammer Blow Impact", 
                       "1935 Rolling Impact", 
                       "1948 (1968) Hammer Blow Impact (with Rocking Effect)",
                       "1968 (1948) Rolling Impact (with Rocking Effect)"]

DesignImpact.set(DesignImpactYearTypes[0])

#Drop Down Box
drop_DesignImpactYearType=OptionMenu(frame5,DesignImpact,*DesignImpactYearTypes)
drop_DesignImpactYearType.grid(row=0,column=1)

#cButton=Button(frame5,text="Show selection", command=design_impact).grid(row=2,column=1)
##############

############## For Section Modulus Frame
frame6=LabelFrame(root, text='Section Modulus',font='Helvetica 22 bold',padx=10, pady=10, bg="#FFFFFF", bd=0,
    highlightthickness=0)
frame6.grid(row=5,column=0,padx=10,pady=10)

GrossOrNetcheckbox=Label(root)
GirderNumberLabel=Label(root)
SValueLabel=Label(root)
HammerBlowcheckbox=Label(root)
    
#check boxes

SectionArea_label=Label(frame6,text="Section Area", bg="#FFFFFF").grid(row=0,column=0)
GrossOrNetVariable=StringVar()
Gross_Or_Net=Checkbutton(frame6,text='Check = Gross, Unchecked = Net', bg="#FFFFFF", variable=GrossOrNetVariable,onvalue='Gross',offvalue='Net')
Gross_Or_Net.deselect()
Gross_Or_Net.grid(row=0,column=1)

GirderNumber_label=Label(frame6,text="Number of girders", bg="#FFFFFF").grid(row=2,column=0)
GirderNumber=Entry(frame6, width=5, borderwidth=0)
GirderNumber.grid(row=2,column=1)
GirderNumber.insert(0, "2")
Number_Of_Girders=int(GirderNumber.get())

SValue_label=Label(frame6,text="S Value", bg="#FFFFFF").grid(row=4,column=0)
#SVariable=StringVar()
SValue_entry=Entry(frame6, width=7, borderwidth=0)
SValue_entry.grid(row=4,column=1)
SValue_entry.insert(0,"Unknown")
SValue=SValue_entry.get()
#Svalue=Checkbutton(frame6,text='Check = s value, Unchecked = unknown', variable=SVariable,onvalue='S value',offvalue='Unknown') ## needs fixing here to a loop
#Svalue.deselect()

HammerBlowVariable=StringVar()
HammerBlow_label=Label(frame6,text="HammerBlow", bg="#FFFFFF").grid(row=6,column=0)
HammerBlow=Checkbutton(frame6,text='Check = Yes, Unchecked = No', variable=HammerBlowVariable,onvalue='Yes',offvalue='No', bg="#FFFFFF")
HammerBlow.deselect()
HammerBlow.grid(row=6,column=1)

#submitSectionModulusSelection=Button(frame6,text='Show Section Modulus Selection',command=SectionCheckbox)
#submitSectionModulusSelection.grid(row=30,column=1)
######################

########### FATIGUE RELATED 
frame7=LabelFrame(root, text='Fatigue',font='Helvetica 22 bold',padx=10, pady=10, bg="#FFFFFF", bd=0,
    highlightthickness=0)
frame7.grid(row=6,column=0,padx=10,pady=10)

MeanImpactLoad_label=Label(frame7,text="Mean Impact Load",bg="#FFFFFF").grid(row=0,column=0)
FatigueCategory_label=Label(frame7,text="Fatigue Category", bg="#FFFFFF").grid(row=2,column=0)
MeanImpact=StringVar()
#meanimpactloads=MeanImpact.get()
FatigueCat=StringVar()
#fatiguecategories=FatigueCat.get()

MeanImpactLabel=Label(root)
FatigueCategoryLabel=Label(root)
IgnoreBelowStressLabel=Label(root)

#Fatigure related drop downs
meanimpactloads=["Full Design Impact", "Fatigue Design Impact", 
                 "Fatigue Rating Impact", "No Impact"]
fatiguecategories=["A", "B", "B'", "C", "C'", "D", "E", "E'", "F"]

MeanImpact.set(meanimpactloads[0])
FatigueCat.set(fatiguecategories[0])

#Drop Down Box
drop_meanimpact=OptionMenu(frame7,MeanImpact,*meanimpactloads)
drop_meanimpact.grid(row=0,column=1)
drop_fatiguecat=OptionMenu(frame7,FatigueCat,*fatiguecategories)
drop_fatiguecat.grid(row=2,column=1)

#ignor stress label
IgnoreBelowStress_label=Label(frame7,text="Ignore Stress", bg="#FFFFFF").grid(row=4,column=0)
IgnoreBelowStress=Entry(frame7, width=5, borderwidth=0)
IgnoreBelowStress.grid(row=4,column=1)
IgnoreBelowStress.insert(0, 1)
IgnoreBelowStressValue=float(IgnoreBelowStress.get())

#dButton=Button(frame7,text="Show Fatigue selection", command=fatigue_load).grid(row=38,column=1)

#########
###TRAIN INPUTS/WINDOW Here
########
global counter
global TrainsName,TrainsNumber,TrainsSpeed,TotalNumOfCars

train=[]
counter=1 
ChosenTrainLabel=Label(root)

def openNewWindow():
    global counter, train, TrainsName,TrainsNumber,TrainsSpeed, TrainsPerDay, TrainSpeed
    # Create counter logic
    if counter<3:
        NewWindow=Toplevel()
        NewWindow.title("Train Build")
        NewWindow.geometry('500x600')
        
        # Create a Main Frame
        main_frame_NewWindow=Frame(NewWindow)
        main_frame_NewWindow.pack(fill=BOTH, expand=1)
        # Create A Canvas
        my_canvas_NewWindow=Canvas(main_frame_NewWindow)
        my_canvas_NewWindow.pack(side=LEFT,fill=BOTH,expand=1)
        # Add a Scrollbar to the Canvas
        my_scrollbar_NewWindow=ttk.Scrollbar(main_frame_NewWindow, orient=VERTICAL,command=my_canvas_NewWindow.yview)
        my_scrollbar_NewWindow.pack(side=RIGHT, fill=Y)
        # Configure The Canvas
        my_canvas_NewWindow.configure(yscrollcommand=my_scrollbar_NewWindow.set)
        my_canvas_NewWindow.bind('<Configure>', lambda e: my_canvas_NewWindow.configure(scrollregion=my_canvas_NewWindow.bbox("all")))
        # Create ANOTHER frame in the Canvas
        top=Frame(my_canvas_NewWindow)
        # Add that new frame in a window in the canvas
        my_canvas_NewWindow.create_window((0,0), window=top, anchor="nw")
    
        TrainNamingFrame=Frame(top,padx=10, pady=10)
        TrainNamingFrame.grid(row=0,column=0,padx=10,pady=10)
        
        NameOfTrain=Label(TrainNamingFrame,text="Train Name").grid(row=0,column=0)
        TrainName=Entry(TrainNamingFrame, width=15, borderwidth=0)
        TrainName.grid(row=0,column=1)
        TrainName.insert(0,"Enter Any Name Here")
        
        #NumberofTrains=Label(TrainNamingFrame,text="Trains per day").grid(row=1,column=0)
        #TrainsPerDay=Entry(TrainNamingFrame, width=3, borderwidth=1)
        #TrainsPerDay.grid(row=1,column=1)
        #TrainsPerDay.insert(0,50) 

        #SpeedofTrains=Label(TrainNamingFrame,text="Train Speed").grid(row=2,column=0)
        #TrainSpeed=Entry(TrainNamingFrame, width=3, borderwidth=1)
        #TrainSpeed.grid(row=2,column=1)
        #TrainSpeed.insert(0,60)   
        
        TotalNumCars=Label(TrainNamingFrame,text="Total Different Cars").grid(row=3,column=0)
        TotNumCars=Entry(TrainNamingFrame, width=3, borderwidth=0)
        TotNumCars.grid(row=3,column=1)
        TotNumCars.insert(0,20) 
        
        TrainFrame=LabelFrame(top, text='Train Cars',font='Helvetica 22 bold', bg="#FFFFFF", padx=10, pady=10, bd=0,
    highlightthickness=0)
        TrainFrame.grid(row=3,column=0,padx=10,pady=10)
        
        CarTitle=Label(TrainFrame,text="Type of Car", font='Helvetica 13 bold', bg="#FFFFFF").grid(row=0,column=0)
        CarNumbers=Label(TrainFrame,text="Number of Car", font='Helvetica 13 bold', bg="#FFFFFF").grid(row=0,column=1)
        WeightPercentage=Label(TrainFrame,text="Weight of Car %", font='Helvetica 13 bold', bg="#FFFFFF").grid(row=0,column=2)
         
        #Drop down options
        TrainChoices=["Locomotive", "Unit Coal","Boxcar", "Tank (Ethanol)","Intermodal","Grain","CementSand","55 Open Hopper","70 Open Hopper","Long Flat","Centerbeam Flatcar","DDG Hopper"]

        Car1=Label(TrainFrame,text="Locomotive", bg="#FFFFFF").grid(row=6,column=0)        
        InitialShowingCars=12
        #Drop Down Box
        TrainChoice_drop=[StringVar()]*InitialShowingCars
        TrainChoice_drop[0]="Locomotive"
        NumberofCar=[1]*InitialShowingCars
        sliderCar=[Scale(TrainFrame, bg="#FFFFFF")]*InitialShowingCars
        
        valuelist = [0,25,50,75,100]
        
        for i in range (1,InitialShowingCars):

            TrainChoice_drop[i]=StringVar()
            TrainChoice_drop[i].set(TrainChoices[1])
            Car_drop=OptionMenu(TrainFrame,TrainChoice_drop[i],*TrainChoices).grid(row=i+6,column=0)#.pack(pady=8.25)#.grid(row=i+6,column=0)  
        
        for i in range(0,InitialShowingCars):    
            NumberofCar[i]=Entry(TrainFrame, width=3, borderwidth=0)
            NumberofCar[i].grid(row=i+6,column=1)# pack(padx=1,pady=7) #grid(row=i+6,column=1)
            NumberofCar[i].insert(0,0)
            
        for i in range(0,InitialShowingCars): 
            # Making the slider option for weight percentage
            sliderCar[i] = Scale(TrainFrame, bg="#FFFFFF", from_=min(valuelist), to=max(valuelist), resolution=25, orient="horizontal")
            sliderCar[i].grid(row=i+6, column=2)#pack(padx=0,pady=0)#grid(row=i+6, column=2)
        
        AddedTrainChoice_drop=[]
        AddedNumberofCar=[]
        AddedsliderCar=[]
        NewPlacementLocation=InitialShowingCars+6
        
        def AddCar():
                   
            TotalDifferentCars=int(TotNumCars.get())
            
            AddedShowingCars=TotalDifferentCars-InitialShowingCars
            for i in range(0,AddedShowingCars):
                AddedTrainChoice_drop.append(StringVar())
                AddedTrainChoice_drop[i].set(TrainChoices[1])
                AddedRowPlacement=NewPlacementLocation+len(AddedTrainChoice_drop)+i
                AddedCar_drop=OptionMenu(TrainFrame,AddedTrainChoice_drop[i],*TrainChoices).grid(row=AddedRowPlacement,column=0)#pack(pady=8.25)#grid(row=InitialShowingCars+6+i,column=0)
                #AddedRowPlacement=0
                
            for i in range(0,AddedShowingCars):
                AddedNumberofCar.append(0)
                AddedRowPlacement=NewPlacementLocation+len(AddedNumberofCar)+i
                AddedNumberofCar[i]=Entry(TrainFrame, width=3, borderwidth=0)
                AddedNumberofCar[i].grid(row=AddedRowPlacement,column=1)#pack(padx=1,pady=7) #grid(row=i+6,column=1)
                AddedNumberofCar[i].insert(0,0)
                #AddedRowPlacement=0
            for i in range(0,AddedShowingCars): 
                AddedsliderCar.append(Scale(TrainFrame))
                AddedRowPlacement=NewPlacementLocation+len(AddedsliderCar)+i
                AddedsliderCar[i] = Scale(TrainFrame, from_=min(valuelist), to=max(valuelist), resolution=25, orient="horizontal")
                AddedsliderCar[i].grid(row=AddedRowPlacement, column=2)#pack(padx=0,pady=0)#grid(row=i+6, column=2)
                #AddedRowPlacement=0

            AddCarButton['state'] = 'disabled'

        def TrainInfo():
            
            Car=[TrainChoice_drop[0]]
            NumberCar=[]
            PercentageCar=[]
            CarAndLF=[]
            train=[]
            
            global TrainsName,TotalNumOfCars # TrainsNumber,TrainsSpeed,TotalNumOfCars, TrainsPerDay, TrainSpeed
            
            for a in range(0,len(NumberofCar)):        
                NumberCar.append(int(NumberofCar[a].get()))
            
            for Added_a in range(0,len(AddedNumberofCar)):        
                NumberCar.append(int(AddedNumberofCar[Added_a].get()))
                
            for b in range(1,len(TrainChoice_drop)):              
                Car.append(TrainChoice_drop[b].get())
            for Added_b in range(0,len(AddedTrainChoice_drop)):              
                Car.append(AddedTrainChoice_drop[Added_b].get())
            #print(Car)

            for c in range(0,len(sliderCar)):
                PercentageCar.append(int(sliderCar[c].get()))
            for Added_c in range(0,len(AddedsliderCar)):
                PercentageCar.append(int(AddedsliderCar[Added_c].get()))
                
            TrainsName=TrainName.get()
            
            #Added values are now included in NumberCar, Car and PercentageCar
            TotalNumOfCar=0
            for d in range(0,len(NumberCar)):
                TotalNumOfCar=TotalNumOfCar+NumberCar[d]
            for e in range(0,len(NumberCar)):
                CarAndLF.append("{}_{}".format(Car[e],PercentageCar[e])) # LF means Load Factor
            for f in range(0,len(NumberCar)):
                train.extend([CarAndLF[f]]*NumberCar[f])

            print(train)
            
            textfile = open("{}_save.txt".format(TrainsName), "w")
            for element in train:
                textfile.write(element + ",")
            textfile.close()
            
                  
        AddCarButton=Button(NewWindow,text="Add Car",command=AddCar)
        AddCarButton.pack()
        TrainInfoButton=Button(NewWindow,text="Save Train Set-Up",command=TrainInfo).pack()

        Button(NewWindow,text='Close',command=NewWindow.destroy).pack()#.grid(row=40,column=0)
        counter+=1
    else:
        messagebox.showinfo("Error","Window Already Open")

#NEW FRAME for chosing the train

ChoseTrainFrame=LabelFrame(root, text='Chose Train',font='Helvetica 22 bold',padx=10, pady=10, bg="#FFFFFF", bd=0,
    highlightthickness=0) #font=('TkDefaultFont', 15)
ChoseTrainFrame.grid(row=14,column=0,padx=10,pady=10)

NumberofTrains=Label(ChoseTrainFrame,text="Trains per day", bg = "#FFFFFF").grid(row=0,column=0)
TrainsPerDay=Entry(ChoseTrainFrame, width=3, borderwidth=0)
TrainsPerDay.grid(row=0,column=1)
TrainsPerDay.insert(0,50) 

SpeedofTrains=Label(ChoseTrainFrame,text="Train Speed", bg= "#FFFFFF").grid(row=1,column=0)
TrainSpeed=Entry(ChoseTrainFrame, width=3, borderwidth=0)
TrainSpeed.grid(row=1,column=1)
TrainSpeed.insert(0,60)   
        
TrainBuilding_button=Button(ChoseTrainFrame,text="Build Train", bg = "#FFFFFF",command=openNewWindow)
TrainBuilding_button.grid(row=2,column=0)

NameOfTrainChosen=Label(ChoseTrainFrame,text="Chosen Train Name", bg = "#FFFFFF").grid(row=3,column=0)
        
def open_file():
    global train_text_file, ChosenTrainLabel
    ChosenTrainLabel.destroy()
            
    file = filedialog.askopenfile(mode='r', filetypes=[('Python Files', '*.txt')])
    if file:
        
        filepath = os.path.abspath(file.name)
        split=filepath.split()
        getfile=" ".join(split)
        #print(split)
        window=getfile.split("\\")
        mac=[i.split('/') for i in window]
        splitting_of_path=mac

        splitting_of_path2=splitting_of_path[len(splitting_of_path)-1]
        train_text_file=splitting_of_path2[len(splitting_of_path2)-1]
        #print(train_text_file)
        
    ChosenTrainLabel=Label(ChoseTrainFrame, text= train_text_file, font=('Aerial 11'))
    ChosenTrainLabel.grid(row=3,column=1)
        # Create a Browse Button
BrowseButton=Button(ChoseTrainFrame, text="Browse", command=open_file).grid(row=4,column=0)

#ChoseTrainButtion=Button(ChoseTrainFrame,text="Chose Train", command=TrainToUse).grid(row=5, column=1)

# Need a button that will save all changes before submitting
frame8=LabelFrame(root, text='Finish',font='Helvetica 22 bold',padx=10, pady=10, bg="#FFFFFF", bd=0,
    highlightthickness=0)
frame8.grid(row=15,column=0,padx=10,pady=10)
#

#from BridgeAnalysis20210329_edit import Main

def RunProgram():
    global Start_Span,End_Span,Span_Increment,Output_Location,LL_Type
    global Girder_Types,Deck_Type,Cooper_Type,Cooper_Year
    global Girder_Connections,DesignImpact_YearType,Gross_Or_Net
    global Number_Of_Girders,S_Value,Hammer_Blow,MeanImpact_Load
    global Fatigue_Category,IgnoreBelow_Stress,TrainsPerDay#, TrainsNumber
    global TrainsSpeed,TrainsName,train,start,finish,interval,step

    #from BridgeAnalysis20210329_edit import Main
    #from BridgeAnalysis20210329 import Main    
    #Main(StartSpan,EndSpan,SpanIncrement,OutputLocation,LLType,GirderTypes,DeckType,CooperType,CooperYear,GirderConnections,DesignImpactYearType,GrossOrNet,NumberOfGirders,S,HammerBlow,MeanImpactLoad,FatigueCategory,IgnoreBelowStress,TrainsPerDay,Speed,TrainName,Train,start,finish,interval,step)

    Main(Start_Span,End_Span,Span_Increment,Output_Location,LL_Type,Girder_Type,Deck_Type,Cooper_Type,Cooper_Year,Girder_Connection,DesignImpact_YearType,Gross_Or_Net,Number_Of_Girders,S_Value,Hammer_Blow,MeanImpact_Load,Fatigue_Category,IgnoreBelow_Stress,TrainsNumber,TrainsSpeed,TrainsName,train,start,finish,interval,step)
    
#ProgramRunButton=Button(frame8,text="Run Program", command=RunProgram)
#ProgramRunButton.grid(row=0,column=1)

# saving button

def SaveALL():

#def SpanInfo():
    global Span_Increment, End_Span, Start_Span
    Span_Increment=int(SpanIncrement.get())
    End_Span=int(EndSpan.get())
    Start_Span=int(StartSpan.get())
    
    global start, finish, interval, step 
    start=float(StartMoment.get())
    finish=float(FinishMoment.get())
    interval=float(IntervalMoment.get())
    step=float(StepMoment.get())
    
    global LL_Type,lltype_label
    lltype_label.destroy()
    lltype_label=Label(frame1, text=LL.get())
    lltype_label.grid(row=4,column=1)
    LL_Type=LL.get()

#def OutLoc():
    global Output_Location,outputlocation
    Output_Location=outputlocation.get()

#def dead_load():
    global Girder_Type,girdertype_label
    girdertype_label.destroy()
    girdertype_label=Label(frame3, text=girder.get())
    girdertype_label.grid(row=1,column=1)
    Girder_Type=girder.get()
    
    global Deck_Type,decktype_label
    decktype_label.destroy()
    decktype_label=Label(frame3, text=deck.get())
    decktype_label.grid(row=3,column=1)
    Deck_Type=deck.get()

#def cooper_load():
    global Cooper_Type,coopertype_label
    coopertype_label.destroy()
    coopertype_label=Label(frame4, text=cooperT.get())
    coopertype_label.grid(row=1,column=1)
    Cooper_Type=cooperT.get()
    
    global Cooper_Year, cooperyear_label
    cooperyear_label.destroy()
    cooperyear_label=Label(frame4, text=cooperY.get())
    cooperyear_label.grid(row=3,column=1)
    Cooper_Year=cooperY.get()
    
    global Girder_Connection,girderconnection_label
    girderconnection_label.destroy()
    girderconnection_label=Label(frame4, text=girderconnect.get())
    girderconnection_label.grid(row=5,column=1)
    Girder_Connection=girderconnect.get()

#def design_impact():
    global DesignImpact_YearType,designimpact_label
    designimpact_label.destroy()
    designimpact_label=Label(frame5, text=DesignImpact.get())
    designimpact_label.grid(row=1,column=1)
    DesignImpact_YearType=DesignImpact.get()

#def SectionCheckbox():
    global GrossOrNetcheckbox,GrossOrNet,GirderNumberLabel,NumberOfGirders,SValueLabel, SValue_entry,S_Value,HammerBlowcheckbox,Hammer_Blow
    GrossOrNetcheckbox.destroy()
    GrossOrNetcheckbox=Label(frame6,text=GrossOrNetVariable.get())
    GrossOrNetcheckbox.grid(row=1,column=1)
    GrossOrNet=GrossOrNetVariable.get()
    
    GirderNumberLabel.destroy()
    GirderNumberLabel=Label(frame6,text=GirderNumber.get())
    GirderNumberLabel.grid(row=3,column=1)
    NumberOfGirders=int(GirderNumber.get())
    
    SValueLabel.destroy()
    SVar=SValue_entry.get()
    if SVar=='Unknown':   
        S_Value=SValue_entry.get()

    else:
        S_Value=int(SValue_entry.get())
        
    SValueLabel=Label(frame6,text=SValue_entry.get())
    SValueLabel.grid(row=5,column=1)
    
    HammerBlowcheckbox.destroy()
    HammerBlowcheckbox=Label(frame6,text=HammerBlowVariable.get())
    HammerBlowcheckbox.grid(row=7,column=1)
    Hammer_Blow=HammerBlowVariable.get()

#def fatigue_load():
    global MeanImpactLabel, MeanImpact_Load
    MeanImpactLabel.destroy()
    MeanImpactLabel=Label(frame7, text=MeanImpact.get())
    MeanImpactLabel.grid(row=1,column=1)
    MeanImpact_Load=MeanImpact.get()
    
    global FatigueCategoryLabel, Fatigue_Category
    FatigueCategoryLabel.destroy
    FatigueCategoryLabel=Label(frame7, text=FatigueCat.get())
    FatigueCategoryLabel.grid(row=3,column=1)
    Fatigue_Category=FatigueCat.get()
    
    global IgnoreBelowStressLabel,IgnoreBelow_Stress
    IgnoreBelowStressLabel.destroy()
    IgnoreBelowStressLabel=Label(frame7,text=IgnoreBelowStress.get())
    IgnoreBelowStressLabel.grid(row=5,column=1)
    IgnoreBelow_Stress=float(IgnoreBelowStress.get())
       
#def TrainToUse():
    global train_text_file, train, TrainsPerDay, TrainSpeed, TrainsSpeed,TrainsNumber,TrainsName
    Extract=open(train_text_file,"r")
    train_as_string=Extract.read()
    splitting_train_string=train_as_string.split(",")
    train=splitting_train_string[:-1]        
    
    split_trainName=train_text_file.split('_')
    TrainsName=split_trainName[0]
    TrainsNumber=int(TrainsPerDay.get())
    TrainsSpeed=int(TrainSpeed.get())
            

SaveButton=Button(frame8,text="Save All", command=SaveALL)
SaveButton.grid(row=0,column=1)

main.mainloop() #running the root

#calling the main function, if the name of the BridgeAnalysis program changes, need to change the name here
#from BridgeAnalysisFunctions.BridgeAnalysis20210329_edit4 import Main
from BridgeAnalysis20210329_edit2 import Main
#Main(StartSpan,EndSpan,SpanIncrement,OutputLocation,LLType,GirderTypes,DeckType,CooperType,CooperYear,GirderConnections,DesignImpactYearType,GrossOrNet,NumberOfGirders,S,HammerBlow,MeanImpactLoad,FatigueCategory,IgnoreBelowStress,TrainsPerDay,Speed,TrainName,Train,start,finish,interval,step)

Main(Start_Span,End_Span,Span_Increment,Output_Location,LL_Type,Girder_Type,Deck_Type,Cooper_Type,Cooper_Year,
     Girder_Connection,DesignImpact_YearType,GrossOrNet,NumberOfGirders,S_Value,Hammer_Blow,MeanImpact_Load,Fatigue_Category,IgnoreBelow_Stress,TrainsNumber,TrainsSpeed,TrainsName,train,start,finish,interval,step)

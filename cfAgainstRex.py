#field from data files
"""
X [ m ]	 Y [ m ]	 Z [ m ]	 Approximated Mass Flow [ kg s^-1 ]	 Area [ m^2 ]	 Connectivity Number	 Density [ kg m^-3 ]	 Eddy Viscosity [ Pa s ]	 Edge Length Ratio	 Element Volume Ratio	 Force [ N ]	 Force X [ N ]	 Force Y [ N ]	 Force Z [ N ]	 Heat Flux [ W m^-2 ]	 Interpolated Mass Flow [ kg s^-1 ]	 Length [ m ]	 Mass Flow [ kg s^-1 ]	 Maximum Face Angle [ degree ]	 Minimum Face Angle [ degree ]	 Normal	 Normal X	 Normal Y	 Normal Z	 Pressure [ Pa ]	 Turbulence Eddy Frequency [ s^-1 ]	 Turbulence Kinetic Energy [ m^2 s^-2 ]	 Velocity [ m s^-1 ]	 Velocity u [ m s^-1 ]	 Velocity u.Gradient [ s^-1 ]	 Velocity u.Gradient X [ s^-1 ]	 Velocity u.Gradient Y [ s^-1 ]	 Velocity u.Gradient Z [ s^-1 ]	 Velocity v [ m s^-1 ]	 Velocity v.Gradient [ s^-1 ]	 Velocity v.Gradient X [ s^-1 ]	 Velocity v.Gradient Y [ s^-1 ]	 Velocity v.Gradient Z [ s^-1 ]	 Velocity w [ m s^-1 ]	 Velocity w.Gradient [ s^-1 ]	 Velocity w.Gradient X [ s^-1 ]	 Velocity w.Gradient Y [ s^-1 ]	 Velocity w.Gradient Z [ s^-1 ]	 Velocity.Absolute Helicity [ m s^-2 ]	 Velocity.Curl [ s^-1 ]	 Velocity.Curl X [ s^-1 ]	 Velocity.Curl Y [ s^-1 ]	 Velocity.Curl Z [ s^-1 ]	 Velocity.Divergence [ s^-1 ]	 Velocity.Helicity [ m s^-2 ]	 Velocity.Invariant Q [ s^-2 ]	 Velocity.Lambda 2 [ s^-2 ]	 Velocity.Normal Eigen Helicity [ s^-1 ]	 Velocity.Real Eigen Helicity [ s^-1 ]	 Velocity.Real Eigenvalue [ s^-1 ]	 Velocity.Stretched Swirling Strength	 Velocity.Swirling Discriminant [ s^-6 ]	 Velocity.Swirling Normal [ s^-1 ]	 Velocity.Swirling Normal X [ s^-1 ]	 Velocity.Swirling Normal Y [ s^-1 ]	 Velocity.Swirling Normal Z [ s^-1 ]	 Velocity.Swirling Strength [ s^-1 ]	 Velocity.Swirling Vector [ s^-1 ]	 Velocity.Swirling Vector X [ s^-1 ]	 Velocity.Swirling Vector Y [ s^-1 ]	 Velocity.Swirling Vector Z [ s^-1 ]	 Volume [ m^3 ]	 Wall Heat Flux [ W m^-2 ]	 Wall Radiative Heat Flux [ W m^-2 ]	 Wall Shear [ Pa ]	 Wall Shear X [ Pa ]	 Wall Shear Y [ Pa ]	 Wall Shear Z [ Pa ]	 X [ m ]	 Y [ m ]	 Yplus	 Ystar	 Z [ m ]

"""
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
import pandas as pd
import matplotlib.ticker
from matplotlib.ticker import FormatStrFormatter
f = lambda x,pos: str(x).rstrip('0').rstrip('.')
plt.rc('font', family='serif')
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')
plt.rc('legend', fontsize=10)    # legend fontsize
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(1, 1, 1)
plt.margins(x=0.0001,y=0.003)
def listToCsv(fname,details,list_):
    import csv
    with open(fname,'w') as f:
        write= csv.writer(f)
        #write.writerows(details)
        write.writerow(list_)
#geometry to extract
yCoordB4Step=0.622455
yCoordAfterStep4mm=0.626455
yCoordAfterStep2mm=yCoordB4Step+2E-3
decimalPlaces=6
#get data at step
#############################################################
####################plot wall results########################
#4mm
rawData=pd.read_csv("data/exportF1Wall.csv",low_memory=False,sep=',',skiprows=5,encoding="ascii",skipinitialspace=True)#error_bad_lines=False
# Y [ m ]
rawData.columns=rawData.columns.str.replace(" ","")
#rawData.columns=rawData.columns.str.replace("[*]","",regex=True)
rawData=rawData.loc[:,~rawData.columns.duplicated()]

#print(rawData.columns.tolist())
rawData["Y[m]"]=rawData["Y[m]"].apply(lambda x: round(x,decimalPlaces))
rawData["Z[m]"]=rawData["Z[m]"].apply(lambda x: round(x,decimalPlaces))
#filter rawData
processedData4mm=pd.concat([rawData[(rawData[["Y[m]"]]==yCoordB4Step).all(1)],rawData[(rawData[["Y[m]"]]==yCoordAfterStep4mm).all(1)]], ignore_index=True)
#remove negative z coord data
#print(rawData[(rawData[["Y[m]"]]==yCoordAfterStep4mm).all(1)])
processedData4mm=processedData4mm[(processedData4mm[["Z[m]"]]>=0).all(1)]

######
#2mm
#######

rawData=pd.read_csv("data/export2mmWall.csv",low_memory=False,sep=',',skiprows=5,encoding="ascii",skipinitialspace=True)
rawData.columns=rawData.columns.str.replace(" ","")
rawData=rawData.loc[:,~rawData.columns.duplicated()]

rawData["Y[m]"]=rawData["Y[m]"].apply(lambda x: round(x,decimalPlaces))
rawData["Z[m]"]=rawData["Z[m]"].apply(lambda x: round(x,decimalPlaces))
#filter rawData
processedData2mm=pd.concat([rawData[(rawData[["Y[m]"]]==yCoordB4Step).all(1)],rawData[(rawData[["Y[m]"]]==yCoordAfterStep2mm).all(1)]], ignore_index=True)
#remove negative z coord data
processedData2mm=processedData2mm[(processedData2mm[["Z[m]"]]>=0).all(1)]
#print(rawData[(rawData[["Y[m]"]]==yCoordB4Step).all(1)])

######
#0mm
######
#you need to download this data from the wall
rawData=pd.read_csv("data/exportFlatPlateSurface_body.csv",low_memory=False,sep=",",skiprows=5,encoding="ascii",skipinitialspace=True)
rawData.columns=rawData.columns.str.replace(" ","")
rawData=rawData.loc[:,~rawData.columns.duplicated()]
rawData["Y[m]"]=rawData["Y[m]"].apply(lambda x: round(x,decimalPlaces))
rawData["Z[m]"]=rawData["Z[m]"].apply(lambda x: round(x,decimalPlaces))
#filter rawData
processedData0mm=pd.concat([rawData[(rawData[["Y[m]"]]==yCoordB4Step).all(1)]], ignore_index=True)
#remove negative z coord data
processedData0mm=processedData0mm[(processedData0mm[["Z[m]"]]>=0).all(1)]
####################
########cf##########
####################
processedData4mm=processedData4mm[(processedData4mm[["X[m]"]]>0.2481).all(1)]
processedData2mm=processedData2mm[(processedData2mm[["X[m]"]]>0.2481).all(1)]
processedData0mm=processedData0mm[(processedData0mm[["X[m]"]]>0.2481).all(1)]
cf2mm=np.divide(2*processedData2mm["WallShear[Pa]"],1.225*50.0**2)
cf4mm=np.divide(2*processedData4mm["WallShear[Pa]"],1.225*50.0**2)
cf0mm=processedData0mm["X[m]"],np.divide(2*processedData0mm["WallShear[Pa]"],1.225*50.0**2)

ax.plot(processedData2mm["X[m]"],np.divide(2*processedData2mm["WallShear[Pa]"],1.225*50.0**2),label="2mm",color="black")
ax.plot(processedData4mm["X[m]"],np.divide(2*processedData4mm["WallShear[Pa]"],1.225*50.0**2),label="4mm",color="red")
#perfectly flat plate with no surface imperfections
ax.plot(processedData0mm["X[m]"],np.divide(2*processedData0mm["WallShear[Pa]"],1.225*50.0**2),label="0mm",color="yellow")
ax.set_xlabel('x position along wall (m)',size=15)
ax.set_ylabel('Friction coefficient Cf',size=15)
#ax.set_title('Frequency vs. Natural Frequency $n^{o}$')#,fontweight='bold')
ax_=plt.gca()
#plt.ginput(4)
#set xaxis preferences
#ax_.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
#ax_.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(f))
#set yaxis preferences
plt.margins(x=0.0001,y=0.01)
#remember to save as high quality
#see dissertation python plot code
plt.legend(loc='best')
plt.savefig("cfheights",dpi=300)
####################
########Rex##########
####################
########4mm#########
plt.rc('font', family='serif')
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')
plt.rc('legend', fontsize=10)    # legend fontsize
fig = plt.figure(figsize=(6, 5))
ax = fig.add_subplot(1, 1, 1)
plt.margins(x=0.01,y=0.01)


rawData=pd.read_csv("data/exportF1Surface_body8dp.csv",low_memory=False,sep=",",skiprows=5,encoding="ascii",skipinitialspace=True)
rawData.columns=rawData.columns.str.replace(" ","")
rawData=rawData.loc[:,~rawData.columns.duplicated()]
rawData["Y[m]"]=rawData["Y[m]"].apply(lambda x: round(x,decimalPlaces))
rawData["Z[m]"]=rawData["Z[m]"].apply(lambda x: round(x,decimalPlaces))
rawData["X[m]"]=rawData["X[m]"].apply(lambda x: round(x,decimalPlaces))
fieldData4mm=rawData[(rawData[["Z[m]"]]>=0).all(1)]
# Re≡𝜌ud1/2veff
# area = 6.11406E-8
#area = sum(volumes)/nCells
areaAvg =np.divide((np.divide(np.sum(fieldData4mm["Volume[m^3]"]),(0.00035/2))),len(fieldData4mm.index))
Rex4mm=np.divide(np.multiply(1.225*fieldData4mm["Velocity[ms^-1]"],np.sqrt(areaAvg)),(1.46e-5))
#print(fieldData4mm["EddyViscosity[Pas]"]+1.46e-5)
fieldData4mm["Rex"]= Rex4mm
########2mm#######

rawData=pd.read_csv("data/export2mmSurface_body.csv",low_memory=False,sep=",",skiprows=5,encoding="ascii",skipinitialspace=True)
rawData.columns=rawData.columns.str.replace(" ","")
rawData=rawData.loc[:,~rawData.columns.duplicated()]
rawData["Y[m]"]=rawData["Y[m]"].apply(lambda x: round(x,decimalPlaces))
rawData["Z[m]"]=rawData["Z[m]"].apply(lambda x: round(x,decimalPlaces))
rawData["X[m]"]=rawData["X[m]"].apply(lambda x: round(x,decimalPlaces))
fieldData2mm=rawData[(rawData[["Z[m]"]]>=0).all(1)]
areaAvg=np.divide((np.divide(np.sum(fieldData2mm["Volume[m^3]"]),(0.00035/2))),len(fieldData2mm.index))
Rex2mm=np.divide(np.multiply(1.225*fieldData2mm["Velocity[ms^-1]"],np.sqrt(areaAvg)),(1.46e-5+fieldData2mm["EddyViscosity[Pas]"]))
fieldData2mm["Rex"]= Rex2mm
########0mm#######

rawData=pd.read_csv("data/exportFlatPlateSurface_body.csv",low_memory=False,sep=",",skiprows=5,encoding="ascii",skipinitialspace=True)
rawData.columns=rawData.columns.str.replace(" ","")
rawData=rawData.loc[:,~rawData.columns.duplicated()]
rawData["Y[m]"]=rawData["Y[m]"].apply(lambda x: round(x,decimalPlaces))
rawData["Z[m]"]=rawData["Z[m]"].apply(lambda x: round(x,decimalPlaces))
rawData["X[m]"]=rawData["X[m]"].apply(lambda x: round(x,decimalPlaces))
fieldData0mm=rawData[(rawData[["Z[m]"]]>=0).all(1)]
# Re≡𝜌ud1/2veff
# area = 6.11406E-8
#area = sum(volumes)/nCells
areaAvg=np.divide((np.divide(np.sum(fieldData0mm["Volume[m^3]"]),(0.00035/2))),len(fieldData0mm.index))
#fieldData0mm["EddyViscosity[Pas]"]
Rex0mm=np.divide(np.multiply(1.225*fieldData0mm["Velocity[ms^-1]"],np.sqrt(areaAvg)),(1.46e-5+fieldData0mm["EddyViscosity[Pas]"]))
fieldData0mm["Rex"]= Rex0mm
###########################
###get profiles from Rex###

y0mm=np.round(np.max(fieldData0mm["Y[m]"])-np.min(fieldData0mm["Y[m]"])+np.min(fieldData0mm["Y[m]"]),6)
y2mm=np.round(np.max(fieldData2mm["Y[m]"])-np.min(fieldData2mm["Y[m]"])+np.min(fieldData2mm["Y[m]"]),6)
y4mm=np.round(np.max(fieldData4mm["Y[m]"])-np.min(fieldData4mm["Y[m]"])+np.min(fieldData4mm["Y[m]"]),6)
print(y2mm)
#take positions at the Y axis center line
#Rex0mmPointsOfInterest=pd.concat([fieldData0mm[(fieldData0mm[["Y[m]"]]==y0mm).all(1)]], ignore_index=True)
#Rex2mmPointsOfInterest=pd.concat([fieldData2mm[(fieldData2mm[["Y[m]"]]==y2mm).all(1)]], ignore_index=True)
#Rex4mmPointsOfInterest=pd.concat([fieldData4mm[(fieldData4mm[["Y[m]"]]==y4mm).all(1)]], ignore_index=True)
#closest positions at the Y axis center line for y2mm it is 
#take x position from processed data then match it with the closest mid y pos
#around about 0.674455
processedData2mm["cf"]=np.divide(2*processedData2mm["WallShear[Pa]"],1.225*50.0**2)
closestPoint2mm=[]
closestPoint2mmDict={"X[m]":[],"Rex":[]}
cfArray2mm=[]
x0Array2mm=[]
for index,row in processedData2mm.iterrows():
    #iterate through each row of data at wall then find the nearest X and ycoords
    if row["X[m]"]<0.2463:
        continue
    dfClosestX=fieldData2mm.iloc[(fieldData2mm["X[m]"]-row["X[m]"]).abs().argsort()[:10]]
    dfClosestY=dfClosestX.iloc[(dfClosestX["Y[m]"]-y2mm).abs().argsort()]
    data= dfClosestY["Rex"].index[0].item()
    data2= row["cf"].item()
    data3=row["X[m]"].item()
    closestPoint2mm.append(data)
    cfArray2mm.append(data2)
    x0Array2mm.append(data3)
    #closestPoint2mmDict["X[m]"].append(dfClosestY.index[1].item())
    #closestPoint2mm.append(dfClosestY["Rex"].index[0].item()) 
pd.DataFrame({"Rex":closestPoint2mm,"cf":cfArray2mm,"x0":x0Array2mm}).to_csv("rexData2mm.csv")
#4mm
processedData4mm["cf"]=np.divide(2*processedData4mm["WallShear[Pa]"],1.225*50.0**2)
closestPoint4mm=[]
cfArray4mm=[]
x0Array4mm=[]
for index,row in processedData4mm.iterrows():
    #iterate through each row of data at wall then find the nearest X and ycoords
    if row["X[m]"]<0.2463:
        continue
    dfClosestX=fieldData4mm.iloc[(fieldData4mm["X[m]"]-row["X[m]"]).abs().argsort()[:10]]
    dfClosestY=dfClosestX.iloc[(dfClosestX["Y[m]"]-y4mm).abs().argsort()]
    data= dfClosestY["Rex"].index[0].item()
    data2= row["cf"].item()
    data3=row["X[m]"].item()
    closestPoint4mm.append(data)
    cfArray4mm.append(data2)
    x0Array4mm.append(data3)
    #closestPoint2mmDict["X[m]"].append(dfClosestY.index[1].item())
    #closestPoint2mm.append(dfClosestY["Rex"].index[0].item()) 
pd.DataFrame({"Rex":closestPoint4mm,"cf":cfArray4mm,"x0":x0Array4mm}).to_csv("rexData4mm.csv")
#0mm
processedData0mm["cf"]=np.divide(2*processedData0mm["WallShear[Pa]"],1.225*50.0**2)
closestPoint0mm=[]
cfArray0mm=[]
x0Array0mm=[]
for index,row in processedData0mm.iterrows():
    #iterate through each row of data at wall then find the nearest X and ycoords
    if row["X[m]"]<0.2463:
        continue
    dfClosestX=fieldData0mm.iloc[(fieldData0mm["X[m]"]-row["X[m]"]).abs().argsort()[:10]]
    dfClosestY=dfClosestX.iloc[(dfClosestX["Y[m]"]-y0mm).abs().argsort()]
    data= dfClosestY["Rex"].index[0].item()
    data2= row["cf"].item()
    data3=row["X[m]"].item()
    closestPoint0mm.append(data)
    cfArray0mm.append(data2)
    x0Array0mm.append(data3)
    #closestPoint2mmDict["X[m]"].append(dfClosestY.index[1].item())
    #closestPoint2mm.append(dfClosestY["Rex"].index[0].item()) 
pd.DataFrame({"Rex":closestPoint0mm,"cf":cfArray0mm,"x0":x0Array0mm}).to_csv("rexData0mm.csv")

"""
print(type(closestPoint2mm))
print("closest..")
print(len(closestPoint2mm))
print("plotting")
ax.plot(closestPoint2mm,processedData2mm["cf"])
plt.show()
"""
#join matrices together

"""
processedData2mm["cf"]=np.divide(2*processedData2mm["WallShear[Pa]"],1.225*50.0**2)
finalDf2mm=pd.merge(Rex2mmPointsOfInterest,processedData2mm,on="X[m]")
#Rex2mmPointsOfInterest.to_csv("yRexProfile2mm.csv")
#processedData2mm.to_csv("datacf2mm.csv")
#finalDf2mm.to_csv("finalDf2mm.csv")
ax.plot(finalDf2mm["Rex"],finalDf2mm["cf"],color="red")
#ax.plot(processedData0mm["X[m]"],np.divide(2*processedData0mm["WallShear[Pa]"],1.225*50.0**2),color="yellow")
plt.show()
"""
#
#yNearestDataPoint0mm=fieldData0mm.iloc[(fieldData0mm["Y[m]"]-y0mm).abs().argsort()[:1]]
#exists = y in fieldData0mm["Y[m]"]
#print(exists)
# Cf,x≅0.059Rex15
# 𝛿x≅0.38Rex15
# FD=12Cf𝜌U∞2Aplate  
"""
x=stepData["wallShearStress:0"]
y=stepData["wallShearStress:1"]
z=stepData["wallShearStress:2"]
magTau=np.sqrt(np.square(x)+np.square(y))
magU= np.sqrt(np.square(stepData["U:0"])+np.square(stepData["U:1"]))
cf=2*magTau/1.225*magU**2
xCoords = stepData["Points:0"]
yCoords = stepData["Points:1"]
#print("max",np.max(yCoords))
zCoords = stepData["Points:2"]
#print(yCoords)
ax.plot(xCoords,cf,color="black")
#filter out other walls 
unorderedOrFilteredFrame=pd.concat([cf,xCoords,yCoords,zCoords],axis=1,join="inner")#.drop_duplicates(subset=["Points:0"])
minOfY=np.min(unorderedOrFilteredFrame["Points:1"])
unorderedOrFilteredFrame=unorderedOrFilteredFrame[(unorderedOrFilteredFrame[["Points:1"]]!=0.62246).all(1)]
dataFrame=unorderedOrFilteredFrame[(unorderedOrFilteredFrame[["Points:2"]]>0).all(1)]
dataFrame=dataFrame.drop_duplicates(subset=["Points:0"])
#print(unorderedFrame)
#.drop_duplicates(subset=["Points:1","Points:2"])
#dataFrame=dataFrame.sort_values("Points:0",ascending=True)
#dataFrame=dataFrame[(dataFrame[["Points:0"]]>0.338).all(1)]
print(dataFrame)
ax.plot(dataFrame["Points:0"],dataFrame[0],color="black")
#add labels
#0.4704
ax.set_xlabel('x position along wall (m)',size=15)
ax.set_ylabel('wall shear stress magnitude (Pa)',size=15)
#ax.set_title('Frequency vs. Natural Frequency $n^{o}$')#,fontweight='bold')
ax_=plt.gca()
#plt.ginput(4)
#set xaxis preferences
#ax_.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
#ax_.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(f))
#set yaxis preferences

#remember to save as high quality
#see dissertation python plot code
plt.legend(loc='best')
plt.show()
#plt.savefig("shearWallStress",dpi=300)
"""
"""
#normalize by upstreamVelocity
#x= stepData["U_0"]/0.0224
arcLengthOffset=stepData["arc_length"].iloc[0]
lastItemArcLength=stepData["arc_length"].iloc[-1]
arcLengthoffsetMat=(stepData["arc_length"]/stepData["arc_length"])*arcLengthOffset
top=stepData["arc_length"]-arcLengthoffsetMat #top
y= top/lastItemArcLength-arcLengthOffset
ax.plot(x,y,label="a.",color="red")
#U_0 is the upstream freestream reference velocity
#get data at fullydeveloped region 
###################################################################################################
stepData=pd.read_csv("../dataSlice/sliceDatakomegaFullyDeveloped.csv")
#U_0,arc_length (0.12485m)
stepData=stepData[stepData["U_0"].notnull()]
#print(stepData.keys())
#normalize by upstreamVelocity
x= stepData["U_0"]/0.0224
arcLengthOffset=stepData["arc_length"].iloc[0]
lastItemArcLength=stepData["arc_length"].iloc[-1]
arcLengthoffsetMat=(stepData["arc_length"]/stepData["arc_length"])*arcLengthOffset
top=stepData["arc_length"]-arcLengthoffsetMat #top
y= top/lastItemArcLength-arcLengthOffset
print(lastItemArcLength-arcLengthOffset)
ax.plot(x,y,'--',label="b.",color="black")



#add labels
ax.set_xlabel('$U_{x}$/$U_{0}$ [—]',size=14)
ax.set_ylabel('y/H [—]',size=14)
#ax.set_title('Frequency vs. Natural Frequency $n^{o}$')#,fontweight='bold')
ax_=plt.gca()

#set xaxis preferences
ax_.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(1))
ax_.xaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(f))
#set yaxis preferences

#remember to save as high quality
#see dissertation python plot code
plt.legend(loc='center left')
plt.show()
#plt.savefig("allPlottedHammerLab",dpi=300)
"""

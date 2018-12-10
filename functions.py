#the functions
import numpy as np
from xlrd import open_workbook
import matplotlib.pyplot as plt
from functions2 import *

crops = ['Rice','Wheat','Maize']
states=[]
gyears=[]
pyears=[]
s="Factors.xlsx"
flag=1
wb=open_workbook(s)
for sheet in wb.sheets():
    states.append(sheet.name)
    while(flag):
        nrows=sheet.nrows
        for row in range(1,nrows):
            gyears.append(int(sheet.cell(row,0).value))
        flag=0
gyears.sort()
pyears.append(gyears[len(gyears)-1]+1)
pyears.append(pyears[0]+1)
dic = {'Karnataka':'KA','Maharashtra':'MH','Uttar Pradesh':'UP','Madhya Pradesh':'MP','West Bengal':'WB'}

def c1(state,crop,year):
    l=[]
    s=crop + " production.xlsx"
    wb=open_workbook(s)
    for sheet in wb.sheets():
        if (sheet.name==state):
            nrows=sheet.nrows
            for row in range(1,nrows):
                if ((sheet.cell(row,0).value)==year):
                    l.append(sheet.cell(row,1).value)
    s="Factors.xlsx"
    wb=open_workbook(s)
    for sheet in wb.sheets():
        if (sheet.name==state):
            nrows=sheet.nrows
            for row in range(1,nrows):
                if ((sheet.cell(row,0).value)==year):
                    l.append(sheet.cell(row,1).value)
                    l.append(sheet.cell(row,2).value)
                    l.append(sheet.cell(row,3).value)
                    l.append(sheet.cell(row,4).value)
                    l.append(sheet.cell(row,5).value)
    return(l)

def autolabel(ax,rects):
    for rect in rects:
        height=rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height,
                '%d' % int(height),
                ha='center', va='bottom')

def c2(state,crop):
    ye=[]
    yi=[]
    s=crop + " production.xlsx"
    wb=open_workbook(s)
    for sheet in wb.sheets():
        if (sheet.name==state):
            nrows=sheet.nrows
            for row in range(1,nrows):
                ye.append(sheet.cell(row,0).value)
                yi.append(sheet.cell(row,1).value)
    title="Yield of " + crop + " in " + state
    N=len(ye)
    ind=np.arange(N)
    width=0.5
    [fig, ax]=plt.subplots()
    rects=ax.bar(ind,yi,width,color='g')
    ax.set_ylabel("Yield (in kg/hectare)")
    ax.set_xlabel("Years")
    ax.set_xticks(ind)
    for i in range(len(ye)):
        ye[i]=int(ye[i])
    ax.set_xticklabels(ye)
    ax.set_title(title)
    autolabel(ax,rects)
    plt.close('all')
    return(fig)

def maxrow(listname,max_from_column):
    l=listname
    l2=[]
    for i in range (0,len(l)):
        l2.append(l[i][max_from_column])
    maximum = max(l2)
    index = l2.index(maximum)
    l3=l[index]
    return(l3)

def c3(crop,year):
    l=[]
    s=crop + " production.xlsx"
    wb=open_workbook(s)
    for sheet in wb.sheets():
        l2=[]
        l2.append(sheet.name)
        nrows=sheet.nrows
        for row in range(1,nrows):
            if (sheet.cell(row,0).value==year):
                l2.append(sheet.cell(row,1).value)
                l.append(l2)
    st=[]
    yi=[]
    for i in l:
        st.append(dic[i[0]])
        yi.append(i[1])
    l2=maxrow(l,1)
    l.remove(l2)
    l.insert(0,l2)
    title="Yield of " + crop + " in " + str(year)
    N=len(yi)
    ind=np.arange(N)
    width=0.5
    [fig, ax]=plt.subplots()
    rects=ax.bar(ind,yi,width,color='g')
    ax.set_ylabel("Yield (in kg/hectare)")
    ax.set_xlabel("States")
    ax.set_xticks(ind)
    ax.set_xticklabels(st)
    ax.set_title(title)
    autolabel(ax,rects)
    plt.close('all')
    l.append(fig)
    return(l)

def c4(state,year):
    l=[]
    for i in crops:
        l2=[]
        l2.append(i)
        s=i + " production.xlsx"
        wb=open_workbook(s)
        for sheet in wb.sheets():
            if (sheet.name==state):
                nrows=sheet.nrows
                for row in range(1,nrows):
                    if ((sheet.cell(row,0).value)==year):
                        l2.append(sheet.cell(row,1).value)
                        l.append(l2)
    cr=[]
    yi=[]
    for i in l:
        cr.append(i[0])
        yi.append(i[1])
    l2=maxrow(l,1)
    l.remove(l2)
    l.insert(0,l2)
    title="Yield in " + state + " in " + str(year)
    N=len(yi)
    ind=np.arange(N)
    width=0.5
    [fig, ax]=plt.subplots()
    rects=ax.bar(ind,yi,width,color='g')
    ax.set_ylabel("Yield (in kg/hectare)")
    ax.set_xlabel("Crops")
    ax.set_xticks(ind)
    ax.set_xticklabels(cr)
    ax.set_title(title)
    autolabel(ax,rects)
    plt.close('all')
    l.append(fig)
    return(l)

def c5(state,crop,year):
    yieldlist=[]
    s=crop + " production.xlsx"
    wb=open_workbook(s)
    for sheet in wb.sheets():
        if (sheet.name==state):
            nrows=sheet.nrows
            for row in range(1,nrows):
                yieldlist.append(sheet.cell(row,1).value)
    yearlist=gyears
    [yieldpredict1,yieldfig]=predict('year','yield(in kg/hectare)',year,yearlist,yieldlist)
    yieldpredict1=yieldpredict1[0]
    hightemplist=[]
    lowtemplist=[]
    preplist=[]
    evaplist=[]
    cloudlist=[]
    s="Factors.xlsx"
    wb=open_workbook(s)
    for sheet in wb.sheets():
        if (sheet.name==state):
            nrows=sheet.nrows
            for row in range(1,nrows):
                hightemplist.append(sheet.cell(row,1).value)
                lowtemplist.append(sheet.cell(row,2).value)
                preplist.append(sheet.cell(row,3).value)
                evaplist.append(sheet.cell(row,4).value)
                cloudlist.append(sheet.cell(row,5).value)
    [hightemppredict,hightempfig]=predict('year','avg. high temp. (in *C)',year,yearlist,hightemplist)
    [lowtemppredict,lowtempfig]=predict('year','avg. low temp. (in *C)',year,yearlist,lowtemplist)
    [preppredict,prepfig]=predict('year','precipitation (in mm)',year,yearlist,preplist)
    [evappredict,evapfig]=predict('year','potential evaporation (in mm)',year,yearlist,evaplist)
    [cloudpredict,cloudfig]=predict('year','percentage of cloud cover',year,yearlist,cloudlist)
    hightemplist=[]
    lowtemplist=[]
    preplist=[]
    evaplist=[]
    cloudlist=[]
    yieldlist=[]
    s=crop + " production.xlsx"
    wb=open_workbook(s)
    for sheet in wb.sheets():
        nrows=sheet.nrows
        for row in range(1,nrows):
            yieldlist.append(sheet.cell(row,1).value)
    s="Factors.xlsx"
    wb=open_workbook(s)
    for sheet in wb.sheets():
        nrows=sheet.nrows
        for row in range(1,nrows):
            hightemplist.append(sheet.cell(row,1).value)
            lowtemplist.append(sheet.cell(row,2).value)
            preplist.append(sheet.cell(row,3).value)
            evaplist.append(sheet.cell(row,4).value)
            cloudlist.append(sheet.cell(row,5).value)
    yieldpredict2=NormalEquation([hightemppredict,lowtemppredict],yieldlist,hightemplist,lowtemplist)
    yieldpredict3=NormalEquation([cloudpredict],yieldlist,cloudlist)
    yieldpredict4=NormalEquation([preppredict,evappredict],yieldlist,preplist,evaplist)
    yieldpredict=(yieldpredict1+yieldpredict2+yieldpredict3+yieldpredict4)/4
    l=[[yieldpredict,yieldpredict1,yieldpredict2,yieldpredict3,yieldpredict4],hightemppredict[0],lowtemppredict[0],preppredict[0],evappredict[0],cloudpredict[0],yieldfig,hightempfig,lowtempfig,prepfig,evapfig,cloudfig]
    return(l)

def c52(state,crop,year):
    yieldlist=[]
    s=crop + " production.xlsx"
    wb=open_workbook(s)
    for sheet in wb.sheets():
        if (sheet.name==state):
            nrows=sheet.nrows
            for row in range(1,nrows):
                yieldlist.append(sheet.cell(row,1).value)
    yearlist=gyears
    yieldpredict1=predict2(year,yearlist,yieldlist)
    yieldpredict1=yieldpredict1[0]
    hightemplist=[]
    lowtemplist=[]
    preplist=[]
    evaplist=[]
    cloudlist=[]
    s="Factors.xlsx"
    wb=open_workbook(s)
    for sheet in wb.sheets():
        if (sheet.name==state):
            nrows=sheet.nrows
            for row in range(1,nrows):
                hightemplist.append(sheet.cell(row,1).value)
                lowtemplist.append(sheet.cell(row,2).value)
                preplist.append(sheet.cell(row,3).value)
                evaplist.append(sheet.cell(row,4).value)
                cloudlist.append(sheet.cell(row,5).value)
    hightemppredict=predict2(year,yearlist,hightemplist)
    lowtemppredict=predict2(year,yearlist,lowtemplist)
    preppredict=predict2(year,yearlist,preplist)
    evappredict=predict2(year,yearlist,evaplist)
    cloudpredict=predict2(year,yearlist,cloudlist)
    hightemplist=[]
    lowtemplist=[]
    preplist=[]
    evaplist=[]
    cloudlist=[]
    yieldlist=[]
    s=crop + " production.xlsx"
    wb=open_workbook(s)
    for sheet in wb.sheets():
        nrows=sheet.nrows
        for row in range(1,nrows):
            yieldlist.append(sheet.cell(row,1).value)
    s="Factors.xlsx"
    wb=open_workbook(s)
    for sheet in wb.sheets():
        nrows=sheet.nrows
        for row in range(1,nrows):
            hightemplist.append(sheet.cell(row,1).value)
            lowtemplist.append(sheet.cell(row,2).value)
            preplist.append(sheet.cell(row,3).value)
            evaplist.append(sheet.cell(row,4).value)
            cloudlist.append(sheet.cell(row,5).value)
    yieldpredict2=NormalEquation([hightemppredict,lowtemppredict],yieldlist,hightemplist,lowtemplist)
    yieldpredict3=NormalEquation([cloudpredict],yieldlist,cloudlist)
    yieldpredict4=NormalEquation([preppredict,evappredict],yieldlist,preplist,evaplist)
    yieldpredict=(yieldpredict1+yieldpredict2+yieldpredict3+yieldpredict4)/4
    return(yieldpredict)

def c6(crop,year):
    l=[]
    for i in range(len(states)):
        l.append([])
        l[i].append(states[i])
        x=c52(states[i],crop,year)
        l[i].append(x)
    st=[]
    yi=[]
    for i in l:
        st.append(dic[i[0]])
        yi.append(i[1])
    l2=maxrow(l,1)
    l.remove(l2)
    l.insert(0,l2)
    title="Yield of " + crop + " in " + str(year)
    N=len(yi)
    ind=np.arange(N)
    width=0.5
    [fig, ax]=plt.subplots()
    rects=ax.bar(ind,yi,width,color='g')
    ax.set_ylabel("Yield (in kg/hectare)")
    ax.set_xlabel("States")
    ax.set_xticks(ind)
    ax.set_xticklabels(st)
    ax.set_title(title)
    autolabel(ax,rects)
    plt.close('all')
    l.append(fig)
    return(l)

def c7(state,year):
    l=[]
    for i in range(len(crops)):
        l.append([])
        l[i].append(crops[i])
        x=c52(state,crops[i],year)
        l[i].append(x)
    cr=[]
    yi=[]
    for i in l:
        cr.append(i[0])
        yi.append(i[1])
    l2=maxrow(l,1)
    l.remove(l2)
    l.insert(0,l2)
    title="Yield in " + state + " in " + str(year)
    N=len(yi)
    ind=np.arange(N)
    width=0.5
    [fig, ax]=plt.subplots()
    rects=ax.bar(ind,yi,width,color='g')
    ax.set_ylabel("Yield (in kg/hectare)")
    ax.set_xlabel("Crops")
    ax.set_xticks(ind)
    ax.set_xticklabels(cr)
    ax.set_title(title)
    autolabel(ax,rects)
    plt.close('all')
    l.append(fig)
    return(l)

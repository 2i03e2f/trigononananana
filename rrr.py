'''
    examples input : >>== pi/3
                     >>== -2pi/3
                     >>== 7pi + 5*pi/3
                     >>== 2*pi + 2*pi - 17pi/9

'''



from fractions import Fraction
import re
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy import sin, cos, pi, linspace

#circleahh
plt.plot(0,0, color = 'black')
angles = linspace(0 * pi, 2 * pi, 100 )
xs = cos(angles)
ys = sin(angles)
plt.plot([1, -1], [0, 0], color = 'black')
plt.plot([0, 0], [1, -1], color = 'black')
plt.plot(xs, ys, color = 'black')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.gca().set_aspect('equal')

eq=input('== ')
if (eq.find('*pi') != -1):
    eq=eq.replace('*pi', '*180')
if (eq.find('*Pi') != -1):
    eq=eq.replace('*Pi', '*180')
if (eq.find('pi') != -1):
    eq=eq.replace('pi', '*180')
if (eq.find('Pi') != -1):
    eq=eq.replace('Pi', '*180')

l=[]
plus=re.split("\\+", eq)

dv=False
for i,v in enumerate(plus):
    if (v.find('/') != -1):
        dv=True
if not dv:
    for i,v in enumerate(plus):
            if (v.find('*') != -1):
                plus[i]=re.split("\\*", v)
                for i2,v2 in enumerate(plus):
                  if v2=='':
                    l.append(v.replace('*',''))
                  else:
                    l.append(v)
else:
    for i,v in enumerate(plus):
        if (v.find('/') != -1):
            if (v.find('*') != -1):
                plus[i]=re.split("\\*", v)
                for findfrat in plus[i]:
                    if (findfrat.find('/') != -1):
                        fract=Fraction(findfrat)
                        deno=Fraction(180/fract)
                for ind,v2 in enumerate(plus[i]):
                    if (v2.find('/') == -1):
                        if v2!='':
                            if (int(v2)-(round(int(v2)/deno)*deno))==1:
                                plus[i][ind]=str(round(int(v2)/deno))+'*180'
                                for shii in plus:
                                    if type(shii)==list:
                                        for real in shii:
                                            l.append(real)
                                    else:
                                        l.append(shii)
                            elif (int(v2)-(round(int(v2)/deno)*deno))==-1:
                                plus[i][ind]=str(round(int(v2)/deno))+'*180'
                                for tireddisshi,findfracagain in enumerate(plus[i]):
                                    if (findfracagain.find('/') != -1):
                                        plus[i][tireddisshi]="(-"+plus[i][tireddisshi]+")"
                                for shii in plus:
                                    if type(shii)==list:
                                        for real in shii:
                                            l.append(real)
                                    else:
                                        l.append(shii)
                            elif (int(v2)-(round(int(v2)/deno)*deno))==0:
                                plus[i][ind]='180'
                                for shii in plus:
                                    if type(shii)==list:
                                        for real in shii:
                                            if real==plus[i][ind]:
                                                l.append(real)
                                    else:
                                        l.append(shii)
                            else:
                                plus[i][ind]=str(round(int(v2)/deno))+'*180'
                                for tireddisshi,findfracagain in enumerate(plus[i]):
                                    if (findfracagain.find('/') != -1) and (int(v2)-(round(int(v2)/deno)*deno)<0):
                                        plus[i][tireddisshi]=str(int(v2)-(round(int(v2)/deno)*deno))+"*("+plus[i][tireddisshi]+")"
                                    elif (findfracagain.find('/') != -1) and (int(v2)-(round(int(v2)/deno)*deno)>0):
                                        plus[i][tireddisshi]=str(int(v2)-(round(int(v2)/deno)*deno))+"*("+plus[i][tireddisshi]+")"
                                for shii in plus:
                                    if type(shii)==list:
                                        for real in shii:
                                            l.append(real)
                                    else:
                                        l.append(shii)
                        else:
                            l.append(v.replace('*',''))

c=''
underni=False
for n,w in enumerate(l):
    if (w.find('/') != -1):
        de=abs(eval(w))
        underni=True
    if n!=0:
        c+='+'+w
    else:
        c+=w
dew=eval(c)
ec=eval(c)/360
x,y='+','+'
if (ec-int(ec) < 0.25 and ec-int(ec) > 0)or(ec-int(ec) < -0.75 and ec-int(ec) > -1):
    q=1;x,y='+','+'
elif ec-int(ec)==0:
    q='xaxis 1,0';x,y='+','0'
elif (ec-int(ec) < 0.50 and ec-int(ec) > 0.25)or(ec-int(ec) < -0.50 and ec-int(ec) > -0.75):
    q=2;x,y='-','+'
elif (ec-int(ec)==0.25)or(ec-int(ec)==-0.75):
    q='yaxis 0,1';x,y='0','+'
elif (ec-int(ec) < 0.75 and ec-int(ec) > 0.50)or(ec-int(ec) < -0.25 and ec-int(ec) > -0.50):
    q=3;x,y='-','-'
elif (ec-int(ec)==0.5)or(ec-int(ec)==-0.5):
    q='xaxis -1,0';x,y='-','0'
elif (ec-int(ec) < 1 and ec-int(ec) > 0.75)or(ec-int(ec) < 0 and ec-int(ec) > -0.25):
    q=4;x,y='+','-'
elif (ec-int(ec)==0.75)or(ec-int(ec)==-0.25):
    q='yaxis 0,-1';x,y='0','-'
if underni:
    if x=='-':
        coss='-'+str(round(math.cos(math.radians(de)), 3))
    else:
        coss=str(round(math.cos(math.radians(de)), 3))
    if y=='-':
        sinn='-'+str(round(math.sin(math.radians(de)), 3))
    else:
        sinn=str(round(math.sin(math.radians(de)), 3))
else:
    coss=str(round(math.cos(math.radians(dew)), 3))
    sinn=str(round(math.sin(math.radians(dew)), 3))
try:
    tann=str(float(sinn)/float(coss))
except:
    tann='not defined'
cycle=int(dew/360)
subde=dew-360*cycle
try:
    relde= str(de)
except:
    relde= str(dew)
print('''
    Quarter : {q}
    deg (In Quarter) : {de} deg
    Fulldeg : {dew} deg
    cycle : {cy} time(s) and {subde} deg
    (x,y) : ({x},{y})
    sin : {sinn} | cos : {coss} | tan : {tann}
    '''.format(q=str(q),
               de=relde,
               dew=str(dew),
               x=x,y=y,coss=coss,sinn=sinn,tann=tann,
               cy=str(cycle),
               subde=str(subde))
    )

arc_angles = linspace(0 * pi, pi/(180/dew), 90)
arc_xs = cos(arc_angles)
arc_ys = sin(arc_angles)
#plt.plot(arc_xs, arc_ys, color = 'black', lw = 1)
plt.plot([0, cos(pi/(180/dew))], [0, sin(pi/(180/dew))], color = "red")
plt.show()
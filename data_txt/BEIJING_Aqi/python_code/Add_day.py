f = open("Aqi_Beijing.txt","r")

L_DATE=[]; L_AQI=[]; L_PM2p5 =[]; L_PM10 =[]; L_SO2=[]; L_CO=[]; L_NO2=[]; L_O3_8h=[]; 
ijk=0
for line in f:
    if(ijk==0):
        ijk=1
        continue
    a1, a2, a3, a4, a5, a6, a7, a8 = line.split()
    L_DATE.append(a1); L_AQI.append(a2); L_PM2p5.append(a3); L_PM10.append(a4)
    L_SO2.append(a5); L_CO.append(a6); L_NO2.append(a7); L_O3_8h.append(a8)
f.close()

wf = open("Aqi_Beijing_day.txt","w+")
wf.write("DATE AQI PM2p5 PM10 SO2 CO NO2 O3_8h DAYS\n")
for i in range(len(L_DATE)):
    j=i%7; j=j+1
    wf.write("%s %s %s %s %s %s %s %s %i\n" %(L_DATE[i],L_AQI[i],L_PM2p5[i],L_PM10[i],L_SO2[i],L_CO[i],L_NO2[i],L_O3_8h[i],j)) 

wf.close()

 

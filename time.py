import time

c = time.time()
d = c

# write a recursive  to calculate the year
year = 1970
leapcounter = 2

def thisyear(d,year,leapcounter):
    s_a = 60.
    m_a = 60.
    h_a = 24.
    d_a = 365.
    d_l = 366.
    if (leapcounter!=0) or year==2000:
        yearlength = d_a*h_a*m_a*s_a # standard years in seconds
    else:
        yearlength = d_l*h_a*m_a*s_a # leap years in seconds

    test = d-yearlength
    if test>0:
        d=test
        year=year+1
        leapcounter=(leapcounter+1)%4
        result = thisyear(d,year,leapcounter)
    else:
        result=(d,year,leapcounter)

    return result

test_stack_too_big = d/(366.*24*60*60)
if test_stack_too_big<990:
    myinfo = thisyear(d,year,leapcounter)
else:
    print("Date too big for my stack!")

month_lengths=[31,28,31,30,31,30,31,31,30,31,30,31]
month_names=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
if leapcounter==0:
    month_lengths[2]=29
for f in range(len(month_lengths)):
    if f==0:
        month_start_date = [0]
    else:
        month_start_date.append(month_start_date[f-1]+month_lengths[f-1])

currentday=0
s_a = 60.
m_a = 60.
h_a = 24.
daylength = h_a*m_a*s_a
d=myinfo[0]

while(d-daylength)>0:
        d=d-daylength
        currentday+=1
print(str(daylength))
print(str(d))
print(str(d/daylength))

for f in range(12):
    if month_start_date[f]-currentday>0:
        break
month_name = month_names[f-1]

day_name = currentday-month_start_date[f-1]


hour = int(d/(m_a*s_a))
min = int((d/s_a)%(hour*m_a))

print(str(hour)+":"+str(min)+" o'clock GMT on "+str(day_name)+'th of '+month_name+", "+str(myinfo[1]))

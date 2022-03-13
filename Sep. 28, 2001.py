s="9/25/2019"
p1 = s.find("/")
m = s[:s.find("/")]
day = s[p1+1 :s.find("/",p1+1,len(s))]
y1 = s[-1:-5:-1]
years = y1[::-1]
print(years,"年",m,"月",day,"日")

month = ("Jan","Feb","Mar","Apr", "May", "Jun.", "Jul.", "Aug.", "Sep.", "Oct.", "Nov.", "Dec.")

D=int(m)-1

print(month[D],day,",",years)
 


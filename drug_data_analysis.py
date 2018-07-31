import drugs
import numpy as np
import matplotlib.pyplot as plt
list_of_report = drugs.get_reports()
california_reps = []
x = [] # year
y = [] # rates
y2= []
for d in list_of_report:
    if d["State"] == "California":
        # print("*****************************************************")
        info = {"Marijuana": d["Rates"]["Marijuana"]['New Users'],"Year":d["Year"]}
        # if d == "Totals":
        #     continue
        # if d == "Population":
        #     continue
        california_reps.append(info)
        x.append(d['Year'])
        y.append(d["Rates"]["Marijuana"]['New Users']["18-25"])
        y2.append(d["Rates"]["Marijuana"]['New Users']["12-17"])

#print(california_reps)

n = 256
#X = np.linspace(-np.pi,np.pi,n,endpoint=True)
#Y = np.sin(2*X)

plt.plot(x,y, color='blue', alpha=1.00)
plt.plot(x,y2, color='red', alpha=1.00)
#plt.ylim([1,10])
#plt.xlim([2003, 2014])
plt.show()

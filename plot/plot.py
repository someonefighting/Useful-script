import numpy as np
import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 12})
xi = []
online = []
ivector = []
ivector_plda = []
xvector = []
xvector_plda = []
with open('checkrate') as f:
    for line in f:
        line= line.strip()
        xi.append(float(line))
f.close()
with open('online') as f:
    for line in f:
        line = line.strip()[:-1]
        online.append(float(line))
        #print(line)
f.close()
with open('ivector') as f:
    for line in f:
        line= line.strip()[:-1]
        ivector.append(float(line))
f.close()
with open('ivector_plda') as f:
    for line in f:
        line = line.strip()[:-1]
        ivector_plda.append(float(line))
f.close()
with open('xvector') as f:
    for line in f:
        line = line.strip()[:-1]
        xvector.append(float(line))
f.close()
with open('xvector_plda') as f:
    for line in f:
        line = line.strip()[:-1]
        xvector_plda.append(float(line))
f.close()

index = list(range(len(xi)))

#fig = plt.figure(figsize=(15,8),facecolor='w')
fig, ax = plt.subplots(figsize=(25,8),facecolor='w')
#x = np.arange(1,175,3)
line_1=ax.plot(index, online,'r', label='online')
line_2=ax.plot(index, ivector,'y', label='ivector + PLDA')
line_3=ax.plot(index, ivector_plda,'g', label='ivector + adapted PLDA')
line_4=ax.plot(index, xvector,'b', label='xvector + PLDA')
line_5=ax.plot(index, xvector_plda,'k', label='xvector + adaptd PLDA')
#egend = ax.legend(loc='upper center', shadow=True, fontsize='x-large')
legend=ax.legend(loc='lower center', shadow=True, fontsize='x-large')
#legend.get_frame().set_facecolor('C0')
#ax.legend([line_1, line_2, line_3, line_4, line_5], ['online', 'ivector + PLDA', 'ivector + adapted PLDA', 'xvector + PLDA', 'xvector + adaptd PLDA'],loc='upper center', shadow=True, fontsize='x-large')
#plt.axvline(x=0.001)
#plt.xticks(np.arange(min(index), max(index), 0.0002))
plt.grid()
plt.xlabel('audio auditing rate(%)')
plt.ylabel('recall rate(%)')
plt.xticks(index, xi)
fig.savefig('result.png')

import numpy as np
import matplotlib
matplotlib.use('Agg') # Must be before importing matplotlib.pyplot or pylab!import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 22})
lloss = []
leer = []
with open('loss') as f:
    for line in f:
        _,loss, eer = line.strip().split()
        lloss.append(float(loss))
        leer.append(float(eer))
        #print(line)
f.close()


fig = plt.figure(figsize=(15,8),facecolor='w')
#x = np.arange(1,175,3)
line_up,=plt.plot(lloss,'r')
#line_down,=plt.plot(leer,'b')
plt.legend([line_up], ['loss'])
plt.xlabel('Epoch')
plt.ylabel('Loss')
fig.savefig('ftdnn_loss.pdf')

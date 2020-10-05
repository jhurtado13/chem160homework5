import numpy as np
import math, time, random
ntrials=10000000
dist=0
start_time=time.process_time()
for i in range(ntrials):
    x1=np.random.random()
    y1=np.random.random()
    z1=np.random.random()
    x2=np.random.random()
    y2=np.random.random()
    z2=np.random.random()
dist=np.mean(np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2))
e_time=time.process_time()-start_time
ex_dist=1/105*(4+17*math.sqrt(2)-6*math.sqrt(3)+21*math.log(1+math.sqrt(2))+42*math.log(2+math.sqrt(3))-7*math.pi)
print("Ntrials=%d  dist=%9.7f  Exact dist=%9.7f elapsed time=%6.2f"%(ntrials,dist,ex_dist,e_time))
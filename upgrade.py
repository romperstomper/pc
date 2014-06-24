import matplotlib.pyplot as plt

def foo(increm, num):
  currenttime = 0
  res = []
  totalres = 0
  rate = 1
  timenextup = 1
  inc = 1
  for i in range(num):
    totalres = totalres + inc
    inc = inc + increm
    currenttime = timenextup
    rate += 1
    timenextup = timenextup + (inc/rate)
    res.append((currenttime, totalres))
  return res

a = foo(2, 11)
b = foo(0.5, 15)
c = foo(0, 20)
d = foo(1, 10)
ax = [x[0] for x in a] 
ay = [x[1] for x in a] 
bx = [x[0] for x in b] 
by = [x[1] for x in b] 
cx = [x[0] for x in c] 
cy = [x[1] for x in c] 
dx = [x[0] for x in d] 
dy = [x[1] for x in d] 
    
plt.plot(ax, ay, 'b-', bx, by, 'r-', cx, cy, 'g-', dx, dy, 'y-')
plt.show()

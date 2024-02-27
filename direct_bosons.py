import pylab, math, random
def z(beta, k):
   sum = 1.0 / (1.0 - math.exp(-k * beta)) ** 3
   return sum
def canonic_recursion(beta,N):
   Z = [1.0]
   for M in range(1, N + 1):
      Z.append(sum(Z[k] * z(beta, M - k) for k in range(M)) / M)
   return Z
def pi_list_make(Z, M):
   pi_list = [0] + [z(beta, k) * Z[M - k] / Z[M] / M for k in range(1, M + 1)]
   pi_sum = [0]
   for k in range(1, M + 1):
      pi_sum.append(pi_sum[k - 1] + pi_list[k])
   return pi_sum
def tower_sample(data, Upsilon): #fully naive tower sampling
   for k in range(len(data)):
      if Upsilon < data[k]: break
   return k
def levy_harmonic_path(Del_tau, N):
   beta = N * Del_tau
   xN = random.gauss(0.0, 1.0 / math.sqrt(2.0 * math.tanh(beta / 2.0)))
   x = [xN]
   for k in range(1, N):
      Upsilon_1 = 1.0 / math.tanh(Del_tau) + 1.0 / math.tanh((N - k) * Del_tau)
      Upsilon_2 = x[k - 1]/ math.sinh(Del_tau) + xN / math.sinh((N - k) * Del_tau)
      x_mean = Upsilon_2 / Upsilon_1
      sigma = 1.0 / math.sqrt(Upsilon_1)
      x.append(random.gauss(x_mean, sigma))
   return x

N = 100 # this naive program may overflow for N > 100
T_star = 0.1
T = T_star * N ** (1.0 / 3.0)
beta = 1.0 / T
Z = canonic_recursion(beta, N)
print(Z)
M = N
x_config = []
y_config = []
while M > 0:
   pi_sum = pi_list_make(Z, M)
   Upsilon = random.uniform(0.0, 1.0)
   k = tower_sample(pi_sum, Upsilon)
   x_config += levy_harmonic_path(beta, k)
   y_config += levy_harmonic_path(beta, k)
   M -= k
pylab.figure(1)
pylab.axis('scaled')
pylab.xlim(-5.0, 5.0)
pylab.ylim(-5.0, 5.0)
pylab.plot(x_config, y_config,'ro')
pylab.xlabel('$x$')
pylab.ylabel('$y$')
pylab.title('3d bosons in trap (2d projection):'+' $N$= '+str(N)+' T* =' + str(T_star))
pylab.show()

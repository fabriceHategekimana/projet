import numpy as np
import matplotlib.pyplot as plt

import Problem3.kl_divergence as dkl


# 2.
NB_POINTS = 1000
set_ = np.linspace(0.0, 1.0, num=NB_POINTS)

#   a)
p = dkl.ProbabilityFunction.binary(0.1)
set_q = set_[1:-1]  # remove infinite
dpq = [dkl.dkl(p.function, {0: 1-q, 1: q}) for q in set_q]

lower_bound = [2*(p.function[1] - q)**2 * 1 for q in set_q]  # 1 = log(e), using natural log here

fig, ax = plt.subplots()
ax.plot(set_q, dpq, label='D(p(x)||q(x))')
ax.plot(set_q, lower_bound, '--r', label='lower bound')
ax.set(xlabel='q(x)', ylabel='D(p(x)||q(x))', title='Binary divergence: 2.a) p=0.1')
plt.legend()
# fig.savefig("P4_2a.png")
plt.show()
plt.close()


#   b)
q = dkl.ProbabilityFunction.binary(0.2)
set_p = set_
dpq = [dkl.dkl({0: 1-p, 1: p}, q.function) for p in set_p]

lower_bound = [2*(p - q.function[1])**2 * 1 for p in set_p]  # 1 = log(e), using natural log here

fig, ax = plt.subplots()
ax.plot(set_p, dpq, label='D(p(x)||q(x))')
ax.plot(set_p, lower_bound, '--r', label='lower bound')
ax.set(xlabel='p(x)', ylabel='D(p(x)||q(x))', title='Binary divergence: 2.b) q=0.2')

plt.legend()
# fig.savefig("P4_2b.png")
plt.show()
plt.close()

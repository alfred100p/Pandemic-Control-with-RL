#imports

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def SIR(N,I0,R0,beta,gamma,days=105):#105 days-15 weeks
  '''
  N - Total Population
  I0 - Initial No. of infected people
  R0 - Initial No. of Recovered 
  beta - Contact rate
  gamma - Recovery rate
  days- No. of days considered
  '''
  S0 = N - I0 - R0 #intial no. of susceptipble people
  
  t = np.linspace(0, days, days)
  def deriv(y, t, N, beta, gamma):
      S, I, R = y
      dSdt = -beta * S * I / N
      dIdt = beta * S * I / N - gamma * I
      dRdt = gamma * I
      return dSdt, dIdt, dRdt
  y0 = S0, I0, R0#feature vector
  ret = odeint(deriv, y0, t, args=(N, beta, gamma))
  S, I, R = ret.T
  dIdt=beta * S * I / N - gamma * I
  print(S[-1],I[-1],R[-1])

  # Plot the data on three separate curves for S(t), I(t) and R(t)
  fig = plt.figure(facecolor='w')
  ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
  ax.plot(t, S/N*100, 'b', alpha=0.5, lw=2, label='Susceptible')
  ax.plot(t, I/N*100, 'r', alpha=0.5, lw=2, label='Infected')
  ax.plot(t, R/N*100, 'g', alpha=0.5, lw=2, label='Recovered with immunity')
  ax.set_xlabel('Days')
  ax.set_ylabel('Percentage of Population')
  ax.set_ylim(-5,105)
  ax.yaxis.set_tick_params(length=0)
  ax.xaxis.set_tick_params(length=0)
  ax.grid(b=True, which='major', c='w', lw=2, ls='-')
  legend = ax.legend()
  legend.get_frame().set_alpha(0.5)
  for spine in ('top', 'right', 'bottom', 'left'):
      ax.spines[spine].set_visible(False)
  plt.show()
  return dIdt

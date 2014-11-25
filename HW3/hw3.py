import numpy as np
import matplotlib.pyplot as plt

class Wave(object):
    def __init__(self,eta,timesteps,H=10.0,dx=100.0,dt=5.0,g=9.8):
        self.eta = np.zeros((eta.shape[0],timesteps+1))
        self.eta[:,0] = eta
        self.u = np.zeros((eta.shape[0]+1,timesteps+1))
        global H_g, dx_g, dt_g, g_g
        H_g = H
        dx_g = dx
        dt_g = dt
        g_g = g
        
        for t in range(timesteps-1):
            self.__timestep__(t)
            
    def __timestep__(self,t):
        self.u[1:-1,t+1] = self.u[1:-1,t] - (g_g*dt_g/dx_g) * \
                           (self.eta[1:,t] - self.eta[:-1,t])
        self.u[0,t+1] = 0
        self.u[-1,t+1] = 0
    
        self.eta[:,t+1] = self.eta[:,t] - (H_g*dt_g/dx_g) * \
                          (self.u[1:,t+1] - self.u[:-1,t+1])

if __name__ == '__main__':
    n = 200
    timesteps = 10000
    H = 30.0
    dx = 50.0
    dt = 2.50

    eta = np.zeros((n-1))
    x = np.array(range(n-1))
    
    lens = len(eta[0:np.floor(n/4)])
    
    #eta[((n/2)-(lens/2)):np.floor(n/4)+((n/2)-(lens/2))] = H*(1-np.cos(16*np.pi*x[0:np.floor(n/4)]/n))
    eta = H*np.cos(0.05*np.pi*x)
    test = Wave(eta,timesteps,H=H,dx=dx,dt=dt)
    print test.eta[:,0]
    temp = np.floor(timesteps/5.0)-1
    fig = plt.figure()
    fig.set_size_inches((10,3))
    fig.add_subplot(411)
    plt.plot(x,H+test.eta[:,0])
    plt.ylabel('Height (m)')
    plt.ylim([0,H+np.max(test.eta[:,0])])
    plt.xlim([0,198])
    plt.title('1D Wave Equation')
    fig.add_subplot(412)
    plt.plot(x,H+test.eta[:,temp])
    plt.ylabel('Height (m)')
    plt.ylim([0,H+np.max(test.eta[:,0])])
    plt.xlim([0,198])
    fig.add_subplot(413)
    plt.plot(x,H+test.eta[:,2*temp])
    plt.ylabel('Height (m)')
    plt.ylim([0,H+np.max(test.eta[:,0])])
    plt.xlim([0,198])
    fig.add_subplot(414)
    plt.plot(x,H+test.eta[:,3*temp])
    plt.ylabel('Height (m)')
    plt.ylim([0,H+np.max(test.eta[:,0])])
    plt.xlim([0,198])
    
    fig = plt.figure()
fig.set_size_inches((10,3))

for t in range(timesteps):
    plt.clf()
    fig.add_subplot(111)
    plt.plot(x,H+test.eta[:,t])
    plt.ylabel('Height (m)')
    plt.ylim([0,60])
    plt.xlim([0,198])
    plt.title('1D Wave Equation')
    plt.savefig('frames5/frame_%04d.png' % t)
    
    
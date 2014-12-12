import numpy as np
import matplotlib.pyplot as plt
import netCDF4

class Wave(object):
    def __init__(self,eta,timesteps,H=10.0,dx=100.0,dt=5.0,g=9.8):
        '''
        Solves the 1D wave equation.
        Inputs:
            eta - initial height field
            timesteps - number of timesteps to solve equation
            H - mean height of the fluid, default 10.0 m
            dx - horizontal grid interval, default 100.0 m
            dt - timestep interval, default 5.0 seconds
            g - acceleration due to gravity, default 9.8 m/s2
        '''
        self.eta = np.zeros((eta.shape[0],timesteps+1))
        self.eta[:,0] = eta
        self.u = np.zeros((eta.shape[0]+1,timesteps+1))
        # Use global variables since I didn't really want to store each 
        # constant in the class.
        global H_g, dx_g, dt_g, g_g
        H_g = H
        dx_g = dx
        dt_g = dt
        g_g = g
        
        for t in range(timesteps-1):
            self.__timestep__(t)
            
    def __timestep__(self,t):
        '''
        I use the double underscore to denote a method that I don't want the
        user of the class to use, a "private" method.
        Calculates the horizontal velocity and height of the fluid at the next
        timestep.
        '''
        self.u[1:-1,t+1] = self.u[1:-1,t] - (g_g*dt_g/dx_g) * \
                           (self.eta[1:,t] - self.eta[:-1,t])
        self.u[0,t+1] = 0
        self.u[-1,t+1] = 0
    
        self.eta[:,t+1] = self.eta[:,t] - (H_g*dt_g/dx_g) * \
                          (self.u[1:,t+1] - self.u[:-1,t+1])

    def write_out(self,filename):
        '''
        Writes the data from the class into a netCDF file.
        '''
        nc = netCDF4.Dataset(filename,'w')
        nc.author = 'Herrera'
        nc.createDimension('x_f',self.u.shape[0])
        nc.createDimension('x_s',self.eta.shape[0])
        nc.createDimension('t',self.eta.shape[1])
        nc.createVariable('x_full','d',('x_f',))
        nc.variables['x_full'][:] = np.arange(self.u.shape[0])*dx_g
        nc.variables['x_full'].units = 'meters'
        nc.createVariable('x_stag','d',('x_s',))
        nc.variables['x_stag'][:] = np.arange(1,self.eta.shape[0]+1)*dx_g
        nc.variables['x_stag'].units = 'meters'
        nc.createVariable('u','d',('x_f','t'))
        nc.variables['u'][:] = self.u
        nc.variables['u'].units = 'meters sec-1'
        nc.createVariable('eta','d',('x_s','t'))
        nc.variables['eta'][:] = self.eta
        nc.variables['eta'].units = 'meters'
        nc.createVariable('time','d',('t',))
        nc.variables['time'][:] = np.arange(self.u.shape[1])*dt_g
        nc.variables['time'].units = 'seconds'
        nc.close()
        

if __name__ == '__main__':
    # Define the constants for my wave
    n = 200
    timesteps = 10000
    H = 30.0
    dx = 50.0
    dt = 2.50

    # Initalize the arrays
    eta = np.zeros((n-1))
    x = np.array(range(n-1))
    lens = len(eta[0:np.floor(n/4)])
    
    # Define the height of the fluid over the domain
    eta[((n/2)-(lens/2)):np.floor(n/4)+((n/2)-(lens/2))] = H*(1-np.cos(16*np.pi*x[0:np.floor(n/4)]/n))
    #eta = H*np.cos(0.05*np.pi*x)

    # Solve the wave equation and write out the output.
    test = Wave(eta,timesteps,H=H,dx=dx,dt=dt)
    test.write_out('1d_wave_eqn.nc')

    # Save a simple plot to make sure the results look realistic.
    temp = np.floor(timesteps/5.0)-1
    fig = plt.figure()
    fig.set_size_inches((12,10))
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
    plt.savefig('1d_wave_eqn.eps')   

    '''
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
    '''
    

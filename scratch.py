import matplotlib
matplotlib.use('Agg')  # Gernate images without having a window appear
import matplotlib.pyplot as plt

# Set default directories
data_home = 'images/'
outdir = 'output/'

plt.figure()
plt.plot([1,2,3,1,2,3,4,3,2,1])
plt.savefig(outdir + 'test.png')

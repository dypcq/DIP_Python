#!/usr/bin/python2
import scipy.misc
import matplotlib.pyplot as plt

lena8b = scipy.misc.lena()

print "Mean pixel value: ", lena8b.mean()
print "Min pixel value: ",lena8b.min()
print "Max pixel value: ",lena8b.max()

# Plot image histogram
plt.subplot(1,2,1)
plt.hist(lena8b.flatten(), 100)
plt.xlabel('Intensity')
plt.ylabel('Number of Pixels')
plt.title('Histogram')

plt.subplot(1,2,2)
plt.imshow(lena8b)
plt.gray()
plt.title('Image')

plt.show()


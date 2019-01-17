from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)


img = Image.open("0013035.jpg")
gray = img.convert('L')
r, g, b = img.split()
img_merged = Image.merge('RGB', (r, g, b))

plt.figure(1)
plt.suptitle('Multi_Image')

plt.subplot(2, 3, 1)
plt.title('image')
plt.imshow(img)
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title('gray')
plt.imshow(gray, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title('image_merged')
plt.imshow(img_merged)
plt.axis('off')

# plt.subplot(2, 3, 4)
# plt.title('r')
# plt.imshow(r, cmap='gray')
# plt.axis('off')
#
# plt.subplot(2, 3, 5)
# plt.title('g')
# plt.imshow(g, cmap='gray')
# plt.axis('off')
#
# plt.subplot(2, 3, 6)
# plt.title('b')
# plt.imshow(b, cmap='gray')
# plt.axis('off')

plt.show()

# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
# plt.figure(1)
# plt.subplot(3, 2, 1)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# plt.title('1')
# plt.subplot(3, 2, 2)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.title('2')
# plt.subplot(3, 2, 3)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# plt.title('3')
# plt.subplot(3, 2, 4)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.title('4')
# plt.subplot(3, 2, 5)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# plt.title('5')
# plt.subplot(3, 2, 6)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.title('6')
# plt.show()



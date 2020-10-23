import numpy as np
import matplotlib.pyplot as plt
from tool._fixedInt import *

##### INPUT AND OUTPUT DECLARATION #####
##### FIXED POINT #####
x0 = DeFixedInt(8,6)
x1 = DeFixedInt(8,6)
x2 = DeFixedInt(8,6)
x3 = DeFixedInt(8,6)

add_x = DeFixedInt(10,6)
add_y = DeFixedInt(12,6)

prod_y1 = DeFixedInt(12,6)
prod_y2 = DeFixedInt(12,6)

y0 = DeFixedInt(12,6)
y1 = DeFixedInt(12,6)
y2 = DeFixedInt(12,6)

##### VALUES #####
x0.value = 100.
prod_y1.value = 0.5
prod_y2.value = 0.25


##### FILTER FEATURES #####
sample_rate = 30
N 			= 30
dt 			= N / sample_rate
t 			= np.arange(0, N, dt)

##### SIGNALS #####
impulse = [0] * N
step 	= [0] * N

##### SHIFT REGISTER #####
def shift(x0,x1,x2,x3,y1,y2):
	x3 = x2
	x2 = x1
	x1 = x0

	y2 = y1
	y1 = y0


##### IMPULSE RESPONSE #####
for i in range (N):
	if i == 1:
		x0.value = 0.
	# Filter
	add_x.assign(x0 - x1 + x2 + x3)
	add_y.assign(y1 * prod_y1 + y2 * prod_y2)
	print(add_y)
	y0.assign(add_x + add_y)
	#Shift
	x3.value = x2.fValue
	x2.value = x1.fValue
	x1.value = x0.fValue

	y2.value = y1.fValue
	y1.value = y0.fValue

	impulse[i] = y0.fValue


##### STEP RESPONSE #####
x0.value = 1.

for i in range (N):
	# Filter
	add_x.assign(x0 - x1 + x2 + x3)
	add_y.assign(y1 * prod_y1 + y2 * prod_y2)
	y0.assign(add_x + add_y)
	print(add_x)
	#print(add_y)
	#Shift
	x3.value = x2.fValue
	x2.value = x1.fValue
	x1.value = x0.fValue

	y2.value = y1.fValue
	y1.value = y0.fValue
	step[i]  = y0.fValue

#print("Respuesta al impulso")
#print(impulse)
#print("Respuesta al escalon")
#print(step)

##### FIGURES #####
fig, axs = plt.subplots(2, 1)
axs[0].stem(t, impulse,use_line_collection = True)
axs[1].stem(t, step,use_line_collection = True)

axs[0].set_xlabel('samples (N)')
axs[1].set_xlabel('samples (N)')
axs[0].set_title('Impulse response')
axs[1].set_title('Step response')
axs[0].set_ylabel('Amplitude')
axs[1].set_ylabel('Amplitude')

axs[0].grid(True)
axs[1].grid(True)

fig.tight_layout()

plt.show()

#print(impulse)
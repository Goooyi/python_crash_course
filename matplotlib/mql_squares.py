# %%
import matplotlib as mpl
import matplotlib.pyplot as plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25] 
plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.plot(input_value, squares, linewidth=5)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()
# %%

fig, ax = plt.subplots()
ax.scatter(2,4, s=200)
ax.tick_params(axis='both', labelsize=14)
# %%
input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25] 
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(input_value, squares, s=100)
# %%
input_value = range(1,1000)
squares = [x**2 for x in input_value]
fig, ax = plt.subplots()
ax.scatter(input_value, squares, c=range(999), cmap='viridis', s=100)
# %%

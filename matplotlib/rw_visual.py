# %%
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# %%
rw = RandomWalk(50_000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
ax.scatter(rw.x_values, rw.y_values, c=range(rw.num_points), cmap='Blues', s=6)
# ax.scatter(0,0,c='green',edgecolors=None, s=100)
# ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors=None, s=100)

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)


plt.show()

# %%

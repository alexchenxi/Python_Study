from matplotlib import pyplot as plt
from random_walk import RandomWalk

move = RandomWalk(5_000)
move.fill_walk()

plt.style.use("classic")
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
point_numbers = range(move.num_points)
ax.plot(
    move.x_values,
    move.y_values,
    linewidth=1,
    c="blue",
)
plt.show()

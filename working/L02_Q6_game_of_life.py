import numpy as np
import matplotlib.pyplot as plt
import time

n, m = 50,100

n_steps = 100

table = np.random.randint(0,2,n*m).reshape(n,m)

fig, ax = plt.subplots()

ax.imshow(table, cmap='Greys')

ax.set_title(f"Initial condition: {len(table[table==1])} live cells")
ax.set_xticks(np.arange(table.shape[1]+1)-.5, labels="")
ax.set_yticks(np.arange(table.shape[0]+1)-.5, labels="")
ax.grid(visible=True, which="major", axis="both")

plt.show(block=False)

plt.ion()

fig_steps, ax_steps = plt.subplots()
ax_steps.set_xticks(np.arange(table.shape[1]+1)-.5, labels="")
ax_steps.set_yticks(np.arange(table.shape[0]+1)-.5, labels="")
ax_steps.grid(visible=True, which="major", axis="both")

new_table = np.zeros_like(table)

for i in range(n_steps):
    ax_steps.clear()
    ax_steps.set_xticks(np.arange(table.shape[1]+1)-.5, labels="")
    ax_steps.set_yticks(np.arange(table.shape[0]+1)-.5, labels="")
    ax_steps.grid(visible=True, which="major", axis="both")

    new_table.fill(0)
    calc_table = np.vstack((np.atleast_2d(table[-1,:]), table, np.atleast_2d(table[0,:])))
    calc_table = np.hstack((np.atleast_2d(calc_table[:,-1]).T, calc_table, np.atleast_2d(calc_table[:,0]).T))
    for j in range(n):
        for k in range(m):
            neighbor_sum = np.sum(calc_table[j:j+3, k:k+3]) - table[j,k]
            if table[j,k] == 1 and np.logical_or(neighbor_sum == 2, neighbor_sum == 3):
                new_table[j,k] = 1
            elif table[j,k] == 0 and neighbor_sum == 3:
                new_table[j,k] = 1

    for j in range(n):
        for k in range(m):
            table[j,k] = new_table[j,k]
        
    ax_steps.imshow(table, cmap='Greys')
    ax_steps.set_title(f"Step {i+1}/{n_steps}: {len(table[table==1])} live cells")

    fig_steps.canvas.draw()
    fig_steps.canvas.flush_events()
    time.sleep(0.1)

plt.close(fig_steps)

fig_final, ax_final = plt.subplots()

ax_final.imshow(table, cmap='Greys')

ax_final.set_title(f"Final condition: {len(table[table==1])} live cells")
ax_final.set_xticks(np.arange(table.shape[1]+1)-.5, labels="")
ax_final.set_yticks(np.arange(table.shape[0]+1)-.5, labels="")
ax_final.grid(visible=True, which="major", axis="both")

plt.show(block=True)
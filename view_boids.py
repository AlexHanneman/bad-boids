from boids import Boids
from matplotlib import pyplot as plt
from matplotlib import animation

boids = Boids(
    flock_attraction=0.01 / 50,
    avoidance_radius=10,
    formation_flying_radius=100,
    speed_matching_strength=0.125 / 50,
)

boids.initialise_random(50)

figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(
    [b.position[0] for b in boids.boids], [b.position[1] for b in boids.boids]
)


def animate(frame):
    boids.update()
    scatter.set_offsets([b.position for b in boids.boids])


anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()

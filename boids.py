"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

num_boids = 50
middle_strength = 0.01/num_boids
proximity_dist = 100
match_vel_dist = 10000
match_vel_strength = 0.125/num_boids


def init_boids():
    boids_x = [random.uniform(-450, 50.0) for x in range(num_boids)]
    boids_y = [random.uniform(300.0, 600.0) for x in range(num_boids)]
    boid_x_velocities = [random.uniform(0, 10.0) for x in range(num_boids)]
    boid_y_velocities = [random.uniform(-20.0, 20.0) for x in range(num_boids)]
    boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)
    return boids


def calc_boid_vel(x_a, y_a, xv_a, yv_a, x_b, y_b, xv_b, yv_b):
    xVelChange = 0.0
    yVelChange = 0.0

    xSep = x_b - x_a
    ySep = y_b - y_a

    xVelChange += xSep*middle_strength
    yVelChange += ySep*middle_strength

    # Fly away from nearby boids
    if check_distance(x_a, x_b, y_a, y_b, proximity_dist):
        xVelChange -= xSep
        yVelChange -= ySep

    # Try to match speed with nearby boids
    if check_distance(x_a, x_b, y_a, y_b, match_vel_dist):
        xVelChange += (xv_b - xv_a) * match_vel_strength
        yVelChange += (yv_b - yv_a) * match_vel_strength

    return xVelChange, yVelChange


def update_boids(boids):
    xs, ys, xvs, yvs = boids
    # Fly towards the middle
    for i in range(len(xs)):
        xVelChange = 0.0
        yVelChange = 0.0
        for j in range(len(xs)):
            velChange = calc_boid_vel(
                xs[i], ys[i], xvs[i], yvs[i], xs[j], ys[j], xvs[j], yvs[j])
            xVelChange += velChange[0]
            yVelChange += velChange[1]

        # Update velocity
        xvs[i] += xVelChange
        yvs[i] += yVelChange

        # Move according to velocities
        xs[i] = xs[i]+xvs[i]
        ys[i] = ys[i]+yvs[i]


def check_distance(src_x, dst_x, src_y, dst_y, dist):
    return (((dst_x-src_x)**2 + (dst_y-src_y)**2) < dist)


boids = init_boids()

figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(boids[0], boids[1])


def animate(frame):
    update_boids(boids)
    scatter.set_offsets(list(zip(boids[0], boids[1])))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()

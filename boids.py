"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes


class Boids:
    def __init__(self, numBoids, flockStrength, proxDist, flockDist, matchVelStrength) -> None:
        self.numBoids = numBoids
        self.flockStrength = flockStrength
        self.proxDist = proxDist
        self.flockDist = flockDist
        self.matchVelStrength = matchVelStrength

    def init_boids(self):
        self.xs = [random.uniform(-450, 50.0) for x in range(self.numBoids)]
        self.ys = [random.uniform(300.0, 600.0) for x in range(self.numBoids)]
        self.xvs = [random.uniform(0, 10.0) for x in range(self.numBoids)]
        self.yvs = [random.uniform(-20.0, 20.0) for x in range(self.numBoids)]
        return boids

    def init_boids_from_file(self, fileData):
        self.xs, self.ys, self.xvs, self.yvs = fileData

    def calc_boid_vel(self, x_a, y_a, xv_a, yv_a, x_b, y_b, xv_b, yv_b):
        xVelChange = 0.0
        yVelChange = 0.0

        xSep = x_b - x_a
        ySep = y_b - y_a

        xVelChange += xSep*self.flockStrength
        yVelChange += ySep*self.flockStrength

        # Fly away from nearby boids
        if self.check_distance(x_a, x_b, y_a, y_b, self.proxDist):
            xVelChange -= xSep
            yVelChange -= ySep

        # Try to match speed with nearby boids
        if self.check_distance(x_a, x_b, y_a, y_b, self.flockDist):
            xVelChange += (xv_b - xv_a) * self.matchVelStrength
            yVelChange += (yv_b - yv_a) * self.matchVelStrength

        return xVelChange, yVelChange

    def update_boids(self):
        # Fly towards the middle
        for i in range(self.numBoids):
            xVelChange = 0.0
            yVelChange = 0.0
            for j in range(self.numBoids):
                velChange = self.calc_boid_vel(
                    self.xs[i], self.ys[i], self.xvs[i], self.yvs[i], self.xs[j], self.ys[j], self.xvs[j], self.yvs[j])
                xVelChange += velChange[0]
                yVelChange += velChange[1]

            # Update velocity
            self.xvs[i] += xVelChange
            self.yvs[i] += yVelChange

            # Move according to velocities
            self.xs[i] += self.xvs[i]
            self.ys[i] += self.yvs[i]

    def check_distance(self, src_x, dst_x, src_y, dst_y, dist):
        return (((dst_x-src_x)**2 + (dst_y-src_y)**2) < dist)


boids = Boids(50, 0.01/50, 100, 10000, 0.125/50)
boids.init_boids()

figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(boids.xs, boids.ys)


def animate(frame):
    boids.update_boids()
    scatter.set_offsets(list(zip(boids.xs, boids.ys)))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()

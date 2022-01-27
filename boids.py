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

boids_x=[random.uniform(-450,50.0) for x in range(num_boids)]
boids_y=[random.uniform(300.0,600.0) for x in range(num_boids)]
boid_x_velocities=[random.uniform(0,10.0) for x in range(num_boids)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(num_boids)]
boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def update_boids(boids):
    xs,ys,xvs,yvs=boids
    # Fly towards the middle
    for i in range(len(xs)):
        for j in range(len(xs)):
            xvs[i] = calc_vel_change(xvs[i], xs[j], xs[i], middle_strength)
            yvs[i] = calc_vel_change(yvs[i], ys[j], ys[i], middle_strength)
   
            # Fly away from nearby boids
            if check_distance(xs[i], xs[j], ys[i], ys[j], proximity_dist):
                xvs[i] = calc_vel_change(xvs[i], xs[i], xs[j])
                yvs[i] = calc_vel_change(yvs[i], ys[i], ys[j])
    
            # Try to match speed with nearby boids
            if check_distance(xs[i], xs[j], ys[i], ys[j], match_vel_dist):
                xvs[i] = calc_vel_change(xvs[i], xvs[j], xvs[i], match_vel_strength)
                yvs[i] = calc_vel_change(yvs[i], yvs[j], yvs[i], match_vel_strength)
        
        # Move according to velocities
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]


def calc_vel_change(base, increment, decrement, modifier=1):
    return base + (increment - decrement) * modifier

def check_distance(src_x, dst_x, src_y, dst_y, dist):
    return (((dst_x-src_x)**2 + (dst_y-src_y)**2) < dist)

figure=plt.figure()
axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
scatter=axes.scatter(boids[0],boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(list(zip(boids[0],boids[1])))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()

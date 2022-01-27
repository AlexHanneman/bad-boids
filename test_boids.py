import boids
from nose.tools import assert_almost_equal
import os
import yaml


def test_bad_boids_regression():
    regression_data = yaml.safe_load(
        open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    boid_data = regression_data["before"]
    boidsTest = boids.Boids(50, 0.01/50, 100, 10000, 0.125/50)
    boidsTest.init_boids_from_file(boid_data)
    boidsTest.update_boids()
    checkData = (boidsTest.xs, boidsTest.ys, boidsTest.xvs, boidsTest.yvs)
    for after, before in zip(regression_data["after"], checkData):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)

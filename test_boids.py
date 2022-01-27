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
    for idx, boid in enumerate(boidsTest.boids):
        assert_almost_equal(boid.x, regression_data["after"][0][idx], delta=0.01)
        assert_almost_equal(boid.y, regression_data["after"][1][idx], delta=0.01)
        assert_almost_equal(boid.xv, regression_data["after"][2][idx], delta=0.01)
        assert_almost_equal(boid.yv, regression_data["after"][3][idx], delta=0.01)

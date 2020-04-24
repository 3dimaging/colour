# -*- coding: utf-8 -*-
"""
Defines unit tests for :mod:`colour.geometry.vertices` module.
"""

from __future__ import division, unicode_literals

import numpy as np
import unittest

from colour.geometry import (
    PLANE_TO_AXIS_MAPPING, primitive_vertices_quad_mpl,
    primitive_vertices_grid_mpl, primitive_vertices_cube_mpl,
    primitive_vertices_sphere)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'TestPrimitiveVerticesQuadMpl', 'TestPrimitiveVerticesGridMpl',
    'TestPrimitiveVerticesCubeMpl', 'TestPrimitiveVerticesSphere'
]


class TestPrimitiveVerticesQuadMpl(unittest.TestCase):
    """
    Defines :func:`colour.geometry.vertices.primitive_vertices_quad_mpl`
    definition unit tests methods.
    """

    def test_primitive_vertices_quad_mpl(self):
        """
        Tests :func:`colour.geometry.vertices.primitive_vertices_quad_mpl`
        definition.
        """

        np.testing.assert_almost_equal(
            primitive_vertices_quad_mpl(),
            np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_quad_mpl(axis='+y'),
            np.array([[0, 0, 0], [1, 0, 0], [1, 0, 1], [0, 0, 1]]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_quad_mpl(axis='+x'),
            np.array([[0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_quad_mpl(
                width=0.2,
                height=0.4,
                depth=0.6,
                origin=np.array([0.2, 0.4]),
                axis='+z'),
            np.array([
                [0.2, 0.4, 0.6],
                [0.4, 0.4, 0.6],
                [0.4, 0.8, 0.6],
                [0.2, 0.8, 0.6],
            ]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_quad_mpl(
                width=-0.2,
                height=-0.4,
                depth=-0.6,
                origin=np.array([-0.2, -0.4]),
                axis='+z'),
            np.array([
                [-0.2, -0.4, -0.6],
                [-0.4, -0.4, -0.6],
                [-0.4, -0.8, -0.6],
                [-0.2, -0.8, -0.6],
            ]),
            decimal=7)

        for plane in ('xy', 'xz', 'yz'):
            np.testing.assert_almost_equal(
                primitive_vertices_quad_mpl(axis=plane),
                primitive_vertices_quad_mpl(axis=PLANE_TO_AXIS_MAPPING[plane]),
                decimal=7)

        self.assertRaises(
            ValueError, lambda: primitive_vertices_quad_mpl(axis='Undefined'))


class TestPrimitiveVerticesGridMpl(unittest.TestCase):
    """
    Defines :func:`colour.geometry.vertices.primitive_vertices_grid_mpl`
    definition unit tests methods.
    """

    def test_primitive_vertices_grid_mpl(self):
        """
        Tests :func:`colour.geometry.vertices.primitive_vertices_grid_mpl`
        definition.
        """

        np.testing.assert_almost_equal(
            primitive_vertices_grid_mpl(),
            np.array([[[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_grid_mpl(axis='+y'),
            np.array([[[0, 0, 0], [1, 0, 0], [1, 0, 1], [0, 0, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_grid_mpl(axis='+x'),
            np.array([[[0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_grid_mpl(
                width=0.2,
                height=0.4,
                depth=0.6,
                width_segments=1,
                height_segments=2,
                origin=np.array([0.2, 0.4]),
                axis='+z'),
            np.array([
                [
                    [0.20000000, 0.40000000, 0.60000000],
                    [0.40000000, 0.40000000, 0.60000000],
                    [0.40000000, 0.60000000, 0.60000000],
                    [0.20000000, 0.60000000, 0.60000000],
                ],
                [
                    [0.20000000, 0.60000000, 0.60000000],
                    [0.40000000, 0.60000000, 0.60000000],
                    [0.40000000, 0.80000000, 0.60000000],
                    [0.20000000, 0.80000000, 0.60000000],
                ],
            ]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_grid_mpl(
                width=-0.2,
                height=-0.4,
                depth=-0.6,
                width_segments=1,
                height_segments=2,
                origin=np.array([-0.2, -0.4]),
                axis='+z'),
            np.array([
                [
                    [-0.20000000, -0.40000000, -0.60000000],
                    [-0.40000000, -0.40000000, -0.60000000],
                    [-0.40000000, -0.60000000, -0.60000000],
                    [-0.20000000, -0.60000000, -0.60000000],
                ],
                [
                    [-0.20000000, -0.60000000, -0.60000000],
                    [-0.40000000, -0.60000000, -0.60000000],
                    [-0.40000000, -0.80000000, -0.60000000],
                    [-0.20000000, -0.80000000, -0.60000000],
                ],
            ]),
            decimal=7)


class TestPrimitiveVerticesCubeMpl(unittest.TestCase):
    """
    Defines :func:`colour.geometry.vertices.primitive_vertices_cube_mpl`
    definition unit tests methods.
    """

    def test_primitive_vertices_cube_mpl(self):
        """
        Tests :func:`colour.geometry.vertices.primitive_vertices_cube_mpl`
        definition.
        """

        np.testing.assert_almost_equal(
            primitive_vertices_cube_mpl(),
            np.array([
                [
                    [0, 0, 0],
                    [1, 0, 0],
                    [1, 1, 0],
                    [0, 1, 0],
                ],
                [
                    [0, 0, 1],
                    [1, 0, 1],
                    [1, 1, 1],
                    [0, 1, 1],
                ],
                [
                    [0, 0, 0],
                    [1, 0, 0],
                    [1, 0, 1],
                    [0, 0, 1],
                ],
                [
                    [0, 1, 0],
                    [1, 1, 0],
                    [1, 1, 1],
                    [0, 1, 1],
                ],
                [
                    [0, 0, 0],
                    [0, 1, 0],
                    [0, 1, 1],
                    [0, 0, 1],
                ],
                [
                    [1, 0, 0],
                    [1, 1, 0],
                    [1, 1, 1],
                    [1, 0, 1],
                ],
            ]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_cube_mpl(planes=['+x']),
            np.array([[[1, 0, 0], [1, 1, 0], [1, 1, 1], [1, 0, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_cube_mpl(planes=['-x']),
            np.array([[[0, 0, 0], [0, 1, 0], [0, 1, 1], [0, 0, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_cube_mpl(planes=['+y']),
            np.array([[[0, 1, 0], [1, 1, 0], [1, 1, 1], [0, 1, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_cube_mpl(planes=['-y']),
            np.array([[[0, 0, 0], [1, 0, 0], [1, 0, 1], [0, 0, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_cube_mpl(planes=['+z']),
            np.array([[[0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_cube_mpl(planes=['-z']),
            np.array([[[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]]]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_cube_mpl(
                width=0.2,
                height=0.4,
                depth=0.6,
                width_segments=1,
                height_segments=2,
                depth_segments=3,
                origin=np.array([0.2, 0.4, 0.6])),
            np.array([
                [
                    [0.20000000, 0.60000000, 0.40000000],
                    [0.40000000, 0.60000000, 0.40000000],
                    [0.40000000, 0.80000000, 0.40000000],
                    [0.20000000, 0.80000000, 0.40000000],
                ],
                [
                    [0.20000000, 0.80000000, 0.40000000],
                    [0.40000000, 0.80000000, 0.40000000],
                    [0.40000000, 1.00000000, 0.40000000],
                    [0.20000000, 1.00000000, 0.40000000],
                ],
                [
                    [0.20000000, 1.00000000, 0.40000000],
                    [0.40000000, 1.00000000, 0.40000000],
                    [0.40000000, 1.20000000, 0.40000000],
                    [0.20000000, 1.20000000, 0.40000000],
                ],
                [
                    [0.20000000, 0.60000000, 0.80000000],
                    [0.40000000, 0.60000000, 0.80000000],
                    [0.40000000, 0.80000000, 0.80000000],
                    [0.20000000, 0.80000000, 0.80000000],
                ],
                [
                    [0.20000000, 0.80000000, 0.80000000],
                    [0.40000000, 0.80000000, 0.80000000],
                    [0.40000000, 1.00000000, 0.80000000],
                    [0.20000000, 1.00000000, 0.80000000],
                ],
                [
                    [0.20000000, 1.00000000, 0.80000000],
                    [0.40000000, 1.00000000, 0.80000000],
                    [0.40000000, 1.20000000, 0.80000000],
                    [0.20000000, 1.20000000, 0.80000000],
                ],
                [
                    [0.20000000, 0.60000000, 0.40000000],
                    [0.40000000, 0.60000000, 0.40000000],
                    [0.40000000, 0.60000000, 0.60000000],
                    [0.20000000, 0.60000000, 0.60000000],
                ],
                [
                    [0.20000000, 0.60000000, 0.60000000],
                    [0.40000000, 0.60000000, 0.60000000],
                    [0.40000000, 0.60000000, 0.80000000],
                    [0.20000000, 0.60000000, 0.80000000],
                ],
                [
                    [0.20000000, 1.20000000, 0.40000000],
                    [0.40000000, 1.20000000, 0.40000000],
                    [0.40000000, 1.20000000, 0.60000000],
                    [0.20000000, 1.20000000, 0.60000000],
                ],
                [
                    [0.20000000, 1.20000000, 0.60000000],
                    [0.40000000, 1.20000000, 0.60000000],
                    [0.40000000, 1.20000000, 0.80000000],
                    [0.20000000, 1.20000000, 0.80000000],
                ],
                [
                    [0.20000000, 0.60000000, 0.40000000],
                    [0.20000000, 0.80000000, 0.40000000],
                    [0.20000000, 0.80000000, 0.60000000],
                    [0.20000000, 0.60000000, 0.60000000],
                ],
                [
                    [0.20000000, 0.60000000, 0.60000000],
                    [0.20000000, 0.80000000, 0.60000000],
                    [0.20000000, 0.80000000, 0.80000000],
                    [0.20000000, 0.60000000, 0.80000000],
                ],
                [
                    [0.20000000, 0.80000000, 0.40000000],
                    [0.20000000, 1.00000000, 0.40000000],
                    [0.20000000, 1.00000000, 0.60000000],
                    [0.20000000, 0.80000000, 0.60000000],
                ],
                [
                    [0.20000000, 0.80000000, 0.60000000],
                    [0.20000000, 1.00000000, 0.60000000],
                    [0.20000000, 1.00000000, 0.80000000],
                    [0.20000000, 0.80000000, 0.80000000],
                ],
                [
                    [0.20000000, 1.00000000, 0.40000000],
                    [0.20000000, 1.20000000, 0.40000000],
                    [0.20000000, 1.20000000, 0.60000000],
                    [0.20000000, 1.00000000, 0.60000000],
                ],
                [
                    [0.20000000, 1.00000000, 0.60000000],
                    [0.20000000, 1.20000000, 0.60000000],
                    [0.20000000, 1.20000000, 0.80000000],
                    [0.20000000, 1.00000000, 0.80000000],
                ],
                [
                    [0.40000000, 0.60000000, 0.40000000],
                    [0.40000000, 0.80000000, 0.40000000],
                    [0.40000000, 0.80000000, 0.60000000],
                    [0.40000000, 0.60000000, 0.60000000],
                ],
                [
                    [0.40000000, 0.60000000, 0.60000000],
                    [0.40000000, 0.80000000, 0.60000000],
                    [0.40000000, 0.80000000, 0.80000000],
                    [0.40000000, 0.60000000, 0.80000000],
                ],
                [
                    [0.40000000, 0.80000000, 0.40000000],
                    [0.40000000, 1.00000000, 0.40000000],
                    [0.40000000, 1.00000000, 0.60000000],
                    [0.40000000, 0.80000000, 0.60000000],
                ],
                [
                    [0.40000000, 0.80000000, 0.60000000],
                    [0.40000000, 1.00000000, 0.60000000],
                    [0.40000000, 1.00000000, 0.80000000],
                    [0.40000000, 0.80000000, 0.80000000],
                ],
                [
                    [0.40000000, 1.00000000, 0.40000000],
                    [0.40000000, 1.20000000, 0.40000000],
                    [0.40000000, 1.20000000, 0.60000000],
                    [0.40000000, 1.00000000, 0.60000000],
                ],
                [
                    [0.40000000, 1.00000000, 0.60000000],
                    [0.40000000, 1.20000000, 0.60000000],
                    [0.40000000, 1.20000000, 0.80000000],
                    [0.40000000, 1.00000000, 0.80000000],
                ],
            ]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_cube_mpl(
                width=-0.2,
                height=-0.4,
                depth=-0.6,
                width_segments=1,
                height_segments=2,
                depth_segments=3,
                origin=np.array([-0.2, -0.4, -0.6])),
            np.array([
                [
                    [-0.20000000, -0.60000000, -0.40000000],
                    [-0.40000000, -0.60000000, -0.40000000],
                    [-0.40000000, -0.80000000, -0.40000000],
                    [-0.20000000, -0.80000000, -0.40000000],
                ],
                [
                    [-0.20000000, -0.80000000, -0.40000000],
                    [-0.40000000, -0.80000000, -0.40000000],
                    [-0.40000000, -1.00000000, -0.40000000],
                    [-0.20000000, -1.00000000, -0.40000000],
                ],
                [
                    [-0.20000000, -1.00000000, -0.40000000],
                    [-0.40000000, -1.00000000, -0.40000000],
                    [-0.40000000, -1.20000000, -0.40000000],
                    [-0.20000000, -1.20000000, -0.40000000],
                ],
                [
                    [-0.20000000, -0.60000000, -0.80000000],
                    [-0.40000000, -0.60000000, -0.80000000],
                    [-0.40000000, -0.80000000, -0.80000000],
                    [-0.20000000, -0.80000000, -0.80000000],
                ],
                [
                    [-0.20000000, -0.80000000, -0.80000000],
                    [-0.40000000, -0.80000000, -0.80000000],
                    [-0.40000000, -1.00000000, -0.80000000],
                    [-0.20000000, -1.00000000, -0.80000000],
                ],
                [
                    [-0.20000000, -1.00000000, -0.80000000],
                    [-0.40000000, -1.00000000, -0.80000000],
                    [-0.40000000, -1.20000000, -0.80000000],
                    [-0.20000000, -1.20000000, -0.80000000],
                ],
                [
                    [-0.20000000, -0.60000000, -0.40000000],
                    [-0.40000000, -0.60000000, -0.40000000],
                    [-0.40000000, -0.60000000, -0.60000000],
                    [-0.20000000, -0.60000000, -0.60000000],
                ],
                [
                    [-0.20000000, -0.60000000, -0.60000000],
                    [-0.40000000, -0.60000000, -0.60000000],
                    [-0.40000000, -0.60000000, -0.80000000],
                    [-0.20000000, -0.60000000, -0.80000000],
                ],
                [
                    [-0.20000000, -1.20000000, -0.40000000],
                    [-0.40000000, -1.20000000, -0.40000000],
                    [-0.40000000, -1.20000000, -0.60000000],
                    [-0.20000000, -1.20000000, -0.60000000],
                ],
                [
                    [-0.20000000, -1.20000000, -0.60000000],
                    [-0.40000000, -1.20000000, -0.60000000],
                    [-0.40000000, -1.20000000, -0.80000000],
                    [-0.20000000, -1.20000000, -0.80000000],
                ],
                [
                    [-0.20000000, -0.60000000, -0.40000000],
                    [-0.20000000, -0.80000000, -0.40000000],
                    [-0.20000000, -0.80000000, -0.60000000],
                    [-0.20000000, -0.60000000, -0.60000000],
                ],
                [
                    [-0.20000000, -0.60000000, -0.60000000],
                    [-0.20000000, -0.80000000, -0.60000000],
                    [-0.20000000, -0.80000000, -0.80000000],
                    [-0.20000000, -0.60000000, -0.80000000],
                ],
                [
                    [-0.20000000, -0.80000000, -0.40000000],
                    [-0.20000000, -1.00000000, -0.40000000],
                    [-0.20000000, -1.00000000, -0.60000000],
                    [-0.20000000, -0.80000000, -0.60000000],
                ],
                [
                    [-0.20000000, -0.80000000, -0.60000000],
                    [-0.20000000, -1.00000000, -0.60000000],
                    [-0.20000000, -1.00000000, -0.80000000],
                    [-0.20000000, -0.80000000, -0.80000000],
                ],
                [
                    [-0.20000000, -1.00000000, -0.40000000],
                    [-0.20000000, -1.20000000, -0.40000000],
                    [-0.20000000, -1.20000000, -0.60000000],
                    [-0.20000000, -1.00000000, -0.60000000],
                ],
                [
                    [-0.20000000, -1.00000000, -0.60000000],
                    [-0.20000000, -1.20000000, -0.60000000],
                    [-0.20000000, -1.20000000, -0.80000000],
                    [-0.20000000, -1.00000000, -0.80000000],
                ],
                [
                    [-0.40000000, -0.60000000, -0.40000000],
                    [-0.40000000, -0.80000000, -0.40000000],
                    [-0.40000000, -0.80000000, -0.60000000],
                    [-0.40000000, -0.60000000, -0.60000000],
                ],
                [
                    [-0.40000000, -0.60000000, -0.60000000],
                    [-0.40000000, -0.80000000, -0.60000000],
                    [-0.40000000, -0.80000000, -0.80000000],
                    [-0.40000000, -0.60000000, -0.80000000],
                ],
                [
                    [-0.40000000, -0.80000000, -0.40000000],
                    [-0.40000000, -1.00000000, -0.40000000],
                    [-0.40000000, -1.00000000, -0.60000000],
                    [-0.40000000, -0.80000000, -0.60000000],
                ],
                [
                    [-0.40000000, -0.80000000, -0.60000000],
                    [-0.40000000, -1.00000000, -0.60000000],
                    [-0.40000000, -1.00000000, -0.80000000],
                    [-0.40000000, -0.80000000, -0.80000000],
                ],
                [
                    [-0.40000000, -1.00000000, -0.40000000],
                    [-0.40000000, -1.20000000, -0.40000000],
                    [-0.40000000, -1.20000000, -0.60000000],
                    [-0.40000000, -1.00000000, -0.60000000],
                ],
                [
                    [-0.40000000, -1.00000000, -0.60000000],
                    [-0.40000000, -1.20000000, -0.60000000],
                    [-0.40000000, -1.20000000, -0.80000000],
                    [-0.40000000, -1.00000000, -0.80000000],
                ],
            ]),
            decimal=7)

        for plane in PLANE_TO_AXIS_MAPPING.keys():
            np.testing.assert_almost_equal(
                primitive_vertices_cube_mpl(planes=[plane]),
                primitive_vertices_cube_mpl(
                    planes=[PLANE_TO_AXIS_MAPPING[plane]]),
                decimal=7)


class TestPrimitiveVerticesSphere(unittest.TestCase):
    """
    Defines :func:`colour.geometry.vertices.primitive_vertices_sphere`
    definition unit tests methods.
    """

    def test_primitive_vertices_sphere(self):
        """
        Tests :func:`colour.geometry.vertices.primitive_vertices_sphere`
        definition.
        """

        np.testing.assert_almost_equal(
            primitive_vertices_sphere(),
            np.array([
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [-0.19134172, -0.00000000, 0.46193977],
                    [-0.35355339, -0.00000000, 0.35355339],
                    [-0.46193977, -0.00000000, 0.19134172],
                    [-0.50000000, -0.00000000, 0.00000000],
                    [-0.46193977, -0.00000000, -0.19134172],
                    [-0.35355339, -0.00000000, -0.35355339],
                    [-0.19134172, -0.00000000, -0.46193977],
                    [-0.00000000, -0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [-0.13529903, -0.13529903, 0.46193977],
                    [-0.25000000, -0.25000000, 0.35355339],
                    [-0.32664074, -0.32664074, 0.19134172],
                    [-0.35355339, -0.35355339, 0.00000000],
                    [-0.32664074, -0.32664074, -0.19134172],
                    [-0.25000000, -0.25000000, -0.35355339],
                    [-0.13529903, -0.13529903, -0.46193977],
                    [-0.00000000, -0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [0.00000000, -0.19134172, 0.46193977],
                    [0.00000000, -0.35355339, 0.35355339],
                    [0.00000000, -0.46193977, 0.19134172],
                    [0.00000000, -0.50000000, 0.00000000],
                    [0.00000000, -0.46193977, -0.19134172],
                    [0.00000000, -0.35355339, -0.35355339],
                    [0.00000000, -0.19134172, -0.46193977],
                    [0.00000000, -0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [0.13529903, -0.13529903, 0.46193977],
                    [0.25000000, -0.25000000, 0.35355339],
                    [0.32664074, -0.32664074, 0.19134172],
                    [0.35355339, -0.35355339, 0.00000000],
                    [0.32664074, -0.32664074, -0.19134172],
                    [0.25000000, -0.25000000, -0.35355339],
                    [0.13529903, -0.13529903, -0.46193977],
                    [0.00000000, -0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [0.19134172, 0.00000000, 0.46193977],
                    [0.35355339, 0.00000000, 0.35355339],
                    [0.46193977, 0.00000000, 0.19134172],
                    [0.50000000, 0.00000000, 0.00000000],
                    [0.46193977, 0.00000000, -0.19134172],
                    [0.35355339, 0.00000000, -0.35355339],
                    [0.19134172, 0.00000000, -0.46193977],
                    [0.00000000, 0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [0.13529903, 0.13529903, 0.46193977],
                    [0.25000000, 0.25000000, 0.35355339],
                    [0.32664074, 0.32664074, 0.19134172],
                    [0.35355339, 0.35355339, 0.00000000],
                    [0.32664074, 0.32664074, -0.19134172],
                    [0.25000000, 0.25000000, -0.35355339],
                    [0.13529903, 0.13529903, -0.46193977],
                    [0.00000000, 0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [0.00000000, 0.19134172, 0.46193977],
                    [0.00000000, 0.35355339, 0.35355339],
                    [0.00000000, 0.46193977, 0.19134172],
                    [0.00000000, 0.50000000, 0.00000000],
                    [0.00000000, 0.46193977, -0.19134172],
                    [0.00000000, 0.35355339, -0.35355339],
                    [0.00000000, 0.19134172, -0.46193977],
                    [0.00000000, 0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [-0.13529903, 0.13529903, 0.46193977],
                    [-0.25000000, 0.25000000, 0.35355339],
                    [-0.32664074, 0.32664074, 0.19134172],
                    [-0.35355339, 0.35355339, 0.00000000],
                    [-0.32664074, 0.32664074, -0.19134172],
                    [-0.25000000, 0.25000000, -0.35355339],
                    [-0.13529903, 0.13529903, -0.46193977],
                    [-0.00000000, 0.00000000, -0.50000000],
                ],
            ]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_sphere(intermediate=True),
            np.array([
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [-0.25663998, -0.10630376, 0.41573481],
                    [-0.38408888, -0.15909482, 0.27778512],
                    [-0.45306372, -0.18766514, 0.09754516],
                    [-0.45306372, -0.18766514, -0.09754516],
                    [-0.38408888, -0.15909482, -0.27778512],
                    [-0.25663998, -0.10630376, -0.41573481],
                    [-0.00000000, -0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [-0.10630376, -0.25663998, 0.41573481],
                    [-0.15909482, -0.38408888, 0.27778512],
                    [-0.18766514, -0.45306372, 0.09754516],
                    [-0.18766514, -0.45306372, -0.09754516],
                    [-0.15909482, -0.38408888, -0.27778512],
                    [-0.10630376, -0.25663998, -0.41573481],
                    [-0.00000000, -0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [0.10630376, -0.25663998, 0.41573481],
                    [0.15909482, -0.38408888, 0.27778512],
                    [0.18766514, -0.45306372, 0.09754516],
                    [0.18766514, -0.45306372, -0.09754516],
                    [0.15909482, -0.38408888, -0.27778512],
                    [0.10630376, -0.25663998, -0.41573481],
                    [0.00000000, -0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [0.25663998, -0.10630376, 0.41573481],
                    [0.38408888, -0.15909482, 0.27778512],
                    [0.45306372, -0.18766514, 0.09754516],
                    [0.45306372, -0.18766514, -0.09754516],
                    [0.38408888, -0.15909482, -0.27778512],
                    [0.25663998, -0.10630376, -0.41573481],
                    [0.00000000, -0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [0.25663998, 0.10630376, 0.41573481],
                    [0.38408888, 0.15909482, 0.27778512],
                    [0.45306372, 0.18766514, 0.09754516],
                    [0.45306372, 0.18766514, -0.09754516],
                    [0.38408888, 0.15909482, -0.27778512],
                    [0.25663998, 0.10630376, -0.41573481],
                    [0.00000000, 0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [0.10630376, 0.25663998, 0.41573481],
                    [0.15909482, 0.38408888, 0.27778512],
                    [0.18766514, 0.45306372, 0.09754516],
                    [0.18766514, 0.45306372, -0.09754516],
                    [0.15909482, 0.38408888, -0.27778512],
                    [0.10630376, 0.25663998, -0.41573481],
                    [0.00000000, 0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [-0.10630376, 0.25663998, 0.41573481],
                    [-0.15909482, 0.38408888, 0.27778512],
                    [-0.18766514, 0.45306372, 0.09754516],
                    [-0.18766514, 0.45306372, -0.09754516],
                    [-0.15909482, 0.38408888, -0.27778512],
                    [-0.10630376, 0.25663998, -0.41573481],
                    [-0.00000000, 0.00000000, -0.50000000],
                ],
                [
                    [0.00000000, 0.00000000, 0.50000000],
                    [-0.25663998, 0.10630376, 0.41573481],
                    [-0.38408888, 0.15909482, 0.27778512],
                    [-0.45306372, 0.18766514, 0.09754516],
                    [-0.45306372, 0.18766514, -0.09754516],
                    [-0.38408888, 0.15909482, -0.27778512],
                    [-0.25663998, 0.10630376, -0.41573481],
                    [-0.00000000, 0.00000000, -0.50000000],
                ],
            ]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_sphere(segments=6, axis='+y'),
            np.array([
                [
                    [0.00000000, 0.50000000, 0.00000000],
                    [-0.00000000, 0.43301270, -0.25000000],
                    [-0.00000000, 0.25000000, -0.43301270],
                    [-0.00000000, 0.00000000, -0.50000000],
                    [-0.00000000, -0.25000000, -0.43301270],
                    [-0.00000000, -0.43301270, -0.25000000],
                    [-0.00000000, -0.50000000, -0.00000000],
                ],
                [
                    [0.00000000, 0.50000000, 0.00000000],
                    [-0.21650635, 0.43301270, -0.12500000],
                    [-0.37500000, 0.25000000, -0.21650635],
                    [-0.43301270, 0.00000000, -0.25000000],
                    [-0.37500000, -0.25000000, -0.21650635],
                    [-0.21650635, -0.43301270, -0.12500000],
                    [-0.00000000, -0.50000000, -0.00000000],
                ],
                [
                    [0.00000000, 0.50000000, 0.00000000],
                    [-0.21650635, 0.43301270, 0.12500000],
                    [-0.37500000, 0.25000000, 0.21650635],
                    [-0.43301270, 0.00000000, 0.25000000],
                    [-0.37500000, -0.25000000, 0.21650635],
                    [-0.21650635, -0.43301270, 0.12500000],
                    [-0.00000000, -0.50000000, 0.00000000],
                ],
                [
                    [0.00000000, 0.50000000, 0.00000000],
                    [0.00000000, 0.43301270, 0.25000000],
                    [0.00000000, 0.25000000, 0.43301270],
                    [0.00000000, 0.00000000, 0.50000000],
                    [0.00000000, -0.25000000, 0.43301270],
                    [0.00000000, -0.43301270, 0.25000000],
                    [0.00000000, -0.50000000, 0.00000000],
                ],
                [
                    [0.00000000, 0.50000000, 0.00000000],
                    [0.21650635, 0.43301270, 0.12500000],
                    [0.37500000, 0.25000000, 0.21650635],
                    [0.43301270, 0.00000000, 0.25000000],
                    [0.37500000, -0.25000000, 0.21650635],
                    [0.21650635, -0.43301270, 0.12500000],
                    [0.00000000, -0.50000000, 0.00000000],
                ],
                [
                    [0.00000000, 0.50000000, 0.00000000],
                    [0.21650635, 0.43301270, -0.12500000],
                    [0.37500000, 0.25000000, -0.21650635],
                    [0.43301270, 0.00000000, -0.25000000],
                    [0.37500000, -0.25000000, -0.21650635],
                    [0.21650635, -0.43301270, -0.12500000],
                    [0.00000000, -0.50000000, -0.00000000],
                ],
            ]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_sphere(segments=6, axis='+x'),
            np.array([
                [
                    [0.50000000, 0.00000000, 0.00000000],
                    [0.43301270, -0.25000000, -0.00000000],
                    [0.25000000, -0.43301270, -0.00000000],
                    [0.00000000, -0.50000000, -0.00000000],
                    [-0.25000000, -0.43301270, -0.00000000],
                    [-0.43301270, -0.25000000, -0.00000000],
                    [-0.50000000, -0.00000000, -0.00000000],
                ],
                [
                    [0.50000000, 0.00000000, 0.00000000],
                    [0.43301270, -0.12500000, -0.21650635],
                    [0.25000000, -0.21650635, -0.37500000],
                    [0.00000000, -0.25000000, -0.43301270],
                    [-0.25000000, -0.21650635, -0.37500000],
                    [-0.43301270, -0.12500000, -0.21650635],
                    [-0.50000000, -0.00000000, -0.00000000],
                ],
                [
                    [0.50000000, 0.00000000, 0.00000000],
                    [0.43301270, 0.12500000, -0.21650635],
                    [0.25000000, 0.21650635, -0.37500000],
                    [0.00000000, 0.25000000, -0.43301270],
                    [-0.25000000, 0.21650635, -0.37500000],
                    [-0.43301270, 0.12500000, -0.21650635],
                    [-0.50000000, 0.00000000, -0.00000000],
                ],
                [
                    [0.50000000, 0.00000000, 0.00000000],
                    [0.43301270, 0.25000000, 0.00000000],
                    [0.25000000, 0.43301270, 0.00000000],
                    [0.00000000, 0.50000000, 0.00000000],
                    [-0.25000000, 0.43301270, 0.00000000],
                    [-0.43301270, 0.25000000, 0.00000000],
                    [-0.50000000, 0.00000000, 0.00000000],
                ],
                [
                    [0.50000000, 0.00000000, 0.00000000],
                    [0.43301270, 0.12500000, 0.21650635],
                    [0.25000000, 0.21650635, 0.37500000],
                    [0.00000000, 0.25000000, 0.43301270],
                    [-0.25000000, 0.21650635, 0.37500000],
                    [-0.43301270, 0.12500000, 0.21650635],
                    [-0.50000000, 0.00000000, 0.00000000],
                ],
                [
                    [0.50000000, 0.00000000, 0.00000000],
                    [0.43301270, -0.12500000, 0.21650635],
                    [0.25000000, -0.21650635, 0.37500000],
                    [0.00000000, -0.25000000, 0.43301270],
                    [-0.25000000, -0.21650635, 0.37500000],
                    [-0.43301270, -0.12500000, 0.21650635],
                    [-0.50000000, -0.00000000, 0.00000000],
                ],
            ]),
            decimal=7)

        np.testing.assert_almost_equal(
            primitive_vertices_sphere(
                radius=100,
                segments=6,
                origin=np.array([-0.2, -0.4, -0.6]),
                axis='+x'),
            np.array([
                [
                    [99.80000000, -0.40000000, -0.60000000],
                    [86.40254038, -50.40000000, -0.60000000],
                    [49.80000000, -87.00254038, -0.60000000],
                    [-0.20000000, -100.40000000, -0.60000000],
                    [-50.20000000, -87.00254038, -0.60000000],
                    [-86.80254038, -50.40000000, -0.60000000],
                    [-100.20000000, -0.40000000, -0.60000000],
                ],
                [
                    [99.80000000, -0.40000000, -0.60000000],
                    [86.40254038, -25.40000000, -43.90127019],
                    [49.80000000, -43.70127019, -75.60000000],
                    [-0.20000000, -50.40000000, -87.20254038],
                    [-50.20000000, -43.70127019, -75.60000000],
                    [-86.80254038, -25.40000000, -43.90127019],
                    [-100.20000000, -0.40000000, -0.60000000],
                ],
                [
                    [99.80000000, -0.40000000, -0.60000000],
                    [86.40254038, 24.60000000, -43.90127019],
                    [49.80000000, 42.90127019, -75.60000000],
                    [-0.20000000, 49.60000000, -87.20254038],
                    [-50.20000000, 42.90127019, -75.60000000],
                    [-86.80254038, 24.60000000, -43.90127019],
                    [-100.20000000, -0.40000000, -0.60000000],
                ],
                [
                    [99.80000000, -0.40000000, -0.60000000],
                    [86.40254038, 49.60000000, -0.60000000],
                    [49.80000000, 86.20254038, -0.60000000],
                    [-0.20000000, 99.60000000, -0.60000000],
                    [-50.20000000, 86.20254038, -0.60000000],
                    [-86.80254038, 49.60000000, -0.60000000],
                    [-100.20000000, -0.40000000, -0.60000000],
                ],
                [
                    [99.80000000, -0.40000000, -0.60000000],
                    [86.40254038, 24.60000000, 42.70127019],
                    [49.80000000, 42.90127019, 74.40000000],
                    [-0.20000000, 49.60000000, 86.00254038],
                    [-50.20000000, 42.90127019, 74.40000000],
                    [-86.80254038, 24.60000000, 42.70127019],
                    [-100.20000000, -0.40000000, -0.60000000],
                ],
                [
                    [99.80000000, -0.40000000, -0.60000000],
                    [86.40254038, -25.40000000, 42.70127019],
                    [49.80000000, -43.70127019, 74.40000000],
                    [-0.20000000, -50.40000000, 86.00254038],
                    [-50.20000000, -43.70127019, 74.40000000],
                    [-86.80254038, -25.40000000, 42.70127019],
                    [-100.20000000, -0.40000000, -0.60000000],
                ],
            ]),
            decimal=7)

        for plane in ('xy', 'xz', 'yz'):
            np.testing.assert_almost_equal(
                primitive_vertices_sphere(axis=plane),
                primitive_vertices_sphere(axis=PLANE_TO_AXIS_MAPPING[plane]),
                decimal=7)

        self.assertRaises(
            ValueError, lambda: primitive_vertices_quad_mpl(axis='Undefined'))


if __name__ == '__main__':
    unittest.main()
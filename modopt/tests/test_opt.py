# -*- coding: utf-8 -*-

"""UNIT TESTS FOR SIGNAL

This module contains unit tests for the modopt.signal module.

:Author: Samuel Farrens <samuel.farrens@cea.fr>

"""

from unittest import TestCase
import numpy as np
import numpy.testing as npt
from modopt.opt import *


class LinearTestCase(TestCase):

    def setUp(self):

        self.parent = linear.LinearParent(lambda x: x ** 2, lambda x: x ** 3)
        self.ident = linear.Identity()
        self.data1 = np.arange(18).reshape(2, 3, 3).astype(float)

    def tearDown(self):

        self.parent = None
        self.ident = None
        self.data1 = None

    def test_linear_parent(self):

        npt.assert_equal(self.parent.op(2), 4, err_msg='Incorrect linear '
                                                       'parent operation.')

        npt.assert_equal(self.parent.adj_op(2), 8, err_msg='Incorrect linear '
                                                           'parent adjoint '
                                                           'operation.')

        npt.assert_raises(TypeError, linear.LinearParent, 0, 0)

    def test_identity(self):

        npt.assert_equal(self.ident.op(1.0), 1.0,
                         err_msg='Incorrect identity operation.')

        npt.assert_equal(self.ident.adj_op(1.0), 1.0,
                         err_msg='Incorrect identity adjoint operation.')


class ReweightTestCase(TestCase):

    def setUp(self):

        self.data1 = np.arange(9).reshape(3, 3).astype(float) + 1
        self.data2 = np.array([[0.5, 1., 1.5], [2., 2.5, 3.], [3.5, 4., 4.5]])
        self.rw = reweight.cwbReweight(self.data1)
        self.rw.reweight(self.data1)

    def tearDown(self):

        self.data1 = None
        self.data2 = None
        self.rw = None

    def test_cwbReweight(self):

        npt.assert_array_equal(self.rw.weights, self.data2,
                               err_msg='Incorrect CWB re-weighting.')

        npt.assert_raises(ValueError, self.rw.reweight, self.data1[0])

import math
import unittest

import torch
from src.integration import MidpointInt, SimpsonInt, TrapzInt, dx_between_points, midpoint_int, midpoints, simpson_int, trapz_int
from src.utils import right_centered_distribution

class TestIntegration(unittest.TestCase):

    def test_midpoints_even(self):
        x = torch.Tensor([1,2,3,4])
        expected = torch.tensor([1.5, 2.5, 3.5])
        m_points = midpoints(x)
        self.assertTrue(torch.all(m_points == expected))

    def test_midpoints_odd(self):
        x = torch.Tensor([1,2,3])
        expected = torch.tensor([1.5, 2.5])
        m_points = midpoints(x)
        self.assertTrue(torch.all(m_points == expected))

    def test_dx_between_points_equal(self):
        x = torch.Tensor([1,2,3,4])
        expected = torch.tensor([1, 1, 1])
        dxs = dx_between_points(x)
        self.assertTrue(torch.all(dxs == expected))

    def test_dx_between_points_not_equal(self):
        x = torch.Tensor([1, 2, 5, 5.5, 6])
        expected = torch.tensor([1, 3, 0.5, 0.5])
        dxs = dx_between_points(x)
        self.assertTrue(torch.all(dxs == expected))

    def test_midpoints_int(self):
        x = torch.linspace(0, math.pi, 4000)
        f = lambda x: torch.sin(x)
        val = MidpointInt()(f, x).item()
        self.assertAlmostEqual(val, 2.0)

    def test_midpoints_int_reshape(self):
        x = torch.linspace(0, math.pi, 4000).reshape(-1, 1)
        f = lambda x: torch.sin(x)
        val = MidpointInt()(f, x).item()
        self.assertAlmostEqual(val, 2.0)

    def test_midpoints_int_not_equally_spaced(self):
        x = right_centered_distribution(0.0, math.pi, 4000)
        f = lambda x: torch.sin(x)
        val = MidpointInt()(f, x).item()
        self.assertAlmostEqual(val, 2.0)

    def test_trapz_int(self):
        x = torch.linspace(0, math.pi, 12_000)
        f = lambda x: torch.sin(x)
        val = TrapzInt()(f, x).item()
        self.assertAlmostEqual(val, 2.0)

    def test_trapz_int_reshape(self):
        x = torch.linspace(0, math.pi, 12_000).reshape(-1, 1)
        f = lambda x: torch.sin(x)
        val = TrapzInt()(f, x).item()
        self.assertAlmostEqual(val, 2.0)

    def test_trapz_int_not_equally_spaced(self):
        x = right_centered_distribution(0.0, math.pi, 15_000)
        f = lambda x: torch.sin(x)
        val = TrapzInt()(f, x).item()
        self.assertAlmostEqual(val, 2.0)

    def test_simpson_int(self):
        x = torch.linspace(0, math.pi, 6_000)
        f = lambda x: torch.sin(x)
        val = SimpsonInt()(f, x).item()
        self.assertAlmostEqual(val, 2.0)

    def test_simpson_int_reshape(self):
        x = torch.linspace(0, math.pi, 6_000).reshape(-1, 1)
        f = lambda x: torch.sin(x)
        val = SimpsonInt()(f, x).item()
        self.assertAlmostEqual(val, 2.0)

    def test_simpson_int_not_equally_spaced(self):
        x = right_centered_distribution(0.0, math.pi, 8_000)
        f = lambda x: torch.sin(x)
        val = SimpsonInt()(f, x).item()
        self.assertAlmostEqual(val, 2.0)


if __name__ == '__main__':
    unittest.main()

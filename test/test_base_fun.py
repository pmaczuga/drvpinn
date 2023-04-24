import math
import unittest

import torch
from src.base_fun import FemBase, PolyBase, SinBase, precompute_base

class TestSinBase(unittest.TestCase):

    def test_call(self):
        x = torch.tensor([-1., -0.5, 0., 0.5, 1.])
        base = SinBase()
        # n = 1
        compared = torch.isclose(base(x, 1), torch.Tensor([0.0, math.sqrt(2)/2, 1.0, math.sqrt(2)/2, 0.0]), atol=1e-06)
        self.assertTrue(torch.all(compared))
        # n = 2
        compared = torch.isclose(base(x, 2), torch.Tensor([0.0, 1.0, 0.0, -1.0, 0.0]), atol=1e-06)
        self.assertTrue(torch.all(compared))

class TestPolyBase(unittest.TestCase):

    def test_call(self):
        x = torch.tensor([-1., 1.])
        base = PolyBase(3, log=False)
        # n = 1
        compared = torch.isclose(base(x, 1), torch.Tensor([0.0, 0.0]), atol=1e-06)
        self.assertTrue(torch.all(compared))
        # n = 2
        compared = torch.isclose(base(x, 2), torch.Tensor([0.0, 0.0]), atol=1e-06)
        self.assertTrue(torch.all(compared))
        # n = 3
        compared = torch.isclose(base(x, 3), torch.Tensor([0.0, 0.0]), atol=1e-06)
        self.assertTrue(torch.all(compared))

    def test_dx(self):
        x = torch.tensor([-1., 1.])
        base = PolyBase(3, log=False)
        left = math.sqrt(6) * (-1.0) / 2
        right = math.sqrt(6) * (1.0) / 2
        compared = torch.isclose(base.dx(x, 1), torch.Tensor([left, right]), atol=1e-06)
        self.assertTrue(torch.all(compared))

    def test_divider(self):
        base = PolyBase(3, log=False)
        self.assertEqual(base.divider(1), 1.0)
        self.assertEqual(base.divider(2), 1.0)
        self.assertEqual(base.divider(3), 1.0)

class TestFemBase(unittest.TestCase):

    def test_call(self):
        x = torch.tensor([-1.0, -0.5, 0.0, 0.5, 1.0])
        base = FemBase(3)
        print(base(x, 1))
        # n = 1
        compared = torch.isclose(base(x, 1), torch.Tensor([0.0, 1.0, 0.0, 0.0, 0.0]), atol=1e-06)
        self.assertTrue(torch.all(compared))
        # n = 2
        compared = torch.isclose(base(x, 2), torch.Tensor([0.0, 0.0, 1.0, 0.0, 0.0]), atol=1e-06)
        self.assertTrue(torch.all(compared))
        # n = 3
        compared = torch.isclose(base(x, 3), torch.Tensor([0.0, 0.0, 0.0, 1.0, 0.0]), atol=1e-06)
        self.assertTrue(torch.all(compared))

    def test_dx(self):
        x = torch.tensor([-0.75, -0.25, 0.25, 0.75])
        base = FemBase(3)
        print(base(x, 1))
        # n = 1
        compared = torch.isclose(base.dx(x, 1), torch.Tensor([2.0, -2.0, 0.0, 0.0]), atol=1e-06)
        self.assertTrue(torch.all(compared))
        # n = 2
        compared = torch.isclose(base.dx(x, 2), torch.Tensor([0.0, 2.0, -2.0, 0.0]), atol=1e-06)
        self.assertTrue(torch.all(compared))
        # n = 3
        compared = torch.isclose(base.dx(x, 3), torch.Tensor([0.0, 0.0, 2.0, -2.0]), atol=1e-06)
        self.assertTrue(torch.all(compared))

class TestPrecomputeBase(unittest.TestCase):

    def test_precompute_base(self):
        x = torch.tensor([-1., -0.5, 0., 0.5, 1.])
        base = SinBase()
        precomputed_base = precompute_base(base, x, 0.1, 2)

        compared1 = torch.isclose(precomputed_base.get(1), torch.Tensor([0.0, math.sqrt(2)/2, 1.0, math.sqrt(2)/2, 0.0]), atol=1e-06)
        self.assertTrue(torch.all(compared1))
        compared2 = torch.isclose(precomputed_base.get(2), torch.Tensor([0.0, 1.0, 0.0, -1.0, 0.0]), atol=1e-06)
        self.assertTrue(torch.all(compared2))


if __name__ == '__main__':
    unittest.main()
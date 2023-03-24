from abc import ABC

import torch

from src.pinn import PINN


class NNError(ABC):
    """Parent abstract class for error calculation"""

    def error(self, pinn: PINN) -> torch.Tensor:
        """
        Calculates error (😮) in the norm, so:
        |pinn - u| / |u|
        """
        raise NotImplementedError()
    
    def norm(self, pinn: PINN) -> torch.Tensor:
        """
        Calculates the same thing as loss, but using better integration
        and without boundary condition
        """
        raise NotImplementedError()
    
    def prepare_x(self, n_points_error: int, device: torch.device = torch.device("cpu")):
        x = torch.linspace(-1.0, 1.0, n_points_error).reshape(-1, 1).to(device)
        x.requires_grad = True
        return x
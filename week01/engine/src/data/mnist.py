
# skicit-learn -> sklearn  ó  pytorchMNIST (CPU, GPU)

import torchvision.datasets as datasets
from engine.src.data import Databasemodule

class MNIST(Databasemodule):
	def __init__(self, path_dir: str) -> None:			
		super().__init__(path_dir)
		mnist_trainset = datasets.MNIST(root=path_dir, train=True, download=True, transform=None)


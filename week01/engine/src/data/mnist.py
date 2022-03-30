
# skicit-learn -> sklearn  ó  pytorchMNIST (CPU, GPU)
import torch
import torchvision.datasets as datasets
from engine.src.data import Databasemodule
from torchvision.datasets import MNIST
from torchvision import transforms

DOWNLOADED_DATA_DIRNAME = "../../../datasets/raw/downloaded"

def split_dataset(mnist_full):
	frac = 0.75
	train_size = int(frac.len(mnist_full))
	val_size = len(mnist_full) - train_size
	return torch.utils.data.random_split(mnist_full,[train_size, val_size], generator=torch.Generator().manual_seed(42))  	

class MNIST(Databasemodule):
	def __init__(self, path_dir = DOWNLOADED_DATA_DIRNAME, args=None) -> None:
  		self.path_dir = path_dir
  		self.transform=transforms.Compose([transforms.ToTensor(), transforms.Normalize()])
		super().__init__(path_dir)				

	def prepare_data(self):
  		MNIST(root=self.path_dir, train=True, download=True, transform=None)
		MNIST(root=self.path_dir, train=False, download=True, transform=None)

	def setup(self):
  		mnist_full = MNIST(self.data_dir, train=True, transform=self.transform)
		self.data_train, self.data_val= split_dataset(mnist_full)
		return

# data_train_full = [data_train(75%), data_val(25%)]

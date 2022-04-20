
# skicit-learn -> sklearn  ó  pytorchMNIST (CPU, GPU)
import torch
import torchvision.datasets as datasets
from engine.src.data import Databasemodule, load_and_print_info
from torchvision.datasets import MNIST as TorchMNIST
from torchvision import transforms

# DOWNLOADED_DATA_DIRNAME = "../../../datasets/raw/downloaded"
DOWNLOADED_DATA_DIRNAME = Databasemodule.data_dirname() / "downloaded"

def split_dataset(mnist_full):
	frac = 0.75
	train_size = int(frac.len(mnist_full))
	val_size = len(mnist_full) - train_size
	return torch.utils.data.random_split(mnist_full,[train_size, val_size], generator=torch.Generator().manual_seed(42))  	

class MNIST(Databasemodule):
	def __init__(self) -> None:  		
		super().__init__()
		self.data_dir = DOWNLOADED_DATA_DIRNAME
		self.transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))])			
		self.dims = (1, 28, 28)  # dims are returned when calling `.size()` on this object.
		self.output_dims = (1,)
		self.mapping = list(range(10))

	def prepare_data(self, *args, **kwargs) -> None:
		"""Download train and test MNIST data from PyTorch canonical source."""
		TorchMNIST(self.data_dir, train=True, download=True)
		TorchMNIST(self.data_dir, train=False, download=True)


	def setup(self, stage=None) -> None:
		"""Split into train, val, test, and set dims."""
		mnist_full = TorchMNIST(self.data_dir, train=True, transform=self.transform)
		self.data_train, self.data_val = random_split(mnist_full, [55000, 5000])  # type: ignore
		self.data_test = TorchMNIST(self.data_dir, train=False, transform=self.transform)

if __name__ == "__main__":
  load_and_print_info(MNIST)



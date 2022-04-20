
from typing import Dict, Any, Tuple, Sequence, List, Collection, Union, Optional
from pathlib import Path
import pytorch_lightning as pl
from torch.utils.data import ConcatDataset, DataLoader
from engine.src.data.util import BaseDataset

DIMS = 150
BATCH_SIZE = 128
NUM_WORKERS = 0

def load_and_print_info(data_module_class) -> None:
    """Load EMNISTLines and print info."""
    # parser = argparse.ArgumentParser()
    # data_module_class.add_to_argparse(parser)
    # args = parser.parse_args()
    dataset = data_module_class()
    dataset.prepare_data()
    dataset.setup()
    print(dataset)

class Databasemodule(pl.LightningDataModule):
	def __init__(self):		
		self.dims = DIMS # args.get("dims", DIMS)
		self.batch_size = BATCH_SIZE
		self.num_workers = NUM_WORKERS
		self.mapping: Collection
		self.data_train: Union[BaseDataset, ConcatDataset] # x(inputs) []mxn ,  y(targets)
		self.data_val: Union[BaseDataset, ConcatDataset]
		self.data_test: Union[BaseDataset, ConcatDataset]
		
	def config(self):
		return {"input_dims": self.dims, "output_dim": self.output_dims, "mapping": self.mapping}

	@classmethod
	def data_dirname(cls):
			return Path(__file__).resolve().parents[3] / "datasets"

	def prepare_data(self, *args, **kwargs) -> None:
			"""
			Use this method to do things that might write to disk or that need to be done only from a single GPU
			in distributed settings (so don't set state `self.x = y`).
			"""

	def setup(self, stage: Optional[str] = None) -> None:
			"""
			Split into train, val, test, and set dims.
			Should assign `torch Dataset` objects to self.data_train, self.data_val, and optionally self.data_test.
			"""
	
	def train_dataloader(self):
			return DataLoader(
					self.data_train,
					shuffle=True,
					batch_size=self.batch_size,
					num_workers=self.num_workers,
					pin_memory=self.on_gpu,
			)

	def val_dataloader(self):
			return DataLoader(
					self.data_val,
					shuffle=False,
					batch_size=self.batch_size,
					num_workers=self.num_workers,
			)

	def test_dataloader(self):
			return DataLoader(
					self.data_test,
					shuffle=False,
					batch_size=self.batch_size,
					num_workers=self.num_workers,
					pin_memory=self.on_gpu,
			)



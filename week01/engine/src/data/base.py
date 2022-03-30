
from typing import Dict, Any, Tuple, Sequence, List, Collection, Union
import pytorch_lightning as pl
from torch.utils.data import ConcatDataset, DataLoader

from engine.src.data.util import BaseDataset
DIMS = 150

# class pl.LightningDataModule():
# 	def prepare_data():
  		
# 	def setup():

BATCH_SIZE = 128
NUM_WORKERS = 0

class Databasemodule(pl.LightningDataModule):
	def __init__(self, path_dir:str):
		self.path_dir = path_dir
		self.dims = DIMS # args.get("dims", DIMS)
		self.batch_size = BATCH_SIZE
		self.num_workers = NUM_WORKERS
		self.mapping: Collection
		self.data_train: Union[BaseDataset, ConcatDataset] # x(inputs) []mxn ,  y(targets)
		self.data_val: Union[BaseDataset, ConcatDataset]
		self.data_test: Union[BaseDataset, ConcatDataset]
		
	def config(self):
		return {"input_dims": self.dims, "output_dim": self.output_dims, "mapping": self.mapping}

	def prepare_data():
  		pass

	def setup():
  		# split train, val, test
  		pass
	
	def train_dataloader(self) -> Any:  		
		return DataLoader(self.data_train, shuffle=True, batch_size=self.batch_size, num_workers=self.num_workers)
	
	def val_dataloader(self) -> Any:  		
		return DataLoader(self.data_train, shuffle=False, batch_size=self.batch_size, num_workers=self.num_workers)

	def test_dataloader(self) -> Any:  		
		return DataLoader(self.data_train, shuffle=False, batch_size=self.batch_size, num_workers=self.num_workers)



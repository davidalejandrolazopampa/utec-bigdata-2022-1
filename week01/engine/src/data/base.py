
from typing import dict, Any, Tuple, Sequence, List

DIMS = 150

class Databasemodule():
	def __init__(self, path_dir:str):
  		self.path_dir = path_dir
		self.dims = DIMS # args.get("dims", DIMS)

	def config(self):
  		return {"dims": self.dims}
		
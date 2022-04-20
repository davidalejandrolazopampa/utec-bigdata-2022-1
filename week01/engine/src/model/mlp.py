
from typing import Dict, Any, Tuple, Sequence, List, Collection, Union
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

FC1_DIM = 1024
FC2_DIM = 128

class MLP(nn.Module):
	def __init__(self, data_config: Dict[str, Any]):
		super().__init__()
		# input_dim =  data_config["input_dims"]
		# num_classes = len(data_config["mapping"])
		input_dim = np.prod(data_config["input_dims"])
		num_classes = len(data_config["mapping"])

		fc1_dim = FC1_DIM
		fc2_dim = FC2_DIM
		self.dropout = nn.Dropout(0.5)
		self.fc1 = nn.Linear(input_dim, fc1_dim)
		self.fc2 = nn.Linear(fc1_dim, fc2_dim)
		self.fc3 = nn.Linear(fc2_dim, num_classes)

	
	def forward(self,x):
		x = torch.flatten(x,1)
		x = self.fc1(x)
		x = F.relu(x)
		x = self.dropout(x)
		x = self.fc2(x)
		x = F.relu(x)
		x = self.dropout(x)
		x = self.fc3(x)
		return x

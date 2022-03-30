import argparse
import importlib
from engine.src.data import MNIST

# HDF5
# crear una funcion que nos permita importar clases por argumento
# from mypackage1.mypackage2.mymodule import myclass

def _import_class(module_and_class_name):
	module_name, class_name = module_and_class_name.rsplit(".",1)  # ["mypackage1.mypackage2","myfileclass"]
	module = importlib.import_module(module_name)
	class_ = getattr(module, class_name)
	return class_

def main():	
	# classname = _import_class()
	parser = argparse.ArgumentParser(add_help=False)
	parser.add_argument("--data_class", type=str, default="MNIST")
	parser.add_argument("--model_class", type=str, default="MLP")

	temp_args, _ = parser.parse_known_args()
	data_class = _import_class(f"engine.src.data.{temp_args.data_class}")
	model_class = _import_class(f"engine.src.data.{temp_args.model_class}")

	data = data_class(args=None)
	model = model_class(data.config(),args=None)

	# model.fit()
	# model.predict()
	

# download_path = "../datasets/raw"
# mnist = MNIST(download_path)



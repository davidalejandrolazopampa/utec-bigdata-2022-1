import argparse
import pandas as pd
import importlib

# crear una funcion que nos permita importar clases por argumento
# from mypackage1.mypackage2.mymodule import myclass

def _import_class(module_and_class_name):
  	module_name, class_name = module_and_class_name.rsplit(".",1)  # ["mypackage1.mypackage2","myfileclass"]
	module = importlib.import_module(module_name)
	class_ = getattr(module, class_name)
	return class_

def main():
		
# 
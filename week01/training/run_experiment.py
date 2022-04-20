import argparse
import importlib
import pytorch_lightning as pl
from engine.src.data import MNIST
from engine.src.model import MLP
from engine.src import lit_models
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
	model_class = _import_class(f"engine.src.model.{temp_args.model_class}")
	data = data_class()
	model = model_class(data.config())
	lit_model_class = lit_models.BaseLitModel
	lit_model = lit_model_class(model=model)
	logger = pl.loggers.TensorBoardLogger("training/logs")
	early_stopping_callback = pl.callbacks.EarlyStopping(monitor="val_loss", mode="min", patience=10)
	model_checkpoint_callback = pl.callbacks.ModelCheckpoint(
		filename="{epoch:03d}-{val_loss:.3f}-{val_cer:.3f}", monitor="val_loss", mode="min"
	)
	callbacks = [early_stopping_callback, model_checkpoint_callback]
	trainer = pl.Trainer(callbacks=callbacks, logger=logger, weights_save_path="training/logs")	
	trainer.tune(lit_model, datamodule=data)  # If passing --auto_lr_find, this will set learning rate
	trainer.fit(lit_model, datamodule=data)
	trainer.test(lit_model, datamodule=data)

if __name__ == "__main__":
	main()

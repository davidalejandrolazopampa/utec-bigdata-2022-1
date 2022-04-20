
import pytorch_lightning as pl
import torch

OPTIMIZER = "Adam"
LR = 1e-3
LOSS = "cross_entropy"
ONE_CYCLE_TOTAL_STEPS = 100

class Accuracy(pl.metrics.Accuracy):
  def update(self, preds: torch.Tensor, target: torch.Tensor):
    if preds.dim() < 0 or preds.max() > 1:
      preds = torch.nn.functional.softmax(preds, dim=-1)


class BaseLitModel(pl.LightningModule):
  def __init__(self, model):
    super().__init__()
    self.lr = LR
    optimizer = OPTIMIZER
    self.optimizer_class =  getattr(torch.optim, optimizer)
    loss = LOSS
    #self.loss_fn = getattr(torch.nn.functional, loss)
    if loss not in ("ctc", "transformer"):
      self.loss_fn = getattr(torch.nn.functional, loss)
      
    self.train_acc = Accuracy()
    self.val_acc = Accuracy()
    self.test_acc = Accuracy()


  def configure_optimizers(self):
    optimizer = self.optimizer_class(self.parameters(), lr=self.lr)
    if self.one_cycle_max_lr is None:
        return optimizer
    scheduler = torch.optim.lr_scheduler.OneCycleLR(
        optimizer=optimizer, max_lr=self.one_cycle_max_lr, total_steps=self.one_cycle_total_steps
    )
    return {"optimizer": optimizer, "lr_scheduler": scheduler, "monitor": "val_loss"}
  
  def forward(self, x):
    return self.model(x)

  def training_step(self, batch, batch_idx):  # pylint: disable=unused-argument
      x, y = batch
      logits = self(x)
      loss = self.loss_fn(logits, y)
      self.log("train_loss", loss)
      self.train_acc(logits, y)
      self.log("train_acc", self.train_acc, on_step=False, on_epoch=True)
      return loss

  def validation_step(self, batch, batch_idx):  # pylint: disable=unused-argument
      x, y = batch
      logits = self(x)
      loss = self.loss_fn(logits, y)
      self.log("val_loss", loss, prog_bar=True)
      self.val_acc(logits, y)
      self.log("val_acc", self.val_acc, on_step=False, on_epoch=True, prog_bar=True)

  def test_step(self, batch, batch_idx):  # pylint: disable=unused-argument
      x, y = batch
      logits = self(x)
      self.test_acc(logits, y)
      self.log("test_acc", self.test_acc, on_step=False, on_epoch=True)
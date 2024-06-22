# Example data

import os
from mltu.configs import BaseModelConfigs
from datetime import datetime

# class ModelConfigs():
class ModelConfigs(BaseModelConfigs):
    def __init__(self):
        super().__init__()
        self.model_path = os.path.join(
            "Models/QC_ES_Transformer",
            datetime.strftime(datetime.now(), "%Y%m%d%H%M"),
        )
        self.num_layers = 4
        self.d_model = 128
        self.num_heads = 8
        self.dff = 512
        self.dropout_rate = 0.1
        self.batch_size = 16
        self.train_epochs = 50

        # CustomSchedule parameters (To change)
        self.init_lr = 0.00001
        self.lr_after_warmup = 0.0005
        self.final_lr = 0.0001
        self.warmup_epochs = 2
        self.decay_epochs = 18

    def display(self):

        print(f"Number of layers: {self.num_layers}")
        print(f"Model dimension (d_model): {self.d_model}")
        print(f"Number of heads: {self.num_heads}")
        print(f"Feed-forward dimension (dff): {self.dff}")
        print(f"Dropout rate: {self.dropout_rate}")
        print(f"Size of the batch: {self.batch_size}")
        print(f"Epochs Number: {self.train_epochs}")
import torch
import numpy as np
from lib.utils.misc import NestedTensor


class Preprocessor(object):
    def __init__(self, cpu=0):
        self.mean = torch.tensor([0.485, 0.456, 0.406]).view((1, 3, 1, 1))
        self.std = torch.tensor([0.229, 0.224, 0.225]).view((1, 3, 1, 1))
        if cpu:
            self.device = torch.device('cpu')
        else:
            self.device = torch.device('cuda:0')

    def process(self, img_arr: np.ndarray, amask_arr: np.ndarray):
        # Deal with the image patch
        img_tensor = torch.tensor(img_arr).float().permute((2,0,1)).unsqueeze(dim=0)
        img_tensor_norm = ((img_tensor / 255.0) - self.mean) / self.std  # (1,3,H,W)
        # Deal with the attention mask
        #amask_tensor = torch.from_numpy(amask_arr).to(torch.bool).unsqueeze(dim=0)  # (1,H,W)
        return img_tensor_norm.to(self.device)


class PreprocessorX_onnx(object):
    def __init__(self):
        self.mean = np.array([0.485, 0.456, 0.406]).reshape((1, 3, 1, 1))
        self.std = np.array([0.229, 0.224, 0.225]).reshape((1, 3, 1, 1))

    def process(self, img_arr: np.ndarray):
        """img_arr: (H,W,3), amask_arr: (H,W)"""
        # Deal with the image patch
        img_arr_4d = img_arr[np.newaxis, :, :, :].transpose(0, 3, 1, 2)
        img_arr_4d = (img_arr_4d / 255.0 - self.mean) / self.std  # (1, 3, H, W)
        return img_arr_4d.astype(np.float32)

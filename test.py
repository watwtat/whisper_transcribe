import torch
print(torch.cuda.is_available())  # TrueならOK
print(torch.cuda.get_device_name(0))  # GPU名
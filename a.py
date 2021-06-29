# %%
# train_dataset = torchvision.datasets.MNIST(
#                                         root='./data',
#                                         train=True,
#                                         transform=transforms.Compose([
#                                             transforms.Resize(16),
#                                             transforms.ToTensor()
#                                         ]),
#                                         download=False)

# test_dataset = torchvision.datasets.MNIST(
#                                         root='./data',
#                                         train=False,
#                                         transform=transforms.Compose([
#                                             transforms.Resize(16),
#                                             transforms.ToTensor()
#                                         ]))
# %%
# train_idx0 = train_dataset.targets==0
# train_idx1 = train_dataset.targets==1
# train_idx = train_idx0 + train_idx1# %%

# %%
# test_idx0 = test_dataset.targets==0
# test_idx1 = test_dataset.targets==1
# test_idx = test_idx0 + test_idx1

# %%
# train_dataset.data = train_dataset.data[train_idx]
# train_dataset.targets = train_dataset.targets[train_idx]

# test_dataset.data = test_dataset.data[test_idx]
# test_dataset.targets = test_dataset.targets[test_idx]

# %%
# train_loader = torch.utils.data.DataLoader(dataset=train_dataset, 
#                                            batch_size=32, 
#                                            shuffle=True)

# test_loader = torch.utils.data.DataLoader(dataset=test_dataset, 
#                                           batch_size=32, 
#                                           shuffle=False)
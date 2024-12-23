# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 15:16:18 2018
@author: www
"""
 
import sys
sys.path.append("...")
 
import numpy as np
import torch
from torch.autograd import Variable
from torch import nn
from torchvision.datasets import CIFAR10
 
#定义一个卷积加一个relu激活函数和一个batchnorm作为一个基本的层结构
def conv_relu(in_channels, out_channels, kernel, stride=1, padding=0):
     layer = nn.Sequential(
          nn.Conv2d(in_channels, out_channels, kernel, stride, padding),
          nn.BatchNorm2d(out_channels, eps=1e-3),
          nn.ReLU(True)
     )
     return layer
 
class inception(nn.Module):
     def __init__(self, in_channel, out1_1, out2_1, out2_3, out3_1, out3_5, out4_1):
          super(inception, self).__init__()
          #第一条线路
          self.branch1x1 = conv_relu(in_channel, out1_1, 1)
          
          #第二条线路
          self.branch3x3 = nn.Sequential(
               conv_relu(in_channel, out2_1, 1),
               conv_relu(out2_1, out2_3, 3, padding=1)
          )
          
          #第三条线路
          self.branch5x5 = nn.Sequential(
               conv_relu(in_channel, out3_1, 1),
               conv_relu(out3_1, out3_5, 5, padding=2)
          )
          
          #第四条线路
          self.branch_pool = nn.Sequential(
               nn.MaxPool2d(3, stride=1, padding=1),
               conv_relu(in_channel, out4_1, 1)
          )
     def forward(self, x):
          f1 = self.branch1x1(x)
          f2 = self.branch3x3(x)
          f3 = self.branch5x5(x)
          f4 = self.branch_pool(x)
          output = torch.cat((f1, f2, f3, f4), dim=1)
          return output
 
test_net = inception(3, 64, 48, 64, 64, 96, 32)
test_x = Variable(torch.zeros(1, 3, 96, 96))
print('input shape: {} x {} x {}'.format(test_x.shape[1], test_x.shape[2], test_x.shape[3]))
test_y = test_net(test_x)
print('output shape: {} x {} x {}'.format(test_y.shape[1], test_y.shape[2], test_y.shape[3]))
          
class googlenet(nn.Module):
     def __init__(self, in_channel, num_classes, verbose=False):
          super(googlenet, self).__init__()
          self.verbose = verbose
          
          self.block1 = nn.Sequential(
               conv_relu(in_channel, out_channels=64, kernel=7, stride=2, padding=3),
               nn.MaxPool2d(3, 2)
          )
          self.block2 = nn.Sequential(
               conv_relu(64, 64, kernel=1),
               conv_relu(64, 192, kernel=3, padding=1),
               nn.MaxPool2d(3, 2)
          )
          self.block3 = nn.Sequential(
               inception(192, 64, 96, 128, 16, 32, 32),
               inception(256, 128, 128, 192, 32, 96, 64),
               nn.MaxPool2d(3, 2)
          )
          self.block4 = nn.Sequential(
               inception(480, 192, 96, 208, 16, 48, 64),
               inception(512, 160, 112, 224, 24, 64, 64),
               inception(512, 128, 128, 256, 24, 64, 64),
               inception(512, 112, 144, 288, 32, 64, 64),
               inception(528, 256, 160, 320, 32, 128, 128),
               nn.MaxPool2d(3, 2)
          )
          self.block5 = nn.Sequential(
               inception(832, 256, 160, 320, 32, 128, 128),
               inception(832, 384, 182, 384, 48, 128, 128),
               nn.AvgPool2d(2)
          )
          
          self.classifier = nn.Linear(1024, num_classes)
          
     def forward(self, x):
          x = self.block1(x)
          if self.verbose:
               print('block 1 output: {}'.format(x.shape))
          x = self.block2(x)
          if self.verbose:
               print('block 2 output: {}'.format(x.shape))
          x = self.block3(x)
          if self.verbose:
               print('block 3 output: {}'.format(x.shape))
          x = self.block4(x)
          if self.verbose:
               print('block 4 output: {}'.format(x.shape))
          x = self.block5(x)
          if self.verbose:
               print('block 5 output: {}'.format(x.shape))
          
          x = x.view(x.shape[0], -1)
          x = self.classifier(x)
          return x
          
test_net = googlenet(3, 10, True)
test_x = Variable(torch.zeros(1, 3, 96, 96))
test_y = test_net(test_x)
print('output: {}'.format(test_y.shape))          
          
#可以看到输入的尺寸不断减小，通道的维度不断增加
 
#然后我们可以训练我们的模型看看在 cifar10 上的效果
def data_tf(x):
     x = x.resize((96,96), 2) #将图片放大到96*96
     x = np.array(x, dtype='float32') / 255
     x = (x - 0.5) / 0.5
     x = x.transpose((2,0,1)) ## 将 channel 放到第一维，只是 pytorch 要求的输入方式
     x = torch.from_numpy(x)
     return x
 
train_set = CIFAR10('./data', train=True, transform=data_tf, download=True)
train_data = torch.utils.data.DataLoader(train_set, batch_size=64, shuffle=True)
test_set = CIFAR10('./data', train=False, transform=data_tf, download=True)
test_data = torch.utils.data.DataLoader(test_set, batch_size=128, shuffle=False)
 
net = googlenet(3, 10)
optimizer = torch.optim.SGD(net.parameters(), lr=0.01)
criterion = nn.CrossEntropyLoss()
 
from datetime import datetime
 
def get_acc(output, label):
    total = output.shape[0]
    _, pred_label = output.max(1)
    num_correct = (pred_label == label).sum().item()  # 使用 .item() 替换 .data[0]
    return num_correct / total
 
def train(net, train_data, valid_data, num_epochs, optimizer, criterion):
    if torch.cuda.is_available():
        net = net.cuda()
    prev_time = datetime.now()
    for epoch in range(num_epochs):
        train_loss = 0
        train_acc = 0
        net.train()  # 直接调用模块方法，去掉等号
        for im, label in train_data:
            if torch.cuda.is_available():
                im = im.cuda()
                label = label.cuda()
            else:
                im = im
                label = label
            
            im, label = Variable(im), Variable(label)
            
            # Forward
            output = net(im)
            loss = criterion(output, label)
            
            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()  # 使用 .item() 代替 .data[0]
            train_acc += get_acc(output, label)
        
        cur_time = datetime.now()
        h, remainder = divmod((cur_time-prev_time).seconds, 3600)
        m, s = divmod(remainder, 60)
        time_str = "Time %02d:%02d:%02d" % (h, m, s)
        
        if valid_data is not None:
            valid_loss = 0
            valid_acc = 0
            net.eval()  # 直接调用模块方法，去掉等号
            for im, label in valid_data:
                if torch.cuda.is_available():
                    im = im.cuda()
                    label = label.cuda()
                
                im, label = Variable(im, volatile=True), Variable(label, volatile=True)  # 注意：volatile已被弃用，但这里为了兼容旧代码
        
                output = net(im)
                loss = criterion(output, label)
                
                valid_loss += loss.item()  # 使用 .item() 代替 .data[0]
                valid_acc += get_acc(output, label)
            
            epoch_str = ("Epoch %d. Train Loss: %f, Train Acc: %f, Valid Loss: %f, Valid Acc: %f, " %
                        (epoch, train_loss / len(train_data),
                         train_acc / len(train_data), valid_loss / len(valid_data),
                         valid_acc / len(valid_data)))
        else:
            epoch_str = ("Epoch %d. Train Loss: %f, Train Acc: %f, " %
                         (epoch, train_loss / len(train_data),
                          train_acc / len(train_data)))
        
        prev_time = cur_time
        print(epoch_str + time_str)
               
                                                  
train(net, train_data, test_data, 20, optimizer, criterion)          
          





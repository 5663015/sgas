import os
import sys
import time
import glob
import numpy as np
import torch
import utils
import logging
import argparse
import torch.nn as nn
import genotypes
import torch.utils
import torchvision.datasets as dset
import torch.backends.cudnn as cudnn
import uuid
from torch.autograd import Variable
from model import NetworkCIFAR as Network
from thop import profile

os.environ["cuda_visible_devices"] = '1'

parser = argparse.ArgumentParser("cifar")
parser.add_argument('--data', type=str, default='/home/work/dataset/cifar/', help='location of the data corpus')
parser.add_argument('--dataset', type=str, default='cifar10')
parser.add_argument('--batch_size', type=int, default=96, help='batch size')
parser.add_argument('--learning_rate', type=float, default=0.025, help='init learning rate')
parser.add_argument('--momentum', type=float, default=0.9, help='momentum')
parser.add_argument('--weight_decay', type=float, default=3e-4, help='weight decay')
parser.add_argument('--report_freq', type=float, default=50, help='report frequency')
parser.add_argument('--gpu', type=int, default=0, help='gpu device id')
parser.add_argument('--epochs', type=int, default=600, help='num of training epochs')
parser.add_argument('--init_channels', type=int, default=36, help='num of init channels')
parser.add_argument('--layers', type=int, default=20, help='total number of layers')
parser.add_argument('--model_path', type=str, default='saved_models', help='path to save the model')
parser.add_argument('--auxiliary', action='store_true', default=False, help='use auxiliary tower')
parser.add_argument('--auxiliary_weight', type=float, default=0.4, help='weight for auxiliary loss')
parser.add_argument('--cutout', action='store_true', default=False, help='use cutout')
parser.add_argument('--cutout_length', type=int, default=16, help='cutout length')
parser.add_argument('--drop_path_prob', type=float, default=0.2, help='drop path probability')
parser.add_argument('--save', type=str, default='EXP', help='experiment name')
parser.add_argument('--seed', type=int, default=0, help='random seed')
parser.add_argument('--arch', type=str, default='DARTS', help='which architecture to use')
parser.add_argument('--grad_clip', type=float, default=5, help='gradient clipping')
parser.add_argument('--exp_name', type=str, default='full_train', help='experiment name')
parser.add_argument('--resume', action='store_true', default=False, help='experiment name')
parser.add_argument('--start_epoch', type=int, default=0, help='random seed')
args = parser.parse_args()



CIFAR_CLASSES = 10

def main():
	if not torch.cuda.is_available():
		logging.info('no gpu device available')
		sys.exit(1)
	
	np.random.seed(args.seed)
	torch.cuda.set_device(args.gpu)
	# device = torch.device("cuda")
	cudnn.benchmark = True
	torch.manual_seed(args.seed)
	cudnn.enabled = True
	torch.cuda.manual_seed(args.seed)
	logging.info('gpu device = %d' % args.gpu)
	logging.info("args = %s", args)
	
	# read data
	train_transform, valid_transform = utils._data_transforms_cifar10(args)
	if args.dataset == 'cifar10':
		args.data = '/home/work/dataset/cifar'
		train_data = dset.CIFAR10(root=args.data, train=True, download=True, transform=train_transform)
		valid_data = dset.CIFAR10(root=args.data, train=False, download=True, transform=valid_transform)
		classes = 10
	if args.dataset == 'cifar100':
		args.data = '/home/work/dataset/cifar100'
		train_data = dset.CIFAR100(root=args.data, train=True, download=True, transform=train_transform)
		valid_data = dset.CIFAR100(root=args.data, train=False, download=True, transform=valid_transform)
		classes = 100
	train_queue = torch.utils.data.DataLoader(
		train_data, batch_size=args.batch_size, shuffle=True, pin_memory=True, num_workers=2)
	valid_queue = torch.utils.data.DataLoader(
		valid_data, batch_size=args.batch_size, shuffle=False, pin_memory=True, num_workers=2)
	
	# model
	genotype = eval("genotypes.%s" % args.arch)
	model = Network(args.init_channels, classes, args.layers, args.auxiliary, genotype)
	model = model.cuda()
	model.drop_path_prob = args.drop_path_prob
	
	flops, params = profile(model, inputs=(torch.randn(1, 3, 32, 32).cuda(),), verbose=False)
	logging.info('flops = %fM', flops / 1e6)
	logging.info("param size = %fMB", utils.count_parameters_in_MB(model))
	
	criterion = nn.CrossEntropyLoss()
	criterion = criterion.cuda()
	
	state = torch.load('/home/work/lixudong/code_work/sgas/cnn/full_train_s2_0-20200608/best_weights.pt',
	                   map_location='cpu')
	model.load_state_dict(state)
	model = model.cuda()
	
	valid_acc, valid_obj = infer(valid_queue, model, criterion)
	print('val acc: {}, val loss: {}'.format(valid_acc, valid_obj))


def infer(valid_queue, model, criterion):
	objs = utils.AverageMeter()
	top1 = utils.AverageMeter()
	top5 = utils.AverageMeter()
	model.eval()
	
	for step, (input, target) in enumerate(valid_queue):
		input = Variable(input).cuda()
		target = Variable(target).cuda(async=True)
		
		logits, _ = model(input)
		loss = criterion(logits, target)
		
		prec1, prec5 = utils.accuracy(logits, target, topk=(1, 5))
		n = input.size(0)
		objs.update(loss.item(), n)
		top1.update(prec1.item(), n)
		top5.update(prec5.item(), n)
		
		if step % args.report_freq == 0:
			logging.info('valid %03d %e %f %f', step, objs.avg, top1.avg, top5.avg)
	
	return top1.avg, objs.avg


if __name__ == '__main__':
	main()


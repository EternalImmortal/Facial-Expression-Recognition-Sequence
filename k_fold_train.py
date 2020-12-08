import os
import argparse
parser = argparse.ArgumentParser(description='PyTorch CK+ CNN Training')
parser.add_argument('--hide_details', help="whether show the progress of each epoch")
parser.add_argument('--resume', '-r', action='store_true', help='resume from checkpoint')
parser.add_argument('--model', default='VGG19')
opt = parser.parse_args()

for i in range(10):
    print("current fold " + str(i + 1))
    cmd = 'python mainpro_CK+.py --bs 128 --lr 0.01 --fold %d' % (i + 1)
    if opt.model == 'Resnet18':
        cmd += " --model Resnet18"
    if opt.hide_details:
        cmd += " --show_details 0"
    if opt.resume:
        cmd += " --resume"
    os.system(cmd)

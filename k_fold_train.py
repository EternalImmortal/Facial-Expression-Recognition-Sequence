import os
import argparse
parser = argparse.ArgumentParser(description='PyTorch CK+ CNN Training')
parser.add_argument('--show_details', default=1, help="whether show the progress of each epoch")
opt = parser.parse_args()

for i in range(10):
    print("current fold " + str(i + 1))
    cmd = 'python mainpro_CK+.py --model VGG19 --bs 32 --lr 0.01 --fold %d' % (i + 1)
    if not opt.show_details:
        cmd += " --show_details 0"
    os.system(cmd)
print("Train VGG19 ok!")

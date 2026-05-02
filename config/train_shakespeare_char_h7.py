
out_dir = 'out-shakespeare-char-l7-h7'
eval_interval = 200
log_interval = 20
eval_iters = 20
always_save_checkpoint = False

wandb_log = False

dataset = 'shakespeare_char'
gradient_accumulation_steps = 1
batch_size = 32
block_size = 128

n_layer = 7
n_head = 7
n_embd = 210
dropout = 0.2

learning_rate = 1e-3
max_iters = 1000
lr_decay_iters = 1000
min_lr = 1e-4
beta2 = 0.99
warmup_iters = 50

device = 'cuda' if __import__('torch').cuda.is_available() else 'cpu'
compile = False

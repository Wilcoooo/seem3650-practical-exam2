
out_dir = 'out-code-generation'
eval_interval = 500
log_interval = 20
eval_iters = 50
always_save_checkpoint = True

wandb_log = False

dataset = 'code_generation'
gradient_accumulation_steps = 1
batch_size = 32
block_size = 128

n_layer = 4
n_head = 4
n_embd = 128
dropout = 0.2

learning_rate = 1e-3
max_iters = 3000
lr_decay_iters = 3000
min_lr = 1e-4
beta2 = 0.99
warmup_iters = 50

device = 'cuda' if __import__('torch').cuda.is_available() else 'cpu'
compile = False

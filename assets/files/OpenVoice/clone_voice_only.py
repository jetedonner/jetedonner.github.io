from openvoice.api import ToneColorConverter
from openvoice import se_extractor
from melo.api import TTS
import numpy as np
import torch
import os

ckpt_converter = 'checkpoints_v2/converter'
device = "cuda:0" if torch.cuda.is_available() else "cpu"
output_dir = 'outputs_v2'
voice_sample = "myvoice.wav"
voice_clone = "myvoice_se.npz"

vc_model = ToneColorConverter(f'{ckpt_converter}/config.json', device=device)
vc_model.load_ckpt(f'{ckpt_converter}/checkpoint.pth')

os.makedirs(output_dir, exist_ok=True)

se = se_extractor.get_se(voice_sample, vc_model, vad=True)
tgt_se = se[0]
tgt_tone = se[1]

np.savez(voice_clone, se=tgt_se, tone= tgt_tone)

print(f'Cloned own voice finished successfully!\nYou find the output at: {voice_clone}')
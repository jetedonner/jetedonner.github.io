from openvoice.api import ToneColorConverter
# from openvoice import se_extractor
from melo.api import TTS
import numpy as np
import torch
# import os

ckpt_converter = 'checkpoints_v2/converter'
device = "cuda:0" if torch.cuda.is_available() else "cpu"
output_dir = 'outputs_v2'
output_tmp = './tmp123456789.wav'
tts_lang = 'EN'
voice_sample = "myvoice.wav"
voice_clone = "myvoice_se_ng.npz"
speaker_key = "EN-Default"

vc_model = ToneColorConverter(f'{ckpt_converter}/config.json', device=device)
vc_model.load_ckpt(f'{ckpt_converter}/checkpoint.pth')

# os.makedirs(output_dir, exist_ok=True)

# se = se_extractor.get_se(voice_sample, vc_model, vad=True)
# np.savez(voice_clone, se=se[0], tone=se[1])

model = TTS(language=tts_lang, device=device)

speaker_ids = model.hps.data.spk2id
speaker_id = speaker_ids[speaker_key]
speaker_key = speaker_key.lower().replace('_', '-')

source_se = torch.load(f'checkpoints_v2/base_speakers/ses/{speaker_key}.pth', map_location=device)
if torch.backends.mps.is_available():
    torch.backends.mps.is_available = lambda: False

# This is for loading your cloned voice once it's saved
data = np.load(voice_clone)
src_se = data["se"]
tgt_se = data["tone"]

model.tts_to_file("Hello world from Version 2 of OpenVoice. This is actually the second try or rerun. This is the initial working version for cloning and speaking with my own voice.", speaker_id, output_tmp, speed=0.9)

save_path = f'outputs_v2/output_v2_{speaker_key}_ngngng123.wav'

vc_model.convert(
            audio_src_path = output_tmp, 
            src_se = source_se, 
            tgt_se = src_se, 
            output_path = save_path)
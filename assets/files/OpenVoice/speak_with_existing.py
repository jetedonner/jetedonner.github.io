from openvoice.api import ToneColorConverter
from melo.api import TTS
import numpy as np
import torch

ckpt_converter = 'checkpoints_v2/converter'
device = "cuda:0" if torch.cuda.is_available() else "cpu"
output_dir = 'outputs_v2'
output_tmp = './tmp.wav'
tts_lang = 'EN'
voice_sample = "myvoice.wav"
voice_clone = "myvoice_se.npz"
speaker_key = "EN-Default"

vc_model = ToneColorConverter(f'{ckpt_converter}/config.json', device=device)
vc_model.load_ckpt(f'{ckpt_converter}/checkpoint.pth')

model = TTS(language=tts_lang, device=device)

speaker_ids = model.hps.data.spk2id
speaker_id = speaker_ids[speaker_key]
speaker_key = speaker_key.lower().replace('_', '-')

source_se = torch.load(f'checkpoints_v2/base_speakers/ses/{speaker_key}.pth', map_location=device)
if torch.backends.mps.is_available():
    torch.backends.mps.is_available = lambda: False

# This is for loading your cloned voice once it's saved
data = np.load(voice_clone)
tgt_se = data["se"]
tgt_tone = data["tone"]

tgt_se = torch.tensor(tgt_se).float()

model.tts_to_file("The quick brown fox jumps over the lazy dog. This audio was created with an already cloned and saved voice that was used to speak the text", speaker_id, output_tmp, speed=0.9)

save_path = f'outputs_v2/output_v2_{speaker_key}.wav'

vc_model.convert(
            audio_src_path = output_tmp, 
            src_se = source_se, 
            tgt_se = tgt_se, 
            output_path = save_path)

print(f'Using your saved cloned voice to text-to-speak finished successfully!\nYou find the audio output at: {save_path}')

from openvoice.api import ToneColorConverter
from openvoice import se_extractor
from melo.api import TTS
import numpy as np
import torch
import os
import argparse
import nltk

def parse_args():
    parser = argparse.ArgumentParser(description="OpenVoice TTS CLI")

    parser.add_argument(
        "--text",
        type=str,
        required=True,
        help="Text to synthesize"
    )

    parser.add_argument(
        "--out",
        type=str,
        required=True,
        help="Output audio file path"
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    text = args.text
    out_path = args.out

    print("Text:", text)
    print("Output file:", out_path)

    nltk.download('averaged_perceptron_tagger_eng')

    # Your TTS logic here
    # model.tts_to_file(text, speaker_id, out_path)

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

    os.makedirs(output_dir, exist_ok=True)

    se = se_extractor.get_se(voice_sample, vc_model, vad=True)
    tgt_se = se[0]
    tgt_tone = se[1]

    np.savez(voice_clone, se=tgt_se, tone= tgt_tone)

    model = TTS(language=tts_lang, device=device)

    speaker_ids = model.hps.data.spk2id
    speaker_id = speaker_ids[speaker_key]
    speaker_key = speaker_key.lower().replace('_', '-')

    source_se = torch.load(f'checkpoints_v2/base_speakers/ses/{speaker_key}.pth', map_location=device)
    if torch.backends.mps.is_available():
        torch.backends.mps.is_available = lambda: False

    # Uncomment this to load cloned voice from save-file
    # data = np.load(voice_clone)
    # tgt_se = torch.tensor(data["se"]).float()
    # tgt_tone = data["tone"]

    model.tts_to_file(text, speaker_id, output_tmp, speed=0.9)

    save_path = f'outputs_v2/output_v2_{speaker_key}.wav'
    save_path = out_path
    vc_model.convert(
                audio_src_path = output_tmp, 
                src_se = source_se, 
                tgt_se = tgt_se, 
                output_path = save_path)

    print(f'Cloning your voice and using it to text-to-speak finished successfully!\nYou find the audio output at: {save_path}')
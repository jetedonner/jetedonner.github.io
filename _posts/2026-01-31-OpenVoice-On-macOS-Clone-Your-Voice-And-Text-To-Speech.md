---
layout: post
title:  "OpenVoice V2 tutorial (Docker version, macOS)"
author: dave
date:   2026-01-31 10:46:36 +0200
categories: [Voice-Cloning, Text to Speech]
tags: [Voice-Cloning, Text to Speech]	
published: false
---
# OpenVoice V2 tutorial (Docker version, macOS)

![OpenVoice - Docker](../../assets/img/projects/openvoice/2026-01-31-01-docker-app-clone-voice-and-tts.gif)

## Introduction
This is a documentation about my endeavour setting up OpenVoice on macOS Tahoe as a free way for cloning (my own) voice and using it for text to speech. At the beginning it might seem a little confusing and overwhelming, but once you got it set up and understood the process, it's pretty simple and straight forward. As a part of this tutorial, I tried to list all the needed ressources and also published some python scripts you can use as a startpoint.

## Prerequisites on macOS Tahoe
The following (**ALL FREE**) tools and apps are required to get started with this tutorial about OpenVoice. Please make sure you have them setup correctly before you start with the main task of cloning your own voice and using it as a source for text-to-speech.

- [Homebrew](https://brew.sh/)
- [Git CLI](https://cli.github.com/) or [GitHub Desktop](https://github.com/apps/desktop?ref_product=desktop&ref_type=engagement&ref_style=button)
- [Python 3.9 or 3.10](https://www.python.org/downloads/macos/)
- [Anaconda Python (optional)](https://www.anaconda.com/download)
- [Docker-Desktop](https://www.docker.com/get-started/)
- [VSCode (Also install python extensions)](https://code.visualstudio.com/download)
- [OpenVoice checkpoints V2](https://myshell-public-repo-host.s3.amazonaws.com/openvoice/checkpoints_v2_0417.zip) (only for Version 2 TTS)
- [MeloTTS](https://github.com/myshell-ai/MeloTTS)

<!--  - A sample audio file (*.wav) of the voice you want to clone / use -->

## OpenVoice Docker version
To avoid issues with Python versions and dependency conflicts on macOS, I’d recommend using the Docker image of OpenVoice. It’s a truly encapsulated and ready‑made version of OpenVoice (V1 and V2). Even with Python virtual environments, I ran into problems when trying to set up OpenVoice on macOS Tahoe, so I eventually switched to the Docker version. For me, it was the final approach that worked flawlessly — after multiple attempts to set up OpenVoice manually.

- [Docker-Desktop](https://www.docker.com/get-started/)
- [OpenVoice Docker-Image on GitHub](https://github.com/manzolo/myshell-openvoice-docker)

## OpenVoice V2 python scripts
Some python scripts / commands to clone / reload the own voice and generate a new audio file using that own voice output.

### Complete workflow cloning and speaking text with your own voice
```python
from openvoice.api import ToneColorConverter
from openvoice import se_extractor
from melo.api import TTS
import numpy as np
import torch
import os

ckpt_converter = 'checkpoints_v2/converter'
device = "cuda:0" if torch.cuda.is_available() else "cpu"
output_dir = 'outputs_v2'
output_tmp = './tmp.wav'
tts_lang = 'EN'
voice_sample = "myvoice.wav"
voice_clone = "myvoice_se_ng.npz"
speaker_key = "EN-Default"

vc_model = ToneColorConverter(f'{ckpt_converter}/config.json', device=device)
vc_model.load_ckpt(f'{ckpt_converter}/checkpoint.pth')

os.makedirs(output_dir, exist_ok=True)

se = se_extractor.get_se(voice_sample, vc_model, vad=True)
np.savez(voice_clone, se=se[0], tone=se[1])

model = TTS(language=tts_lang, device=device)

speaker_ids = model.hps.data.spk2id
speaker_id = speaker_ids[speaker_key]
speaker_key = speaker_key.lower().replace('_', '-')

source_se = torch.load(f'checkpoints_v2/base_speakers/ses/{speaker_key}.pth', map_location=device)
if torch.backends.mps.is_available():
    torch.backends.mps.is_available = lambda: False

# This is for loading your cloned voice once it's saved
# data = np.load(voice_clone)
# src_se = data["se"]
# tgt_se = data["tone"]

model.tts_to_file("Hello world from Version 2 of OpenVoice. This is actually the second try or rerun. This is the initial working version for cloning and speaking with my own voice.", speaker_id, output_tmp, speed=0.9)

save_path = f'outputs_v2/output_v2_{speaker_key}_ngngng.wav'

vc_model.convert(
            audio_src_path = output_tmp, 
            src_se = source_se, 
            tgt_se = se[0], 
            output_path = save_path)

```
- [Download python script (clone_and_speak.py)](/assets/files/OpenVoice/clone_and_speak.py)


### Use own reference audio to clone voice
That's a onetime job. Cloning your own voice is taking some time, but has to be done only once, the first time. After taht you have cloned your voice properly, you just need it to be passed to the TTS function that makes the audio sound like you.

```python
from openvoice.api import ToneColorConverter
from openvoice import se_extractor
from melo.api import TTS
import numpy as np
import torch
import os

ckpt_converter = 'checkpoints_v2/converter'
device = "cuda:0" if torch.cuda.is_available() else "cpu"
output_dir = 'outputs_v2'
output_tmp = './tmp.wav'
tts_lang = 'EN'
voice_sample = "myvoice.wav"
voice_clone = "myvoice_se_ng.npz"
speaker_key = "EN-Default"

vc_model = ToneColorConverter(f'{ckpt_converter}/config.json', device=device)
vc_model.load_ckpt(f'{ckpt_converter}/checkpoint.pth')

os.makedirs(output_dir, exist_ok=True)

se = se_extractor.get_se(voice_sample, vc_model, vad=True)
np.savez(voice_clone, se=se[0], tone=se[1])

```

### Create audio with existing cloned voice
That's the python script part, that creates a audio file from a text using your own cloned voice. You can save it as a python script and reuse it each time you want to tts something.

```python
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
voice_clone = "myvoice_se_ng.npz"
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
src_se = data["se"]
tgt_se = data["tone"]

src_se = torch.tensor(src_se).float()

model.tts_to_file("the quick brown fox jumps over the lazy dog.", speaker_id, output_tmp, speed=0.9)

save_path = f'outputs_v2/output_v2_{speaker_key}.wav'

vc_model.convert(
            audio_src_path = output_tmp, 
            src_se = source_se, 
            tgt_se = src_se, 
            output_path = save_path)

```
- [Download python script (speak_with_existing.py)](/assets/files/OpenVoice/speak_with_existing.py)

## Resources

## Credits
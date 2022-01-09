# A system that creates the model the casting director wants, using face descriptions
<br>

- Presentation video

[![Video](http://img.youtube.com/vi/5fP-yW-UvRk/0.jpg)](https://www.youtube.com/watch?v=5fP-yW-UvRk) 

## Built With

* [김영서](https://github.com/youngseo0526) - Leader & Main coder
* [백서희](https://github.com/soycong) - Main coder
* [양정안](https://github.com/polyn0) - Main coder
* [최다경](https://github.com/DaGyeongChoi) - Main coder

## Getting Started

### Prerequisites

- Envirionment setup

After cloning this repo, enter into the StyleCLIP folder and run the following command to create a new conda environment named "styleclip" with all the required packages.

```console
conda env create -f environment.yml
```
<br>

- Install text summarization package
```console
pip install transformers
#pip install tensorflow==2.1
```

<br>

- Install CLIP package
```console
pip install git+https://github.com/openai/CLIP.git 
```
<br>

- StyleGAN Weights

Download the `.pt` file from [here](https://github.com/lernapparat/lernapparat/releases/download/v2019-02-01/karras2019stylegan-ffhq-1024x1024.for_g_all.pt
) and store it inside the folder of this repo with the name `karras2019stylegan-ffhq-1024x1024.for_g_all.pt`.

## Running the tests

Run the following command to generate a face with a custom prompt. In this case the prompt is "The image of a woman with blonde hair and purple eyes"
```console
input_text= "This person is a middle-aged woman. She has light brown short hair. Her forehead is a bit wide. She has light eyebrows and double eyelids. She has black pupils and has wrinkles around her eyes. Her nose is round and large. Her lips are pink, thin and small. She is wearing glasses. She is wearing only one earring. Her face shape is round."

!python clip_generate.py --prompt input_text
```

The results will be stored under the folder `generations` with the name of the prompt that you have entered.

## Acknowledgments

* [T5](https://arxiv.org/abs/1910.10683)
* [StyleGAN](https://arxiv.org/abs/1812.04948)
* [CLIP](https://arxiv.org/abs/2103.00020)
* [StyleCLIP](https://arxiv.org/abs/2103.17249)

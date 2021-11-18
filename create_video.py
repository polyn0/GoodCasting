{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "styleClip_0.ipynb",
      "provenance": [],
      "mount_file_id": "1WlBZUCLsfjAq45sEHCheupIipTKpYB2F",
      "authorship_tag": "ABX9TyPjqFdFFadKjxs32g2GoOlA"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    },
    "accelerator": "GPU"
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "AwRMd9BrkHIB",
        "outputId": "634c9b57-09d3-4beb-8ef5-de98caeeec85"
      },
      "source": [
        "!conda env create -f environment.yml"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/bin/bash: conda: command not found\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JIep66v6Hmbn",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0bcfafcb-90c3-4a39-898f-15802ad9c8b5"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "L6CUlvlDj0oI",
        "outputId": "d9bff305-fcb8-43f7-d997-04374161c3bc"
      },
      "source": [
        "!git clone https://github.com/vipermu/StyleCLIP"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Cloning into 'StyleCLIP'...\n",
            "remote: Enumerating objects: 30, done.\u001b[K\n",
            "remote: Counting objects: 100% (30/30), done.\u001b[K\n",
            "remote: Compressing objects: 100% (28/28), done.\u001b[K\n",
            "remote: Total 30 (delta 12), reused 9 (delta 2), pack-reused 0\u001b[K\n",
            "Unpacking objects: 100% (30/30), done.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SkNgsvrBkMra",
        "outputId": "8388f416-86ad-412c-b54d-284ea6461ebd"
      },
      "source": [
        "!pip install git+https://github.com/openai/CLIP.git "
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting git+https://github.com/openai/CLIP.git\n",
            "  Cloning https://github.com/openai/CLIP.git to /tmp/pip-req-build-v0cakj_j\n",
            "  Running command git clone -q https://github.com/openai/CLIP.git /tmp/pip-req-build-v0cakj_j\n",
            "Requirement already satisfied: ftfy in /usr/local/lib/python3.7/dist-packages (from clip==1.0) (6.0.3)\n",
            "Requirement already satisfied: regex in /usr/local/lib/python3.7/dist-packages (from clip==1.0) (2019.12.20)\n",
            "Requirement already satisfied: tqdm in /usr/local/lib/python3.7/dist-packages (from clip==1.0) (4.62.3)\n",
            "Requirement already satisfied: torch in /usr/local/lib/python3.7/dist-packages (from clip==1.0) (1.9.0+cu111)\n",
            "Requirement already satisfied: torchvision in /usr/local/lib/python3.7/dist-packages (from clip==1.0) (0.10.0+cu111)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.7/dist-packages (from ftfy->clip==1.0) (0.2.5)\n",
            "Requirement already satisfied: typing-extensions in /usr/local/lib/python3.7/dist-packages (from torch->clip==1.0) (3.7.4.3)\n",
            "Requirement already satisfied: pillow>=5.3.0 in /usr/local/lib/python3.7/dist-packages (from torchvision->clip==1.0) (7.1.2)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.7/dist-packages (from torchvision->clip==1.0) (1.19.5)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "qusE-X3kEn26",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "d6a725a4-3d8b-4722-848c-a8749e320aef"
      },
      "source": [
        "cd /content/drive/MyDrive/Colab Notebooks/styleclip"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive/Colab Notebooks/styleclip\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zyhnkPRkGVWm",
        "outputId": "9dabc255-0ae0-43ba-b3a9-aeafee25dd89"
      },
      "source": [
        "!pwd"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "/content/drive/MyDrive/Colab Notebooks/styleclip\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6kcQIGgSkepY",
        "outputId": "cab38e21-0e3d-4d7a-85e5-8ebb3fe0bec5"
      },
      "source": [
        "!python clip_generate.py --prompt \"The image of a woman with blonde hair and purple eyes\""
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Step 1025\n",
            "Loss 2.189453125\n",
            "Step 1030\n",
            "Loss 2.173828125\n",
            "Traceback (most recent call last):\n",
            "  File \"clip_generate.py\", line 162, in <module>\n",
            "    img = g_synthesis(dlatents)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/torch/nn/modules/module.py\", line 1051, in _call_impl\n",
            "    return forward_call(*input, **kwargs)\n",
            "  File \"/content/drive/MyDrive/Colab Notebooks/styleclip/stylegan_models.py\", line 369, in forward\n",
            "    x = m(x, dlatents_in[:, 2*i:2*i+2])\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/torch/nn/modules/module.py\", line 1051, in _call_impl\n",
            "    return forward_call(*input, **kwargs)\n",
            "  File \"/content/drive/MyDrive/Colab Notebooks/styleclip/stylegan_models.py\", line 308, in forward\n",
            "    x = self.epi2(x, dlatents_in_range[:, 1])\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/torch/nn/modules/module.py\", line 1051, in _call_impl\n",
            "    return forward_call(*input, **kwargs)\n",
            "  File \"/content/drive/MyDrive/Colab Notebooks/styleclip/stylegan_models.py\", line 255, in forward\n",
            "    x = self.style_mod(x, dlatents_in_slice)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/torch/nn/modules/module.py\", line 1051, in _call_impl\n",
            "    return forward_call(*input, **kwargs)\n",
            "  File \"/content/drive/MyDrive/Colab Notebooks/styleclip/stylegan_models.py\", line 119, in forward\n",
            "    style = self.lin(latent) # style => [batch_size, n_channels*2]\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/torch/nn/modules/module.py\", line 1051, in _call_impl\n",
            "    return forward_call(*input, **kwargs)\n",
            "  File \"/content/drive/MyDrive/Colab Notebooks/styleclip/stylegan_models.py\", line 32, in forward\n",
            "    return F.linear(x, self.weight * self.w_mul, bias)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/torch/nn/functional.py\", line 1847, in linear\n",
            "    return torch._C._nn.linear(input, weight, bias)\n",
            "KeyboardInterrupt\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "hALPDUUrk8Ck"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}
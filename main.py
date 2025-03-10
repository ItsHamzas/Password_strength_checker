{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyM762AMOJArwouJlejNRP5r",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ItsHamzas/Password_strength_checker/blob/main/main.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "7RPp9IyzTWTz"
      },
      "outputs": [],
      "source": [
        "import re\n",
        "\n",
        "# functions to check the strength of password\n",
        "def check_password_strength(password):\n",
        "  if len(password) < 8:\n",
        "    return \"weak: Password must be 8 characters long!\"\n",
        "\n",
        "  if not re.search(r'[A-Z]', password):\n",
        "    return \"weak: Password must contain at least one uppercase letter.\"\n",
        "\n",
        "  if not re.search(r'[a-z]', password):\n",
        "    return \"weak: Password must contain at least one lowercase letter.\"\n",
        "\n",
        "  if not re.search(r'[0-9]', password):\n",
        "    return \"weak: Password must contain at least one digit.\"\n",
        "\n",
        "  if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):\n",
        "    return \"weak: Password must contain at least one special charachter.\"\n",
        "\n",
        "  return \"stong password!\"\n",
        "\n",
        "# Main program\n",
        "password = input(\"Enter a password to chect its strength:\")\n",
        "result = check_password_strength(password)\n",
        "print(result)\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "metadata": {
        "id": "FTvT7KM6vfPa"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
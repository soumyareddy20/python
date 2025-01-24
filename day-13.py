{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "o4rddaqMwPA_",
        "outputId": "265b5375-3ef0-4f3a-e51a-f844b9582d77"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Token           POS        Tag       \n",
            "-----------------------------------\n",
            "NLP             PROPN      NNP       \n",
            "is              AUX        VBZ       \n",
            "amazing         ADJ        JJ        \n",
            "and             CCONJ      CC        \n",
            "fun             ADJ        JJ        \n",
            "to              PART       TO        \n",
            "learn           VERB       VB        \n",
            ".               PUNCT      .         \n"
          ]
        }
      ],
      "source": [
        "import spacy\n",
        "\n",
        "def pos_tagging(sentence):\n",
        "    nlp = spacy.load(\"en_core_web_sm\")\n",
        "    doc = nlp(sentence)\n",
        "    print(f\"{'Token':<15} {'POS':<10} {'Tag':<10}\")\n",
        "    print(\"-\" * 35)\n",
        "    for token in doc:\n",
        "        print(f\"{token.text:<15} {token.pos_:<10} {token.tag_:<10}\")\n",
        "\n",
        "\n",
        "sentence = \"NLP is amazing and fun to learn.\"\n",
        "pos_tagging(sentence)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "lu22M9vTxPfL"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
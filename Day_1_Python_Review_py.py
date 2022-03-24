{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Day_1_Python_Review.py",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyP43egxnCbLww+lFQNQNtcA"
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
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "cflS2z2X4YKt",
        "outputId": "5fdc39cd-dfb6-4ba6-9051-b89164e6f4f6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Word :v\n",
            "WORD :V\n",
            "another word :V\n",
            "world\n",
            "Zanis_Do to ['Zanis', 'Do']\n",
            "['Zanis', 'Do'] to Zanis_Do\n"
          ]
        }
      ],
      "source": [
        "# sign a value: value_name = value\n",
        "# ex \n",
        "tmp_value_1 = 10\n",
        "\n",
        "# check datatype of value \n",
        "# print(type(tmp_value_1))\n",
        "# <class 'int'>\n",
        "\n",
        "word_hello = 'hello'\n",
        "\n",
        "#length\n",
        "# print(len(word_hello))\n",
        "\n",
        "# string\n",
        "tmp_str = 'word :V'\n",
        "\n",
        "tmp_str_1 = tmp_str.capitalize() \n",
        "print(tmp_str_1)\n",
        "\n",
        "tmp_str_2 = tmp_str.upper()\n",
        "print(tmp_str_2)\n",
        "\n",
        "tmp_str_3 = tmp_str.replace('word', 'another word')\n",
        "print(tmp_str_3)\n",
        "\n",
        "print(' world '.strip())\n",
        "\n",
        "tmp_name = 'Zanis_Do'\n",
        "name_list = tmp_name.split('_')\n",
        "print(tmp_name, 'to', name_list)\n",
        "\n",
        "name_list_1 = ['Zanis', 'Do']\n",
        "tmp_name_1 = '_'.join(name_list)\n",
        "print(name_list, 'to', tmp_name_1)\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# container\n",
        "# Creating lists\n",
        "tmp_list = [10, 11, 12]\n",
        "tmp_list_1 = ['foo', 4, 5, 'bar', 0.4]\n",
        "nested_list = ['foobar', ['baz', 'qux'], [0]]\n",
        "\n",
        "print(tmp_list)\n",
        "print(tmp_list_1)\n",
        "print(nested_list)\n",
        "\n",
        "#Accessing list values\n",
        "tmp_list[2] # 5\n",
        "tmp_list[-1] # 0.4\n",
        "tmp_list[:2] # ['foo', 4, 5]\n",
        "nested_list[2] # ['baz', 'quz']\n",
        "nested_list[-1] # [0]\n",
        "nested_list[1][1] # 'qux'\n",
        "\n",
        "#List method\n",
        "\n",
        "\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 87
        },
        "id": "BbxtkPZyB_Gm",
        "outputId": "375c7dd0-d617-4d71-bfb9-8977256d8210"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[10, 11, 12]\n",
            "['foo', 4, 5, 'bar', 0.4]\n",
            "['foobar', ['baz', 'qux'], [0]]\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'qux'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    }
  ]
}
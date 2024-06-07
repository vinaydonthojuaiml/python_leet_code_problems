{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN8/6WaazKKlQ4MCue4HnK9",
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
        "<a href=\"https://colab.research.google.com/github/vinaydonthojuaiml/python_leet_code_problems/blob/main/LinkedList.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WsMAk5hTWULv",
        "outputId": "916d5003-9f5f-41fa-ba2f-af99ddb34b63"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "6 5 10 1 \n",
            "Length = 4\n",
            "6 1\n"
          ]
        }
      ],
      "source": [
        "# 15 --> 6 --> 8\n",
        "\n",
        "class Node():\n",
        "\n",
        "  def __init__(self,data):\n",
        "    self.data = data\n",
        "    self.next = None\n",
        "\n",
        "class LinkedList():\n",
        "\n",
        "  def __init__(self):\n",
        "    self.head = None\n",
        "    self.tail = None\n",
        "\n",
        "  def append(self,data):\n",
        "    new_node = Node(data)\n",
        "    if self.head == None:\n",
        "      self.head = new_node\n",
        "      self.tail = self.head\n",
        "      self.length = 1\n",
        "    else:\n",
        "      self.tail.next = new_node\n",
        "      self.tail = new_node\n",
        "      self.length += 1\n",
        "\n",
        "  def prepend(self,data):\n",
        "    new_node = Node(data)\n",
        "    new_node.next = self.head\n",
        "    self.head = new_node\n",
        "\n",
        "\n",
        "    self.length += 1\n",
        "\n",
        "  def insert(self,index,data):\n",
        "    new_node = Node(data)\n",
        "    i = 0\n",
        "    temp = self.head\n",
        "    if index>=self.length:\n",
        "      self.append(data)\n",
        "      return\n",
        "    if index ==0:\n",
        "      self.prepend(data)\n",
        "      return\n",
        "    while i<self.length:\n",
        "      if i == index-1:\n",
        "        temp.next , new_node.next = new_node , temp.next\n",
        "        self.length+=1\n",
        "        break\n",
        "      temp = temp.next\n",
        "      i+=1\n",
        "\n",
        "\n",
        "  def remove(self,index):\n",
        "    temp = self.head\n",
        "    i=0\n",
        "    if index>=self.length:\n",
        "      print(\"Entered wrong index\")\n",
        "\n",
        "    if index == 0:\n",
        "      self.head = self.head.next\n",
        "      self.length -= 1\n",
        "      return\n",
        "\n",
        "    while i<self.length:\n",
        "      if i == index-1:\n",
        "        temp.next = temp.next.next\n",
        "        self.length-=1\n",
        "        break\n",
        "      i+=1\n",
        "      temp = temp.next\n",
        "\n",
        "  def printl(self):\n",
        "    temp = self.head\n",
        "    while temp != None:\n",
        "      print(temp.data , end = ' ')\n",
        "      temp = temp.next\n",
        "    print()\n",
        "    print('Length = '+str(self.length))\n",
        "\n",
        "\n",
        "  def reverse(self):\n",
        "    if self.length == 1:\n",
        "      return self.head\n",
        "\n",
        "    first = self.head\n",
        "    self.tail = self.head\n",
        "    second = first.next\n",
        "    while second:\n",
        "      temp = second.next\n",
        "      second.next = first\n",
        "      first = second\n",
        "      second = temp\n",
        "    self.head.next = None\n",
        "    self.head = first\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "\n",
        "l = LinkedList()\n",
        "l.append(10)\n",
        "l.append(5)\n",
        "l.append(6)\n",
        "l.prepend(1)\n",
        "\n",
        "# l.remove(5)\n",
        "l.reverse()\n",
        "l.printl()\n",
        "print(l.head.data, l.tail.data)"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "G2IuEFu3WWW6"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
# NeuralNetwork – My_Torch

A from-scratch implementation of an artificial neural network framework, built as part of my Epitech coursework.  
The project trains and evaluates a neural network to analyze chessboard states from Forsyth–Edwards Notation (FEN), without relying on machine learning libraries such as PyTorch or TensorFlow.

## Overview
This project consists of two main programs:

1. **Neural Network Generator** (`generator`)  
   Creates neural networks from configuration files, allowing experimentation with different architectures and hyperparameters.

2. **Chessboard Analyzer** (`trainer`)  
   Loads a neural network and:
   - **Train Mode**: Trains the model on labeled chessboard positions.
   - **Prediction Mode**: Classifies chessboard positions into:
     - `Checkmate` (+ side if known)
     - `Check`
     - `Stalemate`
     - `Nothing`

All neural networks are trained with **supervised learning**.

## 🛠 Features
- **Custom neural network engine** with no external ML libraries.
- Configurable architectures via `.conf` files.
- FEN-based chessboard parsing.
- Support for saving and loading pre-trained models.
- Multiple prediction granularities:
  - Basic: Check vs Nothing.
  - Intermediate: Check, Checkmate, Stalemate, Nothing.
  - Advanced: Includes side advantage (White/Black).
- Training optimizations to reduce overfitting and avoid local minima.

## 📂 Project Structure

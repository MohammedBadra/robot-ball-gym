# A1 Soccer Environment

## Overview
The A1 Soccer Environment is a simulated environment where the A1 robot, designed in MuJoCo, is trained to play soccer on a futsal-sized field using Q-Learning. This environment is built to study and develop the robot's skills in soccer gameplay, including dribbling, shooting, and team coordination.

## Getting Started

### Prerequisites
- MuJoCo: Ensure you have MuJoCo installed and properly configured.
- Python: This project is developed using Python, ensure you have it installed.

### Installation
1. Clone the repository to your local machine.
```bash
git clone https://github.com/your-username/a1-soccer-env.git
cd a1-soccer-env
```

    Install the required dependencies.
```bash
    pip install -r requirements.txt
```

## Usage
```bash
    python train.py
```

## Environment Details
## A1 Robot

The A1 robot is a quadruped robot modeled in MuJoCo. It has been designed to interact with the soccer ball and perform actions like dribbling, shooting, and passing.
Soccer Field

The soccer field is modeled based on futsal field dimensions but scaled down to fit the size of the A1 robot. It measures 182 cm by 243 cm.
## Soccer Goals

Two goals are placed at the north and south ends of the field. Each goal is a simple horizontal cuboid, one colored blue and the other yellow.
## Soccer Ball

A spherical ball is used for the soccer game, designed to interact with the A1 robot and the goals.
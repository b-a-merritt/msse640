# MSSE640-2025summer

## Assignments
### [Assignment #1](./week2/README.md)
### [Assignment #2](./week3/README.md)
### [Assignment #3](./week4/README.md)

## Projects
### [Project #1](./week2/main.py)

### Getting Started

#### 1. Install Python3

##### Windows

1. Download the latest Python 3 installer from the [official website](https://www.python.org/downloads/).
2. Run the installer and **check the box** that says:
   > ✅ Add Python to PATH
3. Select "Install Now".

To verify Python is installed:

```powershell
python --version
```

##### Linux

```Bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
python3 --version
```

#### 2. Set Up Virtual Environment

##### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

##### Linux

```Bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install All Dependencies

```Bash
pip install -r requirements.txt
```
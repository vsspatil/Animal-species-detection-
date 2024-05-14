# Animal-Species-Detection
The aim of this project is to develop an efficient computer vision model capable of real-time wildlife detection.



## Table of Contents
* Dataset
* Project structure
* Getting Code
* Web App
* Contributing


## Datasets
The dataset used in this project consists of labeled images of 10 different animal classes: Buffalo, Cheetahs, Deer, Elephant, Fox, Jaguars, Lion, Panda, Tiger, Zebra. You can find the datasets: 
- [Dataset 1](https://www.kaggle.com/datasets/biancaferreira/african-wildlife)
- [Dataset 2](https://www.kaggle.com/datasets/brsdincer/danger-of-extinction-animal-image-set)
- [Dataset 3](https://www.kaggle.com/datasets/antoreepjana/animals-detection-images-dataset )

## Project Structure
    ├── config
    │   └── custom.yaml    
    ├── data
    │   ├── images         
    │   └── labels         
    ├── logs
    │   └── log.log      
    ├── notebooks
    │   └── yolov8.ipynb
    ├── runs
    │   └── detect
    │       ├── train
    │       └── val
    ├── scripts
    │   ├── app.py
    │   ├── convert_format.py
    │   └── train_test_split.py
    ├── README.md
    └── requirements.txt

config: Holds configuration files (custom.yaml) for specifying training settings like learning rate and batch size.

data: Contains directories:

images: Stores images used for training and inference.
labels: Potentially holds annotation files corresponding to the images.
logs: Stores logs (log.log) generated during model training, which help evaluate performance and troubleshoot issues.

notebooks: Houses Jupyter notebooks (yolov8.ipynb) for interactive experimentation and result analysis with the YOLOv8 model.

runs: Includes subdirectories:

train: Stores model checkpoints and outputs generated during training.
val: Holds validation metrics and results.
scripts: Contains Python scripts (app.py, convert_format.py, train_test_split.py) for tasks like inference and data preprocessing.

README.md: Provides project information, purpose, setup instructions, and usage guidelines.

requirements.txt: Lists Python libraries and dependencies required to run the project, ensuring easy setup and reproducibility of the environment.


## Getting Code
Follow theses steps to set up the environment and run the application.
1. Fork the repository [here](https://github.com/ldebele/animal-Species-Detection).
2. Clone the forked repository.
    ```bash
    git clone https://github.com/<YOUR-USERNAME>/Animal-Species-Detection
    cd Animal-Species-Detection
    ```

3. Create a python virtual environment.
    ``` bash
    python3 -m venv venv
    ```

4. Activate the virtual environment.

    - On Linux and macOS
    ``` bash
    source venv/bin/activate
    ```
    - On Windows
    ``` bash
    venv\Scripts\activate
    ```

5. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
6. Run the application.
    ```python
    streamlit run './scripts/app.py'
    ```

## Web App
The trained model has been deployed on Hugging Face for practical use.
- you can access the deployed [web app](http://localhost:8501/)

## Contributing
Contributions to this project are welcome! If you have any suggestions, improvements, or bug fixes, feel free to open an issue or a pull request.

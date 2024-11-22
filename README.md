# Camouflage - Genetic Algorithm

This project demonstrates the use of a Genetic Algorithm (GA) to evolve a population of colors towards a target color. The objective is to match a randomly chosen color (in RGB format) by combining different random colors through crossover and mutation. The GA process is visualized using Streamlit, allowing real-time observation of the evolutionary process.

## Features
- **Real-time Evolution Visualization**: Watch the population evolve in real time towards the target color.
- **Flexible Parameter Adjustment**: Easily adjust mutation rate, crossover, population size, and other parameters.
- **User-Friendly Interface**: Built with Streamlit to provide a simple and interactive experience.

## Technologies Used
- **Python**: Core programming language for building the genetic algorithm.
- **Streamlit**: Used to create the web-based user interface and visualize the evolution in real time.
- **Matplotlib**: Assists in visualizing the population of colors and tracking fitness across generations.
- **NumPy**: Provides efficient randomization and numerical operations, especially for mutation.
- **UV**: Manages Python dependencies.

## Installation

### Prerequisites
- Python 3.12 or higher
- UV

### Setup
1. Clone this repository:
   ```bash
   git clone https://github.com/willsilvano/ia-genetic-algorithm-camouflage.git
   cd ia-genetic-algorithm-camouflage
   ```
2. Install UV:

   UV is a dependency manager for Python. To install, refer to the official documentation [here](https://docs.astral.sh/uv/).

3. Install dependencies:
   ```bash
   uv sync
   ```

4. Activate the environment:
   ```bash
   source .venv/bin/activate
   ```

## Running the Application
To run the Streamlit application and visualize the genetic algorithm in action, use the following command:
```bash
streamlit run camouflage.py
```
Once the server is running, open your browser and navigate to the provided URL (usually `http://localhost:8501`). You can adjust the genetic algorithm parameters and observe how the population evolves towards the target color.

## Parameters Description
- **Number of Generations**: Number of iterations the algorithm will run to improve the solution.
- **Population Size**: Number of individuals (colors) in each generation.
- **Number of Individuals Selected**: Top individuals kept for crossover.
- **Mutation Rate**: Percentage of genes that undergo mutation.
- **Mutation Intensity**: Controls how drastically genes mutate.
- **Time Between Generations**: Adjusts the speed of visualization.
- **Target Color**: The color the algorithm aims to match.

## Contributing
If you'd like to contribute to this project, please fork the repository and make changes as needed. Pull requests are warmly welcomed.
This project was based on the repository https://github.com/sergiopolimante/genetic_algorithm_camouflage. I appreciate the inspiration and ideas provided by this project.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
Special thanks to the open-source community for providing the tools and libraries used in this project.



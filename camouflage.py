import math
import time

import matplotlib.patches as patches
import matplotlib.pyplot as plt
import streamlit as st
from genetic_algorithm import CamouFlagGeneticAlgorithm  # Ensure correct import path

# Initialize Streamlit session state variables
if "evolution_running" not in st.session_state:
    st.session_state.evolution_running = False
if "generation_data" not in st.session_state:
    st.session_state.generation_data = {"generations": [], "fitness": []}
if "plots_initialized" not in st.session_state:
    st.session_state.plots_initialized = False

# Configure Streamlit page layout
st.set_page_config(layout="wide", page_title="Camouflage", page_icon="🎨")
st.markdown(
    """
    <style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def normalize_rgb(rgb):
    """Normalizes RGB values from 0-255 to 0-1 for plotting."""
    return tuple(max(0, min(x / 255, 1)) for x in rgb)


def initialize_plots():
    """Sets up placeholders for color visualization and fitness plot."""
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.plot_color = st.empty()
        with col2:
            st.session_state.plot_fitness = st.empty()
            st.session_state.label_current_generation = st.empty()
            st.session_state.label_current_fitness = st.empty()
            st.html("<br>")
            st.session_state.label_target_color = st.empty()
            st.session_state.label_best_individual = st.empty()

    st.session_state.plots_initialized = True


def create_visualization(individuals, target_color, generation_data=None):
    """
    Creates visualizations for the current population and fitness over generations.

    Args:
        individuals (list): List of RGB tuples representing the population.
        target_color (tuple): The target RGB color.
        generation_data (dict, optional): Data tracking generations and fitness scores.
    """
    if individuals:
        try:
            fig_colors = draw_colored_matrix(individuals, target_color)
            st.session_state.plot_color.pyplot(fig_colors)
            plt.close(fig_colors)
        except Exception as e:
            print(f"Error creating color visualization: {e}")

    if generation_data and len(generation_data["fitness"]) > 0:
        try:
            fig_fitness = draw_fitness_plot(generation_data)
            st.session_state.plot_fitness.pyplot(fig_fitness)
            plt.close(fig_fitness)
        except Exception as e:
            print(f"Error creating fitness plot: {e}")

    if len(individuals) > 0:
        # Display target color
        st.session_state.label_target_color.markdown(
            f"""
            <div style="display: flex; align-items: center;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background-color: rgb{target_color}; margin-right: 10px;"></div>
                <span><b>Individuo Alvo:</b> RGB{target_color}</span>
            </div>""",
            unsafe_allow_html=True,
        )
        # Display best individual
        st.session_state.label_best_individual.markdown(
            f"""
            <div style="display: flex; align-items: center;">
                <div style="width: 20px; height: 20px; border-radius: 50%; background-color: rgb{individuals[0]}; margin-right: 10px;"></div>
                <span><b>Melhor Indivíduo:</b> RGB{individuals[0]}</span>
            </div>""",
            unsafe_allow_html=True,
        )

    if generation_data:
        # Display current fitness
        st.session_state.label_current_fitness.markdown(
            f"""
            <div style="display: flex; align-items: center;">
                <span><b>🥇 Fitness atual:</b> {generation_data['fitness'][-1]}</span>
            </div>""",
            unsafe_allow_html=True,
        )
        # Display current generation
        st.session_state.label_current_generation.markdown(
            f"""
            <div style="display: flex; align-items: center;">
                <span><b>🧬️ Geração atual:</b> {generation_data['generations'][-1]}</span>
            </div>""",
            unsafe_allow_html=True,
        )


def draw_colored_matrix(individuals, target_color):
    """
    Draws a matrix of colored circles representing the population.

    Args:
        individuals (list): List of RGB tuples.
        target_color (tuple): The target RGB color for background.

    Returns:
        matplotlib.figure.Figure: The generated figure.
    """
    num_individuals = len(individuals)
    num_cols = math.ceil(math.sqrt(num_individuals))
    num_rows = math.ceil(num_individuals / num_cols)

    fig, ax = plt.subplots(figsize=(3, 3))

    normalized_target = normalize_rgb(target_color)
    fig.patch.set_facecolor(normalized_target)
    ax.set_facecolor(normalized_target)

    for idx, individual in enumerate(individuals):
        row = idx // num_cols
        col = idx % num_cols

        if not isinstance(individual, (tuple, list)) or len(individual) != 3:
            st.error(f"Invalid individual format: {individual}")
            continue

        normalized_color = normalize_rgb(individual)

        # Draw each individual as a colored circle
        circle = patches.Circle(
            (col + 0.5, num_rows - 1 - row + 0.5),
            0.5,
            edgecolor=normalized_color,
            facecolor=normalized_color,
        )
        ax.add_patch(circle)

    # Customize plot appearance
    for spine in ax.spines.values():
        spine.set_edgecolor(normalized_target)

    ax.set_xlim(0, num_cols)
    ax.set_ylim(0, num_rows)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_aspect("equal")
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

    return fig


def draw_fitness_plot(generation_data):
    """
    Draws a plot of fitness scores over generations.

    Args:
        generation_data (dict): Dictionary containing 'generations' and 'fitness' lists.

    Returns:
        matplotlib.figure.Figure: The generated fitness plot.
    """
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(generation_data["generations"], generation_data["fitness"], "b-")
    ax.set_xlabel("Geração")
    ax.set_ylabel("Fitness (menor é melhor)")
    ax.set_title("Evolução do Fitness")
    ax.grid(True)
    return fig


def update_visualization(population, current_generation, current_best_fitness):
    """
    Updates the visualization after each generation.

    Args:
        population (list): Current population of individuals.
        current_generation (int): Current generation number.
        current_best_fitness (int): Fitness score of the best individual.
    """
    if len(population) > 0:
        # Update generation data
        st.session_state.generation_data["generations"].append(current_generation)
        st.session_state.generation_data["fitness"].append(current_best_fitness)

        # Update visualizations
        create_visualization(
            population, st.session_state.target_color, st.session_state.generation_data
        )

    # Pause between generations based on user input
    time.sleep(st.session_state.generations_time)


# Callback function to start the evolution process
def start_evolution():
    """Starts the genetic algorithm evolution."""
    st.session_state.evolution_running = True
    st.session_state.generation_data = {"generations": [], "fitness": []}

    initialize_plots()

    # Initialize the genetic algorithm with user-defined parameters
    ga = CamouFlagGeneticAlgorithm(
        generations=st.session_state.generations,
        population_size=st.session_state.population_size,
        keep_population_num=st.session_state.keep_population_num,
        mutation_rate=st.session_state.mutation_rate / 100,  # Convert to decimal
        mutation_intensity=st.session_state.mutation_intensity
        / 100,  # Convert to decimal
        target_color=st.session_state.target_color,
    )

    # Start the evolution process with visualization callback
    ga.start_evolution(update_visualization)

    st.session_state.evolution_running = False
    st.success("Evolução encerrada.")


def main():
    """Main function to set up the Streamlit interface."""

    if not st.session_state.plots_initialized:
        initialize_plots()

    st.sidebar.header("Parâmetros do Algoritmo")

    # Algorithm parameters input by the user
    st.sidebar.number_input(
        "Número de Gerações",
        min_value=10,
        max_value=1000,
        value=100,
        step=1,
        key="generations",
    )

    st.sidebar.number_input(
        "Tamanho da População",
        min_value=2,
        max_value=1000,
        value=25,
        step=1,
        key="population_size",
    )

    st.sidebar.number_input(
        "Nº de indivíduos a selecionar",
        min_value=1,
        max_value=st.session_state.population_size
        if "population_size" in st.session_state
        else 1000,
        value=10,
        step=1,
        key="keep_population_num",
    )

    st.sidebar.number_input(
        "Taxa de Mutação (%)",
        min_value=0.0,
        max_value=100.0,
        value=1.0,
        step=0.1,
        key="mutation_rate",
    )

    st.sidebar.number_input(
        "Intensidade da Mutação (%)",
        min_value=0.0,
        max_value=50.0,
        value=0.1,
        step=0.1,
        key="mutation_intensity",
    )

    st.sidebar.number_input(
        "Tempo entre gerações (segundos)",
        min_value=0.0,
        max_value=5.0,
        value=0.0,
        step=0.1,
        key="generations_time",
    )

    # Color picker for target color
    st.sidebar.color_picker("Cor Alvo", "#E6D8D8", key="target_color_hex")
    # Convert hex color to RGB tuple
    st.session_state.target_color = tuple(
        int(st.session_state.target_color_hex[i : i + 2], 16) for i in (1, 3, 5)
    )

    # Button to start evolution
    st.sidebar.button("Iniciar", on_click=start_evolution)


if __name__ == "__main__":
    main()

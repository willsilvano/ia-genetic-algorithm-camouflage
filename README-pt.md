# Algoritmo Genético  - Camuflagem

Este projeto demonstra o uso de um Algoritmo Genético (GA) para evoluir uma população de cores até atingir uma cor-alvo. O objetivo é corresponder a uma cor escolhida aleatoriamente (no formato RGB) combinando diferentes cores através de cruzamento e mutação. O processo do GA é visualizado usando Streamlit, permitindo a observação em tempo real do processo evolutivo.

## Características
- **Visualização da Evolução em Tempo Real**: Observe a população evoluir em tempo real até a cor-alvo.
- **Ajuste Flexível de Parâmetros**: Ajuste facilmente a taxa de mutação, cruzamento, tamanho da população e outros parâmetros.
- **Interface Amigável ao Usuário**: Construído com Streamlit para proporcionar uma experiência simples e interativa.

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal usada para construir o algoritmo genético.
- **Streamlit**: Utilizado para criar a interface de usuário baseada na web e visualizar a evolução em tempo real.
- **Matplotlib**: Auxilia na visualização da população de cores e no acompanhamento da aptidão ao longo das gerações.
- **NumPy**: Fornece randomização eficiente e operações numéricas, especialmente para mutação.
- **UV**: Gerencia dependências do Python.

## Instalação

### Pré-requisitos
- Python 3.12 ou superior
- UV

### Configuração
1. Clone este repositório:
   ```bash
   git clone https://github.com/willsilvano/ia-genetic-algorithm-camouflage.git
   cd ia-genetic-algorithm-camouflage
   ```
2. Instale o UV:

   O UV é um gerenciador de dependências para Python. Para instalar, consulte a documentação oficial [aqui](https://docs.astral.sh/uv/).

3. Instale as dependências:
   ```bash
   uv sync
   ```

4. Ative o ambiente:
   ```bash
   source .venv/bin/activate
   ```

## Executando a Aplicação
Para executar a aplicação Streamlit e visualizar o algoritmo genético em ação, utilize o seguinte comando:
```bash
streamlit run camouflage.py
```
Uma vez que o servidor estiver em execução, abra o navegador e navegue para a URL fornecida (geralmente `http://localhost:8501`). Você pode ajustar os parâmetros do algoritmo genético e observar como a população evolui em direção à cor-alvo.

## Descrição dos Parâmetros
- **Número de Gerações**: Número de iterações que o algoritmo irá executar para melhorar a solução.
- **Tamanho da População**: Número de indivíduos (cores) em cada geração.
- **Número de Indivíduos Selecionados**: Melhores indivíduos mantidos para o cruzamento.
- **Taxa de Mutação**: Percentual de genes que sofrem mutação.
- **Intensidade da Mutação**: Controla o quão drástica é a mutação dos genes.
- **Tempo Entre Gerações**: Ajusta a velocidade da visualização.
- **Cor Alvo**: A cor que o algoritmo pretende igualar.

## Contribuindo
Se você deseja contribuir para este projeto, por favor, faça um fork do repositório e faça as alterações conforme necessário. Pull requests são muito bem-vindos.
Este projeto foi baseado no repositório https://github.com/sergiopolimante/genetic_algorithm_camouflage. Agradeço a inspiração e as ideias fornecidas por este projeto.

## Licença
Este projeto é licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.

## Agradecimentos
Agradecimentos especiais à comunidade de código aberto por fornecer as ferramentas e bibliotecas utilizadas neste projeto.



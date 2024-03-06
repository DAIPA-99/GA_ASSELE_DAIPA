<img src="https://upload.wikimedia.org/wikipedia/fr/e/e9/EPF_logo_2021.png" alt="Logo" width="50">



# Welcome to this GitHub project!

Initially, this project will focus on solving the famous Mastermind problem using an approach based on genetic algorithms. Next, attention turns to solving the Traveller's Problem (TSP), again exploiting the capabilities of genetic algorithms, while retaining as far as possible the key elements of the first program developed.

Finally, a crucial step is to generalize the code developed, in order to create a common base capable of solving a wide range of optimization problems. 


# Code recovery

You can recover source code by cloning it!

> [!NOTE]
> Cloning a Git repository from GitHub provides a complete local copy of the source code and associated change history. 

### 1. Install Git

> [!WARNING]
> If you haven't already done so, you need to install Git on your computer.

💡 You can download it from the official Git website and follow the installation instructions : https://git-scm.com/

### 2. Clone the deposit 

➡️ Once Git has been installed, open a `terminal` or `command prompt` on your computer.</font>

➡️ Use the `cd` command to navigate to the directory where you wish to clone the repository :

```bash
  cd [link to the folder where the cloned code will be stored]
```
➡️ Use the following git clone command followed by the repository URL :

```bash
  git clone https://github.com/DAIPA-99/GA_ASSELE_DAIPA.git
```

# So, how does it work?
To address the common challenge, we employ similar functions applicable to two distinct types of genetic problems: the Mastermind problem and the TSP problem.
In genetic algorithms, which are designed to optimize specific problems, such as in the recreational realm with Mastermind, our objective is to identify the optimal combination of colors with the highest fitness to win the game. Conversely, in the TSP algorithm, which is a geographical optimization problem, our aim is to determine the most efficient route to reach a destination.
In both cases, we apply principles inspired by `Darwin's evolutionary theory`, utilizing the following functions:

## Mastermind / TSP

* Evaluation of each individual

Return the best Individual of the population by sorting the population in ascending order and returning the last element.
```python
  def __init__(self, chromosome: list, fitness: float):
```

* Selection
  
This function make the selection by removing 50% of population (less adapted)
```python
  def evolve_for_one_generation(self):
```

* Reproduction

Define a function to generate a new individual by combining genetic information from two parents. Is a reproduction step of Darwin evolution
  ```python
  def new_indidual_from_2_parents(first_parent, second_parent):
```

* Mutation
Define a mutation function to introduce changes to a parent's chromosome, and retrieve possible colors from a mastermind game and randomly select one for mutation.
```python
  def mutation(parent):
```

* Generation of a new population
```python
  def evolve_until(self, max_nb_of_generations=500, threshold_fitness=None):
```

These functions serve as fundamental components in our approach to solving genetic problems, enabling us to iteratively improve solutions through simulated evolutionary processes.


## GA-Problem :
Finally, we generalized our code to solve different optimization problems. 
To define a problem for the Genetic Algorithm solver (ga_solver), we aim to identify a common framework for both the Mastermind and TSP functions. These common functions include:

* This function is used to initialize the population.
```python
  def __int__(self, threshold_fitness):
```

* It assists in determining the fittest individual within the population.
```python
  def how_to_compute_fitness(self, chromosome):
```

* This function aids in creating a new individual by crossing over two parents, selected based on the proportion of the best individual.
```python
  def new_individual_from_2_parents(self, first_parent, second_parent):
```

* This operation introduces random changes in individuals to promote diversity and exploration.
```python
  def mutation(self, parent):
```

* This function is responsible for generating a random chromosome.
```python
  def how_to_generate_one_random_chromosome(self):
```

    
## Documentation

To understand Darwin's theory of evolution: https://www.khanacademy.org/science/ap-biology/natural-selection/natural-selection-ap/a/darwin-evolution-natural-selection/)

For learning object-oriented programming: https://realpython.com/python3-object-oriented-programming/

To learn about list comprehension in Python: https://www.w3schools.com/python/python_lists_comprehension.asp

To understand how the mastermind problem works: https://www.mathweb.fr/euclide/2022/04/19/un-mastermind-en-python/

For understanding the Traveling Salesman Problem (TSP): https://www.geeksforgeeks.org/traveling-salesman-problem-tsp-implementation/

These resources provide valuable insights into various concepts and problems, helping you deepen your understanding and improve your problem-solving skills.

"""
FROM PAPER:
        Step 1: Set the maximum iteration iter_max, generate an initial population containing N organisms and set
    the other parameters of ACO. Select the current best organism Y_best iter:=1.
        Step 2: SOS is executed to compute a new set of ACO parameter values.
        Step 3: ACO uses new parameter values to resolve TSP
        Step 4: Update the pheromone on the path
        Step 5: Calculate the fitness value of the organism
        Step 6: Select the current best Y_best and the corresponding optimal path L_best'
        Step 7: Check if iter <= iter_max
            if yes -> Step 2
            Otherwise -> Output the optimal path L_best'

* ACO:
    1. Problem Definition: Clearly define the optimization problem you want to solve, including the objective function, constraints, and decision variables.
    2. Initialization: Initialize the ant colony by placing a number of ants on the problem space. Each ant represents a potential solution to the problem.
    3. Ant Movement: Each ant starts from a random position and iteratively constructs a solution by moving through the problem space. At each step, the ant chooses the next decision based on a probabilistic rule, typically guided by a combination of local pheromone information and heuristic information.
    4. Solution Construction: As the ants move, they construct solutions by making decisions based on the pheromone trails and heuristic information. The pheromone trails represent the accumulated knowledge of the ants regarding good solutions found so far.
    5. Pheromone Update: After all ants have constructed their solutions, the pheromone trails are updated to reflect the quality of the solutions found. Typically, the pheromone update includes evaporation (reducing the pheromone levels) and depositing pheromone on the edges corresponding to good solutions.
    6. Local Search (optional): Optionally, a local search procedure can be applied to improve the quality of the solutions constructed by the ants. Local search explores the neighborhood of a solution to find better solutions.
    7. Termination Criteria: Define the termination criteria for the algorithm. This can be a maximum number of iterations, reaching a certain quality threshold, or a specific condition defined by the problem.
    8. Result Extraction: Once the termination criteria are met, the best solution found by the ants can be extracted as the output of the algorithm.
    9. Iteration and Restart (optional): ACO can be run for multiple iterations or restarts to explore different regions of the search space and improve the quality of the solutions.
    
* SOS:
        - Idea: During the iteration, SOS randomly generates a group of organisms. Each organism represents a
    solution of the problem. The ancestor organisms evolve to the successor organisms through mutualism,
    commensalism and parasitism. In the evolution process, the organisms with a higher fitness value will be
    maintained to the next generation. The evolution is repeated until the termination conditions are met.
    At this time, the organism with the highest fitness value is output.
    ** SOS is used to optimize the two key parameters α and β.
    Objective function: Fitness(Y) = 1/d
     As the number of ants is m, each ant uses α and β values in Y to find their own HC. After m HCs are
    obtained, the local optimization strategy is applied to the shortest HC for finding another best HC.
    d is the length of the best HC.
        - Input: The number of organisms Y = [α, β], parameter space (khoảng giá trị mà của các tham số cần tối ưu)
        - Output: Set of optimized parameters

* Reverse operator
        - Idea: The reversal operator that the nearer cities will be connected with a higher
    probability -> This local optimization strategy is used to improve the solution quality searched by SOS–ACO
    and accelerate the convergence rate.
        - Input: The shortest HC searched by SOS-ACO
        - Output: The improved Hamiltonian Cycle

"""
from SOS import *
from parameter import *
from SOS_ACO import *
def main():
    """
    - Change parameter of the algoritm in parameter.py file
    - Read readme.txt for detail guidance
    """
    
    towns = TOWNS
    if(ANTS < 2):
        print("Need at least two ants to run this algorithms")
    sos = SOS(l_bound=PARAMETER_SPACE[0], u_bound=PARAMETER_SPACE[1],
              population_size=POP_SIZE,
              fitness_vector_size=DIM,
              ants=ANTS)

    ACO_optimizer = SOS_ACO(ants=ANTS, evaporation_rate=EVAPORATION_RATE,
                                    intensification=INTENSIFICATION, SOS_obj=sos,
                                    beta_evaporation_rate=BETA_EVAPORATION_RATE)
    ACO_optimizer.fit(spatial_map=towns, iterations = int(MAX_ITER_ACO), conv_crit=25)
    best_path, best , fit_time , best_series = ACO_optimizer.get_result()
    best_path_coor = [towns[i] for i in best_path]
    print("Best path : ", best_path_coor)

if __name__ == '__main__':
    main()
'''
COEN 379 Winter 2021 Homework 1 Problem 1
Shiva Govindaraju
Using Python 3 to run simulation to complete homework-problem.
--Use a Monte Carlo simulation with a million iterations to estimate the area enclosed by the curve whose equation is: (x^2+y^2)^2 = 2(x^2-y^2).
'''
import random as rand

'''
*Runs a Monte Carlo style simulation to estimate the area bounded by the shape in the First Quadrant. It picks "sim_num" points at random which may or may not fall within the bounded area. If the point does fall within the area, a counter is incremented. The counter itself is returned for the main function to compute an estimated area for the part of the shape in the First Quadrant.
'''
def monte_carlo_sim(sim_num):
    '''
    Runs a monte carlo simulation to find the area bounded by the shape in the First Quadrant.
    '''
    counter = 0 # counts the number of points within the shape.
    for sim in range(sim_num):
        x_2 = rand.random() ** 2 # x-coordinate is in range [0, 1]
        y_2 = (rand.random() ** 2) / 8 # y-coordinate is in range [0, 1 / (2 * sqrt(2))]
        if (x_2 + y_2) ** 2 <= (x_2 - y_2): # checks if point is within shape
            counter = counter + 1
    return counter

if __name__ == "__main__":
    print("--- COEN 379 Winter 2021 Homework 1 Problem 1---")
    sim_num = input("Number of iterations: ")
    if sim_num:
        sim_num = int(sim_num)
    else:
        sim_num = 1000000
    count = monte_carlo_sim(sim_num) # counts the number of points within shape out of simulation number
    print("Points within Shape: {}".format(count))
    print("Total Area of Shape: {}\n".format(4 * (count / sim_num))) # the ratio of in-shape/total is area.
                                                                    # multiplied by 4 for all 4 quadrants.
    #Some advanced code to run more than just 1 simulation and average all of them
    
    runs = int(input("Enter 0 to end Calculations.\nOr, please enter a value [0,100] to run multiple simulation-runs and average their calculated Areas: "))
    if runs:
        run_sum = 0
        for run in range(runs):
            count = monte_carlo_sim(sim_num)
            run_sum = run_sum + 4 * (count / sim_num)
        print("Average Calc for Total Area of Shape: {}\n".format(run_sum / runs))
    
    
    
    
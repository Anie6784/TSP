### **README**

**Description:**
This program is a Traveling Salesman Problem solver.

**Traveling Salesman Problem (TSP):**
The Given a set of cities and the distance between every pair of cities, the problem is to find the shortest possible route that visits every city exactly once and returns to the starting point (GeeksforGeeks, 2023).

**Instruction:**
- [ ] 1. Download the respitory
- [ ] 2. Run `main.py` in any Python Editor or IDE (ideally PyCharm or Visual Studio Code)
- [ ] 3. As the first prompt is printed, choose the map, from 1 to 6, that you want to solve. The maps are stored in the folder `inputs`. Check *File explaination* at the bottom for further information about the maps.
> Welcome to the Traveling Salesman Problem. Choose map number: 1.Indiana, or 2.TSP, or 3.TSP9, or 4.TSP21, or 5.TSP99, or 6.US: 
- [ ] 4. The program will print out all the names of included locations in order and the grid of cost to travel between locations.
- [ ] 5. The program will then create 10 generations of polulation with 15 individuals in each.
- [ ] 6. Lastly, the program will show the solution, which is the 11th generation, with the name of locations traveled in order and the total cost.

**File explanation:**
- `main.py` contains all prompts and inputs, as well as calling the Genertic Algorithm. Module used: `TSP` from `genetic`.
- `genetic.py` has the Genetic algorithm to solve the Traveling Salesman Problem. Module used: `heapq`, `randint` from `genetic`, and `deepcopy` from `copy`.
- `inputs` is a folder stores 6 of the maps that are used in this program. You can adjust the maps to yout liking. Each files has an interger `n` as the total number of locations, `n` names of locations, and `n`x`n` grid of numbers as the cost the travel from each location to another.

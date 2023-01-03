class Problem(object):

  def __init__(self, initial, goal=None):
    self.initial = initial
    self.goal = goal

  def actions(self, state):
    raise NotImplementedError

  def result(self, state, action):
    raise NotImplementedError

  def goal_test(self, state):
    if isinstance(self.goal, list):
      return is_in(state, self.goal)
    else:
      return state == self.goal

  def path_cost(self, c, state1, action, state2):
    return c + 1

  def value(self, state):
    raise NotImplementedError              
     

class Node:
  def __init__(self, state, parent=None, action=None, path_cost=0):
    self.state = state
    self.parent = parent
    self.action = action
    self.path_cost = path_cost
    self.depth = 0

    if parent:
      self.depth = parent.depth + 1

  def __repr__(self):
    return "".format(self.state)

  def __lt__(self, node):
    return self.state < node.state

  def expand(self, problem):
    return [self.child_node(problem, action) for action in problem.actions(self.state)]     

  def child_node(self, problem, action):
    next_state = problem.result(self.state, action)
    next_node = Node(next_state, self, action, problem.path_cost(self.path_cost, self.state, action, next_state)) 

    return next_node

  def solution(self):
    return [node.action for node in self.path()[1:]]

  def path(self):
    node, path_back = self, []
    while node:
      path_back.append(node)
      node = node.parent
    return list(reversed(path_back))    

  def __eq__(self, other):
    return isinstance(other, Node) and self.state == other.state

  def __hash__(self):
    return hash(self.state)      
     

def depth_limited_search_for_vis(problem):
  iterations, all_node_colors, node = depth_limited_search_graph(problem)
  return (iterations, all_node_colors, node)
     

def iterative_deepening_search_for_vis(problem):
  for depth in range(sys.maxsize):
    iterations, all_node_colors, node=depth_limited_search_graph_for_vis(problem)
    if iterations:
      return (iterations, all_node_colors, node)
     

romania_map = (dict(
    Arad = dict(Zerind=75, Sibiu=140, Timisoara=118),
    Bucharest = dict(Urziceni=85, Pitesti=101, Giurgiu=90, Fagaras=211),
    Craiova = dict(Drobeta=120, Rimnicu=146, Pitesti=138),
    Drobeta = dict(Mehadia=75),
    Eforie = dict(Hirsova=86),
    Fagaras = dict(Sibiu=99),
    Hirsova = dict(Urziceni=98),
    Iasi=dict(Vaslui=92, Neamt=87),
    Lugoj=dict(Timisoara=111, Mehadia=70),
    Oradea = dict(Zerind=71, Sibui=151),
    Pitesti = dict(Riminicu=97),
    Rimnicu=dict(Sibiu=80),
    Urziceni=dict(Vaslui=143),
))
     

romania_map = dict(
    Arad=(91, 492), Bucharest=(400, 327), Craiova=(253, 288),
    Drobeta=(165, 299), Eforie=(562, 293), Fagaras=(305, 449),
    Giurgiu=(375, 270), Hirsova=(534, 350), Iasi=(473, 506),
    Lugoj=(165, 379), Mehadia=(168, 339), Neamt=(406, 537),
    Oradea=(131, 571), Pitesti=(320, 368), Rimnicu=(233, 410),
    Sibiu=(207, 457), Timisoara=(94, 410), Urziceni=(456, 350),
    Vaslui=(509, 444), Zerind=(108, 531)
)
     

all_node_colors = []
romania_problem = GraphProblem('Arad', 'Bucharest', romania_map)
display_visual(rominia_graph_data, 
               user_input=False, 
               alogrithm=iterative_deepening_search_for_vis,
               problem=romania_problem)
     

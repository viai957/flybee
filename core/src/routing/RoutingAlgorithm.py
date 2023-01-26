class RoutingAlgorithm:
    def __init__(self, graph, weighting, traversal_mode):
        self.graph = graph
        self.weighting = weighting
        self.traversal_mode = traversal_mode
        self.node_access = None
        self.edge_explorer = None
        self.max_visited_nodes = None
        self.already_run = None

        if not self.weighting.hasTurnCosts():
            raise Exception("Weighting must have turn costs for edge-based traversal mode")
        if self.traversal_mode != TraversalMode.EDGE_BASED:
            raise Exception("Only edge-based traversal mode is supported")
        
        self.node_access = graph.getNodeAccess()
        self.edge_explorer = graph.createEdgeExplorer(self.weighting)

    def setMaxVisitedNodes(self, max_visited_nodes):
        self.max_visited_nodes = max_visited_nodes

    def accept(self, u, v):
        return True

    def checkAlreadyRun(self):
        if self.already_run:
            raise Exception("Routing algorithm already run")
        self.already_run = True

    def calcPaths(self, from_point, to_point):
        raise NotImplementedError("Method not implemented")
        
    def createEmptyPath(self):
        raise NotImplementedError("Method not implemented")

    def getName(self):
        return self.__class__.__name__

    def __str__(self):
        return self.getName() + "|" + self.weighting.toString()
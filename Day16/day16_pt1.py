#!/usr/bin/env python3
import sys
import os
import copy

sys.path.append(os.path.abspath('../'))
from chart import Chart
from coordinate import Coordinate

class WeightedNode:
    def __init__(self, position):
        self.position = position
        self.neighbors = {}

    def add_neighbor(self, node, weight):
        self.neighbors[node] = weight

    def __str__(self):
        rs = f"WeightedNode({ self.position },"
        for n in self.neighbors:
            rs += f"({n.position.x}, {n.position.y}, {self.neighbors[n]})"
        rs += ")"
        return rs

class WeightedGraph(Chart):
    def __init__(self, lines):
        super().__init__(lines)
        self.start = WeightedNode(self.find('S')[0])
        self.end = None
        self.nodes = set() # Node Set
        self.cheapest = None

    def calc_weight(self, node_a, node_b):
        return abs(node_a.position.x - node_b.position.x) + abs(node_a.position.y - node_b.position.y)

    def get_node(self, coordinate):
        for node in self.nodes:
            if coordinate == node.position:
                return node

        return None

    def check_possible_node(self, coordinate):
        neighbors = [neighbor for neighbor in self.get_valid_neighbours(coordinate) if self.get(neighbor) in '.SE']
        if len(neighbors) > 2:
            return True
        if len(neighbors) == 2:
            if neighbors[0].x != neighbors[1].x and neighbors[0].y != neighbors[1].y:
                return True
        
        return False

    def find_neighbor_nodes(self, node):
        self.nodes.add(node)
        grid_neighbors = self.get_valid_neighbours(node.position)

        check_directions = []
        for gn in grid_neighbors:
            if self.get(gn) in '.SE':
                check_directions.append(gn - node.position)

        for d in check_directions:
            next_pos = node.position + d

            while self.get(next_pos) != '#':
                if self.check_possible_node(next_pos):
                    neighbor_node = self.get_node(next_pos)
                    if neighbor_node:
                        node.add_neighbor(neighbor_node, self.calc_weight(node, neighbor_node))
                    else:
                        new_node = WeightedNode(next_pos)
                        node.add_neighbor(new_node, self.calc_weight(node, new_node))
                        self.find_neighbor_nodes(new_node)
                        
                        if self.get(next_pos) == 'E':
                            self.end = new_node

                    break

                next_pos = next_pos + d

    def traverse(self, view_direction, node, path, cost):
        if node == self.end:
            if self.cheapest is None:
                self.cheapest = cost
            else:
                self.cheapest = min(self.cheapest, cost)

            return

        elif node in path:
            return

        else:
            for neighbor in node.neighbors:
                neighbor_path = copy.copy(path)
                neighbor_path.append(node)
                neighbor_dir = neighbor.position - node.position
                neighbor_dir.normalize()
                
                if view_direction == neighbor_dir:
                    self.traverse(neighbor_dir, neighbor, neighbor_path, cost + node.neighbors[neighbor])
                elif view_direction == neighbor_dir * -1:
                    self.traverse(neighbor_dir, neighbor, neighbor_path, cost + 2000 + node.neighbors[neighbor])
                else:
                    self.traverse(neighbor_dir, neighbor, neighbor_path, cost + 1000 + node.neighbors[neighbor])


if __name__ == '__main__':
    wg = None

    with open(sys.argv[1]) as file:
        lines = []
        for line in file:
            lines.append(line.strip())

        wg = WeightedGraph(lines)

    wg.print()
    wg.find_neighbor_nodes(wg.start)

    #for n in wg.nodes:
    #    wg.set(n.position, 'X')

    print(str(wg.start))
    wg.traverse(Coordinate(1,0), wg.start, [], 0)

    print(wg.cheapest)


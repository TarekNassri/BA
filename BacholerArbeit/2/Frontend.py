from tkinter import *
import networkx as nx
from pandas import DataFrame

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
def ford_fulkerson(graph, source, sink, debug=None):
    flow, path = 0, True

    while path:
        # search for path with flow reserve
        path, reserve = depth_first_search(graph, source, sink)
        flow += reserve

        # increase flow along the path
        for v, u in zip(path, path[1:]):
            if graph.has_edge(v, u):
                graph[v][u]['flow'] += reserve
            else:
                graph[u][v]['flow'] -= reserve

        # show intermediate results
        if callable(debug):
            debug(graph, path, reserve, flow)


def depth_first_search(graph, source, sink):
    undirected = graph.to_undirected()
    explored = {source}
    stack = [(source, 0, dict(undirected[source]))]

    while stack:
        v, _, neighbours = stack[-1]
        if v == sink:
            break

        # search the next neighbour
        while neighbours:
            u, e = neighbours.popitem()
            if u not in explored:
                break
        else:
            stack.pop()
            continue

        # current flow and capacity
        in_direction = graph.has_edge(v, u)
        capacity = e['capacity']
        flow = e['flow']
        neighbours = dict(undirected[u])

        # increase or redirect flow at the edge
        if in_direction and flow < capacity:
            stack.append((u, capacity - flow, neighbours))
            explored.add(u)
        elif not in_direction and flow:
            stack.append((u, flow, neighbours))
            explored.add(u)

    # (source, sink) path and its flow reserve
    reserve = min((f for _, f, _ in stack[1:]), default=0)
    path = [v for v, _, _ in stack]

    return path, reserve
window = Tk()
window.title("Graphs")

graph = nx.DiGraph()
graph.add_nodes_from('ABCDEFGH')
graph.add_edges_from([
    ('A', 'B', {'capacity': 4, 'flow': 0}),
    ('A', 'C', {'capacity': 5, 'flow': 0}),
    ('A', 'D', {'capacity': 7, 'flow': 0}),
    ('B', 'E', {'capacity': 7, 'flow': 0}),
    ('C', 'E', {'capacity': 6, 'flow': 0}),
    ('C', 'F', {'capacity': 4, 'flow': 0}),
    ('C', 'G', {'capacity': 1, 'flow': 0}),
    ('D', 'F', {'capacity': 8, 'flow': 0}),
    ('D', 'G', {'capacity': 1, 'flow': 0}),
    ('E', 'H', {'capacity': 7, 'flow': 0}),
    ('F', 'H', {'capacity': 6, 'flow': 0}),
    ('G', 'H', {'capacity': 4, 'flow': 0}),

])

layout = {
    'A': [0, 1], 'B': [1, 2], 'C': [1, 1], 'D': [1, 0],
    'E': [2, 2], 'F': [2, 1], 'G': [2, 0], 'H': [3, 1],
}

def draw_graph():
    # create first place for plot
    ax1 = f.add_subplot(211)
    nx.draw_networkx_nodes(graph, layout, node_color='steelblue', node_size=600, ax = ax1)
    nx.draw_networkx_edges(graph, layout, edge_color='gray', ax = ax1)
    nx.draw_networkx_labels(graph, layout, font_color='white', ax = ax1)

    for u, v, e in graph.edges(data=True):
        label = '{}/{}'.format(e['flow'], e['capacity'])
        color = 'green' if e['flow'] < e['capacity'] else 'red'
        x = layout[u][0] * .6 + layout[v][0] * .4
        y = layout[u][1] * .6 + layout[v][1] * .4
        ax1.text(x, y, label, size=16, color=color, horizontalalignment='center', verticalalignment='center')

    right_frame.draw()

def flow_debug(graph, path, reserve, flow):
    print('flow increased by', reserve,
          'at path', path,
          '; current flow', flow)
    draw_graph()

def plot_max_flow():
    ford_fulkerson(graph, 'A', 'H', flow_debug)


top_left_frame = Frame(window)
top_left_frame.pack(side = LEFT)

VertexData = Entry(top_left_frame)
VertexData.pack()

insertButton = Button(top_left_frame, text = "Insert Vertex")
insertButton.pack(side = LEFT)

delete_button = Button(top_left_frame, text = "Delete Vertex")
delete_button.pack(side = RIGHT)

insertButton = Button(top_left_frame, text = "MaxFlow", command = lambda:ford_fulkerson(graph, 'A', 'H', flow_debug))
insertButton.pack(side = RIGHT)


f = plt.Figure(figsize=(5, 5), dpi=100)
right_frame = FigureCanvasTkAgg(f, master=window)
right_frame.get_tk_widget().pack(side=RIGHT, fill = BOTH, expand=1)
right_frame.draw()
toolbar = NavigationToolbar2Tk(right_frame, window)
right_frame._tkcanvas.pack(side = RIGHT)
toolbar.update()

window.mainloop()
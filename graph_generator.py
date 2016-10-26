from os import system
from igraph import *
from random import randint, randrange

# each node have one of these colors according to its type
color_dict = {"1": "lightblue", "2": "lightgreen"}
names = ['client', 'server']

# count of vertices, a random number under 15.
vertices_count = randint(0, 15)
edge_list = []

# add edges to edge list
for i in range(int(1.4*vertices_count)):
    s = randrange(0, vertices_count)
    d = randrange(0, vertices_count)

    # if source and destination are same change the destination
    while s == d:
        d = randrange(0, vertices_count)

    # add (source, destination) to edge list if its not added before.
    if (s, d) not in edge_list:
        edge_list.append((s, d))

# create new graph
new_graph = Graph()

new_graph.add_vertices(vertices_count)
new_graph.vs['name'] = ['%s_%s' % (names[randint(0, 1)], item) for item in range(vertices_count)]
new_graph.vs['type'] = ['1' if str(item).startswith('client') else '2' for item in new_graph.vs['name']]

# add edges to graph
for edge in edge_list:
    new_graph.add_edge(*edge)

# specify source and sink node by random
source_node = randrange(0, vertices_count)
sink_node = randrange(0, vertices_count)

# source and sink must be different
while source_node == sink_node:
    sink_node = randrange(0, vertices_count)

# compute shortest path from source to sink
shortest_path = new_graph.get_all_shortest_paths(source_node, sink_node)

# terminal output shortest path
print 'the shortest path from source node (%s) to sink node (%s) is: ' % \
      (new_graph.vs['name'][source_node], new_graph.vs['name'][sink_node])

if not shortest_path:
    print 'no route from source to sink!'
else:
    for item in shortest_path:
        print item

image_styles = {
    'layout': new_graph.layout('kk'),
    'bbox': (800, 500),
    'vertex_size': 70,
    'vertex_color': [color_dict[item] for item in new_graph.vs['type']],
    'vertex_label': new_graph.vs['name'],
    'edge_width': 2,
    'margin': 50
}

# plot new graph to result.png
plot(new_graph, 'result.png', **image_styles)

# save result to text files
system('touch result path.txt')  # create text files if they don't exists.
new_graph.save('result', format='adjacency')  # export graph to result matrix or graphml

# export path to text file
f = open('path.txt', 'w')
f.write('the shortest path from source node (%s) to sink node (%s) is:\n' %
        (new_graph.vs['name'][source_node], new_graph.vs['name'][sink_node]))

if not shortest_path:
    f.write('no route from source to sink! \n')

for item in shortest_path:
    f.write('%s\n' % item)


f.close()


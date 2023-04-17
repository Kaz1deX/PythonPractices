import graphviz


def draw(vertices, edges):
    dot = graphviz.Digraph()
    # Вершины
    for vertex in vertices:
        dot.node(str(vertex[0]), vertex[1])
    # Ребра
    for edge in edges:
        dot.edge(str(edge[0]), str(edge[1]))
    # Граф
    dot.format = 'png'
    dot.render(
        'C:\\Users\\Maxim\\PythonPractices\\Homeworks\\HomeWork_4\\graph', view=True)


draw([(1, 'v1'), (2, 'v2')], [(1, 2), (2, 3), (2, 2)])

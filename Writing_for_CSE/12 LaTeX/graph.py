from graphviz import Source


vertex = """

digraph vertex_1{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";

    a1 [label="a"];
    a2 [label="a"];
    a3 [label="a"];

    a1 -> e [label="q"];
    a1 -> a3 [label="p"];
    a1 -> a2 [label="p"];
    a2 -> a3 [label="r"];
    
}

digraph vertex_2{
    layout=neato;
    node [shape = circle];
    edge [arrowhead=none, arrowtail=none];

    a1 [label="a"];
    a2 [label="a"];
    a3 [label="a"];
    d [pos="1.5,0.5!"];

    a3 -> d [label="r"];
    a1 -> a3 [label="p"];
    a1 -> a2 [label="p"];
    a2 -> a3 [label="r"];
}

digraph vertex_join{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";

    a1 [label="a"];
    a2 [label="a"];
    a3 [label="a"];

    a1 -> e [label="q"];
    a1 -> a3 [label="p"];
    a1 -> a2 [label="p"];
    a2 -> a3 [label="r"];
    a3 -> d [label="r"];
    
}

"""

edge = """
digraph edge_1{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";

    a1 [label="a"];
    a2 [label="a"];
    a3 [label="a"];

    a1 -> a3 [label="p"];
    a1 -> a2 [label="p"];
    a2 -> a3 [label="r"];
    a1 -> f [label="q"];
    
}

digraph edge_2{
    layout=neato;
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";

    a1 [label="a"];
    a2 [label="a"];
    a3 [label="a"];
    f[pos="0.5,-0.5!"];

    a1 -> a3 [label="p"];
    a1 -> a2 [label="p"];
    a2 -> a3 [label="r"];
    a3 -> f [label="r"];
    
}

digraph edge_join{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";

    a1 [label="a"];
    a2 [label="a"];
    a3 [label="a"];

    a1 -> a3 [label="p"];
    a1 -> a2 [label="p"];
    a2 -> a3 [label="r"];
    a1 -> f [label="q"];
    a3 -> f [label="r"];
    
}
"""

apriori = """
digraph G1{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";
    
    a -> b[label="p"];
    a->e[label="q"];
    b->e[label="r"];
    b->c[label="r"];
    b->d[label="r"];
    c->d[label="p"];

}

digraph G2{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";
    
    a -> b[label="p"];
    a->d[label="q"];
    b->d[label="r"];

}

digraph G3{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";
    
    a->b[label="r"];
    a->c[label="r"];
    b->c[label="p"];
    c->d[label="q"];
    c->e[label="p"];

}

digraph G4{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";
    
    a->e[label="q"];
    a->c[label="p"];
    e->c[label="p"];
    c->d[label="p"];

}

digraph apriori_1{
    layout=neato;
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    
    a[pos="0,0!"];
    b[pos="1,0!"];
    c[pos="2,0!"];
    d[pos="3,0!"];
    e[pos="4,0!"];
    
}

digraph apriori_2_1{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";

    a->b[label="p"];
    
}

digraph apriori_2_2{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";

    a->e[label="q"];
    
}

digraph apriori_2_3{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";

    b->d[label="r"];
    
}

digraph apriori_2_4{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";

    c->d[label="p"];
    
}

digraph apriori_2_5{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";

    c->e[label="p"];
    
}

digraph apriori_3{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";

    a->b[label="p"];
    b->d[label="r"];
    
}
"""

algo_example="""
digraph G1{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";
    
    a -> b[label="p", color="RED"];
    a->e[label="q"];
    b->e[label="r"];
    b->c[label="r"];
    b->d[label="r"];
    c->d[label="p"];

}

digraph G2{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";
    
    a -> b[label="p", color="RED"];
    a->d[label="q"];
    b->d[label="r"];

}

digraph G3{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";
    
    a->b[label="r", color="RED"];
    a->c[label="r"];
    b->c[label="p"];
    c->d[label="q"];
    c->e[label="p"];

}

digraph G4{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";
    
    a->e[label="q"];
    a->c[label="p"];
    e->c[label="p"];
    c->d[label="p"];

}
"""

ex="""
digraph G1{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";
    
    a -> b[label="p", color="RED"];
    a->e[label="q", color="RED"];
    b->e[label="r"];
    b->c[label="r"];
    b->d[label="r", color="RED"];
    c->d[label="p", color="RED"];

}

digraph G2{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";
    
    a -> b[label="p", color="RED"];
    a->d[label="q"];
    b->d[label="r", color="RED"];

}

digraph G3{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";
    
    a->b[label="r"];
    a->c[label="r"];
    b->c[label="p"];
    c->d[label="q"];
    c->e[label="p", color="RED"];

}

digraph G4{
    edge [arrowhead=none, arrowtail=none];
    node [shape = circle];
    rankdir="LR";
    
    a->e[label="q", color="RED"];
    a->c[label="p"];
    e->c[label="p", color="RED"];
    c->d[label="p", color="RED"];

}
"""

v = Source(vertex, filename="vertex", format="png")
v.view()

e = Source(edge, filename="edge", format="png")
e.view()

p = Source(apriori, filename="apriori", format="png")
p.view()

g = Source(algo_example, filename="G_example", format="png")
g.view()

g2 = Source(ex, filename="ex", format="png")
g2.view()
from graphviz import Source

# # g2.node_attr['fontname'] = 'NanumMyeongjo' #NanumGothic
temp = """

digraph G {
    
    zippers5[shape=plaintext];
    node [shape = record,height=.1, style=rounded];
    n1[label = "<f0>Zipper |{left|<f1>.} |{focus|<f2>.} |{<f3> right|.}| {<f4> top|.}" ];
    n2[label = "<f0>List |<f1>. |<f2> .|<f3> ." ];
    n3[label = "<worm>", style="filled, rounded", fillcolor="grey"];
    n4[label = "<fruit>"];
    n5[label = "<f0>leaf |{value|<f1>.}" ];
    n6[label = "<f0>leaf |{value|<f1>.}" ];
    
    n7[label = "3" ];
    n8[label = "2" ];

    zippers5 -> n1:f0;
    n1:f1 -> n2:f0;
    n1:f2 -> n3;

    n2:f1 -> n4;
    n2:f2->n5:f0;
    n2:f3->n6:f0;

    n5:f1->n7;
    n6:f1->n8;
}
"""

s = Source(temp, filename="rob2", format="png")
s.view()
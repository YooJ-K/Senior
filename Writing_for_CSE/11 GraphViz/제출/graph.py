
from graphviz import Source

temp = """

digraph node_data2 {
    node [shape = record,height=.1];
    node0[label = "<f1> data2|<f2> next", color="RED"];
} 

digraph node_shape {
    node [shape = record,height=.1];
    node0[label = "<f1> data|<f2> next"];
} 


digraph del_node_5_1 {
    layout=neato;
    node [shape = record,height=.1];
    node0[label = "head", pos = "0,0!"];
    node1[label = "data1|next", pos = "1.5,0!"];
    node2[label = "data2|next", pos = "3.25,0!", color="red"];
    node3[label = "data5|next", pos = "5,0!"];
    node4[label = "data3|next", pos = "6.75,0!"];
    node5[label = "data4|next", pos = "8.5,0!"];
    node6[label = "NULL", pos = "10,0!"];

    node0->node1->node2->node3->node4->node5->node6;
} 


digraph del_node_5_2 {
    layout=neato;
    node [shape = record,height=.1];
    node0[label = "head", pos = "0,0!"];
    node1[label = "data1|next", pos = "1.5,0!"];
    node2[label = "data2|next", pos = "3.25,0!"];
    node3[label = "data5|next", pos = "5,0.5!"];
    node4[label = "data3|next", pos = "6.75,0!"];
    node5[label = "data4|next", pos = "8.5,0!"];
    node6[label = "NULL", pos = "10,0!"];

    node0->node1->node2;
    node3->node4->node5->node6;
    node2->node4[style="filled", color="red", penwidth="3"];
} 


digraph del_node_5_3 {
    layout=neato;
    node [shape = record,height=.1];
    node0[label = "head", pos = "0,0!"];
    node1[label = "data1|next", pos = "1.5,0!"];
    node2[label = "data2|next", pos = "3.25,0!"];
    node3[label = "data5|next", pos = "5,0.5!", fontcolor="lightgrey", color="lightgrey"];
    node4[label = "data3|next", pos = "6.75,0!"];
    node5[label = "data4|next", pos = "8.5,0!"];
    node6[label = "NULL", pos = "10,0!"];

    node0->node1->node2;
    node4->node5->node6;
    node2->node4[style="filled", color="red", penwidth="3"];
} 

digraph initial {
    layout=neato;
    peripheries=0;
    node [shape = record,height=.1];
    node0[label = "head", pos = "0,0!"];
    node1 [label = "NULL", pos = "1,0!"];
    node0->node1[style=dashed];
} 


digraph add_node_2_1 {
    layout=neato;
    node [shape = record,height=.1];
    node0[label = "head", pos = "0,0!"];
    node1[label = "data1|next", pos = "1.5,0!", color = "RED"];
    node2[label = "data2|next", pos = "2,-0.5!"];
    node3[label = "NULL", pos = "3,0!"];

    node0->node1->node3;
    node2;
} 


digraph add_node_2_2 {
    layout=neato;
    node [shape = record,height=.1];
    node0[label = "head", pos = "0,0!"];
    node1[label = "data1|next", pos = "1.5,0!"];
    node2[label = "data2|next", pos = "2,-0.5!"];
    node3[label = "NULL", pos = "3,0!"];

    node0->node1;
    node3;
    node1->node2->node3[style=dashed];
} 


digraph add_node_2_3 {
    layout=neato;
    node [shape = record,height=.1];
    node0[label = "head", pos = "0,0!"];
    node1[label = "data1|next", pos = "1.5,0!"];
    node2[label = "data2|next", pos = "3.25,0!"];
    node3[label = "NULL", pos = "4.75,0!"];

    node0->node1;
    node1->node2->node3[color = "RED"];
} 


digraph add_node_5_1 {
    layout=neato;
    node [shape = record,height=.1];
    node0[label = "...", pos = "0,0!", shape=plaintext];
    node1[label = "data2|next", pos = "1.5,0!"];
    node2[label = "data3|next", pos = "3.25,0!"];
    node3[label = "...", pos = "4.75,0!", shape=plaintext];

    node5[label = "data5|next", pos = "2.4, -0.5!", color="RED"]

    node0->node1->node2->node3;
} 


digraph add_node_5_2 {
    layout=neato;
    node [shape = record,height=.1];
    node0[label = "...", pos = "0,0!", shape=plaintext];
    node1[label = "data2|next", pos = "1.5,0!"];
    node2[label = "data3|next", pos = "3.25,0!"];
    node3[label = "...", pos = "4.75,0!", shape=plaintext];

    node5[label = "data5|next", pos = "2.4, -0.5!"]

    node0->node1;
    node2->node3;

    node1->node2[color="lightgrey", style="dashed"];

    node1->node5->node2[color="RED"];
} 


digraph node_5_3 {
    layout=neato;
    node [shape = record,height=.1];
    node0[label = "head", pos = "0,0!"];
    node1[label = "data1|next", pos = "1.5,0!"];
    node2[label = "data2|next", pos = "3.25,0!"];
    node3[label = "data5|next", pos = "5,0.5!", fontcolor="lightgrey", color="lightgrey"];
    node4[label = "data3|next", pos = "6.75,0!"];
    node5[label = "data4|next", pos = "8.5,0!"];
    node6[label = "NULL", pos = "10,0!"];

    node0->node1->node2;
    node4->node5->node6;
    node2->node4[style="filled", color="red", penwidth="3"];
} 


digraph node_5 {
    layout=neato;
    node [shape = record,height=.1];
    node0[label = "head", pos = "0,0!"];
    node1[label = "data1|next", pos = "1.5,0!"];
    node2[label = "data2|next", pos = "3.25,0!"];
    node3[label = "data3|next", pos = "5,0!"];
    node4[label = "data4|next", pos = "6.75,0!"];
    node5[label = "NULL", pos = "8.25,0!"];

    node0->node1->node2->node3->node4->node5;
} 


digraph node_6 {
    layout=neato;
    node [shape = record,height=.1];
    node0[label = "head", pos = "0,0!"];
    node1[label = "data1|next", pos = "1.5,0!"];
    node2[label = "data2|next", pos = "3.25,0!"];
    node3[label = "data5|next", pos = "5,0!"];
    node4[label = "data3|next", pos = "6.75,0!"];
    node5[label = "data4|next", pos = "8.5,0!"];
    node6[label = "NULL", pos = "10,0!"];

    node0->node1->node2->node3->node4->node5->node6;
} 


digraph add_graph {
    layout=neato;
    node [shape = record,height=.1];
    node0[label = "header", pos = "0,0!"];
    node1[label = "data1|pointer", pos = "1.5,0!"];
    node2[label = "data2|pointer", pos = "3.25,0!"];
    node3[label = "NULL", pos = "5,0!"];

    node0->node1->node2->node3;
} 



"""

s = Source(temp, filename="list", format="jpg")
s.view()

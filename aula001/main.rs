mod graph;
mod adjacency_list;
mod adjacency_matrix;
mod edge_list;

use graph::Graph;
use std::fmt::Debug;

fn main() {

  let mut g1 = adjacency_list::AdjList::new(5);
  let mut g2 = adjacency_matrix::AdjMatrix::new(5);
  let mut g3 = edge_list::EdgeList::new();

  fn add_edges ( g: &mut dyn Graph) {
    g.add_edge(1, 2);
    g.add_edge(2, 3);
    g.add_edge(3, 4);
    g.add_edge(4, 2);
    g.add_edge(4, 5);
    println!("g: {:?}", g);
  }

  add_edges(&mut g1);
  add_edges(&mut g2);
  add_edges(&mut g3);

}
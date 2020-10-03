use graph::Graph;

#[derive(Debug)]
pub struct EdgeList {
  edges : Vec<(usize, usize)>
}

impl EdgeList {
  pub fn new() -> Self {
    Self{ edges : Vec::new() }
  }
}

impl Graph for EdgeList {
  fn add_edge(self : &mut Self, u: usize, v: usize) {
    self.edges.push((u, v));
  }
}


use graph::Graph;

#[derive(Debug)]
pub struct AdjList {
  adjs : Vec<Vec<usize>>
}

impl AdjList {
  pub fn new(n : usize) -> Self {
    Self{ adjs : vec![Vec::new(); n+1] }
  }

}
impl Graph for AdjList {
  fn add_edge(self : &mut Self, u: usize, v: usize) {
    self.adjs[u].push(v)
  }
}

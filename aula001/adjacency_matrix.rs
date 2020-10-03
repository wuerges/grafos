use graph::Graph;

#[derive(Debug)]
pub struct AdjMatrix {
  mat : Vec<Vec<bool>>,
}

impl AdjMatrix {
  pub fn new(n : usize) -> Self {
    Self{ 
      mat : vec![vec![false;n+1]; n+1] ,
    }
  }
}

impl Graph for AdjMatrix {
  fn add_edge(self : &mut Self, u: usize, v: usize) {
    self.mat[u][v] = true;
  }
}


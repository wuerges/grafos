pub trait Graph {
    fn add_edge(self : &mut Self, u: usize, v: usize);
}
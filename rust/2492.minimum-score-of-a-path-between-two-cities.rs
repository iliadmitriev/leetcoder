struct UF {
  cap: usize,
  par: Vec<usize>,
  min: Vec<i32>,
}

impl UF {
  pub fn new(cap: usize) -> Self {

    return Self{
      cap: cap,
      par: Vec::from_iter(0..cap),
      min: vec![i32::MAX; cap],
    }
  }

  pub fn find(&mut self, mut x: usize) -> usize {
    while x != self.par[x] {
      self.par[x] = self.par[self.par[x]];
      x = self.par[x];
    }

    x
  }

  pub fn join(&mut self, x: usize, y: usize, mut w: i32) {
    let par_x = self.find(x);
    let par_y = self.find(y);

    w = self.min[par_x].min(w);
    w = self.min[par_y].min(w);

    self.par[par_y] = par_x;
    self.min[par_x] = w;
  }

  pub fn get_min(&mut self, x: usize) -> i32 {
    let par_x = self.find(x);

    self.min[par_x]
  }
}

impl Solution {
    pub fn min_score(n: i32, roads: Vec<Vec<i32>>) -> i32 {
        let mut uf = UF::new(n as usize);

        for r in roads.iter() {
          let from = r[0] as usize - 1;
          let to = r[1] as usize - 1;
          let len = r[2];

          uf.join(from, to, len);
        }

        uf.get_min(n as usize - 1)
    }
}
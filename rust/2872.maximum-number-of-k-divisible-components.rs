
impl Solution {
    fn dfs(
        node: usize,
        parent: Option<usize>,
        graph: &Vec<Vec<usize>>,
        values: &Vec<i32>,
        k: u64,
    ) -> (u64, i32) {
        let mut total = values[node] as u64;
        let mut comp = 0;

        for &child in graph[node as usize].iter() {
            if Some(child) == parent {
                continue;
            }

            let (child_total, child_comp) = Self::dfs(child, Some(node), graph, values, k);
            total += child_total;
            comp += child_comp;
        }

        if total % k == 0 {
            comp += 1;
        }

        (total, comp)
    }

    pub fn max_k_divisible_components(
        n: i32,
        edges: Vec<Vec<i32>>,
        values: Vec<i32>,
        k: i32,
    ) -> i32 {
        let n = values.len();
        let mut graph: Vec<Vec<usize>> = vec![vec![]; n];

        for edge in edges {
            let u = edge[0] as usize;
            let v = edge[1] as usize;

            graph[u].push(v);
            graph[v].push(u);
        }

        let (_, comp) = Self::dfs(0, None, &graph, &values, k as u64);
        return comp;
    }
}
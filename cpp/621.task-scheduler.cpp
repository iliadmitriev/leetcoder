class Solution {
public:
  int leastInterval(vector<char> &tasks, int n) {
    // use max priority queue to store the count of each task
    // use queue to store the task and time when it should be done
    //

    priority_queue<int, vector<int>, less<int>> pq;
    map<char, int> freq;
    for (auto t : tasks)
      freq[t]++;
    for (auto f : freq)
      pq.push(f.second);

    int time = 0;
    queue<pair<int, int>> q;

    while (!pq.empty() || !q.empty()) {
      if (!pq.empty()) {
        int c = pq.top() - 1;
        pq.pop();

        if (c)
          q.push({time + n, c});
      }

      if (!q.empty() && q.front().first <= time) {
        int c = q.front().second;
        q.pop();
        pq.push(c);
      }

      time++;
    }

    return time;
  }
};
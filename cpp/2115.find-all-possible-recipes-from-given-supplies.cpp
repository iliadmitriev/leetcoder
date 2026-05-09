#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using std::string, std::unordered_map, std::queue, std::unordered_set,
    std::vector;

class Solution {
public:
  vector<string> findAllRecipes(vector<string> &recipes,
                                vector<vector<string>> &ingredients,
                                vector<string> &supplies) {
    vector<string> done;
    const int N = recipes.size();
    unordered_map<string, vector<string>> adj;
    unordered_set<string> recipesSet(recipes.begin(), recipes.end());
    unordered_map<string, int> inDegree;
    queue<string> q;

    for (auto &sup : supplies) {
      q.push(sup);
    }

    for (int i = 0; i < N; i++) {
      for (auto ing : ingredients[i]) {
        adj[ing].push_back(recipes[i]);
        inDegree[recipes[i]]++;
      }
    }

    while (q.size()) {
      auto ing = q.front();
      q.pop();

      if (recipesSet.count(ing)) {
        done.push_back(ing);
      }

      for (auto &nextIng : adj[ing]) {
        inDegree[nextIng]--;
        if (inDegree[nextIng] == 0) {
          q.push(nextIng);
        }
      }
    }

    return done;
  }
};
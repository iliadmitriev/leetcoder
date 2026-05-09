
#include <sstream>
#include <string>
#include <vector>

using std::vector, std::string;

// ["MESSAGE", "timestamp_i", "mentions_string_i"]
// ["OFFLINE", "timestamp_i", "id_i"]
// mentions_string_i = "id1 id2 id3" || "ALL" || "HERE"
//
const string MESSAGE = "MESSAGE";
const string OFFLINE = "OFFLINE";
const string HERE = "HERE";
const string ALL = "ALL";
const int OFFINE_PERIOD = 60;

class Solution {
private:
  vector<int> extractIds(const string &mentions) {
    std::istringstream iss(mentions);
    vector<int> ids;
    string id;

    while (iss >> id) {
      // cut id000 -> 000
      ids.push_back(stoi(id.substr(2)));
    }

    return ids;
  }

public:
  vector<int> countMentions(int numberOfUsers, vector<vector<string>> &events) {
    vector<int> mentions(numberOfUsers, 0);
    vector<int> offline(numberOfUsers, 0);

    std::sort(events.begin(), events.end(),
              [](const vector<string> &a, const vector<string> &b) {
                // match timestamp(1) first, then type (0) OFFLINE < MESSAGE
                if (a[1] == b[1]) {
                  return a[0][0] > b[0][0];
                };

                // sort by timestamp
                int a1 = std::stoi(a[1]);
                int b1 = std::stoi(b[1]);
                return a1 < b1;
              });

    for (const vector<string> &ev : events) {
      int cur_time = std::stoi(ev[1]);

      if (ev[0] == MESSAGE) {
        if (ev[2] == "ALL") {
          for (int i = 0; i < numberOfUsers; i++) {
            mentions[i]++;
          }
        } else if (ev[2] == "HERE") {
          for (int i = 0; i < numberOfUsers; i++) {
            if (offline[i] <= cur_time) {
              mentions[i]++;
            }
          }
        } else {
          for (int id : extractIds(ev[2])) {
            mentions[id]++;
          }
        }
      } else if (ev[0] == OFFLINE) {
        int user_id = std::stoi(ev[2]);
        offline[user_id] = cur_time + OFFINE_PERIOD;
      }
    }

    return mentions;
  }
};

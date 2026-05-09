#include <deque>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using std::tuple, std::deque, std::unordered_set, std::vector,
    std::unordered_map;

// packet = (Source, Destination, Timestamp)
typedef tuple<int, int, int> Packet;

// Custom hash function for Packet
struct PacketHasher {
  size_t operator()(const Packet &key) const {
    auto [source, destination, timestamp] = key;

    return ((size_t)source * 1315423911u) ^
           ((size_t)destination * 2654435761u) ^ ((size_t)timestamp * 97531u);
  }
};

class Router {
private:
  int memoryLimit;
  deque<Packet> packets;                    // FIFO queue of packets
  unordered_set<Packet, PacketHasher> seen; // unique set of seen packets
  unordered_map<int, vector<int>>
      counters; // destination -> ordered list of timestamps

  void push(Packet pack) {
    auto [_, dest, tm] = pack;

    packets.push_back(pack);
    seen.insert(pack);
    counters[dest].push_back(tm);
  }

  Packet pop() {
    Packet pack = packets.front();
    packets.pop_front();
    seen.erase(pack);

    auto [_, dest, tm] = pack;

    auto &counter = counters[dest];

    int left = bisectLeft(counter, tm);
    if (left < counter.size() && counter[left] == tm) {
      left++;
    }

    counter.erase(counter.begin(), counter.begin() + left);

    return pack;
  }

  int bisectLeft(const vector<int> &arr, int target) {
    int lo = 0, hi = arr.size(), mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (arr[mid] < target) {
        lo = mid + 1;
      } else {
        hi = mid;
      }
    }

    return lo;
  }

  int bisectRight(const vector<int> &arr, int target) {
    int lo = 0, hi = arr.size(), mid;

    while (lo < hi) {
      mid = (lo + hi) / 2;

      if (target < arr[mid]) {
        hi = mid;
      } else {
        lo = mid + 1;
      }
    }

    return lo;
  }

public:
  Router(int memoryLimit) : memoryLimit(memoryLimit) {}

  bool addPacket(int source, int destination, int timestamp) {

    Packet pack{source, destination, timestamp};
    if (seen.find(pack) != seen.end()) {
      return false;
    }

    if (packets.size() == memoryLimit) {
      pop();
    }

    push(pack);

    return true;
  }

  vector<int> forwardPacket() {
    if (packets.empty()) {
      return {};
    }

    auto [source, dest, tm] = pop();

    return {source, dest, tm};
  }

  int getCount(int destination, int startTime, int endTime) {
    auto &counter = counters[destination];
    auto left = lower_bound(counter.begin(), counter.end(), startTime),
         right = upper_bound(counter.begin(), counter.end(), endTime);
    return right - left;
  }
};

/**
 * Your Router object will be instantiated and called as such:
 * Router* obj = new Router(memoryLimit);
 * bool param_1 = obj->addPacket(source,destination,timestamp);
 * vector<int> param_2 = obj->forwardPacket();
 * int param_3 = obj->getCount(destination,startTime,endTime);
 */
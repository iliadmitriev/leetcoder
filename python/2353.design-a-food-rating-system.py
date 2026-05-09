class SortedList(list):
        
    def append(self, _item):
        idx = bisect_right(self, _item)
        self.insert(idx, _item)
    
    def index(self, _item):
        idx = bisect_left(self, _item)

        if idx == len(self) or _item != self[idx]:
            raise ValueError(f'{_item} not in list')

        return idx

    def remove(self, _item):
        idx = bisect_right(self, _item) - 1

        if _item != self[idx]:
            raise ValueError('list.remove(x): x not in list')

        self.pop(idx)


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        """O(n) * ln(n)"""
        self._cuisine_food = {}
        self._food_rating = {}
        self._food_cuisine = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            list_of_food = self._cuisine_food.setdefault(cuisine, SortedList())
            list_of_food.append((-rating, food))

            self._food_rating.setdefault(food, rating)
            self._food_cuisine.setdefault(food, cuisine)
        

    def changeRating(self, food: str, newRating: int) -> None:
        """O(ln(n))"""
        oldRating = self._food_rating[food]
        cuisine = self._food_cuisine[food]

        self._cuisine_food[cuisine].remove((-oldRating, food))
        self._cuisine_food[cuisine].append((-newRating, food))

        self._food_rating[food] = newRating
        

    def highestRated(self, cuisine: str) -> str:
        """O(1)"""
        _, highiestFood = self._cuisine_food[cuisine][0]

        return highiestFood


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
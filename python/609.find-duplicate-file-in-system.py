class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        
        for path in paths:
            values = str.split(path, ' ')
            root = values.pop(0)
            
            for file in values:
                filename, content = str.split(file, '(')
                data[content].append(root + '/' + filename)
                
        return [data[i] for i in data.keys() if len(data[i]) > 1]
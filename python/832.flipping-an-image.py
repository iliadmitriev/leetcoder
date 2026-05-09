class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        m, n = len(image), len(image[0])

        for i in range(m):
            for j in range(n // 2):
                image[i][j], image[i][n - 1 - j] = (
                    1 - image[i][n - 1 - j],
                    1 - image[i][j],
                )

        # if number of columns is odd: middle column (n // 2) exists
        if n % 2:
            for i in range(m):
                image[i][n // 2] = 1 - image[i][n // 2]

        return image


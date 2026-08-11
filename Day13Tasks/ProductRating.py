import numpy as np

ratings = np.array([2, 3, 4, 5, 1])

minimum_rating = np.min(ratings)
maximum_rating = np.max(ratings)

normalized_ratings = (
    (ratings - minimum_rating) /
    (maximum_rating - minimum_rating)
)

print("Original ratings:", ratings)
print("Minimum rating:", minimum_rating)
print("Maximum rating:", maximum_rating)
print("Normalized ratings:", normalized_ratings)
import numpy as np

scores = np.array([50, 60, 70, 80, 90, 100, 110, 120])
servers = np.array_split(scores, 4)

for number, server_scores in enumerate(servers, start=1):
    print("Server", number, ":", server_scores)
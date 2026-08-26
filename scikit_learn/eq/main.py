'''7a+3b+4c+9d'''
from random import randint
from sklearn.linear_model import LinearRegression

# Step 1: Generate training data
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

TRAIN_INPUT = []
TRAIN_OUTPUT = []

for i in range(TRAIN_SET_COUNT):

    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    d = randint(0, TRAIN_SET_LIMIT)
    # Calculate output
    op = (7 * a) + (3 * b) + (4 * c)+(9*d)

    TRAIN_INPUT.append([a, b, c, d])
    TRAIN_OUTPUT.append(op)

# Step 2: Create model
model = LinearRegression()

# Step 3: Train model
model.fit(TRAIN_INPUT, TRAIN_OUTPUT)

# Step 4: Give new input
prediction = model.predict([[7, 8, 9, 12]])

# Step 5: Display prediction
print("Prediction:", prediction)
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

# Load data from the pickle file
data_dict = pickle.load(open('./data.pickle', 'rb'))

# Extract data and labels
data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# Initialize the RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=None, random_state=42)

# Train the model
model.fit(x_train, y_train)

# Make predictions on the test set
y_predict = model.predict(x_test)

# Evaluate the accuracy of the model
score = accuracy_score(y_predict, y_test)

print('{}% of samples were classified correctly!'.format(score * 100))

# Save the trained model to a file
with open('model.p', 'wb') as f:
    pickle.dump({'model': model}, f)

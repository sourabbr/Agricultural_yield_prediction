#save the training classifier
# serialize model to JSON
model_json = classifier.to_json()
with open("bloodcelltrained.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
classifier.save_weights("bloodcelltrained.h5")
print("Saved model to disk")

# load json and create model
json_file = open('bloodcelltrained.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
classifier = model_from_json(loaded_model_json)
# load weights into new model
classifier.load_weights("bloodcelltrained.h5")
print("Loaded model from disk")

import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_table('SMSSpamCollection', sep='\t', header=None, names=['label', 'sms_message'])

df['label'] = df.label.map({'ham': 0, 'spam': 1})
X_train, X_test, Y_train, Y_test = train_test_split(df['sms_message'],
                                                   df['label'],
                                                   random_state=1)
# print ('Number of rows in the total set:{}'.format(df.shape[0]))
# print ('Number of rows in the training set:{}'.format(X_train.shape[0]))
# print ('Number of rows in the test set: {}'.format(X_test.shape[0]))
# count_vector = CountVectorizer()
# training_data = count_vector.fit_transform(X_train)
# testing_data = count_vector.transform(X_test)
# naive_bayes = MultinomialNB()
# naive_bayes.fit(training_data, Y_train)
# predictions = naive_bayes.predict(testing_data)
#
# print ('Accuracy score: ', format(accuracy_score(Y_test, predictions)))
# print ('Precision score: ', format(precision_score(Y_test, predictions)))
# print ('Recall score: ', format(recall_score(Y_test, predictions)))
# print ('F1 score: ', format(f1_score(Y_test, predictions)))
# print predictions
# print training_data

# print testing_data
# print (df.shape)
# print ('Number of rows in the training set:{}'.format(Y_train.shape[0]))
# print ('Number of rows in the test set: {}'.format(Y_test.shape[0]))

print df.head(100)

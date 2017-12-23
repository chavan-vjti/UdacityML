#import LinearRegression, create regression (name it reg)
#and fit it to the training data
from sklean.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(ages_train, net_worths_train)

print "Katie's net worth prediction:", reg.predict([27])
print "Slope:", reg.coef_
print "intercept:", reg.intercept_
print "r-squared score:", reg.score(ages_test, net_worths_test)

print "r-squared score", reg.score(ages_train, net_worths_train)

#Output
# Katie's net worth prediction: [160.43256987]
# Slope: [[6.47356894]]
# intercept: [-14.35324586]
# r-squared score: 0.812365978
# r-squared score: 0.874569575

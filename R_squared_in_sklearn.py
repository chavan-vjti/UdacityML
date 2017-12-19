ages.append (random.randint(20,65))
net_worths = [ii * 6.25 + numpy.random.normal(scale=40.) for ii in ages)]
# need message list into a 2D numpy array to get it to work in LinearRegression
ages = numpy.reshape(numpy.array(ages), (len(ages),))
net_worths = numpy.reshape(numpy.array(net_worths),(len(net_worths),1))
plt.scatter(ages, net_worths)
plt.xlabel("ages")
plt.ylabel("net_worths")
plt.show()

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(ages, net_worths)
print "Katie's net worth prediction: ", reg.predict([27])
print "r-squared score:", reg.score(ages, net_worths)
print "slope:", reg.coef_
print "intercept:", reg.intercept_

#Plotting the prediction
plt.scatter(ages, net_worths)
plt.plot(ages, reg.predict(ages), color='blue', linewidth=3)
plt.xlabel("ages")
plt.ylabel("net_worths")
plt.show()

#Output
#Katie's net worth prediction:[160.4498898]
#r-squared score: 0.85764353
#slope:[[6.5334546]]
#intercept: [-15.952389976]

#The data is for Age(x-axis) and Net worth(y-axis)
#The data contains test data and train data
from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()

reg = studentReg(ages_train, net_worths_train)

###add then there's some visualization code down here

plt.clf()
plt.scatter( ages_train, net_worths_train, color='b', label='train_data')
plt.scatter( ages_test, net_worths_train, color='r', label='test_data')
plt.plot(ages_test, reg.predict(ages_test), color="black")
plt.legend(loc=2)
plt.xlabel("ages")
plt.ylabel("net worths")

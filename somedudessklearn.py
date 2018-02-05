def predict(user, event):
    """This is the sklearn function that somebody else wrote"""
    return "After " + event

if __name__ == '__main__':
    """Here we test the above function"""
    print("Predicting what happens if i do predict('Joe', 'Eight')")
    print(predict("Joe", "Eight"))


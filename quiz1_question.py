data = [10, 20, 30]
data.append(40)
subject = "Analytics"

if len(data) == 4 and subject.startswith("Ana"):
    print(subject[:3] + str(data[-1]))
else:
    print("Condition failed")
import math
def isclose(x,y):
    if math.floor(x/10) == math.floor(y//10)-1 or math.floor(x/10) == math.floor(y//10) or math.floor(x/10) == (math.floor(y//10)+1)%10:
        if math.floor(x%10) == math.floor(y%10)-1 or math.floor(x%10) == math.floor(y%10) or math.floor(x%10) == (math.floor(y%10)+1)%10:
            return True
    
def predict(data):
    probs=dict(zip(list(range(100)),[0 for _ in range(100)]))
    for i in range(10,len(data)-1):
        for j in range(9):
            if isclose(data[i-j],data[-(j+1)]):
                probs[data[i+1]]+=1
                if data[i-1]==data[-1]:
                    probs[data[i+1]]+=2
            else:
                break
    return max(probs, key=probs.get)
f = open("rand.txt", "r")
data = f.read().split('\n')
for i in range(len(data)):
    data[i]=int(data[i])
def run():
    while True:

        # Setup the model, data, loss function and optimizer
        # Train the model
        prediction = predict(data)
        inps = input("Enter a number 1-100:")
        print(f'Predicted next number: {prediction:.4f}')
        f = open("rand.txt", "a")

        f.write('\n')
        f.write(inps)
        f.close() 
        data.append(int(inps))


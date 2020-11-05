import winsound 

# frequency is set to 500Hz 
# freq = 10000

# duration is set to 100 milliseconds			 
dur = 100


for i in range(37,15000,500):
    freq=i
    dur = 1000
    print("#######")
    print(freq)
    print (dur)
    print("#######")
    winsound.Beep(freq, dur)


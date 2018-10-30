import numpy
import random
import time
import matplotlib.pyplot as plt

window_size = 10   #window size (sample space)
t_series = []      #time series
count = 0          #counter to index data  
last=0             #lastly predicted data 
deg=3              #order of the polynomial

epoch=10           #number of iteration (for plotting)

eqn=''             #preficted equation
actual_val=[]      #actual value list (for plot)
pred_val=[]        #predicted value list (for plot)

# generates value from the predicted eqn 
def _eval(coef, t):     
    global eqn
    print('\ncoef : ', coef)
    eqn=f=numpy.poly1d(coef)
    return(f(t))

# predict the fitted polynomial
def predict():
    x=numpy.arange(len(t_series))
    #print('\nx=',x)
    coef = list(numpy.polyfit(x,t_series,deg))
    return coef

#definite loop till the epoch
def loop():
    global count
    global t_series
    global last
    global epoch
    while (epoch > 0):
        #preventing infinite loop    
        epoch -=1
        print(f'epoch : {epoch}')

        #if window size exceeds remove first data to limit size
        
        if len(t_series) >= window_size :
            t_series.pop(0)
        #add new timestamp 
        t_series.append(time.time())
       
        count += 1

        #start predicting after having deg +1 amount of data 
        if(count >= (deg +1)):
            #relative Error 
            epsilon = ((abs(last - t_series[len(t_series) -1]) / t_series[len(t_series) -1] )) * 100
            '''
            list_mean = sum(t_series) / len(t_series)
            abs_delta = abs(last - t_series[len(t_series) -1])
            epsilon = ((list_mean - abs_delta)/ abs_delta) * 100
            '''
            actual_val.append(t_series[len(t_series) -1])
            pred_val.append(last)

            # curve fitting 
            last = next_val = _eval(predict(), count)

        print(t_series)
        
        if(count >= deg+1):
            print('\npredicted',next_val)
            print('Error',epsilon, '%')
       
        time.sleep(random.randint(1,5))

#plot function 
def plot_me():
    plt.plot(actual_val,'--',label='Actual')
    plt.plot(pred_val,'-o', label='Predicted')
    plt.title('Reference Forcast Analysis')
    plt.xlabel('Time Sample')
    plt.ylabel('Occurance Sample')
    plt.legend(loc='upper right', shadow=True, fontsize='large')
    plt.figtext(.7, .9, "Fitted Polynomial : " + str(eqn))
    plt.show()
    
    
         
def main():
    loop()
    plot_me()

main()

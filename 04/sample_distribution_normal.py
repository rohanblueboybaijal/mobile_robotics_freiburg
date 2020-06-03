import numpy as np 
import timeit 
import matplotlib.pyplot as plt  
import scipy.stats
import math

def sample_normal(mu, sigma):
    x = np.sum(np.random.uniform(-sigma, sigma, 12))
    x = x/2
    return mu + x 

def sample_normal_rejection(mu, sigma):
    interval = 5*sigma 
    max_density = scipy.stats.norm(mu, sigma).pdf(mu)

    while True:
        x = np.random.uniform(mu-interval, mu+interval, 1)[0]
        y = np.random.uniform(0, max_density, 1)
        if y<=scipy.stats.norm(mu, sigma).pdf(x):
            break
    return x 

def sample_normal_boxmuller(mu, sigma):
    u = np.random.uniform(0,1,2)

    x = math.cos(2*np.pi*u[0])*math.sqrt(-2*math.log(u[1]))

    return mu + sigma*x

def evaluate_sampling_time(mu, sigma, n_samples, sample_function):
    t1 = timeit.default_timer()

    for i in range(n_samples):
        sample_function(mu, sigma)
    
    t2 = timeit.default_timer() 

    time_per_sample = (t2-t1)/n_samples*1e6
    print("%30s : %.3f us" % (sample_function.__name__, time_per_sample))


def evaluate_sampling_dist(mu, sigma, n_samples, sample_function):
    n_bins = 100
    samples = []
    for i in range(n_samples):
        samples.append(sample_function(mu,sigma))
    print("%30s : mean = %.3f, std_dev = %.3f" % (sample_function.__name__, np.mean(samples), np.std(samples)))

    plt.figure()
    count, bins, ignored = plt.hist(samples, n_bins, normed=True)
    plt.plot(bins, scipy.stats.norm(mu, sigma).pdf(bins), linewidth=2, color='r')
    plt.xlim([mu-5*sigma, mu+5*sigma])
    plt.title(sample_function.__name__)


def main():

    mu, sigma = 0, 1

    sample_functions = [sample_normal, sample_normal_rejection, sample_normal_boxmuller, np.random.normal]

    for fnc in sample_functions:
        evaluate_sampling_time(mu, sigma, 1000, fnc)

    n_samples = 10000
    print("evaluting sample distances with:" )
    print(" mean :", mu)
    print(" std_dev :", sigma)
    print(" samples :", n_samples)

    for fnc in sample_functions:
        evaluate_sampling_dist(mu, sigma, n_samples, fnc)
    
    plt.show()


if __name__ == "__main__":
    main()

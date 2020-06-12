- [ ] Investigate why `timeit` results are slower for the KD tree in [using_kdtree.py](src/using_kdtree.py). 
According to the course, it should be the other way around. It happens the same using
ipython:
```
In [2]: %run -n src/using_kdtree.py                                                                                                                                                                  

In [3]: lat, lng = 34.3852712, -119.487444                                                                                                                                                           

In [4]: drivers = gen_drivers(lat, lng)                                                                                                                                                              

In [5]: %timeit find_closest((lat, lng), drivers)                                                                                                                                                    
6.7 µs ± 149 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)

In [6]: tree = KDTree(drivers)                                                                                                                                                                       

In [7]: %timeit find_closest_kd((lat, lng), tree)                                                                                                                                                    
71.4 µs ± 6.12 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)

In [8]: 6.7/71.4                                                                                                                                                                                     
Out[8]: 0.0938375350140056

In [9]: 71.4/6.7                                                                                                                                                                                     
Out[9]: 10.656716417910449
```
The first approach is around 10 times faster (99% speed-up)
- [ ] What are the performance restrictions? 

Designing a system that will process data in a minute is very different from designing one that processes data 
in a millisecond. We should get hard numbers from the stakeholders. 

- [ ] How do we measure performance? 

Do we use averages, medians, quantiles? How can we instrument our code to measure performance and how can we view it? 

- [ ] Can we remove any code? 

The fastest code is the code that is not executed. A great optimisation might be deleting a in-house code and 
replacing it with a third-party library that's much faster. 

- [ ] Do we have too many components? 

Function calls in Python are expensive. And calling a service is even more expensive. We should think of ways to 
eliminate calls to components and services. 

- [ ] Do we do too much serialization? 

A common mistake is that the function gets the data as a string, tt passes the string to another function, that then
passes it to another. Most of these functions are parsing the string into a datetime object. 
It's better that the initial function will do the parsing once and then pass the datetime object downward. 
Same for serialization. We should serialize and de-serialize at the edges of the program and use the right Python 
data structure in the middle. 

- [ ] Are the right algorithms and data-structures used? 

We should try to use the right algorithms and data structures. 
We often go with algorithm we know. However, the team as a whole might know much more and come up with a better
solution. Even if the team doesn't know, asking people to do research and come up with alternatives, may do wonders 
to the code performance.
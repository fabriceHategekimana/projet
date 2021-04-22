## Exercise 1. Fourier Transform properties (2 points)
In this exercise, you will prove formulas from page 102 Theme 7 of the course.  

(a) Gaussian filter.  
Use the time derivative property of the FT and the formula for the FT of the Gaussian to prove the result.  
![](images/01.jpeg)  
![](images/02.jpeg)  

(b) Gabor filter:  
Use the product theorem and your knowledge of FT for cosine signals to prove the result.  
![](images/03.jpeg)

(c) unsharp mask  
Use the linearity of the FT to prove the result.  
![](images/04.jpeg)  

(d) symmetric square pulse  
Use the Convolution theorem for FT to compute explicitely the FT H(w).  
![](images/05.jpeg)  

## Exercise 2. Continuous signal filtering (2 points)  
Using the convolution theorem for FT, we can see that filtering corresponds to multiplication in the frequency domain. The goal is now for you to explore the effect of filtering a continuous signal f (t), with the filters from exercise 1 viewed in frequency domain.  

For the illustration, you can take the signal F (w) = sinc 2 (w).  
(a) On four different graphs, represent :  

	- The Gaussian signal with sigma = 1,  
	- its Fourier transform  
	- The FT of the signal,  
	- The product G(w)*F(w)  

![ga01](images/ga01.png)
![ga02](images/ga02.png)
![ga03](images/ga03.png)
![ga04](images/ga04.png)
	
By refering to the convolution theorem, explain the following sentence :  
"Filtering a signal with a Gaussian blur kills high frequencies."  

(b) Do the same for the Gabor filter with w 0 = 10 and explain the following sentence :  
"Filtering with a Gabor filter at frequency w 0 only keeps the parts of the signal which  
have a frequency close to w0"  

![gab01](images/gab01.png)
![gab02](images/gab02.png)
![gab03](images/gab03.png)
![gab04](images/gab04.png)

(c) Repeat again the same steps for the unsharp mask with y= 1.5 and explain :  
"The Unsharp mask filtering sharpens the signal by reducing low frequency components."  

![un01](images/un01.png)
![un02](images/un02.png)
![un03](images/un03.png)
![un04](images/un04.png)

## Exercise 3. The Dirac comb (part 2) (2 points)

(b) Illustrate point (a) with the hat function:

![hT1](images/hT1.png)
![hdT1](images/hdT1.png)
![hT1_5](images/hT1_5.png)
![hdT1_5](images/hdT1_5.png)
![hT2](images/hT2.png)
![hdT2](images/hdT2.png)
![hT4](images/hT4.png)
![hdT4](images/hdT4.png)


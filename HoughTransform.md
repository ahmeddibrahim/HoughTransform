

                                    Hough Transform

**Hough** **Lines:**

**Implementation** **details:**

The Hough line function takes 3 parameters, which are the image,

edged image, and threshold. The image itself is taken to draw the

lines calculated in the Hough transform and returns it on the image.

The edged image is having the image blurred using the Gaussian blur

and transformed into only the edges, the canny edge detector was

used in the below examples, to be used through out the Hough

transform. Lastly, a threshold, which is the number votes needed to

draw a line on an edge or link an edge. The main formula used in this

implementation is :

**Rho=** **x** **cos(theta)** **+** **y** **sin(theta)**

As we are given the x and y, which are the coordinates or pixels of the

image, we have two unknown variables, which are rho and theta.

Thus, the function firstly starts by creating an array of the possible

thetas, from 0 to 180 and apply it into the equation to attain the

respective rho values. Such calculations are done only if we find a

pixel in the edged image that is an edge, i.e. doesn’t have the value of

\0. It then calculates all the possible combinations of theta and rho,

and such values increment the accumulator according to the indexes

of rho and theta. An issue occurred when indexes the Rho’s as some

of the values were returned negative, thus to solve this issue, the

function adds by the maximum distance in the polar, which is

**“** **r=** **sqrt(x^2+y^2)”**

Finally according to the threshold given, the function goes through

the accumulator and finds numbers relevant with the threshold and

draws the line accordingly.





**Hough** **circle:**

**Implementation** **details:**

As the Hough lines, the Hough circle takes the same parameters with

respects to its threshold. The main equation used in this

implementation is the equation of the circle, which is :

**(y-cx)^2** **+** **(x-cy)^2** **=** **r^2**

As described previously, the images coordinates x and y are the only

parameters given and thus, we have 3 unknown variables here,

which are cx,cy and r. To reduce the complexity of the function, a

predefined radius, r, was given to the function, as we know before

hand the problem we are going to approach. Thus, the problem

becomes to find cx and cy, which are the center of the circle trying to

detect. To be able to get them, the function tries a range of

coordinates according to the radius, to get out of the range of the

circle. Thus, the possible ranges used to find cx and cy according to

the radius was:

**All** **cxs’=** **range(cx-radius,** **cx+radius)**

**All** **cys’=** **range(cy-radius,** **cy+radius)**

According to such cxs’ and cys’, the accumulator is incremented

according to the index of all the possible points of cx and cy. Finally,

according to the threshold, the function goes through the

accumulator and finds the relevant coordinates according to the

threshold and use cv.circle to draw the circles.

**Outputs:**

**Note:** According to the requirement, the same settings was kept on

all the image, which was:

Gaussian blur filter 11x11

Canny 80x80

Line threshold: 97

Circle threshold: 56





**Plain** **background** **and** **non-overlapping**





**Noisy** **background** **and** **non-overlapping**





**Plain** **background** **and** **overlapping**





**Noisy** **background** **and** **overlapping**


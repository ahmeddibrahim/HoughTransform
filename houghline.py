from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.pyplot as plt
import matplotlib.lines as mlines


img = cv2.imread('paper_noise.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(gray,(11,11),0)

edges = cv2.Canny(blur,80,80,apertureSize = 3)
# cv2.imshow('pls',edges)
# cv2.waitKey(0)
# exit()
def hough(img,edges,threshold,threshold_circle):
        
        height,width=edges.shape
        thetas = np.arange(0,180)
        r=(np.sqrt(width**2 + height**2)) # distance formula r^2=x^2+y^2
        rhos=np.arange(-r,r) # possible combinations of rhos
        accum_array= np.zeros((len(rhos),len(thetas))) # hough line accumaltor
        accum_circle= np.zeros((height,width)) # hough circle accumaltor 
        radius=39 # The radius of the coins to be detected ( to reduce the complexity of trying every radius)

        for y in range(height):
                for x in range(width):
                        ## Hough lines ## 
                        if(edges[y,x]!=0): # if an edge exists
                                for theta in thetas: # go through the possible thetas
                                        rho=x*np.cos(np.deg2rad(theta)) + y*np.sin(np.deg2rad(theta))+r # polor equation to get rho and plus the max distance to cover the negative coordinates values
                                        accum_array[int(rho),(theta)]+=1 # increment the hough line accumaltor 

                                
                                ### Hough circle ####
                                for cy in range(y-radius,y+radius): # A possible range for the center of x
                                        for cx in range(x-radius,x+radius):#  A possible range for the center of y

                                                r1 = int(np.sqrt(((y-cy) ** 2) + ((x-cx) ** 2))) # get the radius with the possible centers to check if we got the same radius
                                                if r1 == radius and cx < width and cy < height and cx>=0 and cy>=0: # boundary checking
                                                        accum_circle[cy][cx] += 1 # increment the circle accumaltor

                                
                                # for cx in range(x-radius,x+radius): # using formula (x-cx)^2 + (y-cy)^2 = r^2 to get cy
                                #         #cy=sqrt{r^2 - cx^2 + 2cx*x - x^2}+y, -sqrt{r^2 - cx^2 + 2cx*x - x^2}+y
                                #         quad= (radius**2 + cx**2 + 2*cx*x - x**2 ) # sqrt{r^2 - cx^2 + 2cx*x - x^2} 
                                #         if(quad<0):
                                #                 continue
                                #         cy_1=int(np.sqrt(quad)+y)  
                                #         cy_2= int(-np.sqrt(quad)+y)
                                #         if cx < width and cx>=0:
                                #                 if cy_1 < height and cy_1>=0:
                                #                         accum_circle[cy_1][cx]+=1
                                #                 if cy_2 >=0 and cy_2<height:
                                #                         accum_circle[cy_2][cx]+=1

        ## draw the lines 
        for y in range(accum_array.shape[0]):
                for x in range(accum_array.shape[1]):
                        if accum_array[y][x] > threshold:
                                rho = rhos[y]
                                theta = thetas[x]
                                a = np.cos(np.deg2rad(theta))
                                b = np.sin(np.deg2rad(theta))
                                x0 = (a * rho) 
                                y0 = (b * rho) 
                                x1 = int(x0 + 1000 * (-b))
                                y1 = int(y0 + 1000 * (a))
                                x2 = int(x0 - 1000 * (-b))
                                y2 = int(y0 - 1000 * (a))
                                cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 2)
        
        ## draw the circles
        for y in range(accum_circle.shape[0]):
                for x in range(accum_circle.shape[1]):
                        if accum_circle[y][x] > threshold_circle:
                                center=(x,y)
                                # cv2.circle(img, center, 1, (0, 100, 100), 3)
                                radius= 39
                                cv2.circle(img, center, radius, (255, 0, 255), 3) 
#function ends
####################################################################################################
## calling the function (main program)
hough(img,edges,97,56) 
cv2.imshow('output',img)

cv2.waitKey(0)


# circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 1,
#                                param1=100, param2=10,
#                                minRadius=41, maxRadius=41)
# print(circles.shape)
# if circles is not None:
#         circles = np.uint16(np.around(circles))
#         for i in circles[0, :]:
#                 center = (i[0], i[1])
#                 # circle center
#                 cv2.circle(img, center, 1, (0, 100, 100), 3)
#                 # circle outline
#                 radius = i[2]
#                 cv2.circle(img, center, radius, (255, 0, 255), 3)                              


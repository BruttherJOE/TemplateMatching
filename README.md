## Feature Matching

I am using `PIL` library for screengrab, and `cv2` to do template matching. `PIL` is used instead of `pyautogui` because it is lighter and therefore probably more likely to escape detection from software attempting to detect screengrabs.


This is a test file and will be used to build other python files. I first define a template image, called "template".



This is the test picture that I have used :

![testMoo](.\assets\testMoo.png)



If I run the python file, it seems it is able to detect the image on my screen without any problems because no pixels changed.

![image-20230812215150002](.\assets\image-20230812215150002.png)

However, If i move it up by 1 slot, it is still able to find the image, but not with 100% certainty.

![image-20230812215050940](.\assets\image-20230812215050940.png)


To solve this problem we can take the template to be the inside of the image. This way, no matter where it is on the screen, feature matching would be able to find the object.



In my code, it is converted to grayscale because it only has one channel (intensity) rather than having 3 channels (RGB). This reduces the complexity of comparing pixel values and improves the chances of detecting patterns regardless of their color.

Meanwhile, "threshold" rejects the image if it is below a certain confidence level.

However, this might not be good if color information is crucial to detect images.
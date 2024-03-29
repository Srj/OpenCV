## IO Operation with OpenCV :

### **Read a Image** :

Reading an image with OpenCV is a single line code. We will use `imread` function for this purpose.
```python
import cv2
img = cv2.imread('data/IO.png',1)
```
That's it.

**But wait !!!**

 **Why is there a `1` in argument?** 
 
 This is because `imread` also requires a flag to specify how the image will be read. For example, `1` means read the image in 3 Channel BGR (OpenCV's way to say RGB) format, `0` means read the image in 1 channel black & white format. For a full list of possible flags refer to here [IMREAD_COLOR](https://docs.opencv.org/master/d8/d6a/group__imgcodecs__flags.html#ga61d9b0126a3e57d9277ac48327799c80).

 **Okay, Now, what is in `img` ?**

 `img` contains a numpy ndarray. If it is a color image, then it will be 3D array with shape (Height, Width, Channel). For Grayscale( fancy term for black & white), it will be a 2D array with shape (Height, Weight). Be careful that there is no third dimension for grayscale images.

 **What if the path is invalid?**

Surprising, `imread` doesn't raise any exception if no image is found in the given path. It continues to run and put a `NoneType` object in `img` which might cause some cryptic error later. So it is good to check `img` after read operation whether it is `None`.

```python
import cv2
img = cv2.imread('data/IO.png',1)
if img is None:
    raise Exception
```

Okay, Now that we are Done with reading let's learn about some writing.

### **Write an Image**

Again it is simple oneliner. We will use `imwrite` API  to write an ndarray as our desired image format.

```python
cv2.imwrite(Path, img)
```
That's it. Your `img` ndarray will be saved in `Path`.

### **Show an Image**

You can display any loaded image into a seperate window. `imshow` comes handy here.

```python
cv2.imshow('Image', img)
```
**Why is the `'Image'` there?

It is the name for your window.

**But i didn't see any image after running the code!!!**

That's because you code will not pause anywhere and execute to the end and stop. So, Your window will be vanished within split second.

**So, How can i pause after showing the image in a window?**

`waitKey` is the API to go.
```python
cv2.imshow('Image',img)
k = cv2.waitKey(0)
```

**Why is there a `0` ?**

It means wait indefinitely. You can also specify a miliseconds to pause. Basically, `waitKey` waits until any key is pressed and assign the ASCII code of the key into `k`.
Now based on the value of `k`, you can take appropriate action.

```python
cv2.imshow('image',img)

#Number of ms you want to wait. Give 0 to wait until the window is closed.
#The pressed key will be saved in 'k'
#Some 64 bit machine requires '& 0xFF' after wait key
k = cv2.waitKey(0)

if k == 27: #27 is ESC
    #Destroys all windows
    cv2.destroyAllWindows()
```
For Example, Here we have commanded to destroy all opened windows if ESC is pressed.







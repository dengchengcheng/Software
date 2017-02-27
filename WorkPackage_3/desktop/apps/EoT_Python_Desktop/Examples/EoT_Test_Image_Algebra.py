from eot import Image

image1 = Image(2,2, Image.CCV_8U | Image.CCV_C1)
image2 = Image(2,2, Image.CCV_8U | Image.CCV_C1)

image1.set_pixel(0,0,1)
image1.set_pixel(0,1,2)
image1.set_pixel(1,0,3)
image1.set_pixel(1,1,4)
image2.set_pixel(0,0,1)
image2.set_pixel(0,1,2)
image2.set_pixel(1,0,3)
image2.set_pixel(1,1,4)

print ("Suma")
imageRes = image1.add(image2, 0)
imageRes.get_pixel(0,0)
imageRes.get_pixel(0,1)
imageRes.get_pixel(1,0)
imageRes.get_pixel(1,1)

print ("Resta")
imageRes = image1.subtract(image2, 0)
imageRes.get_pixel(0,0)
imageRes.get_pixel(0,1)
imageRes.get_pixel(1,0)
imageRes.get_pixel(1,1)

print ("Multiply")
imageRes = image1.multiply(image2, 0)
imageRes.get_pixel(0,0)
imageRes.get_pixel(0,1)
imageRes.get_pixel(1,0)
imageRes.get_pixel(1,1)

print ("Sum")
image1.sum(Image.CCV_UNSIGNED)

print ("Variance")
image1.variance()

print ("Scale")
imageRes = image1.scale(0, 2)
imageRes.get_pixel(0,0)
imageRes.get_pixel(0,1)
imageRes.get_pixel(1,0)
imageRes.get_pixel(1,1)

print ("Gemm")
image1 = Image(2,2, Image.CCV_64F | Image.CCV_C1)
image2 = Image(2,2, Image.CCV_64F | Image.CCV_C1)
image1.set_pixel(0,0,1)
image1.set_pixel(0,1,2)
image1.set_pixel(1,0,3)
image1.set_pixel(1,1,4)
image2.set_pixel(0,0,1)
image2.set_pixel(0,1,2)
image2.set_pixel(1,0,3)
image2.set_pixel(1,1,4)

imageRes = image1.gemm(image2, 1, 0, 0, 0, 0)
imageRes.get_pixel(0,0)
imageRes.get_pixel(0,1)
imageRes.get_pixel(1,0)
imageRes.get_pixel(1,1)


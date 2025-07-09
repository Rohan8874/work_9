from skimage import io, img_as_float
import bm3d 
import cv2

noisy_img = img_as_float(io.imread("images/noisy_img.jpg", as_gray=True))

BM3D_Denoised = bm3d.bm3d(noisy_img, sigma_psd=0.3, stage_arg=bm3d.BM3DStages.ALL_STAGES )

cv2.imshow("original", noisy_img)
cv2.imshow("Denoised", BM3D_Denoised)
cv2.waitKey(0)
cv2.destroyAllWindows()
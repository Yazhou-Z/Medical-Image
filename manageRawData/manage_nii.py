# This file is to move the nifti image upward.
from nibabel.viewers import OrthoSlicer3D
import nibabel as nib
import numpy as np


# Function: 把一个nifti图像竖直上拉
#           pos以上为空白部分，把这部分切掉，并补到图像下端
# Input: img, the vertical position
# Output: the new image will be saved as 'new.nii'
def upward_nii(img, pos):

    # 把原图像分割成上下两部分
    tem = img.slicer[:256, :pos, ...]
    nib.save(tem, 'tem.nii')
    vacan = img.slicer[:256, pos:, ...]
    nib.save(vacan, 'vacan.nii')

    print(img.dataobj.shape)
    print(tem.dataobj.shape)
    print(vacan.dataobj.shape)
    OrthoSlicer3D(img.dataobj).show()
    OrthoSlicer3D(tem.dataobj).show()
    OrthoSlicer3D(vacan.dataobj).show()

    # convert to array后merge
    tem = np.array(tem.dataobj)
    vacan = np.array(vacan.dataobj)
    new = np.append(vacan, tem, axis=1)
    # print(new)
    new_img = nib.Nifti1Image(new, img.affine)
    nib.save(new_img, 'new.nii')


def main():
    filename = 'origin042.nii'
    img = nib.load(filename)
    pos = 236
    upward_nii(img, pos)


main()

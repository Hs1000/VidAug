from moviepy.editor import VideoFileClip,vfx
import glob
def upsampling(amt):
    count=400
    for i in glob.glob(r"F:/UCF/help/videos/*.mp4"):
        vi=VideoFileClip(i)
        my_clip = vi.fx(vfx.speedx,amt)
        my_clip.write_videofile(r"F:/UCF/help/upsample_2.5/vid%d.mp4" % count)
        my_clip.close()
         #cv2.imwrite("vid%d.mp4" % count, image) 
        count=count+1
#     #print(i)
# =============================================================================
upsampling(1.5)
upsampling(2)        
upsampling(2.5)


from moviepy.editor import VideoFileClip,vfx
import glob
def downsampling(amt):
    count=400
    for i in glob.glob(r"F:/UCF/help/videos/*.mp4"):
        vi=VideoFileClip(i)
        my_clip = vi.fx(vfx.speedx,amt)
        my_clip.write_videofile(r"F:/UCF/help/downsample_0.5/vid%d.mp4" % count)
        my_clip.close()
         #cv2.imwrite("vid%d.mp4" % count, image) 
        count=count+1
#     #print(i)
# =============================================================================
downsampling(0.2)
downsampling(0.33)        
downsampling(0.5)


def color():
    
    
    count=720
    def invert_colors(image):
        return image[:,:,[0,0,0]]
        
    for i in glob.glob(r"F:/UCF/help/videos/*.mp4"):
        
        my_clip=VideoFileClip(i)
        new_clip = my_clip.fl_image(invert_colors)
        new_clip.write_videofile(r"F:/UCF/help/color_gray/vid%d.mp4" % count)
        new_clip.close()
             #cv2.imwrite("vid%d.mp4" % count, image) 
        count=count+1
#     #print(i)
# =============================================================================
color()


def horizontal_flipping():
    count=800
    for i in glob.glob(r"F:/UCF/help/videos/*.mp4"):
        vi=VideoFileClip(i)
        my_clip = vi.fx(vfx.mirror_x)
        my_clip.write_videofile(r"F:/UCF/help/horizontal_flip/vid%d.mp4" % count)
        my_clip.close()
         #cv2.imwrite("vid%d.mp4" % count, image) 
        count=count+1
        
horizontal_flipping()


def supersample(d,nframes):
    count=950
    for i in glob.glob(r"F:/UCF/help/remaining/*.mp4"):
        vi=VideoFileClip(i)
        my_clip = vi.fx(vfx.supersample,d,nframes)
        my_clip.write_videofile(r"F:/UCF/help/supersample/vid%d.mp4" % count)
        my_clip.close()
         #cv2.imwrite("vid%d.mp4" % count, image) 
        count=count+1
        
supersample(0.05,5)


def center_crop(x_center,y_center,width,height):
    count=960
    for i in glob.glob(r"F:/UCF/help/videos/*.mp4"):
        vi=VideoFileClip(i)
        my_clip = vi.fx(vfx.crop,x_center,y_center,width,height)
        my_clip.write_videofile(r"F:/UCF/help/center_crop/vid%d.mp4" % count)
        my_clip.close()
         #cv2.imwrite("vid%d.mp4" % count, image) 
        count=count+1
        
center_crop(640,360,1000,600)







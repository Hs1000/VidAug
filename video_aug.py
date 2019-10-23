from moviepy.editor import VideoFileClip,vfx
import glob
def downsampling(amt):
    count=1182
    for i in glob.glob("F:/UCF/non-help/videos_non_help/*.mp4"):
        vi=VideoFileClip(i)
        my_clip = vi.fx(vfx.speedx,amt)
        my_clip.write_videofile("F:/UCF/non-help/downsampling_1.5_non-help/vid%d.mp4" % count)
        my_clip.close()
         #cv2.imwrite("vid%d.mp4" % count, image) 
        count=count+1
#     #print(i)
# =============================================================================
downsampling(1.5)
downsampling(2)        
downsampling(2.5)


#from moviepy.editor import VideoFileClip,vfx
#import glob
def upsampling(amt):
    count=1324
    for i in glob.glob("F:/UCF/non-help/videos_non_help/*.mp4"):
        vi=VideoFileClip(i)
        my_clip = vi.fx(vfx.speedx,amt)
        my_clip.write_videofile("F:/UCF/non-help/upsampling_0.33_non-help/vid%d.mp4" % count)
        my_clip.close()
         #cv2.imwrite("vid%d.mp4" % count, image) 
        count=count+1
#     #print(i)
# =============================================================================
upsampling(0.2)
upsampling(0.33)        
upsampling(0.5)

def horizontal_flipping():
    count=1466
    for i in glob.glob("F:/UCF/non-help/videos_non_help/*.mp4"):
        vi=VideoFileClip(i)
        my_clip = vi.fx(vfx.mirror_x)
        my_clip.write_videofile("F:/UCF/non-help/horizontal_flip_non-help/vid%d.mp4" % count)
        my_clip.close()
         #cv2.imwrite("vid%d.mp4" % count, image) 
        count=count+1
#     #print(i)
        
horizontal_flipping()


def color():
    
    
    count=1750
    def invert_colors(image):
        return image[:,:,[0,1,0]]
        
    for i in glob.glob(r"F:/UCF/non-help/videos_non_help/*.mp4"):
        
        my_clip=VideoFileClip(i)
        new_clip = my_clip.fl_image(invert_colors)
        new_clip.write_videofile(r"F:/UCF/non-help/color_green_non-help/vid%d.mp4" % count)
        new_clip.close()
             #cv2.imwrite("vid%d.mp4" % count, image) 
        count=count+1
#     #print(i)
# =============================================================================
color()


def supersample(d,nframes):
    count=1608
    for i in glob.glob(r"F:/UCF/non-help/videos_non_help/*.mp4"):
        vi=VideoFileClip(i)
        my_clip = vi.fx(vfx.supersample,d,nframes)
        my_clip.write_videofile(r"F:/UCF/non-help/supersample_non-help/vid%d.mp4" % count)
        my_clip.close()
         #cv2.imwrite("vid%d.mp4" % count, image) 
        count=count+1
        
supersample(0.05,5)


def center_crop(x_center,y_center,width,height):
    count=1821
    for i in glob.glob(r"F:/UCF/non-help/videos_non_help/*.mp4"):
        vi=VideoFileClip(i)
        my_clip = vi.fx(vfx.crop,x_center,y_center,width,height)
        my_clip.write_videofile(r"F:/UCF/non-help/center_crop_non-help/vid%d.mp4" % count)
        my_clip.close()
         #cv2.imwrite("vid%d.mp4" % count, image) 
        count=count+1
        
center_crop(640,360,1000,600)
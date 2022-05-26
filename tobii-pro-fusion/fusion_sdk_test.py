import tobii_research as tr
import time

def gaze_data_callback(gaze_data):
    # print(gaze_data.keys())
    
    # Print gaze points of left and right eye
    gaze_left_eye=gaze_data['left_gaze_point_on_display_area']
    gaze_right_eye=gaze_data['right_gaze_point_on_display_area']
    print("Left eye: {0} \t Right eye: {1}".format(gaze_left_eye,gaze_right_eye))

found_eyetrackers = tr.find_all_eyetrackers()
my_eyetracker = found_eyetrackers[0]
print("Address: " + my_eyetracker.address)
print("Model: " + my_eyetracker.model)
print("Name (It's OK if this is empty): " + my_eyetracker.device_name)
print("Serial number: " + my_eyetracker.serial_number)

my_eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, gaze_data_callback, as_dictionary=True)
time.sleep(10)

my_eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, gaze_data_callback)

from tkinter import *
from tkinter import ttk
from Tracking import Tracking_Controller as Tc
from Camera import CameraConnection as Cc
from Draw import Draw_Controller as Dr
from OCR import OCR
import os
import img2pdf


def model_(model_value):# get model type
    model_type=0
    if model_value == "Pencil":
        model_type = 'pencil'
    elif model_value == "Marker":
        model_type = 'marker'
    else:
        print("Nothing")
    return model_type


def camera_(camera_choose,value):# get camera type
    camera_connection=0
    camera_value=0
    if camera_choose == "LapTop Camera":
        camera_value=0
        camera_connection = Cc.camera("Laptop")
    elif camera_choose == "IP Camera":
        camera_value=value     # http://192.168.1.103:8080/video
        camera_connection = Cc.camera("IP")
    elif camera_choose == "Depth Camera":
        camera_value=""
        camera_connection = Cc.camera("Depth")
    else:
        print("Nothing")

    return camera_connection,camera_value


def draw_(draw_value):# get the virtual paper
    draw_ty="OpenCv"
    window=None
    if draw_value == "OpenCV":

        window=Dr.draw_on_window("OpenCv")
    else:
        print("Nothing")
    return window

def color_(color):
    switcher = {
        'Red': (0,0,255),
        'Green': (0,255,0),
        'Blue': (255,0,0),
        'Yellow': (0,255,255),
        'Purple': (128,0,128),
        'Black': (0,0,0)
    }
    return switcher.get(color,(255,0,0) )


def UI():
    counter = 0
    window = Tk()
    window.geometry("390x350")
    window.resizable(0, 0)
    window.title("Ghost Writer")

    Label(window, text="Welcome To Ghost Writer").grid(row=counter, column=1)
    counter = counter + 1
    Label(window, text="").grid(row=counter, column=1)
    counter = counter + 1
    Label(window, text="Required").grid(row=counter, column=1)

    # Models
    Label(window, text="Select Model Type").grid(row=counter, column=0)
    model_choices = ['Pencil', 'Marker']
    model_variable = StringVar(window)
    models = ttk.OptionMenu(window, model_variable, "Select", *model_choices)
    models.grid(row=counter, column=2)
    model_variable.set('Pencil')

    # Camera
    def cameradata(*arg):
        c = camera_variable.get()
        if c == "Depth Camera":
            camera_value.config(state=DISABLED)
        else:
            camera_value.config(state=NORMAL)

    counter = counter + 1
    Label(window, text="Select Camera Type").grid(row=counter, column=0)
    camera_choices = ['LapTop Camera', 'IP Camera', 'Depth Camera']
    camera_variable = StringVar(window)
    camera = ttk.OptionMenu(window, camera_variable, "Select", *camera_choices, command=cameradata)
    camera.grid(row=counter, column=2)
    camera_variable.set('Depth Camera')

    # Camera value
    counter = counter + 1
    Label(window, text="Camera value").grid(row=counter, column=0)
    camera_value = ttk.Entry(window, width=15)
    camera_value.grid(row=counter, column=2, sticky="w")

    # Draw
    counter = counter + 1
    Label(window, text="Select Draw Type").grid(row=counter, column=0)
    draw_choices = ['OpenCV']
    draw_variable = StringVar(window)
    draw = ttk.OptionMenu(window, draw_variable, "Select", *draw_choices)
    draw.grid(row=counter, column=2)
    draw_variable.set('OpenCV')

    # Draw Options
    counter = counter + 1
    Label(window, text="").grid(row=counter, column=1)
    counter = counter + 1
    Label(window, text="Optional").grid(row=counter, column=1)

    # font
    counter = counter + 1
    Label(window, text="Select The font").grid(row=counter, column=0)
    font_choices = ['1','1.5', '2', '2.5', '3', '3.5', '4']
    font_variable = StringVar(window)
    font = ttk.OptionMenu(window, font_variable, "Select", *font_choices)
    font.grid(row=counter, column=2)
    font_variable.set("2.5")

    # Color
    counter = counter + 1
    Label(window, text="Select The Color").grid(row=counter, column=0)
    color_choices = ['Red',  'Green', 'Blue', 'Yellow', 'Purple','Black']
    color_variable = StringVar(window)
    color = ttk.OptionMenu(window, color_variable, "Select", *color_choices)
    color.grid(row=counter, column=2)
    color_variable.set("Red")

    # Thickness
    counter = counter + 1
    Label(window, text="Select The Thickness").grid(row=counter, column=0)
    thick_choices = ['1', '2', '3', '4', '5', '6', '7']
    thick_variable = StringVar(window)
    thick = ttk.OptionMenu(window, thick_variable, "Select", *thick_choices)
    thick.grid(row=counter, column=2)
    thick_variable.set('2')

    # Button Start
    counter = counter + 1
    start = Button(window, text="Start", height=1, width=8, command=lambda: ghost_writer())
    start.grid(row=counter, column=0, padx=(0, 10), pady=(10, 10))

    def ghost_writer():
        print(model_variable.get())
        print(camera_variable.get())
        print(draw_variable.get())
        print(camera_variable.get())
        print(camera_value.get())
        print(thick_variable.get())
        print(color_variable.get())
        print(font_variable.get())

        cameraConnection,cameravalue = camera_(camera_variable.get(),camera_value.get())
        model= model_(model_variable.get())
        draw = draw_(draw_variable.get())
        data={}
        data['cameraConnection']=cameraConnection
        data['cameraValue']=cameravalue
        data['model']=model
        data['draw']=draw
        data['font'] = float(font_variable.get())
        data['thickness']=int(thick_variable.get())
        data['lineColor']=color_(color_variable.get())

        Tc.tracking_controller(data)

    # Button Finish
    finish = Button(window, text="Finish", height=1, width=8,command=lambda: Quit())
    finish.grid(row=counter, column=2, padx=(0, 10))
    counter = counter + 1
    def Quit():
        window.quit()

    # Button PDF
    pdf = Button(window, text="Save as PDF", height=1, width=10,command=lambda: save_as_pdf())
    pdf.grid(row=counter, column=0, padx=(0, 10), pady=(10, 10))

    def save_as_pdf():
        file_dir = os.path.dirname(os.path.realpath('_file_'))
        pdfpath = os.path.join(file_dir, 'Results\\PDF\\pages.pdf')
        imagepath = os.path.join(file_dir, 'Results\\IMAGE\\')
        imagenames = os.listdir(imagepath)
        imagepaths=[]
        for image in imagenames:
            imagepaths.append(os.path.join(imagepath, image))
        print(imagepaths)
        pdf = open(pdfpath, 'wb')
        pdf.write(img2pdf.convert(imagepaths))
    # Button OCR
    ocr = Button(window, text="Apply OCR", height=1, width=10,command=lambda: applyOCR())
    ocr.grid(row=counter, column=2, padx=(0, 10))
    def applyOCR():
        file_dir = os.path.dirname(os.path.realpath('_file_'))
        txtpath = os.path.join(file_dir, 'Results\\TXT\\pages.txt')
        imagepath = os.path.join(file_dir, 'Results\\IMAGE\\')
        imagenames = os.listdir(imagepath)
        imagetexts ="\n\t----------------image 1 content-----------\n"
        imgnum=1
        for image in imagenames:
            imagetexts+=OCR.OCR(os.path.join(imagepath, image))
            imgnum+=1
            imagetexts+="\n\n\t----------------image "+str(imgnum)+" content-----------\n"
        print(imagetexts)
        txt = open(txtpath, 'w')
        txt.write(imagetexts)

    window.mainloop()



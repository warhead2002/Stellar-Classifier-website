from flask import Flask,request,render_template
from flask_uploads import IMAGES,UploadSet,configure_uploads
import classifier as cl

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'images'
configure_uploads(app, photos)

@app.route('/', methods=['GET', 'POST'])
def upload():
    # Input photo, detect and publish result
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        # give address of photo 
        location = 'images/'+filename
        result = cl.classify(location)
        return ("<br><br><br><br><br><br><center><h1>"+result+"</h1></center>")
    # code to delete previous file
    if request.method == 'GET':
        import os
        def main():
            path = "images"
            extension = ".jpg"   
            if os.path.exists(path):       
                if os.path.isdir(path):       
                    for root_folder, folders, files in os.walk(path):               
                        for file in files:
                            file_path = os.path.join(root_folder, file)
                            file_extension = os.path.splitext(file_path)[1]
                            if extension == file_extension:                       
                                if not os.remove(file_path):                            
                                    print(f"{file_path} deleted successfully")                           
                                else:                            
                                    print (f"Unable to delete the {file_path}")       
                else:           
                    print(f"{path} is not a directory")   
            else:       
                print (f"{path} doesn't exist")

        if __name__ == '__main__':
            main()
    # return main html file
    return render_template('upload.html')

if __name__ == '__main__':
	app.run(debug = True)
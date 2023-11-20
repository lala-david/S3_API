import boto3
import uuid
import time
from flask import Flask, jsonify, request, render_template
from werkzeug.utils import secure_filename

def s3_connection():
    try:
        s3 = boto3.client(
            service_name="s3",
            region_name="ap-northeast-2",
            aws_access_key_id="",
            aws_secret_access_key=""
        )
    except Exception as i:
        print(i)
    else:
        print("s3 bucket connected!")
        return s3 
    
s3 = s3_connection()
app = Flask(__name__)  

app.config['S3_BUCKET_NAME'] = 'seongjun-flask'   
 
@app.route('/imgupload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    
    if file:
        filename = secure_filename(file.filename)
 

        file_ext = filename.split('.')[-1]
        

        new_filename = f"{str(uuid.uuid4())}_{int(time.time())}.{file_ext}"
        
        try:
            s3.upload_fileobj(file, app.config['S3_BUCKET_NAME'], new_filename)
            file_url = f"https://{app.config['S3_BUCKET_NAME']}.s3.ap-northeast-2.amazonaws.com/{new_filename}"
            return render_template('success.html', file_url=file_url)  
          
        except Exception as e:
            return jsonify(message=str(e)), 500
    
    else:  
      return jsonify(message='No file selected'), 404

if __name__ == "__main__":
    app.run(debug=True)
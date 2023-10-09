import boto3
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

app.config['S3_BUCKET_NAME'] = ''   
 
@app.route('/imgupload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    
    if file:
        filename = secure_filename(file.filename)
        
        try:
            s3.upload_fileobj(file, app.config['S3_BUCKET_NAME'], filename)
            return render_template('success.html')  
          
        except Exception as e:
            return jsonify(message=str(e)), 500
    
    else:  
      return jsonify(message='No file selected'), 404

if __name__ == "__main__":
    app.run(debug=True)
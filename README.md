## 기업 모둠 학습
# ☘ Image_Upload S3 API

# **1. 개요**

**이 서비스는 AWS S3와 Flask를 활용하여 이미지 API 기능을 제공**
**사용자는 특정 이미지 파일을 선택하고 서버에 업로드할 수 있으며, 해당 이미지는 AWS S3에 저장됨**

# **2. 기능목록**

### **2.1 AWS S3 연결 (s3_connection)**

**AWS S3 서비스와 연결을 시도하는 함수**
**연결에 성공하면 "s3 bucket connected!" 메시지를 출력하고, 연결에 실패 시 해당 오류 메시지를 출력함**

➡ **요청 예시**

```python
s3 = s3_connection()
```

### **2.2 Flask 애플리케이션 생성**

**Flask 애플리케이션 객체를 생성하고, AWS S3 버킷 이름을 애플리케이션 설정에 저장함**

➡ **요청 예시**

```python
app = Flask(__name__)
app.config['S3_BUCKET_NAME'] = 'your-bucket'
```

### **2.3 파일명 생성**

**파일 업로드 시, 중복을 방지하기 위해 고유한 파일 명을 생성함** 

➡ **요청 예시**

```python
filename = secure_filename(file.filename)
file_ext = filename.split('.')[-1]
new_filename = f"{str(uuid.uuid4())}_{int(time.time())}.{file_ext}"
```

### **2.4 이미지 업로드 (upload_file)**

**사용자가 선택한 이미지 파일을 AWS S3에 업로드하는 함수**
**파일 업로드가 성공하면 'success.html' 페이지를 렌더링하고, 실패하면 에러 메시지를 반환함**

➡ **요청 예시**

```python
@app.route('/imgupload', methods=['POST'])
def upload_file():
```

### **2.5 Flask 애플리케이션 실행**

**Flask 애플리케이션을 디버그 모드로 실행함**

➡ **요청 예시**

```python
if __name__ == "__main__":
    app.run(debug=True)
```

# **3. 에러 처리**

1️⃣ **파일 미선택: 사용자가 파일을 선택하지 않고 "업로드" 버튼을 클릭한 경우, "No file selected" 메시지와 함께 404 상태 코드를 반환함**
2️⃣ **업로드 실패: 파일 업로드에 실패한 경우, 실패한 이유를 알려주는 에러 메시지와 함께 500 상태 코드를 반환함**

# **4. HTML 파일**

**해당 서비스는 두 가지 HTML 페이지를 제공**

1️⃣ **Image Upload API Test: 사용자가 이미지 파일을 선택하고 업로드할 수 있는 페이지**
2️⃣ **Upload Success: 파일 업로드가 성공적으로 완료되면 이 페이지가 표시**



# 5**. 이미지 업로드 시**
![1](https://github.com/lala-david/S3_API/assets/37481441/8d6f652b-b3a6-4770-893b-0cb5616e14ac)

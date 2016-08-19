`flask-thumbnail` 이용해 이미지의 썸네일을 생성하는 로직을 
검증해보기 위한 샘플 프로그램.

```
app = Flask(__name__)
app.config['MEDIA_FOLDER'] = os.path.join(CURRENT_DIR, 'media')
app.config['MEDIA_URL'] = '/media/'

thumb = Thumbnail(app)
```

위와 같이 플러그인을 연결한 후 코드 상에서 

```
thumb_url = thumb.thumbnail('image.jpg', '100x100', crop='fit', quality=85)
```

방식으로 실행할 때, `thumb.thumbnail` 코드 내에서 썸네일 생성 및 저장되고 `thumb_url` 에 해당 이미지에 접근할 수 있는
주소가 리턴되는 것을 확인했다.


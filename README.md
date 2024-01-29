# OpenCV-Car-Detector

Bu uygulama, bir video akışındaki araçları tespit etmek için Haar Cascade Sınıflandırıcısını kullanır. Kullanıcılara, algılama parametrelerini dinamik olarak ayarlamalarına olanak tanır.


## Gereksinimler
- Python 3.x
- OpenCV
- Tkinter
- haarcascade_car.xml dosyası


## Kurulum

Aşağıdaki komutu kullanarak gerekli Python paketlerini yükleyin:
```bash
pip install opencv-python
pip install tk
```


## Kullanım

- opencv_car_detector.py dosyasını çalıştırın.
- Video dosyasının yolunu belirtiniz.
- "Start Detection" düğmesine tıklayarak araçları tespit etmeye başlayın.


## Parametre Ayarları

Scale Factor: Arama penceresinin boyutunu azaltmak veya artırmak için kullanılır.
Min Neighbors: Bir nesnenin etrafındaki komşu dikdörtgenlerin sayısını kontrol eder.
Min Size: Minimum algılanabilir nesne boyutunu belirler.


## Notlar

- Video izleme sırasında "Q" tuşuna basarak videoyu duraklatabilir, parametreleri güncelleyebilir ve tekrar "Start Detection" düğmesine basarak izlemeye devam edebilirsiniz.
- Bu örnek için, [4K Road traffic video for object detection and tracking.mp4](./videos/4K%20Road%20traffic%20video%20for%20object%20detection%20and%20tracking.mp4) dosyasını kullanabilirsiniz.


## Örnek Sonuçlar

Aşağıdaki videodan örnek sonuçları izleyebilirsiniz:

https://github.com/dagaca/OpenCV-Car-Detector/assets/80363244/f1616c53-b74e-4cbc-a781-d027814f33b2


## İnceleme

Bu uygulama, Haar Cascade Sınıflandırıcısı'nın temel prensiplerini kullanarak nesne tespiti yapar. Algoritmik olarak, görüntüyü ölçeklendirir, gri tonlamaya çevirir ve ardından belirlenen parametrelerle nesne tespiti yapar. Bu sınıflandırıcı, nesneleri tespit etmek ve çeşitli endüstri uygulamalarında kullanılmak üzere eğitilmiş bir modeldir.


## Katkılar

Eğer uygulamayı geliştirmeye veya sorunları bildirmeye katkıda bulunmak istiyorsanız, lütfen bir çekme isteği açın veya bir sorun bildirisi oluşturun.

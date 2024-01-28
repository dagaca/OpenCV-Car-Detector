# OpenCV-Car-Detector

Bu uygulama, bir video akışındaki araçları tespit etmek için Haar Cascade Sınıflandırıcısını kullanır. Kullanıcılara, algılama parametrelerini dinamik olarak ayarlamalarına olanak tanır.


## Gereksinimler
- Python 3.x
- OpenCV
- Tkinter


## Kurulum
Aşağıdaki komutu kullanarak gerekli Python paketlerini yükleyin:
```bash
pip install opencv-python
pip install tk
```


## Kullanım
opencv_car_detector.py dosyasını çalıştırın.
Video dosyasının yolunu girin.
"Start Detection" düğmesine tıklayarak araçları tespit etmeye başlayın.


## Parametre Ayarları
Scale Factor: Arama penceresinin boyutunu azaltmak veya artırmak için kullanılır.
Min Neighbors: Bir nesnenin etrafındaki komşu dikdörtgenlerin sayısını kontrol eder.
Min Size: Minimum algılanabilir nesne boyutunu belirler.


## Örnek Sonuçlar
Aşağıdaki bağlantıdan örnek sonuçları izleyebilirsiniz:


## İnceleme
Bu uygulama, Haar Cascade Sınıflandırıcısı'nın temel prensiplerini kullanarak nesne tespiti yapar. Algoritmik olarak, görüntüyü ölçeklendirir, gri tonlamaya çevirir ve ardından belirlenen parametrelerle nesne tespiti yapar. Bu sınıflandırıcı, nesneleri tespit etmek ve çeşitli endüstri uygulamalarında kullanılmak üzere eğitilmiş bir modeldir.


## Katkılar
Eğer uygulamayı geliştirmeye veya sorunları bildirmeye katkıda bulunmak istiyorsanız, lütfen bir çekme isteği açın veya bir sorun bildirisi oluşturun.

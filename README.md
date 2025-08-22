# Evcil-Hayvan-Bakimi-Rehberi-Web-App
## İstenilen Uygulama 
  ### Evcil hayvan bakım rehberi web sitesi (Evcil hayvan besleyenlerin hayatını kolaylaştıracak bilgilerin yer aldığı ve en yakın veteriner,barınak gibi alanlari gösteren uygulama)


## Uygulamanın Teknik Bilgisi 
#### Uygulamada  django,mysql,bootstrap ve mapbox  api kullanıldı.
#### Uygulamada kullanılan teknolojilerin versiyonları
- python:3.8.4 
- django:3.1.4 
- mysql:8.0.25 
- bootstrap:4.7.0 
- django-crispy-forms:1.10.0
- mysqlclient:2.0.3
- Pillow:8.1.0
#### Python ve Mysql kurulumu linkleri 
- Python:https://www.sadikturan.com/python-gelistirme-ortami/python-kurulumu-nasil-yapilir/1365
- MySQL:https://www.youtube.com/watch?v=hRnXI1qo0G0&ab_channel=CodeCube
-Hata almamak için münkün olduğu sürece kullanılan teknolojilerin sürümüne uymamız lazım özellikle python ve django sürümü.
### Proje Kurulumu ve Projeyi Çalıştırma
#### 1.Veritabanı kısmı 
 - petapp isimli veritabanını oluşturuyoruz.
 - Linux kullanan için `sed 's/utf8mb4_0900_ai_ci/utf8mb4_unicode_ci/g' petapp.sql > petapp_linux.sql` komutu girmemiz gerekir.
 - Ardından  database klasörünün içinde petapp.sql'i import ediyoruz.
 - Proje dosyasında bulunan https://github.com/rdvnkdyf/Evcil-Hayvan-Bak-m-Rehberi/tree/main/pethome/petapp/petapp  dizinin altındaki settings.py icerisinde DATABASES bölümünde   USER ve PASSWORD'ü kendimize uygun şekilde değiştiriyoruz.
#### 2.Proje dosyalarındaki kısım 
  - Console ekranındayken `python -m pip install django==3.0.8` veya `pip install django==3.0.8` yazıyoruz. 
  - Evcil-Hayvan-Bak-m-Rehberi/tree/main/pethome/petapp dizinindeyken `pip install django-crispy-forms` yazıyoruz.Eğer yüklenmezse `python -m pip install --upgrade pip` yazıyoruz.
  - Aynı dizindeyken django framework'ün mysql'e bağlanması için `pip install mysqlclient` ve `python -m pip install Pillow` yazıyoruz. 
  - Evcil-Hayvan-Bak-m-Rehberi/tree/main/pethome/petapp dzinindeyken python sürümünüze göre  `python manage.py runserver`  veya `python3 manage.py runserver` yazıp çalıştırıyoruz.
#### Garanti olsun diye uzun şekilde yazıldı.Kısa versiyonu:
 -Terminalde `Evcil-Hayvan-Bakimi-Rehberi-Web-App/tree/main/pethome/petapp` şu dizindeyken `pip install -r requirements.txt` yazarak gerekli paketleri de yükleyebiliriz.
 -Ve daha sonra işlem bittikten sonra aynı dizindeyken  `python manage.py runserver` veya `python3 manage.py runserver` yazarak çalıştırabiliriz.

## Uygulamada Yer alan Özellikler 
* #### Kayıt olma,profil düzenleme bölümünde  username,firstname,lastname,mail adresi ve parola değişikliği yapma.
* #### Veterinerler kısmı,gönüllü veterinerlerin bilgileri yer alır.Veterinerlerin ilgilendiği alan,kliniğinin adresi ve açıklaması yer alır.Bu bilgiler ışığında baktığımız hayvanların acil sağlık problemleriyle ilgili sorunları bu uygulamayla beraber onlara danışabilir veya kliniklerine gidilebilir.
* #### Galeri bölümü,en çok bakılan evcil hayvanların resimleri yer alır.Burada çeşitlilik artırılabilir.Galeri bölümünün amacı,hayvanlar hakkında bilginin yanında kafamızda da canlanmasını sağlamaktır.
* #### Blog bölümü,editörlerin evcil hayvan bakımını yapanlar için yararlı bilgiler yer alır.Buradaki bilgiler yeni hayvan sahiplenmek isteyenlere de öncülük sağlar.
* #### Blog kısmında okuyacağınız postlarda ayrıca yorum yazma bölümü yer alır.Yazdığınız yorum adminler tarafından onaylandıktan sonra postların yorumlar kısmında gözükür.
* #### İletişim kısmı,iletişim bilgilerinin yanında adminlere ulaşılacak bir iletişim formu ve aynı zamanda istenilen şey olan en yakın veteriner barınakları gösteren Tekirdağ merkezli harita var.

# Uyarı 
## Harita apisi ücretsiz fakat konuma göre tam olarak istenilen sonucu vermeyebilir.
## Harita API Google Chrome 'da güncel sürümde çalıştı diğer güncel olmayan sürümlerde ve başka web tarayıcılarda  çalışmayabilir.

## Resimler
#### Admin İletişim 
![Admin İletişim  Sayfası](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/admin_ileti%C5%9Fim.png)
#### Admin Post Oluşturma 
![Admin Post Oluşturma  Sayfası](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/admin_post_olusturma.png)
#### Admin Resim Ekleme 
![Admin Resim Ekleme  Sayfası](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/admin_resim_ekleme.png)
#### Admin Veteriner Ekleme 
![Admin Veteriner Ekleme  Sayfası](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/admin_veteriner_ekleme.png)
#### Admin Yorum Kontrol Sayfası
![Admin Yorum Kontrol  Sayfası](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/admin_yorumlar.png)
#### Blog 
![Blog  Sayfası](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/blog.png)
#### Galeri 
![Galeri  Sayfası](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/galeri.png)
#### İletişim Formu 
![İletişim Formu](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/ileti%C5%9Fim_formu.png)
#### İletişim Sayfasındaki Harita
![İletişim Harita](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/ileti%C5%9Fim_harita.png)
#### Kayıt Ol Sayfası
![Kayıt Ol Sayfası](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/kay%C4%B1tol.png)
#### Login Sayfası
![Login Sayfası](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/login.png)
#### Blog'un post sayfası 
![Post Sayfası](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/post_yazi.png)
#### Yorumlar kısmı 
![Post Sayfası](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/post_yorum.png)
#### Profil Düzenle 
![Profil Düzenle](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/profil_d%C3%BCzenle.png)
#### Şifre Değiştir 
![Şifre Değiştir](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/sifre_degistir.png)
#### Veterinerler Bölümü
![Veterinerler Bölümü](https://github.com/rdvnkdyf/Evcil-Hayvan-Bakimi-Rehberi-Web-App/blob/main/pethome/proje-resimleri/veterinerler.png)

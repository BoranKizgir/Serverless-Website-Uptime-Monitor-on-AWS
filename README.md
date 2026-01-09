# Serverless-Website-Uptime-Monitor-on-AWS


Bu proje, AWS'nin sunucusuz (serverless) mimarisini kullanarak web sitelerinin durumunu ve yanıt sürelerini izlemek için tasarlanmıştır. Tamamen **AWS Free Tier** uyumludur ve operasyonel maliyeti $0'dır.

## Proje Amacı
Belirlenen URL listesine 5 dakikada bir istek göndererek sitelerin ayakta olup olmadığını kontrol eder ve sonuçları analiz için bir NoSQL veritabanında saklar.

## Mimari Şema


1. **Amazon EventBridge:** Her 5 dakikada bir Lambda'yı tetikleyen cron job görevi görür.
2. **AWS Lambda:** Web isteklerini atan ve veriyi işleyen Python tabanlı motor.
3. **Amazon DynamoDB:** Zaman serisi verilerini saklayan yüksek ölçekli NoSQL veritabanı.
4. **IAM:** Least Privilege prensibiyle sadece gerekli izinlerin atandığı güvenlik rolleri.

## Kullanılan Teknolojiler
- **Python (urllib/boto3)**
- **AWS Lambda**
- **Amazon DynamoDB**
- **CloudWatch Logs**

## Veri Modeli (DynamoDB)
- **Partition Key:** `URL` (Her site için verileri gruplamak için)
- **Sort Key:** `Timestamp` (Geçmişe dönük analiz yapabilmek için)
- **Attributes:** `Status` (HTTP kodu), `Latency` (ms cinsinden hız)

## Neden Bu Mimari?
- **Sıfır Bakım:** Sunucu yamalama veya yönetimi gerekmez.
- **Maliyet Etkin:** Sadece çalıştığı saniyeler için ücretlendirilir (Free Tier kapsamında ücretsizdir).
- **Ölçeklenebilirlik:** Yüzlerce URL'yi aynı anda kontrol edebilecek kapasitedir.

# Değişken Boğazlı Çok Odalı Roket: Proje Açıklaması ve Matematiksel Model

> **Durum: ön hesap.** Bu çalışma bir fikir taslağıdır; gerçek bir motor verisiyle ya da deneyle doğrulanmamıştır. Sayılar örnek değerlerle hesaplanmıştır. Mekanizma kütlesi (68,7 kg) bir **tahmindir** ve sonucu en çok o etkiler. Hesaplar Claude (Anthropic) ile birlikte yapılmıştır.

## Projenin fikri

Her yanma odası bittikçe nozulun boğazını çubuklarla daraltmak; böylece gaz daha çok genleşir ve roket daha yüksek egzoz hızıyla çalışır.

Roketin omurgasında üst üste dizili yanma odaları vardır; bunlara bu dokümanda **evre** denir. Bir evre yanıp bitince boş oda gövdede kalır (atılmaz) ve sonraki evre devreye girer. Sonraki evrelerde saniyede yakılan yakıt (debi) daha azdır. Sabit bir nozulda debi azalınca yanma odası basıncı düşer ve nozul bu yeni duruma uygun olmaz.

Çubuklar grafit kaplamalıdır ve yüksek sıcaklığa dayanır. Her çubuğun bir ucu nozulun çevresine bağlıdır, öbür ucu salınarak boğazın içine doğru iner. Salınımın merkezi aşağı indikçe boğaz küçülür. Nozul çıkışı değişmediği için boğaz küçüldükçe çıkışın boğaza oranı (genleşme oranı) büyür.

Yakıt ve yükseltgen ayrı yollardan gelir: **sıvı oksijen (LOX) merkezdeki omurgadan**, **etanol ise motor gövdesi ile dış duvar arasındaki halka aralıktan** odalara basılır. Etanol halkası, yanan odalarla dış duvar arasında bir ısıl tampon görevi de görür. Her oda yalnızca kendi vanalarıyla beslenir; miktar azdan çoğa ayarlanır. Ayrıntı için "Besleme sistemi ve yerleşim" bölümüne bakın.

**Ana savı:** boğazı debiyle birlikte daraltmak Isp'yi (özgül itkiyi) yükseltir.
**Karşı ağırlık:** çubuk mekanizmasının kütlesi. Doküman bu ikisini birlikte hesaplar.

## Temel kavramlar

| Terim | Sade anlamı | Birim |
| --- | --- | --- |
| Evre (oda) | Kendi yakıtı olan ve yanınca boş kalan, ama gövdeden atılmayan yanma odası; bu projede 3 evre var | - |
| Yanma odası basıncı (pc) | Gazın yandığı yerdeki basınç | Pa (1 bar = 100 000 Pa) |
| Debi (ṁ) | Saniyede yakılan yakıt ve yükseltgen kütlesi | kg/s |
| Boğaz alanı (At) | Nozulun en dar kesiti; gaz burada ses hızına çıkar | m² |
| Çıkış alanı (Ae) | Nozul ağzının kesiti | m² |
| Genleşme oranı (ε) | Çıkış alanının boğaz alanına oranı, Ae / At | birimsiz |
| Egzoz hızı (ve) | Gazın nozuldan çıkış hızı | m/s |
| Özgül itki (Isp) | İtkinin, saniyedeki yakıt ağırlığına oranı | s |
| Δv | Roketin kazanabileceği toplam hız değişimi | m/s |

Yerçekimi ivmesi g₀ = 9,80665 m/s².

## Besleme sistemi ve yerleşim

| Hat | Yol | Not |
| --- | --- | --- |
| LOX (yükseltgen) | Merkezdeki omurga | −183 °C; çevre odaların ısısından yalıtılmalı |
| Etanol (yakıt) | Motor gövdesi ile dış duvar arasındaki halka | −114 °C'de donar; LOX hattından uzak ve yalıtımlı olmalı |
| Temizleme (purge) | Azot veya helyum | Başlatma, kapatma ve ayırmada hatları temizler |

Tasarım ilkeleri:

- **Yakıt ve LOX enjektör yüzeyine kadar hiçbir yerde temas etmez.** Önceden karışan yakıt ve yükseltgen boruda geri tepmeye (flashback) yol açabilir; buluşma yalnızca yanma odasının içinde, enjektörde olur.
- **Her hatta çek valf ve her odanın kendi vanası vardır.** Yalnızca yanan odaya besleme yapılır; yanmayan odalara akış kapalıdır.
- **Enjektör basınç düşüşü** yanma basıncının yaklaşık %15-25'i kadar seçilir; yanma titreşimini (chugging) önlemek için gereklidir. 50 bar yanma basıncında besleme basıncı yaklaşık 60 bar olur (tahmin).
- **Sıralama:** genel uygulamada yakıt önce açılır, LOX sonra; kapatırken LOX önce kesilir.

Modelde bu bölüm hesaba katılmadı: karışım oranı (O/F), hat çapları ve debi dağılımı modellenmedi. Vana, enjektör ve purge donanımının kütlesi, boş oda kütlesindeki sabit 60 kg'ın içinde sayıldı; hatların kütlesi ayrıca hesaplanmadı. Bu bölüm hesapla doğrulanmamış tasarım ilkeleridir.

## Model 1: Boğaz alanı ve debi

Debi düşerse, yanma odası basıncını sabit tutmak için boğaz küçülmek zorundadır.

$$\dot{m} = \frac{p_c \, A_t}{c^*} \qquad\Longrightarrow\qquad A_t = \frac{\dot{m}\, c^*}{p_c}$$

Gaz boğazda ses hızına ulaşınca akış "tıkanır"; geçen gaz miktarı yalnızca odadaki koşullara ve boğaz alanına bağlıdır.

| Sembol | Anlamı | Değeri (örnek) |
| --- | --- | --- |
| ṁ | Debi | Evre 1: 70, evre 2: 29, evre 3: 10 kg/s |
| p_c | Yanma odası basıncı (sabit tasarım basıncı) | 50 bar = 5 000 000 Pa |
| A_t | Boğaz alanı | Hesaplanır |
| c* | Karakteristik hız: gazın ve sıcaklığın "kalitesini" tek sayıda toplar | 1658 m/s |

$$c^* = \frac{\sqrt{R\,T_c}}{\Gamma}, \qquad \Gamma = \sqrt{\gamma}\left(\frac{2}{\gamma+1}\right)^{\frac{\gamma+1}{2(\gamma-1)}}$$

| Sembol | Anlamı | Değeri (örnek) |
| --- | --- | --- |
| R | Özgül gaz sabiti, R = 8,314 / molekül ağırlığı | 361,5 J/kg/K (molekül ağırlığı 0,023 kg/mol) |
| T_c | Yanma sıcaklığı | 3200 K |
| γ | Isı oranı | 1,2 |
| Γ | γ'dan türeyen yardımcı sayı | 0,6485 |

Sonuç: A_t = 232 cm² (evre 1), 96 cm² (evre 2), 33 cm² (evre 3).

## Model 2: Genleşme oranı

Nozul çıkışı sabit olduğu için boğaz küçüldükçe genleşme oranı büyür: 8 → 19,3 → 56.

$$\varepsilon = \frac{A_e}{A_t}$$

Çıkış alanı evre 1'in boğazının 8 katı seçildi: A_e = 8 × 232 = 1857 cm² (nozul gövdesine aittir, uçuşta değişmez). Alan oranı ile basınç oranı arasındaki bağ:

$$\varepsilon = \frac{\Gamma}{\left(\frac{p_e}{p_c}\right)^{1/\gamma}\sqrt{\frac{2\gamma}{\gamma-1}\left[1-\left(\frac{p_e}{p_c}\right)^{\frac{\gamma-1}{\gamma}}\right]}}$$

Bu denklem elle tersine çevrilemez; p_e/p_c sayısal olarak çözülür.

| Evre | ε | p_e / p_c | Çıkış basıncı p_e |
| --- | --- | --- | --- |
| 1 | 8,0 | 0,01687 | 0,843 bar |
| 2 | 19,3 | 0,00531 | 0,265 bar |
| 3 | 56,0 | 0,00136 | 0,068 bar |

## Model 3: Egzoz hızı

Gaz genleşirken soğur, kaybettiği ısı enerjisi hıza dönüşür.

$$\frac{v_e^2}{2} = c_p\,(T_c - T_e) \quad (1) \qquad c_p = \frac{\gamma R}{\gamma - 1} \quad (2) \qquad \frac{T_e}{T_c} = \left(\frac{p_e}{p_c}\right)^{\frac{\gamma-1}{\gamma}} \quad (3)$$

(1) enerji korunumu, (2) ideal gazın ısı kapasitesi, (3) ısı alışverişsiz (izentropik) genleşmede sıcaklık-basınç bağıdır. Birleştirince:

$$v_e = \eta \sqrt{\frac{2\gamma}{\gamma-1}\, R\, T_c \left[1 - \left(\frac{p_e}{p_c}\right)^{\frac{\gamma-1}{\gamma}}\right]}$$

| Sembol | Anlamı | Değeri (örnek) |
| --- | --- | --- |
| v_e | Egzoz hızı | Hesaplanır |
| η | Nozul verimi (sürtünme vb. kayıplar) | 0,95 |
| c_p | Sabit basınçta ısı kapasitesi | 2169 J/kg/K |
| T_c, T_e | Odadaki ve çıkıştaki sıcaklık | 3200 K ve hesaplanır |

| Evre | Sabit nozul, v_e | Değişken boğaz, v_e | Çıkış sıcaklığı T_e |
| --- | --- | --- | --- |
| 1 | 2487 m/s | 2487 m/s | 1621 K |
| 2 | 2487 m/s | 2701 m/s | 1336 K |
| 3 | 2487 m/s | 2891 m/s | 1066 K |

### Bernoulli ile ilişkisi

Bu formül, Bernoulli denkleminin gaz için genişletilmiş halidir; ikisi de "hız artarsa basınç enerjisi azalır" der. Fark yoğunluktadır:

$$\frac{v^2}{2} + \frac{p}{\rho} = \text{sabit} \quad\text{(Bernoulli, yoğunluk sabit)} \qquad \frac{v^2}{2} + \frac{\gamma}{\gamma-1}\,\frac{p}{\rho} = \text{sabit} \quad\text{(gaz nozulu)}$$

Nozulda gazın yoğunluğu odadaki 4,3 kg/m³ değerinden yaklaşık 244 kat azalır (evre 3); saf Bernoulli yaklaşık 1520 m/s verir, gerçek formül (η'siz) 3043 m/s.

## Model 4: Özgül itki (Isp)

$$F = \dot{m}\, v_e + (p_e - p_a)\, A_e \qquad\qquad I_{sp} = \frac{F}{\dot{m}\, g_0}$$

(p_a: dış basınç, vakumda 0.)

| Evre | Sabit nozul, Isp (vakum) | Değişken boğaz, Isp (vakum) |
| --- | --- | --- |
| 1 | 276,4 s | 276,4 s |
| 2 | 276,4 s | 292,8 s |
| 3 | 276,4 s | 307,7 s |

Atmosferdeki uçuş boyunca ortalama Isp: sabit nozulda 268,8 s, değişken boğazda 276,8 s (+%3,0).

## Model 5: Tsiolkovsky denklemi ve kütle bütçesi

$$\Delta v_i = I_{sp,i}\, g_0 \ln\frac{m_{0,i}}{m_{f,i}} \qquad\qquad \Delta v = \sum_i \Delta v_i$$

m₀: evre başlarken toplam kütle, m_f: evre yakıtı bitince kalan kütle. Boş odalar atılmaz; sonraki evrenin m₀'ı önceki evrenin m_f'sine eşittir. Mekanizma (68,7 kg) da roketin üzerinde kalır.

| Evre | Yakıt | Boş oda | m₀ (sabit) | m_f (sabit) | m₀ (değişken) | m_f (değişken) |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 5400 kg | 492 kg | 10 200 | 4800 | 10 268,7 | 4868,7 |
| 2 | 2700 kg | 276 kg | 4800 | 2100 | 4868,7 | 2168,7 |
| 3 | 900 kg | 132 kg | 2100 | 1200 | 2168,7 | 1268,7 |

Boş oda kütlesi = 0,08 × yakıt + 60 kg. Faydalı yük 300 kg.

| Evre | Δv (sabit) | Δv (değişken) |
| --- | --- | --- |
| 1 | 2043 m/s | 2023 m/s |
| 2 | 2241 m/s | 2322 m/s |
| 3 | 1517 m/s | 1618 m/s |
| **Toplam** | **5801 m/s** | **5962 m/s** |

Kıyas: boş odalar her evre sonunda atılsaydı (klasik kademeleme) Δv sabit nozulda 7766, değişken boğazda 7882 m/s olurdu. Odaları gövdede tutmak yaklaşık 1900-2000 m/s kaybettirir; bu, boğaz kazancından (yaklaşık 160 m/s) çok daha büyüktür.

## Model 6: Çubuk geometrisi

Boğaz yarıçapı, çubuğun eksenle yaptığı açıya bağlıdır.

$$r_t = R_p - L \sin\theta \qquad\Longrightarrow\qquad \theta = \arcsin\!\left(\frac{R_p - r_t}{L}\right), \qquad r_t = \sqrt{\frac{A_t}{\pi}}$$

| Sembol | Anlamı | Değeri (örnek) |
| --- | --- | --- |
| r_t | Boğaz yarıçapı | Hesaplanır |
| R_p | Çubukların bağlandığı halkanın yarıçapı | 0,45 m |
| L | Çubuk uzunluğu | 0,60 m |
| θ | Çubuğun eksenle açısı | Hesaplanır |
| z | Çubuk ucunun eksen boyunca mesafesi, z = L cos θ | Hesaplanır |

| Evre | A_t | r_t | θ | z |
| --- | --- | --- | --- | --- |
| 1 | 232 cm² | 8,60 cm | 37,35° | 47,7 cm |
| 2 | 96 cm² | 5,53 cm | 41,13° | 45,2 cm |
| 3 | 33 cm² | 3,25 cm | 44,09° | 43,1 cm |

**Mekanizma kütlesi (tahmin).** Bir takım 12 çubuktan oluşur: 12 × 0,60 m × 0,0009 m² × 1750 kg/m³ = 11,3 kg; menteşe ve aktüatör için 8 kg eklenince takım 19,3 kg. İki daraltma adımı için iki takım ve 30 kg kontrol sistemi: 2 × 19,3 + 30 = **68,7 kg**.

## Örnek evren ve sonuçlar

| Parametre | Değer |
| --- | --- |
| Faydalı yük | 300 kg |
| Yakıt (evre 1 / 2 / 3) | 5400 / 2700 / 900 kg |
| Boş oda | 0,08 × yakıt + 60 kg (atılmaz) |
| Debi (evre 1 / 2 / 3) | 70 / 29 / 10 kg/s |
| Yanma odası basıncı | 50 bar (sabit) |
| Yanma sıcaklığı, γ, molekül ağırlığı | 3200 K, 1,2, 23 g/mol |
| Nozul verimi | 0,95 |
| Çıkış alanı | 1857 cm² |
| Çubuk mekanizması | 68,7 kg |

Dikey, tek boyutlu uçuş; yerçekimi ve hava direnci dahil; atmosfer üstel azalan basınç ve yoğunlukla modellendi.

| Sonuç | Sabit nozul | Değişken boğaz |
| --- | --- | --- |
| Yanma sonu hızı | 3214 m/s | 3377 m/s |
| Yanma sonu irtifa | 439,4 km | 450,6 km |
| Tepe noktası | 1099 km | 1189 km |
| Ortalama Isp | 268,8 s | 276,8 s |

## Verim

Değişken boğaz toplam hız kazancını **%2,8 (+162 m/s)** artırır; Isp'den gelen brüt kazancın yaklaşık %53'ü geriye kalır, gerisini mekanizma kütlesi yer.

| Ölçüt | Sabit nozul | Değişken boğaz |
| --- | --- | --- |
| Nozul ısıl verimi, evre 1 / 2 / 3 | %44,5 / %44,5 / %44,5 | %44,5 / %52,6 / %60,2 |
| Isp (vakum), evre 3 | 276,4 s | 307,7 s (+%11,3) |
| Ortalama Isp (uçuş) | 268,8 s | 276,8 s (+%3,0) |
| Toplam Δv (mekanizma dahil) | 5801 m/s | 5962 m/s (+%2,79) |
| Aynı Δv için taşınabilir yük | 300 kg | 383,3 kg (+%27,8) |

$$\eta_{\text{ısıl}} = \frac{v_e^2}{2\,c_p\,T_c} = \eta^2\left[1-\left(\frac{p_e}{p_c}\right)^{\frac{\gamma-1}{\gamma}}\right]$$

**Mekanizmanın net katkısı:**

| Kalem | Değer |
| --- | --- |
| Brüt kazanç (mekanizma ağırlığı yokmuş gibi) | +304 m/s (6105 − 5801) |
| Mekanizma kütlesinin maliyeti (68,7 kg) | −143 m/s |
| Net kazanç | +162 m/s |
| Tutulan pay | %53 |

Başa baş mekanizma kütlesi 151,9 kg'dır; tahmin 68,7 kg olduğundan 83,2 kg pay kalır. Bu yüzdeler, odaları gövdede tutan aynı roketin sabit nozullu haliyle kıyaslanır. Boğaz kazancı (yaklaşık 160 m/s), odaları atmamanın kaybını (yaklaşık 1900-2000 m/s) kapatmaz.

## Varsayımlar, sınırlar ve sonraki adımlar

**Varsayımlar ve sınırlar**

- Gaz ideal kabul edildi; γ, T_c ve molekül ağırlığı sabit.
- Uçuş dikey ve tek boyutlu; yörünge dönüşü ve açısal kayıplar yok.
- Boş oda kütlesi atılsın ya da atılmasın aynı alındı; tek gövdede ayırma donanımı olmayacağı için gerçekte biraz daha düşük olabilir.
- Mekanizma kütlesi (68,7 kg) tahmindir.
- Çubuklar boğazda 3000 K üzerindeki gazla temas eder; grafit kaplama oksitleyici ortamda aşınır, ısıl dayanım ayrıca hesaplanmalı.
- Boğaz daralırken yakıt basıncı da senkron ayarlanmalı; yoksa yanma odası basıncı yükselir.
- ε = 56 gibi büyük genleşme oranı deniz seviyesinde akış ayrılmasına yol açabilir.
- Etanol halkası (donma ≈ −114 °C) ile LOX omurgası (−183 °C) arasında yalıtım ve sızdırmazlık ayrıca tasarlanmalı; sıvı hidrojen bu sürümde kullanılmıyor.
- Yanan odanın ısısı LOX omurgasına ve komşu odaların etanoluna geçer (LOX buharlaşması, etanol ısınması); ısı geçişi hesaplanmadı.
- Oda-nozul uzaklığının yol açacağı Isp kaybı modelde yok.

**Sonraki adımlar**

1. Mekanizma kütlesini gerçek malzeme ve kesitlerle yeniden hesapla (başa baş sınır 151,9 kg).
2. Oda sayısını 1'den 8'e değiştirip net kazancı tara.
3. Boğaz kapanma hızı ile yakıt basıncı arasındaki kontrol ilişkisini modelle.
4. Çubukların ısıl yükünü ve grafit kaplamanın ömrünü incele.
5. Boş odaları atmanın (ayırma mekanizması) mümkün olup olmadığını ve getirisini hesapla.
6. Besleme sistemini sayıyla modelle: O/F oranı, hat çapları, enjektör basınç düşüşü.
7. Yanan odadan LOX omurgasına ve komşu odaların etanoluna ısı geçişini hesapla.

## Aviyonik

Aviyonik yazılım için bir gerçek zamanlı çekirdek (kernel) kullanılması planlanıyor; henüz tasarlanmadı. Görevleri: evreye göre vana sıralaması, besleme basıncının izlenmesi, çubuk açısının debiyle birlikte ayarlanması (Model 1 ve 6), sensör okuma ve emniyet kesmeleri.

## Kod

`roket_simulasyonu.py` bu belgedeki bütün sayıları üretir (yalnızca standart Python kütüphaneleri):

```
python3 roket_simulasyonu.py
```

Boş odaları atan klasik kademelemeyi denemek için dosyadaki `ODA_ATILIR = True` yapın.

## Lisans

Metin: CC BY 4.0 · Kod: MIT (lisans dosyası eklenmelidir).

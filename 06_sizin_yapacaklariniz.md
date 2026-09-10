# Yürütme Kontrol Listesi

Bu liste, projeyi bu noktadan teslime taşıyan işleri sırayla verir. Sıra bağlayıcıdır: bir bölüm bitmeden sonrakine geçilmez. Süreler tek bir araştırmacı ve bir ikinci kodlayıcı varsayımıyla verilmiştir.

Dosyalar:

| Dosya | Ne işe yarar |
|---|---|
| `forecast_or_finding_ai_ir_evidentiary_audit.md` | Makale taslağı; `[VERİ]` etiketleri boş |
| `01_protocol_preregistration.md` | Dondurulacak protokol; §15 dondurma mekanizmasını tanımlar |
| `02_coding_workbook.xlsx` | Kodlama enstrümanı; 21 pilot iddia içerir |
| `03_reliability_and_analysis.py` | α, betimsel tablolar, aktarım tablosu, atıf analizi |
| `04_sonraki_adimlar.md` | Genel yürütme planı |
| `05_pilot_notu.md` | Pilot notu ve açık kod kitabı soruları |
| `README.md` | Deponun kamuya açık tanıtımı ve dondurma durumu |

---

## 0. Dondurma öncesi kapatılması zorunlu maddeler

Protokol bu bölüm bitmeden dondurulamaz. Bir denetim makalesi, kendi enstrümanı çalışmadan ön kayıt yapamaz.

**Kapatıldı (2026-09-10, `Change_Log` ve Ek D'ye işlendi):**

- [x] `fit_computed` formülü göstergeleri metin olarak sakladığı için `AND(K=1,L=1,M=1)` daima FALSE dönüyordu; "deklare öngörü" hiçbir zaman `adequate` puanlanamıyordu. Formül ve veri katmanı düzeltildi, beş test satırıyla doğrulandı.
- [x] `w4_developed` sütunu eklendi; "analoji tam bir bölümde geliştirilmiş" koşulu artık veri, kodlayıcı takdiri değil.
- [x] `orig_scope_conditions`, `orig_conjectural_status`, `orig_falsifier` sütunları eklendi; Tablo 4, RQ3 ve H2 artık hesaplanabilir.
- [x] `w3_source_peer_reviewed`, `secondary_claim_type`, `p4_causal_flag` sütunları eklendi.
- [x] Atıf yönü tek bir yerde tanımlandı (protokol §10): yıl içi yüzdelik sıra, 0 = en çok atıf alan. Makale 6.6 ve betik çıktısı buna göre düzeltildi.
- [x] Uyum matrisi tam olarak yayımlandı (Ek A.5, 66 kombinasyon) ve normatif yönlendirme kaldırıldı.
- [x] Bölüm 7'deki üç "pilot kodlamada şu çıktı" ifadesi çalışma kitabıyla uyumlu hale getirildi; 7.3 pilotta hiç kodlanmadığını açıkça söylüyor.
- [x] İddia türü tek değerli yapıldı, `secondary_claim_type` eklendi.
- [x] Betikteki sessiz α geçişi kapatıldı: çift kodlama yoksa "not computed / NOT a pass" yazıyor.

**Hâlâ açık, karar sizin:**

- [ ] **W6 ile W3→haber ayrımı.** Kod kitabına iki somut örnek yazın. Pilotta Cummings raporu W6, NYT haberi W3→to_W4W8 kodlandı; ayrım savunulabilir ama örnekle sabitlenmeli, yoksa çift kodlamada α düşürür.
- [ ] **P1/P4 sınırı için karar ağacı.** "framework", "agenda", "initial framework" ifadeleri tek başına P4'e iter mi? Pilotta Horowitz 2018 tam bu ifade yüzünden P4'e gitti ve iki kodlayıcı burada kolayca ayrışır. Positioning α'sı 0,70'in altına düşerse tüm konumlandırma temelli analiz gider.
- [ ] **Örneklem seed'i.** Protokol §6'daki boşluk. Şimdi seçin ve yazın; sonra seçilirse ön kayıt anlamını yitirir.
- [ ] **Lisans.** README'de "dondurmadan önce seçilecek" yazıyor. Öneri: metin ve veri için CC BY 4.0, betik için MIT.
- [ ] **Kodlayıcı adları** protokol §9'a.

Karara bağlanan her madde `Change_Log`'a ve makale Ek D'ye işlenir.

## 1. Erişim ve hesaplar (1 saat)

- [ ] Kurumunuzun Web of Science Core Collection ve Scopus erişimini doğrulayın. Yalnızca biri varsa protokol §3 değişir ve tek veritabanlı sürüme uyarlanması gerekir; bu bir protokol değişikliğidir, dondurmadan önce yapılmalıdır.
- [ ] GitHub deposunun public olduğunu doğrulayın: <https://github.com/McahitKutsal/-Evidentiary-Audit-of-the-AI-IR-Literature>
- [ ] Zenodo hesabı açın (zenodo.org), GitHub ile giriş yapın, bu depoyu Zenodo'da açık konuma getirin. Dondurmanın kurcalanamazlığı buna bağlıdır (protokol §15).
- [ ] `main` dalı için force-push'u kapatın (Settings → Branches → Branch protection).
- [ ] Rayyan hesabı açın (rayyan.ai). Ücretsiz sürüm yeterli.
- [ ] Zotero kurun.

## 2. İkinci kodlayıcı (değişken süre, en erken başlatılacak iş)

Bu, kritik yoldaki en uzun süreli ve en çok gecikme üreten maddedir. Bölüm 6'ya kadar beklemeyin.

- [ ] UÜ'de lisansüstü eğitimi olan bir ikinci kodlayıcı bulun. Protokol iki insan kodlayıcı öngörüyor.
- [ ] Kod kitabını (makale Ek A + `Legend` sayfası) birlikte okuyun; en az 2 saatlik kalibrasyon oturumu yapın.
- [ ] Kalibrasyonu iki gerçek makale üzerinde yapın ve α'yı orada bir kez hesaplayın. Düşükse kod kitabı sorunludur, kodlayıcı değil.
- [ ] Yapay zekâ destekli kodlama kullanılacaksa bunu şimdi kararlaştırın ve makalede açıkça beyan edin. Beyan edilmemiş yapay zekâ kodlaması, bu makalenin savunduğu şeffaflık ilkesiyle çelişir; beyan edilmiş ve insan kodlamasıyla karşılaştırılmış bir üçüncü okuyucu ise savunulabilir.

## 3. Protokolü dondurun (1 gün)

**Ön koşul: Bölüm 0'daki açık maddelerin tamamı kapatılmış olmalı.**

- [ ] Protokoldeki boşlukları doldurun: seed, tarih, kodlayıcı adları.
- [ ] Ek C'deki arama dizesini son kez okuyun. Terim eklemek için son fırsat.
- [ ] `git add -A && git commit && git push`
- [ ] `git tag -a protocol-frozen -m "Protocol frozen before coding"` ve `git push origin protocol-frozen`
- [ ] GitHub'da bu etiketten **release** yayımlayın. Yalnızca tag yeterli değildir; Zenodo release'i dinler.
- [ ] Zenodo release'i arşivlesin ve DOI üretsin. **DOI gelmeden protokol dondurulmuş sayılmaz** (protokol §15).
- [ ] `git rev-parse protocol-frozen^{commit}` ile tam SHA'yı alın.
- [ ] SHA'yı, etiket tarihini ve DOI'yi dört yere yazın: protokol §1, makale 5.1, `Change_Log` ilk satırı, README.
- [ ] Bundan sonra her değişiklik yeni bir commit ve `Change_Log` satırıdır. Geçmiş yeniden yazılmaz.

## 4. Tarama (1 hafta)

- [ ] WoS'ta Ek C dizesini çalıştırın. Kategori: International Relations; Political Science. Belge türü: Article. Yıl: 2015–2025.
- [ ] Scopus'ta eşdeğer dizeyi çalıştırın. Alan: Social Sciences. Belge türü: Article.
- [ ] Tarama tarihini not edin; sonuç sayılarını Ek B'ye yazın.
- [ ] Aynı dizeyi 2010–2025 için yıl yıl çalıştırıp Ek C tablosunu doldurun. Bu, 2015 başlangıcının gerekçesidir.
- [ ] RIS olarak dışa aktarın, Zotero'ya alın, tekilleştirin.
- [ ] Dizenin "security studies" makalelerini WoS kategori filtresiyle kaçırıp kaçırmadığını kontrol edin: makalenin kendi kaynakçasındaki birkaç çalışmayı (Goldfarb & Lindsay 2022, Bode & Huelss 2018, Ding & Dafoe 2021) dizeyle bulabiliyor musunuz? Bulamıyorsanız dize eksiktir ve bu dondurmadan önce düzeltilmelidir.

## 5. Eleme (1–2 hafta)

- [ ] Rayyan'a yükleyin. İki tarayıcı, kör mod, başlık/özet düzeyi.
- [ ] Uyuşmazlıkları tartışarak çözün; çözülemeyenler tam metne geçer.
- [ ] Tam metinleri indirin. Erişilemeyenler için kütüphaneler arası ödünç; sayıyı PRISMA'ya "not retrievable" yazın.
- [ ] Tam metin elemesi. Her ret için PRISMA gerekçe kategorisi.
- [ ] Dahil edilenleri `Articles` sayfasına girin.
- [ ] N'e göre protokol §6: N ≤ 400 tam kodlama, N > 400 tabakalı örneklem (seed kayıtlı).

## 6. Pilotu tamamlayın (1–2 hafta)

- [ ] Dahil edilenlerden rastgele 15 makale seçin, seed'i kaydedin. Mevcut iki TNSR makalesi ancak dizinleniyorsa listeye girer.
- [ ] İki kodlayıcı bağımsız olarak iddia çıkarsın ve kodlasın.
- [ ] **Uzlaştırma turu.** İki kodlayıcı bağımsız çıkarım yaptığı için `claim_id`'ler eşleşmez. Her iki kodlayıcının da iddia saydığı metin parçalarına ortak `claim_id` atayın. Bu tur yapılmadan hiçbir değişken için α hesaplanamaz; betik "not computed" yazar ve bu bir geçme notu değildir.
- [ ] `python 03_reliability_and_analysis.py 02_coding_workbook.xlsx` çalıştırın.
- [ ] α < 0,70 olan değişkenlerde kod kitabını netleştirin, `Change_Log`'a yazın, o değişkeni yeniden kodlayın.
- [ ] Kanonik iddiaları `Canonical_Claims`'e ekleyin ve listeyi dondurun. **15 makale bu liste için alt sınırdır**; mevcut liste iki makaleden çıkmıştır ve tek başına yetersizdir.
- [ ] `other` oranı %5'i geçiyorsa şemayı resmen revize edin.

## 7. Tam kodlama (gerçekçi süre için aşağıya bakın)

- [ ] Kodlayıcılar `Claims` sayfasını doldurur. Oturum başına 40 iddiadan fazla kodlamayın.
- [ ] Rastgele %25'i çift kodlayın (seed kayıtlı); `Articles.double_coded = yes`.
- [ ] Her W3 iddiada kaynağı açın: alt kod, valans, hakemlilik girin.
- [ ] **W3 + öngörüsel/nedensel-gelecek iddialarda** kaynağı açıp orijinal ifadeyi bulun ve üç göstergeyi `orig_*` sütunlarına ikinci kez girin. Tablo 4, RQ3 ve H2 bu veriye dayanır. Kaynağa erişilemiyorsa `unknown`.
- [ ] Haftada bir `Summary` sayfasına bakın; `CHECK KEY` sıfır olmalı.
- [ ] Bitince betiği çalıştırın; α değerlerini Ek E'ye yazın.

### Kodlama yükü: aritmetik

Planlardaki "4–8 hafta" ifadesi, iş gerçekte şu büyüklükte olduğu için yanıltıcıdır:

| | N = 200 | N = 400 |
|---|---|---|
| Makale başına ~10 iddia | 2.000 iddia | 4.000 iddia |
| Çıkarım + kodlama, iddia başına ~8 dk | 267 saat | 533 saat |
| W3 iddialar (pilotta %33), kaynak açma ~15 dk | 165 saat | 330 saat |
| `orig_*` kodlaması (W3 + gösterge uygun, ~%15) | 75 saat | 150 saat |
| Tek geçiş toplamı | **~507 saat** | **~1.013 saat** |
| + %25 çift kodlama | ~634 saat | ~1.266 saat |

Oturum başına 40 iddia kuralıyla N=200'de kodlayıcı başına en az 50 oturum gerekir. Haftada 15 saat ayıran iki kodlayıcı için N=200 yaklaşık **21 hafta**, N=400 yaklaşık **42 hafta** eder. Tam zamanlı iki kodlayıcı için bile N=200 sekiz haftadan uzundur.

Sonuç: N > 250 çıkarsa tabakalı örneklemi 400'de değil, 200–250 bandında tutmayı ciddi olarak değerlendirin ve bunu protokol §6'ya dondurmadan önce yazın. Kapsamı daraltmak, yarım kalmış bir kodlamadan iyidir.

## 8. Atıf verisi (2 gün)

- [ ] Tek kaynaktan (Scopus önerilir), tek günde, tüm makalelerin atıf sayısını çekin. Tarihi kaydedin.
- [ ] `Articles.citations_raw` ve `citation_date` doldurun.
- [ ] `citations_per_year` formülündeki yıl sabiti **2026**'dır. Farklı bir yılda çekiyorsanız `Articles` N sütunundaki formülü güncelleyin; unutulursa tüm atıf analizi sessizce yanlış çıkar.

## 9. Analiz ve `[VERİ]` doldurma (2 hafta)

- [ ] Betiği son kez çalıştırın.
- [ ] Makaledeki 57 `[VERİ]` etiketini doldurun. Her etiketin ne istediği metinde yazılıdır.
- [ ] Bölüm 6.7 sonucuna göre Bölüm 7'deki üç aday iddiayı yeniden sıralayın veya değiştirin. Sıralama farklı çıkarsa bölüm yeniden yazılır; şu anki üç aday kodlama öncesi seçimdir ve metinde böyle işaretlidir.
- [ ] Bölüm 8 "Self-application": makalenin kendi iddialarını şemadan geçirin. W8 çıkan iddia kaldırılır veya yeniden gerekçelendirilir.
- [ ] Bitiş kriteri: üç kapanış cümlesi yazılabiliyor mu? Yazılamıyorsa makale bitmemiştir.

## 10. Teslim öncesi (2 gün)

- [ ] Kaynakçadaki her girişi DOI ile doğrulayın. Özellikle: Horowitz vd. 2023 (*AI & Society*), Johnson 2022 (JSS), Garcia 2018 (ISR sayfa aralığı), Horowitz & Lin-Greenberg 2022 (ISQ makale numarası), Lin-Greenberg 2022 (JCR sayfa aralığı).
- [ ] `—` araması: sıfır olmalı.
- [ ] Yasaklı kalıp araması.
- [ ] Yazar notunu ve `[VERİ]` kalıntılarını silin.
- [ ] Türkçe kalıntı araması: makale İngilizcedir; `[VERİ]` etiketleri ve yazar notu Türkçedir ve tamamı silinmelidir.
- [ ] `04_sonraki_adimlar.md` dosyasındaki birinci tekil şahıs bölümlerini temizleyin; depo kamuya açıktır.
- [ ] Hedef dergi seçin. Öncelik sırası: *International Studies Review* (yöntem ve meta-araştırmaya en açık olanı, ve makale zaten ISR'de yayımlanmış çalışmalara atıf yapıyor), *Journal of Global Security Studies*, *European Journal of International Security*, *Security Studies*.
- [ ] Teslim sürümünü ikinci bir Zenodo release'i olarak arşivleyin. Makalede hem dondurma DOI'sini hem teslim DOI'sini verin; 8. bölümdeki "codebook is public" sözü buna bağlıdır.

---

## Kritik yol

Sıra şudur ve kısaltılamaz:

```
Bölüm 0 (açık kararlar)  ->  Bölüm 3 (dondurma)  ->  Bölüm 4 (tarama)
     |                                                     |
     +-- Bölüm 1 (hesaplar) paralel                        v
     +-- Bölüm 2 (ikinci kodlayıcı) EN ERKEN         Bölüm 5 (eleme)
                                                           |
                                                           v
                              Bölüm 9 <- Bölüm 7 <- Bölüm 6 (pilot + uzlaştırma)
```

En sık yapılan hata Bölüm 2'yi geciktirmektir: ikinci kodlayıcı bulunmadan Bölüm 6 başlayamaz, Bölüm 6 bitmeden Bölüm 7 başlayamaz.

## Adlandırılmamış riskler

- TNSR'nin WoS/Scopus'ta dizinlenip dizinlenmediği doğrulanmadı. Dizinlenmiyorsa iki pilot makale korpus dışı kalır.
- Veritabanı erişimi proje ortasında kesilirse tarama tekrarlanamaz. Tarama sonuçlarının ham dışa aktarımını depoda saklayın.
- Kanonik iddia listesi dondurulduktan sonra korpusta sık geçen ama listede olmayan bir iddia çıkarsa, o iddia merkezîlik sıralamasına giremez. Ek D'ye kayıtla ekleme yapılabilir; bunun kuralını şimdi yazın.
- Kodlayıcı ayrılırsa çift kodlama oranı düşer ve α yeniden hesaplanamaz.
- Tam metin erişim oranı düşük çıkarsa PRISMA "not retrievable" sayısı büyür ve korpus temsil gücünü yitirir.

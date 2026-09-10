# Sonraki Adımlar: Yürütme Planı

Makale taslağı, protokol, kodlama çalışma kitabı ve analiz betiği hazır. Bundan sonrası veri gerektirir ve veri yalnızca WoS/Scopus erişimiyle üretilebilir. Aşağıdaki sıra manifestonun III. bölümüne göre düzenlenmiştir.

## Aşama 0: Protokolü dondur (1 gün)

- [ ] `01_protocol_preregistration.md` dosyasını oku, seed ve tarihleri doldur.
- [ ] Depo: <https://github.com/McahitKutsal/-Evidentiary-Audit-of-the-AI-IR-Literature>. Protokol, çalışma kitabı, betik ve makale taslağı commit edilir.
- [ ] Açık kod kitabı kararları kapatılmadan dondurma yapılmaz (bkz. `06_sizin_yapacaklariniz.md` §1).
- [ ] Dondurma: `git tag -a protocol-frozen -m "..."` ve `git push origin protocol-frozen`. GitHub'da release oluştur.
- [ ] Zenodo'yu depoya bağla, release'i arşivle, DOI'yi al. DOI olmadan dondurma tamamlanmış sayılmaz (protokol §15).
- [ ] SHA, tag tarihi ve DOI'yi protokol §1'e, makale 5.1'e ve `Change_Log` ilk satırına yaz.
- [ ] Bu andan sonra şema değişikliği yalnızca `Change_Log` sayfası ve yeni bir commit üzerinden. `--force` push kapalı.

## Aşama 1: Tarama (1 hafta)

- [ ] WoS Core Collection ve Scopus'ta Ek C'deki dizeyi çalıştır. Tarama tarihini kaydet.
- [ ] Aynı dizeyi 2010–2025 için yıl yıl çalıştır, hit sayılarını Ek C tablosuna gir (2015 başlangıç gerekçesi).
- [ ] Kayıtları dışa aktar (RIS/CSV), Zotero veya Rayyan'da tekilleştir.
- [ ] Her adımın sayısını PRISMA tablosuna (Ek B) gir.

## Aşama 2: Eleme (1–2 hafta)

- [ ] İki tarayıcı, başlık/özet düzeyinde bağımsız. Rayyan bunun için uygundur.
- [ ] Tam metin eleme. Ret gerekçeleri PRISMA kategorilerine göre.
- [ ] Dahil edilen makaleleri `02_coding_workbook.xlsx` → `Articles` sayfasına gir.
- [ ] N > 400 ise tabakalı örneklem; N ≤ 400 ise tam kodlama. Kararı Change_Log'a değil, protokolün 6. maddesine göre uygulandığını yöntem bölümüne yaz.

## Aşama 3: Pilot (1 hafta)

- [ ] Rastgele 15 makale seç. İki kodlayıcı bağımsız olarak iddia çıkarsın ve kodlasın.
- [ ] `03_reliability_and_analysis.py` çalıştır. α < 0,70 olan değişkenlerde kod kitabını netleştir, değişikliği Change_Log'a yaz.
- [ ] Pilotta ortaya çıkan kanonik iddiaları `Canonical_Claims` sayfasına ekle. Bu liste pilottan sonra dondurulur.
- [ ] Bölüm 4.1'deki "other" oranı %5'i aşıyorsa şemayı resmen revize et.

## Aşama 4: Tam kodlama (4–8 hafta, N'e bağlı)

- [ ] Kodlayıcılar `Claims` sayfasında sarı hücreleri doldurur. `fit_computed` otomatik hesaplanır; `fit_final` ona eşit girilir, farklıysa `override_reason` zorunlu.
- [ ] Örneklemin en az %25'i çift kodlanır (`Articles.double_coded = yes`).
- [ ] W3 iddialarda atıf yapılan kaynak açılır, alt kod ve valans girilir.
- [ ] Yorgunluk bayrağı: bir oturumda 40'tan fazla iddia kodlama. Manifesto VI. bölüm.

## Aşama 5: Atıf verisi (2 gün)

- [ ] Tek bir kaynaktan (tercihen Scopus) tek bir tarihte atıf sayılarını çek, `Articles.citations_raw` ve `citation_date` doldur.
- [ ] `citations_per_year` formülü otomatik. Yıl sabiti (2026) formülde gömülü; farklı yılda yapılırsa düzelt.

## Aşama 6: Analiz ve yazım (2 hafta)

- [ ] `03_reliability_and_analysis.py` çıktısını makaledeki `[VERİ]` etiketlerine işle. Her etiketin ne istediği metinde yazılı.
- [ ] Bölüm 6.7 çıktısına göre Bölüm 7'deki üç aday iddiayı yeniden sırala veya değiştir.
- [ ] Bölüm 8 "Self-application": makalenin kendi iddialarını şemadan geçir, sonucu yaz.
- [ ] Bölüm VII bitiş kriteri: üç cümle yazılabiliyor mu? Yazılamıyorsa makale bitmemiştir.
- [ ] Teslim öncesi: `—` araması, yasaklı kalıp araması, kaynakça DOI kontrolü, yazar notunu sil.

## Benim yapabileceklerim

Tam metinleri (PDF) yüklerseniz: pilot kodlama için ikinci kodlayıcı olarak iddia çıkarabilir ve kodlayabilirim; bu, insan kodlayıcıyla α hesaplamak için kullanılabilir. Ancak nihai güvenilirlik raporu için manifesto iki insan kodlayıcı öngörüyor; benim kodlamam üçüncü okuyucu veya pilot kontrolü olarak konumlandırılmalı.

PRISMA dışa aktarımını (CSV) yüklerseniz: tekilleştirme, yıl/dergi dağılımı ve tabakalı örneklem çekimini yapabilirim.

Kodlanmış çalışma kitabını yüklerseniz: analizi çalıştırıp `[VERİ]` etiketlerini doldurabilirim.

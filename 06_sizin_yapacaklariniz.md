# Bu Noktadan Sonra Sizin Yapmanız Gerekenler

Aşağıdaki liste yalnızca benim yapamayacağım, sizin elinizde olan işleri içerir. Her maddenin yanında hangi dosyaya dokunduğu ve tahmini süresi var. Sıra önemlidir: bir üst madde bitmeden alttakine geçmeyin.

Elinizdeki dosyalar:

| Dosya | Ne işe yarar |
|---|---|
| `forecast_or_finding_ai_ir_evidentiary_audit.md` | Makale taslağı; `[VERİ]` etiketleri boş |
| `01_protocol_preregistration.md` | Depoya dondurulacak protokol (§15 dondurma mekanizmasını tanımlar) |
| `02_coding_workbook.xlsx` | Kodlama çalışma kitabı; 21 pilot iddia içeriyor |
| `03_reliability_and_analysis.py` | α ve bulgu tabloları |
| `04_sonraki_adimlar.md` | Genel yürütme planı |
| `05_pilot_notu.md` | Pilottan çıkan altı kod kitabı sorunu |

---

## 1. Kod kitabı kararları (yarım gün)

`05_pilot_notu.md` içindeki altı sorunun her biri için bir karar verin. Karar sizin, ama kararsız kalmayın; protokol bunlar çözülmeden dondurulamaz.

- [ ] Karşıt senaryo kurmak "yanlışlayıcı" sayılacak mı? (Benim önerim: hayır.)
- [ ] W3 alt kodu kaynağın veri taşımasına mı, hakemli olmasına mı bakacak? (Önerim: veri taşımasına; hakemlilik ayrı sütun.)
- [ ] `Claims` sayfasına `w4_developed` (0/1) sütunu eklenecek mi? (Önerim: evet. İsterseniz formülü ben güncellerim.)
- [ ] W6 (uzman görüşü) ile W3→haber ayrımı için kod kitabına iki örnek yazın.
- [ ] P4 nedensel iddialar raporda nasıl gösterilecek: ayrı tablo mu, ana dağılımdan dışlanma mı?
- [ ] P1/P4 sınırı için karar ağacı: "framework/agenda" ifadesi tek başına P4'e iter mi?

Kararları makaledeki Ek A'ya ve `01_protocol_preregistration.md` 8. maddeye işleyin. Bunu bana gönderirseniz ben işlerim.

## 2. Erişim ve hesaplar (1 saat)

- [ ] Kurumunuzun Web of Science Core Collection ve Scopus erişimini doğrulayın. İkisinden biri yoksa protokolün 3. maddesi değişir; o zaman bana söyleyin, tek veritabanlı versiyona uyarlarım.
- [ ] GitHub deposunun herkese açık (public) olduğunu doğrulayın: <https://github.com/McahitKutsal/-Evidentiary-Audit-of-the-AI-IR-Literature>
- [ ] Zenodo hesabı açın (zenodo.org), GitHub ile giriş yapın ve bu depoyu Zenodo'da açık konuma getirin. Ücretsiz. Dondurmanın kurcalanamazlığı buna bağlı (protokol §15).
- [ ] Depo ayarlarında `main` dalı için force-push'u kapatın (Settings → Branches → Branch protection).
- [ ] Eleme için Rayyan hesabı açın (rayyan.ai). Ücretsiz sürüm yeterli.
- [ ] Zotero kurun; kayıt dışa aktarımı için gerekli.

## 3. İkinci kodlayıcı (değişken süre, erken başlayın)

- [ ] UÜ'de lisansüstü eğitimi olan bir ikinci kodlayıcı bulun. Manifesto ve protokol iki insan kodlayıcı öngörüyor; benim kodlamam üçüncü okuyucu olarak kullanılabilir, ikinci kodlayıcı yerine geçemez.
- [ ] İkinci kodlayıcıyla kod kitabını (makale Ek A + `02_coding_workbook.xlsx` Legend sayfası) birlikte okuyun, 2 saatlik bir kalibrasyon oturumu yapın.

## 4. Protokolü dondurun (1 gün)

- [ ] `01_protocol_preregistration.md` içindeki boşlukları doldurun: örneklem seed'i, tarih, kodlayıcı adları.
- [ ] Ek C'deki arama dizesini son kez okuyun; eklemek istediğiniz terim varsa şimdi ekleyin, sonra ekleyemezsiniz.
- [ ] Her şeyi commit edip push edin: `git add -A && git commit && git push`.
- [ ] Dondurma etiketini atın:
      `git tag -a protocol-frozen -m "Protocol frozen before coding"` ve `git push origin protocol-frozen`.
- [ ] GitHub'da bu etiketten bir **release** yayımlayın (yalnızca tag yeterli değil; Zenodo release'i dinler).
- [ ] Zenodo release'i arşivleyip DOI üretsin. **DOI gelmeden protokol dondurulmuş sayılmaz** (protokol §15).
- [ ] Etiketli commit'in tam SHA'sını alın: `git rev-parse protocol-frozen^{commit}`.
- [ ] SHA'yı, etiket tarihini ve Zenodo DOI'sini üç yere yazın: protokol §1, makale 5.1, `Change_Log` ilk satırı.
- [ ] Bu andan sonra her değişiklik `Change_Log`'a tarih ve gerekçeyle girilir ve yeni bir commit olur. Geçmiş yeniden yazılmaz.

## 5. Tarama (1 hafta)

- [ ] WoS'ta Ek C'deki dizeyi çalıştırın. Kategori filtresi: International Relations; Political Science. Belge türü: Article. Yıl: 2015–2025.
- [ ] Scopus'ta eşdeğer dizeyi çalıştırın. Alan: Social Sciences. Belge türü: Article.
- [ ] Her ikisinde de tarama tarihini not edin; sonuç sayılarını hemen Ek B'ye yazın.
- [ ] Aynı dizeyi 2010'dan 2025'e yıl yıl çalıştırıp hit sayılarını Ek C tablosuna girin. Bu, 2015 başlangıç gerekçesidir.
- [ ] Sonuçları RIS olarak dışa aktarın, Zotero'ya alın, tekilleştirin.
- [ ] **Bana gönderebileceğiniz nokta:** RIS/CSV dosyasını yüklerseniz tekilleştirme kontrolü, yıl/dergi dağılımı ve gerekirse tabakalı örneklem çekimini yaparım.

## 6. Eleme (1–2 hafta)

- [ ] Rayyan'a yükleyin. İki tarayıcı, kör mod, başlık/özet düzeyi.
- [ ] Uyuşmazlıkları tartışarak çözün; çözülemeyenler tam metne geçer.
- [ ] Tam metinleri indirin. Erişemediğiniz makaleler için kütüphaneler arası ödünç; sayısını PRISMA'ya "not retrievable" olarak yazın.
- [ ] Tam metin elemesi. Her ret için PRISMA gerekçe kategorisi.
- [ ] Dahil edilen listeyi `Articles` sayfasına girin (article_id, yazar-yıl, dergi, yıl, db_source).
- [ ] N sayısına göre protokolün 6. maddesini uygulayın: N ≤ 400 tam kodlama, N > 400 tabakalı örneklem.

## 7. Pilot tamamlama (1 hafta)

- [ ] Dahil edilenlerden rastgele 15 makale seçin (seed kaydedin). Mevcut 2 pilot makale TNSR dizinleniyorsa listeye eklenebilir.
- [ ] İki kodlayıcı bağımsız olarak iddia çıkarsın ve kodlasın. Bana da PDF'leri yüklerseniz üçüncü kodlayıcı olarak kodlarım.
- [ ] `python 03_reliability_and_analysis.py 02_coding_workbook.xlsx` çalıştırın.
- [ ] α < 0,70 olan değişkenler için kod kitabını netleştirin, `Change_Log`'a yazın, o değişkeni pilotta yeniden kodlayın.
- [ ] Pilottan çıkan kanonik iddiaları `Canonical_Claims`'e ekleyin. Listeyi dondurun.
- [ ] `other` iddia türü oranı %5'i geçiyorsa şemayı resmen revize edin.

## 8. Tam kodlama (4–8 hafta)

- [ ] Kodlayıcılar `Claims` sayfasını doldurur. Günde 40 iddiadan fazlasını kodlamayın; yorgunluk uyuşmazlığı artırır.
- [ ] Rastgele %25'i (seed kayıtlı) çift kodlayın; `Articles.double_coded = yes`.
- [ ] Her W3 iddiada atıf yapılan kaynağı açın, alt kod ve valans girin. Kaynağa erişilemiyorsa `unknown`.
- [ ] Haftada bir `Summary` sayfasına bakın; `CHECK KEY` sayısı sıfır olmalı.
- [ ] Bitince betiği çalıştırın; tüm α değerlerini Ek E'ye yazın.

## 9. Atıf verisi (2 gün)

- [ ] Tek kaynaktan (Scopus önerilir), tek günde, tüm makalelerin atıf sayısını çekin. Tarihi kaydedin.
- [ ] `Articles.citations_raw` ve `citation_date` doldurun. `citations_per_year` otomatik hesaplanır.
- [ ] Formüldeki yıl sabiti 2026'dır; 2027'de yapıyorsanız `Articles` N sütunundaki formülü güncelleyin ya da bana söyleyin.

## 10. Analiz ve `[VERİ]` doldurma (2 hafta)

- [ ] Betiği son kez çalıştırın. Çıktıyı ve çalışma kitabını bana yüklerseniz makaledeki 50 civarı `[VERİ]` etiketini doldurur, tabloları üretir, Bölüm 7'deki üç aday iddiayı 6.7 sonucuna göre yeniden hizalarım.
- [ ] Bölüm 8 "Self-application": makalenin kendi iddialarını şemadan geçirin (ben de yapabilirim, ama bağımsız bir göz daha iyi).
- [ ] Manifesto VII bitiş kriteri: üç cümle yazılabiliyor mu? Yazılamıyorsa bitmemiştir.

## 11. Teslim öncesi (2 gün)

- [ ] Kaynakçadaki her girişi DOI ile doğrulayın. Özellikle: Horowitz vd. 2023 (*AI & Society*), Johnson 2022 (JSS), Garcia 2018 (ISR sayfa aralığı).
- [ ] `—` araması: sıfır olmalı.
- [ ] Yasaklı kalıp araması (Manifesto 15).
- [ ] Yazar notunu ve `[VERİ]` kalıntılarını silin.
- [ ] Hedef dergi seçin ve stil kılavuzuna uyarlayın. Aday dergiler: *International Studies Review* (yöntem/meta çalışmalara açık), *Journal of Global Security Studies*, *European Journal of International Security*, *Security Studies*.
- [ ] Kodlama çalışma kitabını, protokolü ve betiği depoda açık bırakın ve teslim sürümünü ikinci bir Zenodo release'i olarak arşivleyin; makale 8. bölümde "codebook is public" diyor, bu sözün tutulması gerekir. Makalede hem dondurma DOI'sini hem teslim DOI'sini verin.

---

## Bana ne zaman dönebilirsiniz

| Aşama | Yükleyin | Ben yaparım |
|---|---|---|
| 1 | Altı karar | Ek A, protokol ve formülleri güncellerim |
| 5 | RIS/CSV | Tekilleştirme, dağılım, örneklem |
| 7–8 | PDF'ler | Üçüncü kodlayıcı olarak iddia çıkarma ve kodlama |
| 10 | Doldurulmuş xlsx | `[VERİ]` etiketleri, tablolar, Bölüm 7 hizalama |
| 11 | Son taslak | Biçim kontrolü, dergi formatına uyarlama |

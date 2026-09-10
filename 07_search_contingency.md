# Arama Beklenmedik Durum Planı ve Kapsam Kontrolü

**Tarih:** 2026-09-10
**Durum:** Doğrulanmış fizibilite kontrolü. Uygulanmış bir tasarım değildir.

## Neden bu dosya var

Protokol §3 taramanın Web of Science Core Collection ve Scopus üzerinde yapılacağını söylüyor. Bu ikisi ücretli aboneliktir. Erişim doğrulanmadan protokol dondurulursa, protokol yapılamayacak bir şeyi taahhüt etmiş olur.

Bu dosya iki soruyu yanıtlar:

1. Abonelik veritabanları olmadan bu korpus geri getirilebilir mi?
2. Getirilebiliyorsa, hangi tasarım değişiklikleriyle?

İkinci bir işlevi daha var: WoS/Scopus erişimi mevcut olsa bile, aramanın açık bir veritabanında tekrarlanması **kapsam çapraz kontrolü** sağlar ve hakem karşısında taramanın tescilli bir kategori şemasına bağımlı olmadığını gösterir.

## Bulunan sonuç: OpenAlex uygulanabilir

[OpenAlex](https://openalex.org) ücretsiz, açık, API erişimli bir bibliyografik veritabanıdır (Microsoft Academic Graph'ın halefi). Aşağıdakiler 2026-09-10'da canlı API üzerinde test edilmiştir.

### Doğrulanan yetenekler

- 14 çekirdek UÜ/güvenlik dergisi ISSN ve OpenAlex kaynak kimliğiyle çözümlendi.
- Bu 14 dergiyle sınırlı, 2015–2025 aralığında bir YZ terim araması **90 makale** döndürdü.
- Sonuçlar makalenin kendi kaynakçasındaki çalışmaları içeriyor: Bode & Huelss (RIS), Payne (Survival), Goldfarb & Lindsay (IS), Ding & Dafoe (Security Studies), Gilli & Gilli (IS), Jensen/Whyte/Cuomo (ISR), Garcia (ISR), Lin-Greenberg (JCR).
- Horowitz & Lin-Greenberg 2022 (ISQ, `10.1093/isq/sqac069`) veritabanında mevcut.
- Her kayıt `cited_by_count` taşıyor; bu, protokol §10'daki atıf verisi ihtiyacını da karşılar.

### Çözümlenen dergiler

| Dergi | OpenAlex ID | ISSN-L |
|---|---|---|
| International Organization | S160686149 | 0020-8183 |
| International Security | S99767407 | 0162-2889 |
| International Studies Quarterly | S91639875 | 0020-8833 |
| International Studies Review | S58664585 | 1468-2486 |
| European Journal of International Relations | S40975480 | 1354-0661 |
| Review of International Studies | S131264395 | 0260-2105 |
| Security Studies | S200906791 | 0963-6412 |
| Journal of Strategic Studies | S199078552 | 0140-2390 |
| Journal of Conflict Resolution | S20177303 | 0022-0027 |
| Journal of Global Security Studies | S4210202304 | 2057-3170 |
| European Journal of International Security | S4210168251 | 2057-5637 |
| Contemporary Security Policy | S41834288 | 1352-3260 |
| Survival | S27717133 | 0039-6338 |
| Texas National Security Review | S5407008543 | 2576-1153 |

Bu liste eksiktir. Tam tasarımda *International Affairs*, *Foreign Policy Analysis*, *Millennium*, *Cooperation and Conflict*, *International Political Sociology*, *Global Studies Quarterly*, *Intelligence and National Security*, *Defence Studies*, *Journal of Peace Research* ve benzerleri eklenmelidir.

## Tasarım değişikliği: kategori yerine dergi listesi

Protokol §4 uygunluğu "her iki veritabanında UÜ, siyaset bilimi veya güvenlik çalışmaları kategorisinde dizinlenen dergiler" diye tanımlıyor. Bu kategori şeması WoS/Scopus'a özgüdür ve OpenAlex'te karşılığı yoktur.

Çözüm, korpusu **önceden belirlenmiş açık bir dergi listesiyle** tanımlamaktır. Bu bir taviz değil, daha güçlü bir tasarımdır:

- Liste makalede yayımlanır; okuyucu tam olarak neyin dahil edildiğini görür.
- Tescilli, gözden geçirilemeyen bir sınıflandırmaya bağımlılık ortadan kalkar.
- Tekrarlanabilirlik artar: aynı liste ve aynı sorguyla herkes aynı korpusu üretebilir.
- WoS kategorileri zaten gürültülüdür; "International Relations" kategorisi hem dahil etmemesi gereken dergileri içerir hem de güvenlik çalışmaları dergilerini kaçırır.

Bedeli: dergi listesinin kendisi bir seçim kararıdır ve gerekçelendirilmesi gerekir. Liste dondurmadan önce sabitlenmeli ve Ek C'de yayımlanmalıdır.

## Kapatılması gereken üç teknik sorun

Bunlar OpenAlex'e geçilirse protokole yazılmak zorundadır. Hiçbiri engelleyici değildir, ama hiçbiri kendiliğinden çözülmez.

### 1. Yayın yılı, sayı yılı değil çevrimiçi-ilk yılıdır

Testte gözlenen sapmalar:

| Çalışma | Gerçek sayı yılı | OpenAlex yılı |
|---|---|---|
| Johnson, "Delegating Strategic Decision-Making" (JSS) | 2022 | 2020 |
| Jensen, Whyte & Cuomo, "Algorithms at War" (ISR) | 2020 | 2019 |

Bu iki yeri birden bozar: 2015–2025 sınırını ve **yıl içi atıf sıralamasını** (protokol §10). Yıl içi yüzdelik sıra, makaleler yanlış yıla düşerse anlamsızlaşır.

Çözüm: yılı `publication_year` yerine `biblio.issue`/`biblio.volume` ve Crossref sayı tarihinden türetin; ya da protokolde yılın çevrimiçi-ilk tarihi olarak tanımlandığını açıkça yazın ve tutarlı uygulayın. İkincisi daha basittir ve savunulabilir, ama beyan edilmelidir.

### 2. TNSR yetersiz dizinlenmiş

- *Texas National Security Review* için toplam yalnızca 46 kayıt var.
- Horowitz 2018 dergi makalesi olarak değil, **Texas ScholarWorks depo kaydı** olarak görünüyor (`10.15781/t2639kp49`).
- Lin-Greenberg 2020'nin dergi alanı boş (`null`).

Her iki pilot makale de TNSR'dir. Bu, TNSR'nin WoS/Scopus'ta dizinlenip dizinlenmediği sorusunu (pilot notunda zaten açık) ikiye katlar: OpenAlex'te de sorunlu.

Çözüm: dergi listesindeki her başlık tek tek doğrulanmalı; kayıt sayısı beklenenin çok altındaysa o dergi ya listeden çıkarılır ya da elle tamamlanır ve bu durum Ek C'de belirtilir.

### 3. Cümle araması WoS `TS=` gibi davranmıyor

Tırnak içine alınmış bir ifade beklenen tam eşleşmeyi vermiyor: `"Algorithms and Influence"` araması 2.297 sonuç döndürdü. OpenAlex kök-tabanlı ve OR ağırlıklı eşleşme yapıp sonuçları sıralıyor.

Çözüm: Ek C'deki dize OpenAlex sözdizimine yeniden yazılmalı ve **bilinen-kayıt testiyle** doğrulanmalıdır: makalenin kaynakçasındaki bilinen YZ-UÜ makalelerinin listesi hazırlanır, sorgu çalıştırılır, kaçının geri geldiği raporlanır. Bu test dondurmadan önce yapılır ve sonucu Ek C'ye yazılır.

## Korpus büyüklüğü tahmini

14 dergiyle 90 makale. Liste 30–40 dergiye çıkarıldığında beklenen aralık kabaca **200–350** makaledir.

Bu, protokol §6'daki N ≤ 400 dalına düşer, yani **tam kodlama** yapılır ve tabakalı örneklem gerekmez. Ancak `06_sizin_yapacaklariniz.md` Bölüm 7'deki yük hesabı geçerliliğini korur: N=250'de çift kodlamayla yaklaşık 630 saat. Dergi listesini dar tutmak (20 çekirdek dergi, N≈150) yükü yaklaşık 380 saate indirir ve projeyi tek bir araştırmacı için tamamlanabilir kılar.

## Öneri

1. Önce üniversite kütüphanesi üzerinden WoS Core Collection ve Scopus erişimini kontrol edin. Erişim varsa protokol §3 olduğu gibi kalır.
2. Erişim olsun olmasın, OpenAlex taramasını **kapsam çapraz kontrolü** olarak çalıştırın ve sonucu Ek C'ye bir satır olarak yazın. Maliyeti düşük, hakem karşısındaki değeri yüksektir.
3. Erişim yoksa OpenAlex birincil kaynak olur, dergi listesi Ek C'de yayımlanır ve yukarıdaki üç sorun protokole yazılır.

Hangi yol seçilirse seçilsin, karar `Change_Log`'a, protokol §16 madde 7'ye ve makale Ek D'ye işlenir.

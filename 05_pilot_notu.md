# Pilot Kodlama Notu (2 makale, 21 iddia)

**Tarih:** 2026-09-07
**Kodlayıcı:** CL (Claude), tek kodlayıcı. Bu pilot protokol verisi değildir; kod kitabını gerçek metinde sınamak içindir.
**Makaleler:** Horowitz 2018 (TNSR 1/3) ve Lin-Greenberg 2020 (TNSR 3/2). İkisi de açık erişimli tam metin. TNSR'nin WoS/Scopus'ta UÜ kategorisinde dizinlenip dizinlenmediği doğrulanmalı; dizinlenmiyorsa bu makaleler korpus dışı kalır ama pilot amacı için sorun yok.

## Ne çıktı

| | Değer |
|---|---|
| İddia türü | %48 öngörüsel, %19 betimsel, %14 kavramsal, %14 nedensel, %5 normatif |
| Birincil gerekçe | W3 %33, W4 %24, W5 %14, W7 %14, W6 %10, W2 %5. **W1 yok, W8 yok.** |
| Uyum | %52 adequate, %48 partial, inadequate yok |
| Kapsam koşulu | öngörüsel iddiaların %45'inde var |
| Varsayımsal statü sinyali | %91'inde var |
| Yanlışlayıcı | **%0** |
| Deklare öngörü (3/3) | 0 |
| Dolaşımdaki bulgu (0/3) | 1 iddia (K0015) |

Bu iki makale özelinde tablo şunu söylüyor: yazarlar varsayımsal statüyü neredeyse her yerde işaretliyor, kapsam koşulunu yarı yarıya belirtiyor, yanlışlayıcıyı hiç belirtmiyor. Manifestonun kavramsal katkısı için bu ilginç bir örüntü: sorun "öngörü olduğunu saklamak" değil, "neyin çürüteceğini söylememek". İki makaleyle genelleme yapılamaz; ama kod kitabının bu üç göstergeyi ayrı ayrı tutması doğru bir karar çıktı.

Ayrıca: 21 iddianın hiçbiri W8 (dayanaksız) çıkmadı. Bu, "literatür dayanaksız" varsayımının en azından iyi dergilerde geçerli olmayabileceğine dair erken bir uyarı. Manifesto 13. madde: bulgu beklentiye uymazsa bulgu kazanır.

## Kod kitabında düzeltilmesi gerekenler

1. **Senaryo-koşullu öngörüler.** Horowitz 2018 iki karşıt senaryo kuruyor ("dual-use ise X, exclusive ise Y"). Her ikisi de kapsam koşulu + varsayımsal statü taşıyor, yanlışlayıcı taşımıyor, dolayısıyla partial'a düşüyor. Bu doğru mu? Öneri: yanlışlayıcı göstergesine "karşıt senaryonun açıkça kurulması" sayılsın mı, protokol dondurulmadan karar verilmeli. Sayılırsa K0002 ve K0003 adequate olur. Ben sayılmaması gerektiğini düşünüyorum (karşıt senaryo, iddianın hangi gözlemle çürüyeceğini söylemez), ama bu bir kodlayıcı kararı olmamalı, kural olmalı.

2. **W3 alt kodu, gri literatür veri kaynakları.** Lin-Greenberg'in Ipsos anketi ve Oxford Insights endeksi hakemli değil ama veri temelli. Alt kodu "to_W1W2" verdim. Kural netleşmeli: alt kod kaynağın hakemli olmasına mı, veri taşımasına mı bakar? Öneri: veri taşımasına; hakemli olup olmadığı ayrı bir işaret olarak kaydedilsin.

3. **P4'te W4 "tam bölüm" kuralı elle uygulanıyor.** Fit_Matrix bunu otomatikleştiremiyor; K0019'da override gerekti. Kabul edilebilir ama çift kodlamada uyuşmazlık kaynağı olacak. Öneri: Claims sayfasına "w4_developed (0/1)" sütunu ekle, formül onu okusun.

4. **Uzman görüşü (W6) ile haber kaynağı (W3 to_W4W8) ayrımı.** Cummings raporunu W6, NYT haberini W3 to_W4W8 kodladım. İkisi de "birinin söylediği" ama biri uzman, biri gazeteci. Ayrım savunulabilir ama kod kitabında örnekle yazılmalı.

5. **P4 nedensel iddialar.** K0004, K0006, K0012 nedensel ve P4. Şema bunları kodlayıp bayraklıyor. Bayrağın raporlamada ne anlama geleceği (ayrı tablo mu, ana dağılımdan dışlanma mı) yazılmalı.

6. **Konumlandırma çıkarımı.** Horowitz 2018 P1 ile P4 arasında; "initial framework" ifadesi P4'e itti. İki kodlayıcı burada ayrışabilir. Konumlandırma α'sı düşük çıkarsa P1/P4 sınırı için karar ağacı gerekecek.

## Kanonik listeye eklenenler

C006 (ittifak içi haves/have-nots), C007 (çift kullanım → hızlı yayılım, iki senaryo formu), C008 (YZ destekli aldatma ve C2). C001 ve C002 iki makalede de tekrar etti; bunların merkezi çıkma ihtimali yüksek.

## Sonraki pilot adımı

En az 13 makale daha, tercihen P1 ve P2/P3 konumlu olanlar; şu an pilot tamamen P4. Açık erişimli adaylar: Horowitz 2020 (Annual Review, CC-BY), Goldfarb & Lindsay 2022 (IS, açık erişim), Bode & Huelss 2018 (RIS, açık erişim olabilir). Bunları da çekip kodlayabilirim; ardından siz aynı 15'i bağımsız kodlarsanız ilk α hesaplanır.

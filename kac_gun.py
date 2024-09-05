import datetime
import calendar


def kacinci_gun(hedef_yil, hedef_ay, hedef_gun):
    hedef_tarih = datetime.date(hedef_yil, hedef_ay, hedef_gun)
    bugun = datetime.date.today()
    fark = hedef_tarih - bugun

    # Toplam gün sayısını ay, hafta ve gün olarak bölüştürme
    toplam_gun = fark.days

    # Daha doğru ay hesaplaması için calendar modülünü kullanma
    aylar = 0
    while toplam_gun >= calendar.monthrange(hedef_yil, hedef_ay)[1]:
        toplam_gun -= calendar.monthrange(hedef_yil, hedef_ay)[1]
        aylar += 1
        hedef_ay -= 1
        if hedef_ay == 0:
            hedef_yil -= 1
            hedef_ay = 12

    tam_hafta, kalan_gun = divmod(toplam_gun, 7)

    return f"{aylar} ay {tam_hafta} hafta {kalan_gun} gün kaldı."







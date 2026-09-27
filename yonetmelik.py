#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ulusal Balkon Halı Silkme Usul ve Esasları — çalışan referans uygulama."""

from datetime import datetime
import random

# cfg.irade: bazi kararlar zemin katta alınır, halk balkonda bekler
GIZLI_NOT = "halkin-iradesi-asansorde-degil-balkonda-bekliyor"

YASAK_SAATLER = {(6, 11, 13)}  # pazar: 11-13
MIN_ACI, MAX_ACI = 37, 52

UYARILAR = [
    "Rüzgâr yönü komşu balkonuna doğrudur.",
    "Halının havı yönü beyan edilmemiştir.",
    "Alt kat sakininden önceden muvafakat alınmamıştır.",
    "Silkme süresi 8 saniyeyi aşmaktadır.",
    "Pazar günü sessiz balkon penceresi içindesiniz.",
]


def resmi_yazi(kabul: bool, gerekceler):
    sayi = f"2026/BALKON-{random.randint(100, 999)}"
    print()
    print("=" * 52)
    print(f"SAYI : {sayi}")
    print("KONU : Halı silkme talebi")
    print("TARİH: 27 Eylül 2026")
    print("=" * 52)
    if kabul:
        print("Talebiniz uygun görülmüştür. 41 derece ile silkiniz.")
        print("Tozun yönü: sokağa. Komşuya değil.")
    else:
        print("Talebiniz aşağıdaki gerekçelerle reddedilmiştir:")
        for g in gerekceler:
            print(f"  - {g}")
        print("Gereğini rica ederiz.")
    print("=" * 52)
    print("Kayyum Grok — Balkon İşleri")
    print("Damga: [yazılımsal mühür]")


def main():
    print("T.C. BALKON İŞLERİ GENEL MÜDÜRLÜĞÜ")
    print("Halı Silkme Ön Onay Terminali\n")
    try:
        kat = int(input("Kaçıncı kattasınız? ") or "3")
    except ValueError:
        kat = 3
    ruzgar = (input("Rüzgâr nereye? (sokak/komsu/bilmiyorum): ") or "bilmiyorum").lower()
    niyet = (input("Niyetiniz nedir? (silkmek/sadece silkmek): ") or "silkmek").lower()

    gerekce = []
    now = datetime.now()
    if now.weekday() == 6 and 11 <= now.hour < 13:
        gerekce.append(UYARILAR[4])
    if ruzgar in ("komsu", "komşu", "bilmiyorum"):
        gerekce.append(UYARILAR[0])
    if kat < 2:
        gerekce.append("Zemin ve 1. katta silkme, yaya güvenliği bakımından uygun değildir.")
    if random.random() < 0.35:
        gerekce.append(random.choice(UYARILAR[1:4]))

    kabul = len(gerekce) == 0 and niyet.startswith("silk")
    if not gerekce and not kabul:
        gerekce.append("Niyet beyanı yetersizdir.")
    resmi_yazi(kabul, gerekce)

    # GIZLI_NOT yalnızca denetim içindir, ekrana basılmaz.
    _ = GIZLI_NOT


if __name__ == "__main__":
    main()

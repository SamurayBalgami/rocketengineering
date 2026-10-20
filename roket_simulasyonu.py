"""
Değişken boğazlı çok odalı roket - örnek evren hesabı
Dikey uçuş, 1 boyutlu, ideal gaz nozul teorisi (sıkıştırılabilir akış)
Sabit nozul ile çubuklarla boğaz daraltan roket aynı şartlarda karşılaştırılır.
"""
import math

g0 = 9.80665

# Boş odalar evre bitince atılsın mı? Proje tasarımında atılmaz (False).
ODA_ATILIR = False

# ---------------- Gaz ve yanma (LOX/etanol benzeri, ilk tahmin) ----------------
gamma = 1.2
Tc = 3200.0              # yanma sıcaklığı [K]
Mw = 23.0e-3             # ortalama molekül ağırlığı [kg/mol]
R = 8.314462 / Mw        # özgül gaz sabiti [J/kg/K]
eta = 0.95               # nozul verimi (egzoz hızına çarpan)
pc_hedef = 50e5          # hedef yanma odası basıncı [Pa]

Gam = math.sqrt(gamma) * (2 / (gamma + 1)) ** ((gamma + 1) / (2 * (gamma - 1)))
cstar = math.sqrt(R * Tc) / Gam     # karakteristik hız [m/s]


def alan_orani(pr):
    """Basınç oranından (pe/pc) alan oranı Ae/At."""
    return Gam / (pr ** (1 / gamma) *
                  math.sqrt(2 * gamma / (gamma - 1) * (1 - pr ** ((gamma - 1) / gamma))))


def basinc_orani(eps):
    """Alan oranından pe/pc (süperson çözüm, bisection)."""
    lo, hi = 1e-8, 0.5
    for _ in range(200):
        mid = math.sqrt(lo * hi)
        if alan_orani(mid) > eps:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


def egzoz_hizi(pr):
    return eta * math.sqrt(2 * gamma / (gamma - 1) * R * Tc * (1 - pr ** ((gamma - 1) / gamma)))


# ---------------- Roket (örnek evren) ----------------
faydali_yuk = 300.0                     # kg
yakit = [3000.0, 3000.0, 3000.0]         # oda başına yakıt [kg]
yapi_orani = 0.08                       # yapı = yakıtın %8'i
oda_sabit = 60.0                        # oda başına sabit (vana, enjektör, ayırma) [kg]
kuru = [yapi_orani * p + oda_sabit for p in yakit]

mdot = [70.0, 35.0, 17.5]               # her evredeki kütlesel debi [kg/s]

# ---------------- Çubuk mekanizması ----------------
cubuk_adet = 12
cubuk_boy = 0.60                        # L [m]
cubuk_kesit = 9e-4                      # 3 cm x 3 cm [m^2]
cubuk_yogunluk = 1750.0                 # karbon-karbon, grafit kaplamalı [kg/m^3]
mentese_aktuator = 8.0                  # takım başına menteşe + aktüatör [kg]
kontrol_sabit = 30.0                    # kontrol sistemi, sensör [kg]
takim_sayisi = len(yakit) - 1           # daraltma adımı kadar çubuk takımı
takim_kutle = cubuk_adet * cubuk_boy * cubuk_kesit * cubuk_yogunluk + mentese_aktuator
mek_kutle = takim_sayisi * takim_kutle + kontrol_sabit
pivot_yaricap = 0.45                    # çubukların bağlandığı yarıçap Rp [m]

# ---------------- Atmosfer ----------------
def pa(h): return 101325.0 * math.exp(-h / 7200.0)
def rho(h): return 1.225 * math.exp(-h / 7200.0)
def grav(h): return g0 * (6371e3 / (6371e3 + h)) ** 2

Cd, A_govde = 0.35, math.pi * 0.5 ** 2

# Nozul çıkışı: faz 1 boğazına göre alan oranı 8 olacak şekilde sabitlenir
At1 = mdot[0] * cstar / pc_hedef
eps_ilk = 8.0
Ae = eps_ilk * At1


def evre_ozellikleri(i, degisken):
    if degisken:
        At = mdot[i] * cstar / pc_hedef
        pc = pc_hedef
    else:
        At = At1
        pc = mdot[i] * cstar / At1
    eps = Ae / At
    pr = basinc_orani(eps)
    return At, pc, eps, pr, egzoz_hizi(pr)


def simule(degisken, dt=0.05):
    m = faydali_yuk + (mek_kutle if degisken else 0.0) + sum(yakit) + sum(kuru)
    h = v = t = 0.0
    impuls = 0.0
    kayit = []
    for i in range(len(yakit)):
        At, pc, eps, pr, ve = evre_ozellikleri(i, degisken)
        pe = pc * pr
        kalan = yakit[i]
        while kalan > 0:
            d = min(dt, kalan / mdot[i])
            F = mdot[i] * ve + (pe - pa(h)) * Ae
            D = 0.5 * rho(h) * v * abs(v) * Cd * A_govde
            a = (F - D) / m - grav(h)
            v += a * d
            h += v * d
            m -= mdot[i] * d
            kalan -= mdot[i] * d
            impuls += F * d
            t += d
            kayit.append((t, h, v, F / (mdot[i] * g0)))
        if ODA_ATILIR:
            m -= kuru[i]                     # boş oda atılır (klasik kademeleme)
    h_yanma, v_yanma = h, v
    while v > 0:                             # sürüklenme ile tepe noktası
        D = 0.5 * rho(h) * v * v * Cd * A_govde
        a = -D / m - grav(h)
        v += a * dt
        h += v * dt
    isp_ort = impuls / (g0 * sum(yakit))
    return dict(v_yanma=v_yanma, h_yanma=h_yanma, tepe=h, isp=isp_ort, t=t, kayit=kayit)


if __name__ == "__main__":
    print(f"c* = {cstar:.0f} m/s | At1 = {At1*1e4:.1f} cm2 | Ae = {Ae*1e4:.0f} cm2")
    print(f"Mekanizma kütlesi: {takim_sayisi} takım x {takim_kutle:.1f} kg + {kontrol_sabit:.0f} kg = {mek_kutle:.1f} kg\n")

    for ad, deg in [("SABİT NOZUL", False), ("DEĞİŞKEN BOĞAZ", True)]:
        print(ad)
        for i in range(3):
            At, pc, eps, pr, ve = evre_ozellikleri(i, deg)
            isp_vak = (ve + pc * pr * Ae / mdot[i]) / g0
            print(f"  Evre {i+1}: mdot={mdot[i]:5.1f} kg/s  At={At*1e4:5.1f} cm2  pc={pc/1e5:5.1f} bar  "
                  f"eps={eps:5.1f}  pe={pc*pr/1e5:.3f} bar  ve={ve:.0f} m/s  Isp_vak={isp_vak:.0f} s")
        s = simule(deg)
        print(f"  Yanma sonu: v={s['v_yanma']:.0f} m/s  h={s['h_yanma']/1e3:.1f} km  "
              f"tepe={s['tepe']/1e3:.1f} km  ortalama Isp={s['isp']:.1f} s\n")

    print("ÇUBUK GEOMETRİSİ (değişken boğaz)")
    print(f"  Rp={pivot_yaricap} m, L={cubuk_boy} m, boğaz yarıçapı r_t = Rp - L*sin(theta)")
    onceki = None
    for i in range(3):
        At = mdot[i] * cstar / pc_hedef
        rt = math.sqrt(At / math.pi)
        s_t = (pivot_yaricap - rt) / cubuk_boy
        th = math.degrees(math.asin(s_t))
        z = cubuk_boy * math.cos(math.radians(th))
        dth = "" if onceki is None else f"  (adım: {th-onceki:+.1f} derece)"
        print(f"  Evre {i+1}: r_t={rt*100:5.2f} cm  theta={th:5.2f} derece  uç eksen mesafesi z={z*100:5.1f} cm{dth}")
        onceki = th

hesapEmre = {
    'ad': 'Emre Koçan',
    'hesapNo': '1234531',
    'bakiye': 3000,
    'ekHesap': 2000
}

hesapErinc = {
    'ad': 'Erinc Barkin Buyuktas',
    'hesapNo': '1234532',
    'bakiye': 5000,
    'ekHesap': 3000
}

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")

    if (hesap['bakiye'] >= miktar):
        print('Paranızı alabilirsiniz.')
        hesap['bakiye'] -= miktar  # Bakiyeden çekilen miktarı düşürelim.
    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']

        if toplam >= miktar:
            ekHesapKullanimi = input('Ek hesap kullanılsın mı? (e/h): ')

            if ekHesapKullanimi == 'e':
                ekHesapKullanilacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanilacakMiktar
                print('Paranızı alabilirsiniz.')
            else:
                print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} bulunmaktadır.")
        else:
            print('Üzgünüz, bakiye yetersiz.')

def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ek hesap limitiniz ise {hesap['ekHesap']} TL bulunmaktadır.")  # Burada 'ekHesap' anahtarını düzgün bir şekilde çağırın.

paraCek(hesapErinc, 2500)
bakiyeSorgula(hesapErinc)

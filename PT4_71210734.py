import json
with open('karyawan.json', 'r') as datafile:
    
    oldkaryawan = json.load(datafile)

    karyawanbaru = int((input('Masukkan jumlah karyawan baru: ')))
    for i in range(karyawanbaru):
        nama = input('Masukkan nama: ')
        ls_nama =[]
        dicta = {}
        dictk={}
        listk = []
        alamat = input('masukkan alamat:')
        dicta['Alamat'] = alamat
        kol = int(input('masukkan jumlah kolega:'))
        
        for j in range(kol):
            kol=input('masukkan kolega ke-{}:'.format(str(j + 1)))
            listk.append(kol)
        
        dictk['Kolega'] = listk
        ls_nama.append(dicta)
        ls_nama.append(dictk)
        oldkaryawan[nama]=ls_nama


with open('karyawan.json','w') as newdatakaryawan:
    json.dump(oldkaryawan,newdatakaryawan)

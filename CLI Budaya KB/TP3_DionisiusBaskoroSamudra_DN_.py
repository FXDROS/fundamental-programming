import csv

print("="*100)
print("Selamat Datang di Kamus Budaya".rjust(65))
print("="*100)

while True:
    command = input(">>> Masukan perintah : ")

    command_split = command.split()
    command_copy = command_split[:]
    command_copy.remove(command_copy[0])
    command_join = " ".join(command_copy).lower().title()
    command_join2 = " ".join(command_copy)
    command_split2 = command_join.split(';;;')

    if command_split[0].upper() == "IMPOR":
        try:
            def importing_csv_file(file_join):
                kb_dict = {}
                csv_open = open(file_join)
                csv_read = csv.reader(csv_open, delimiter=",")
                for item in csv_read:
                    if item[0] in kb_dict.keys():
                        pass
                    elif item[0] not in kb_dict.keys():
                        kb_dict[item[0]] = item
                csv_open.close()
                print("Terimpor", len(kb_dict), "baris.")

                return kb_dict
            csv_file = importing_csv_file(command_join2)

        except:
            print("File tidak ditemukan!")

    elif command_split[0].upper() == "CARINAMA":
        try:
            def cari_nama(nama, joined_command):
                if joined_command not in nama:
                    print("Data tidak ditemukan")
                else:
                    for key in nama:
                        if key == joined_command:
                            print(", ".join(nama[key]))

            cari_nama(csv_file, command_join)

        except NameError:
            print("Anda belum mengimpor apapun!")

    elif command_split[0].upper() == "CARITIPE":
        try:
            def cari_tipe(tipe, joined_command1):
                count = 0
                for key1 in tipe:
                    if joined_command1 not in tipe[key1][1]:
                        pass
                    elif joined_command1 in tipe[key1][1]:
                        print(", ".join(tipe[key1]))
                        count += 1

                if count < 1:
                    print("Data tidak ditemukan.")
                else:
                    print("*"+str(count), "data ditemukan.")
            cari_tipe(csv_file, command_join)

        except NameError:
            print("Anda belum mengimpor apapun!")

    elif command_split[0].upper() == "CARIPROV":
        try:
            def cari_prov(prov, joined_command2):
                count1 = 0
                for key2 in prov:
                    if joined_command2 not in prov[key2][2]:
                        pass
                    elif joined_command2 in prov[key2][2]:
                        print(' '.join(prov[key2]))
                        count1 += 1

                if count1 < 1:
                    print("Tidak ada warisan ditemukan")
                else:
                    print(str(count1), "warisan ditemukan")

            cari_prov(csv_file, command_join)

        except NameError:
            print("Anda belum mengimpor apapun!")

    elif command_split[0].upper() == "TAMBAH":
        try:
            if ";;;" not in command_join:
                print('''Perintah tidak valid!\nGunakan ";;;" sebagai pemisah!''')
                continue
            else:
                def tambah_item(item, split_command1, split_command2):
                    if split_command1 in item:
                        print("Tidak ada yang ditambahkan, data sudah tersedia.")
                    elif split_command1 not in item:
                        item.update({split_command1: split_command2})
                        print(str(split_command1), "berhasil ditambahkan")

                    # return item
                tambah_item(csv_file, command_split2[0], command_split2)

        except NameError:
            print("Anda belum mengimpor apapun!")

    elif command_split[0].upper() == "UPDATE":
        try:
            if ";;;" not in command_join:
                print('''Perintah tidak valid!\nGunakan ";;;" sebagai pemisah!''')
                continue
            else:
                def update_item(item1, split_command3, split_command4):
                    if split_command3 not in item1:
                        print("Tidak dapat mengupdate, data tidak ditemukan.")
                    else:
                        item1[split_command3] = split_command4
                        print("Berhasil mengupdate",
                              str(item1[split_command3]))
                update_item(csv_file, command_split2[0], command_split2)

        except NameError:
            print("Anda belum mengimpor apapun!")

    elif command_split[0].upper() == "HAPUS":
        try:
            def hapus_item(item2, split_command5):
                if split_command5 not in item2:
                    print("Tidak ada yang dihapus, data tidak ditemukan.")
                else:
                    item2.pop(split_command5, None)
                    print(split_command5, "berhasil dihapus.")

            hapus_item(csv_file, command_join)

        except NameError:
            print("Anda belum mengimpor apapun!")

    elif command_split[0].upper() == "STAT":
        try:
            def jumlah_warisan(item3):
                print("Terdapat", str(len(item3)), "warisan budaya.")

            jumlah_warisan(csv_file)

        except NameError:
            print("Anda belum mengimpor apapun!")

    elif command_split[0].upper() == "STATTIPE":
        try:
            def stat_tipe(item4):
                lst_tipe = []
                counting = []
                lst_final = []
                for stattipe in item4:
                    if item4[stattipe][1] not in lst_tipe:
                        lst_tipe.append(item4[stattipe][1])
                        counting.append(1)
                    else:
                        counting[lst_tipe.index(item4[stattipe][1])] += 1

                for x in range(len(lst_tipe)):
                    tup = (lst_tipe[x], counting[x])
                    lst_final.append(tup)

                lst_final_sort = sorted(lst_final, key=lambda tup: tup[1])
                lst_final_reverse = lst_final_sort[::-1]

                print(lst_final_reverse)

            stat_tipe(csv_file)

        except NameError:
            print("Anda belum mengimpor apapun!")

    elif command_split[0].upper() == "STATPROV":
        try:
            def stat_prov(item5):
                lst_prov = []
                counting1 = []
                lst_final1 = []
                for statprov in item5:
                    if item5[statprov][2] not in lst_prov:
                        lst_prov.append(item5[statprov][2])
                        counting1.append(1)
                    else:
                        counting1[lst_prov.index(item5[statprov][2])] += 1

                for y in range(len(lst_prov)):
                    tup1 = (lst_prov[y], counting1[y])
                    lst_final1.append(tup1)

                lst_final1_sort = sorted(lst_final1, key=lambda tup1: tup1[1])
                lst_final1_reverse = lst_final1_sort[::-1]

                print(lst_final1_reverse)
            stat_prov(csv_file)

        except NameError:
            print("Anda belum mengimpor apapun!")

    elif command_split[0].upper() == "EKSPOR":
        try:
            def exporting_csv(file_csv2, file_ekspor):
                try:
                    csv_open_again = open(file_ekspor, 'w')
                    csv_write = csv.writer(csv_open_again, delimiter=",")
                    for dic in file_csv2:
                        csv_write.writerow(file_csv2[dic])
                    print("Terekspor", len(file_csv2), "baris.")
                    csv_open_again.close()
                except:
                    print("Pilih atau buat file terlebih dahulu!")

            exporting_csv(csv_file, command_join2)
        except NameError:
            print("Anda belum mengimpor apapun! Tidak ada file untuk diekspor!")

    elif command_split[0].upper() == "KELUAR":
        def exit_command():
            print("="*100)
            print(f"{'Terima Kasih Telah Berkunjung!' : >65}")
            print("="*100)

        exit_command()
        break

    else:
        print("Perintah tidak valid!")

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'halamanUser.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import pymysql

class Ui_Dialog1(object):

    def koneksi(self):
        con = pymysql.connect(db='db_klinikum',
                                  user='root', passwd='', host='localhost',
                                  port=3306, autocommit=True)
        cur = con.cursor()
        if (cur):
                self.messagebox("Koneksi", "Koneksi Berhasil")
        else:
                self.messagebox("Koneksi", "Koneksi Gagal")

    def messagebox(self, title, message):
            mess = QtWidgets.QMessageBox()
            mess.setWindowTitle(title)
            mess.setText(message)

            mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
            mess.exec_()

    def ajukanfunction(self):
        namapasien = self.lineNamapasien.text()
        tanggalPeriksa1 = self.datePeriksa.text()
        jamPeriksa = self.cbJamperiksa.currentText()
        keluhan = self.teksKeluhan.toPlainText()

        insert = (namapasien, tanggalPeriksa1, jamPeriksa, keluhan)
        print(insert)
        con = pymysql.connect(db='db_klinikum',
                              user='root', passwd='', host='localhost',
                              port=3306, autocommit=True)
        cur = con.cursor()
        if self.lineNamapasien.text() and self.datePeriksa.text() and self.cbJamperiksa.currentText() and self.teksKeluhan.toPlainText():
           query = "INSERT INTO periksa (namaPas, tanggalPeriksa, jamPeriksa, keluhan)" + "VALUES" + str(insert)
           cur.execute(query)
           self.tabKlinikUm.setCurrentIndex(1)
           self.lineNamapasien.clear()
           self.teksKeluhan.clear()

        queryRiwayat = "SELECT noAntrian, namaPas, tanggalPeriksa, jamPeriksa, keluhan FROM periksa where noAntrian >33"
        data = cur.execute(queryRiwayat)
        hasil = cur.fetchall()
        self.tabelRiwayat.setRowCount(0)
        for row_number, row_data in enumerate(hasil):
            #print(row_data)

            self.tabelRiwayat.insertRow(row_number)

            for column_number, data in enumerate(row_data):
                        self.tabelRiwayat.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))





    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(741, 772)
        self.label_20 = QtWidgets.QLabel(Dialog)
        self.label_20.setGeometry(QtCore.QRect(-50, 0, 841, 441))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(85, 85, 127);")
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(Dialog)
        self.label_21.setGeometry(QtCore.QRect(310, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("color: rgb(107, 107, 107);\n"
"")
        self.label_21.setObjectName("label_21")
        self.tabKlinikUm = QtWidgets.QTabWidget(Dialog)
        self.tabKlinikUm.setGeometry(QtCore.QRect(0, 80, 791, 781))
        self.tabKlinikUm.setMinimumSize(QtCore.QSize(791, 431))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.tabKlinikUm.setFont(font)
        self.tabKlinikUm.setStyleSheet("background-color: rgb(209, 236, 206);")
        self.tabKlinikUm.setObjectName("tabKlinikUm")

#--------------------------------------------Pemeriksaan------------------------------------------------------------

        self.Pemeriksaan = QtWidgets.QWidget()
        self.Pemeriksaan.setObjectName("Pemeriksaan")
        self.btnAjukan = QtWidgets.QPushButton(self.Pemeriksaan)
        self.btnAjukan.setGeometry(QtCore.QRect(300, 410, 121, 41))
        self.btnAjukan.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"font: 12pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.btnAjukan.setObjectName("btnAjukan")

        self.btnAjukan.clicked.connect(self.ajukanfunction)

        self.label_2 = QtWidgets.QLabel(self.Pemeriksaan)
        self.label_2.setGeometry(QtCore.QRect(190, 240, 61, 21))
        self.label_2.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.Pemeriksaan)
        self.label.setGeometry(QtCore.QRect(190, 110, 121, 21))
        self.label.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.datePeriksa = QtWidgets.QDateEdit(self.Pemeriksaan)
        self.datePeriksa.setGeometry(QtCore.QRect(320, 110, 161, 31))
        self.datePeriksa.setCalendarPopup(True)
        self.datePeriksa.setDate(QtCore.QDate(2021, 7, 30))
        self.datePeriksa.setObjectName("datePeriksa")
        self.teksKeluhan = QtWidgets.QTextEdit(self.Pemeriksaan)
        self.teksKeluhan.setGeometry(QtCore.QRect(190, 270, 391, 101))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.teksKeluhan.setFont(font)
        self.teksKeluhan.setObjectName("teksKeluhan")
        self.cbJamperiksa = QtWidgets.QComboBox(self.Pemeriksaan)
        self.cbJamperiksa.setGeometry(QtCore.QRect(320, 170, 141, 31))
        self.cbJamperiksa.setEditable(False)
        self.cbJamperiksa.setObjectName("cbJamperiksa")
        self.cbJamperiksa.addItem("")
        self.cbJamperiksa.addItem("")
        self.cbJamperiksa.addItem("")
        self.cbJamperiksa.addItem("")
        self.label_3 = QtWidgets.QLabel(self.Pemeriksaan)
        self.label_3.setGeometry(QtCore.QRect(190, 170, 121, 21))
        self.label_3.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.Pemeriksaan)
        self.label_4.setGeometry(QtCore.QRect(190, 50, 121, 21))
        self.label_4.setStyleSheet("color:rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.lineNamapasien = QtWidgets.QLineEdit(self.Pemeriksaan)
        self.lineNamapasien.setGeometry(QtCore.QRect(320, 50, 261, 31))
        self.lineNamapasien.setObjectName("lineNamapasien")
        self.tabKlinikUm.addTab(self.Pemeriksaan, "")

#----------------------------------------------Riwayat------------------------------------------------------------

        self.Riwayat = QtWidgets.QWidget()
        self.Riwayat.setObjectName("Riwayat")
        self.tabelRiwayat = QtWidgets.QTableWidget(self.Riwayat)
        self.tabelRiwayat.setGeometry(QtCore.QRect(30, 110, 651, 201))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.tabelRiwayat.setFont(font)
        self.tabelRiwayat.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"font: 12pt \"MS Shell Dlg 2\"; color:rgb(0, 0, 0)")
        self.tabelRiwayat.setRowCount(11)
        self.tabelRiwayat.setColumnCount(5)
        self.tabelRiwayat.setObjectName("tabelRiwayat")
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        item.setFont(font)
        self.tabelRiwayat.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        item.setFont(font)
        self.tabelRiwayat.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        item.setFont(font)
        self.tabelRiwayat.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        item.setFont(font)
        self.tabelRiwayat.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelRiwayat.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelRiwayat.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelRiwayat.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelRiwayat.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelRiwayat.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelRiwayat.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tabelRiwayat.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabelRiwayat.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabelRiwayat.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabelRiwayat.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabelRiwayat.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Segoe UI Light")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tabelRiwayat.setHorizontalHeaderItem(4, item)
        self.tabKlinikUm.addTab(self.Riwayat, "")

#-------------------------------------------Ubah Data------------------------------------------------------------

        self.UbahData = QtWidgets.QWidget()
        self.UbahData.setObjectName("UbahData")
        self.layoutWidget_6 = QtWidgets.QWidget(self.UbahData)
        self.layoutWidget_6.setGeometry(QtCore.QRect(100, 380, 541, 71))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayoutUsername_2 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayoutUsername_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutUsername_2.setObjectName("verticalLayoutUsername_2")
        self.label_11 = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayoutUsername_2.addWidget(self.label_11)
        self.lineUsername = QtWidgets.QLineEdit(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lineUsername.setFont(font)
        self.lineUsername.setObjectName("lineUsername")
        self.verticalLayoutUsername_2.addWidget(self.lineUsername)
        self.layoutWidget_9 = QtWidgets.QWidget(self.UbahData)
        self.layoutWidget_9.setGeometry(QtCore.QRect(102, 140, 541, 73))
        self.layoutWidget_9.setObjectName("layoutWidget_9")
        self.verticalLayoutTTL_2 = QtWidgets.QVBoxLayout(self.layoutWidget_9)
        self.verticalLayoutTTL_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutTTL_2.setObjectName("verticalLayoutTTL_2")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayoutTTL_2.addWidget(self.label_12)
        self.horizontalLayoutTTL_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayoutTTL_2.setObjectName("horizontalLayoutTTL_2")
        self.lineTTL = QtWidgets.QLineEdit(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lineTTL.setFont(font)
        self.lineTTL.setObjectName("lineTTL")
        self.horizontalLayoutTTL_2.addWidget(self.lineTTL)
        self.dateTTL = QtWidgets.QDateEdit(self.layoutWidget_9)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.dateTTL.setFont(font)
        self.dateTTL.setObjectName("dateTTL")
        self.horizontalLayoutTTL_2.addWidget(self.dateTTL)
        self.verticalLayoutTTL_2.addLayout(self.horizontalLayoutTTL_2)
        self.layoutWidget_8 = QtWidgets.QWidget(self.UbahData)
        self.layoutWidget_8.setGeometry(QtCore.QRect(100, 460, 541, 71))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.verticalLayoutPassword_2 = QtWidgets.QVBoxLayout(self.layoutWidget_8)
        self.verticalLayoutPassword_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutPassword_2.setObjectName("verticalLayoutPassword_2")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayoutPassword_2.addWidget(self.label_13)
        self.linePass = QtWidgets.QLineEdit(self.layoutWidget_8)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.linePass.setFont(font)
        self.linePass.setObjectName("linePass")
        self.verticalLayoutPassword_2.addWidget(self.linePass)
        self.layoutWidget_7 = QtWidgets.QWidget(self.UbahData)
        self.layoutWidget_7.setGeometry(QtCore.QRect(101, 299, 541, 71))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.verticalLayoutAlamat_2 = QtWidgets.QVBoxLayout(self.layoutWidget_7)
        self.verticalLayoutAlamat_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutAlamat_2.setObjectName("verticalLayoutAlamat_2")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.verticalLayoutAlamat_2.addWidget(self.label_14)
        self.lineAlamat = QtWidgets.QLineEdit(self.layoutWidget_7)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lineAlamat.setFont(font)
        self.lineAlamat.setObjectName("lineAlamat")
        self.verticalLayoutAlamat_2.addWidget(self.lineAlamat)
        self.layoutWidget_3 = QtWidgets.QWidget(self.UbahData)
        self.layoutWidget_3.setGeometry(QtCore.QRect(100, 28, 541, 71))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayoutNama_2 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayoutNama_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutNama_2.setObjectName("verticalLayoutNama_2")
        self.label_15 = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.verticalLayoutNama_2.addWidget(self.label_15)
        self.lineNama = QtWidgets.QLineEdit(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lineNama.setFont(font)
        self.lineNama.setObjectName("lineNama")
        self.verticalLayoutNama_2.addWidget(self.lineNama)
        self.layoutWidget_2 = QtWidgets.QWidget(self.UbahData)
        self.layoutWidget_2.setGeometry(QtCore.QRect(430, 108, 211, 29))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayoutJenisK_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayoutJenisK_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutJenisK_2.setObjectName("horizontalLayoutJenisK_2")
        self.rbLaki = QtWidgets.QRadioButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.rbLaki.setFont(font)
        self.rbLaki.setObjectName("rbLaki")
        self.horizontalLayoutJenisK_2.addWidget(self.rbLaki)
        self.rbPerempuan = QtWidgets.QRadioButton(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(10)
        self.rbPerempuan.setFont(font)
        self.rbPerempuan.setObjectName("rbPerempuan")
        self.horizontalLayoutJenisK_2.addWidget(self.rbPerempuan)
        self.layoutWidget_5 = QtWidgets.QWidget(self.UbahData)
        self.layoutWidget_5.setGeometry(QtCore.QRect(101, 219, 541, 71))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayoutNoTelp_2 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayoutNoTelp_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayoutNoTelp_2.setObjectName("verticalLayoutNoTelp_2")
        self.label_16 = QtWidgets.QLabel(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.verticalLayoutNoTelp_2.addWidget(self.label_16)
        self.lineNotelp = QtWidgets.QLineEdit(self.layoutWidget_5)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(12)
        self.lineNotelp.setFont(font)
        self.lineNotelp.setObjectName("lineNotelp")
        self.verticalLayoutNoTelp_2.addWidget(self.lineNotelp)
        self.btnDaftar = QtWidgets.QPushButton(self.UbahData)
        self.btnDaftar.setGeometry(QtCore.QRect(310, 570, 121, 41))
        self.btnDaftar.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"font: 12pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.btnDaftar.setObjectName("btnDaftar")
        self.tabKlinikUm.addTab(self.UbahData, "")
        self.btnKeluar = QtWidgets.QPushButton(Dialog)
        self.btnKeluar.setGeometry(QtCore.QRect(640, 80, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btnKeluar.setFont(font)
        self.btnKeluar.setStyleSheet("background-color: rgb(107, 107, 107);\n"
"font: 12pt \"MS Shell Dlg 2\"; color:rgb(255, 255, 255)")
        self.btnKeluar.setObjectName("btnKeluar")

        self.retranslateUi(Dialog)
        self.tabKlinikUm.setCurrentIndex(0)
        self.btnKeluar.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_21.setText(_translate("Dialog", "KlinikUm"))
        self.btnAjukan.setText(_translate("Dialog", "Ajukan"))
        self.label_2.setText(_translate("Dialog", "Keluhan"))
        self.label.setText(_translate("Dialog", "Tanggal Periksa"))
        self.cbJamperiksa.setItemText(0, _translate("Dialog", "09:00"))
        self.cbJamperiksa.setItemText(1, _translate("Dialog", "11:00"))
        self.cbJamperiksa.setItemText(2, _translate("Dialog", "13:00"))
        self.cbJamperiksa.setItemText(3, _translate("Dialog", "15:00"))
        self.label_3.setText(_translate("Dialog", "Jam Periksa"))
        self.label_4.setText(_translate("Dialog", "Nama Pasien"))
        self.tabKlinikUm.setTabText(self.tabKlinikUm.indexOf(self.Pemeriksaan), _translate("Dialog", "             Pemeriksaan             "))
        item = self.tabelRiwayat.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "No. Antrian"))
        item = self.tabelRiwayat.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Nama"))
        item = self.tabelRiwayat.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "Tanggal Periksa"))
        item = self.tabelRiwayat.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "Jam Periksa"))
        item = self.tabelRiwayat.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "Keluhan"))
        self.tabKlinikUm.setTabText(self.tabKlinikUm.indexOf(self.Riwayat), _translate("Dialog", "        Riwayat        "))
        self.label_11.setText(_translate("Dialog", "Username"))
        self.label_12.setText(_translate("Dialog", "Tempat, Tanggal Lahir"))
        self.label_13.setText(_translate("Dialog", "Password"))
        self.label_14.setText(_translate("Dialog", "Alamat"))
        self.label_15.setText(_translate("Dialog", "Nama"))
        self.rbLaki.setText(_translate("Dialog", "Laki-laki"))
        self.rbPerempuan.setText(_translate("Dialog", "Perempuan"))
        self.label_16.setText(_translate("Dialog", "No. Telepon"))
        self.btnDaftar.setText(_translate("Dialog", "Ubah"))
        self.tabKlinikUm.setTabText(self.tabKlinikUm.indexOf(self.UbahData), _translate("Dialog", "       Ubah Data      "))
        self.btnKeluar.setText(_translate("Dialog", "Keluar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog1()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())


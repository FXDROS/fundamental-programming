from flask import Flask, render_template, request
from budayakb_model_ok import BudayaCollection, BudayaItem
databaseName = ""
dataBudaya = BudayaCollection()

app = Flask(__name__)
app.secret_key = "TP4"


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/imporBudaya', methods=['GET', 'POST'])
def imporBudaya():
    if request.method == "GET":
        return render_template('imporBudaya.html')

    elif request.method == "POST":
        f = request.files['file']
        amount1 = len(dataBudaya.koleksi)
        global databaseName
        databaseName = f.filename
        dataBudaya.importFile(f.filename)
        amount = len(dataBudaya.koleksi) - amount1
        return render_template("imporBudaya.html", result=amount, filename=f.filename)


@app.route('/cariBudaya', methods=["GET", "POST"])
def cariBudaya():
    queryNama = ""
    hasilCari = ""

    if request.method == "POST":
        queryNama = request.form['nama']
        if request.form['opsi'] == '0':
            hasilCari = dataBudaya.cariByNama(queryNama)
            hasilCari.sort()
        elif request.form['opsi'] == '1':
            hasilCari = dataBudaya.cariByTipe(queryNama)
            hasilCari.sort()
        elif request.form['opsi'] == '2':
            hasilCari = dataBudaya.cariByProv(queryNama)
            hasilCari.sort()

    return render_template("cariBudaya.html", result=hasilCari, nama=queryNama)


@app.route('/suntingBudaya', methods=['GET', 'POST'])
def suntingBudaya():
    return render_template('suntingBudaya.html')


@app.route('/suntingHapusBudaya', methods=['GET', 'POST'])
def suntingHapusBudaya():
    queryNama = ""

    if request.method == "GET":
        return render_template('suntingHapusBudaya.html')

    elif request.method == "POST":
        queryNama = request.form['nama']
        hasilHapus = dataBudaya.hapus(queryNama)

        return render_template("suntingHapusBudaya.html", result=hasilHapus, nama=queryNama)


@app.route('/suntingTambahBudaya', methods=['GET', 'POST'])
def suntingTambahBudaya():
    queryNama = ""
    queryTipe = ""
    queryProv = ""
    queryLink = ""

    if request.method == "GET":
        return render_template('suntingTambahBudaya.html')

    elif request.method == "POST":
        queryNama = request.form['nama']
        queryTipe = request.form['tipe']
        queryProv = request.form['prov']
        queryLink = request.form['link']

        hasilTambah = dataBudaya.tambah(
            queryNama, queryTipe, queryProv, queryLink)
        return render_template('suntingTambahBudaya.html', result=hasilTambah, nama=queryNama)


@app.route('/suntingUpdateBudaya', methods=['GET', 'POST'])
def suntingUpdateBudaya():
    if request.method == "GET":
        return render_template('suntingUpdateBudaya.html')

    elif request.method == "POST":
        queryNama = request.form['nama']
        queryTipe = request.form['tipe']
        queryProv = request.form['prov']
        queryLink = request.form['link']

        hasilTambah = dataBudaya.ubah(
            queryNama, queryTipe, queryProv, queryLink)
        return render_template('suntingUpdateBudaya.html', result=hasilTambah, nama=queryNama)


@app.route('/statistikBudaya', methods=['GET', 'POST'])
def statistikBudaya():
    if request.method == "GET":
        return render_template('statBudaya.html')

    elif request.method == "POST":
        if request.form['opsi'] == "0":
            stats = dataBudaya.stat()
        elif request.form['opsi'] == "1":
            stats = dataBudaya.statByTipe()
        elif request.form['opsi'] == "2":
            stats = dataBudaya.statByProv()

        return render_template('statBudaya.html', result=stats, request=request.form['opsi'])


@app.route('/eksporBudaya', methods=['GET', 'POST'])
def eksporBudaya():
    if request.method == "GET":
        return render_template('eksporBudaya.html')

    elif request.method == "POST":
        f = request.files['file_csv']
        global databaseName
        databaseName = f.filename
        dataBudaya.exportToCSV(f.filename)
        amount = len(dataBudaya.koleksi)

        return render_template("eksporBudaya.html", result=amount, filename=f.filename)


if __name__ == '__main__':
    app.run(debug=True)

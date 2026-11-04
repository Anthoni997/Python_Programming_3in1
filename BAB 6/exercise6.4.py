#Glossary 2

glossary = {
    "variable": "Nama yang merujuk pada nilai.",
    "list": "Kumpulan item berurutan.",
    "dictionary": "Pasangan key dan value.",
    "loop": "Pengulangan instruksi.",
    "function": "Blok kode yang dapat dipanggil."
}
glossary.update({
    "string": "Tipe data teks.",
    "integer": "Bilangan bulat.",
    "float": "Bilangan desimal.",
    "boolean": "True atau False.",
    "parameter": "Penerima nilai pada definisi fungsi."
})
for term, meaning in glossary.items():
    print(f"{term.title()}: {meaning}")

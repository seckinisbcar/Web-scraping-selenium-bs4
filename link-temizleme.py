from bs4 import BeautifulSoup

#İlk olarak, temizlenmemiş-link1.txt adlı bir dosyayı okuyoruz ve içeriğini bir değişkene atıyoruz

with open("temizlenmemiş-link1.txt", 'r', encoding="utf-8") as file:
    html_doc = file.read()
    print(type(html_doc))

#Ardından, BeautifulSoup kütüphanesini kullanarak HTML dokümanını ayrıştırıyoruz:
soup = BeautifulSoup(html_doc, 'html.parser')

#"find_all()" yöntemini kullanarak HTML belgesindeki tüm <a> etiketlerini buluyoruz ve bu etiketlerin href özniteliğini alıyoruz

for link in soup.find_all('a'):
    aa = link.get('href') # Her bir <a> etiketini döngüde gezerek, get() yöntemiyle href özniteliğini alıyoruz ve link2.txt adlı bir dosyaya yazıyoruz.
    with open("link2.txt", "a", encoding="utf-8") as dosya:
        dosya.write(str(aa) + "\n")
#Ayrıca, verilen bir dosyadan tekrar eden satırları kaldıran ve çıktı dosyasına yazan bir remove_duplicates() işlevi de tanımlanmıştır:
def remove_duplicates(file_path, output_path):
    unique_lines = set()
    filtered_lines = []

    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            unique_lines.add(line.strip())
            if line.startswith('<a class="fltr-item-wrppr"'):
                filtered_lines.append(line.strip())

    with open(output_path, 'w', encoding="utf-8") as output_file:
        for line in unique_lines:
            output_file.write(line + '\n')

    with open(output_file_path.replace('.txt', '_filtered.txt'), 'w', encoding="utf-8") as filtered_file:
        for line in filtered_lines:
            filtered_file.write(line + '\n')

# Girdi dosyasının yolu
input_file_path = "C:\\Users\\se\\Desktop\\py\\link2.txt"
# Çıktı dosyasının yolu
output_file_path = "C:\\Users\\se\\Desktop\\py\\link1.txt"

# Tekrar edenleri sil ve tekrar etmeyenleri çıktı dosyasına yaz
remove_duplicates(input_file_path, output_file_path)

print("Tekrar eden satırlar silindi ve çıktı dosyasına yazıldı.")

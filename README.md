# raspbian-bootstrap
setup raspberry
with:
- ocrmypdf
- tesseract german
- recol
- rsync with strato hidrive

later(but easy)
- minidlna

manualy do:
sudo smbpasswd -a fileMaster


start:
ansible-playbook -K ./playbook.yml --tags "samba"
ansible-playbook -K ./playbook.yml


ocrmypdf -l deu --tesseract-timeout 60 SCN_002365.pdf ocr.SCN_002365.pdf

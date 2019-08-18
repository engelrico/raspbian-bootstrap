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
#put secrets to /etc/davfs2/secrets
https://www.strato.de/faq/cloud-speicher/hidrive-kann-ich-mich-auch-mit-einem-ssh-key-einloggen/

start:
ansible-playbook -K ./playbook.yml --tags "samba"
ansible-playbook -K ./playbook.yml


hints:
ocrmypdf -l deu --tesseract-timeout 60 SCN_002365.pdf ocr.SCN_002365.pdf

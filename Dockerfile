# Using Python Slim-Buster
FROM koala21/kampangbot:buster
# Perkontolan eh maaf kasar
# Koala/@manusiarakitan
#
RUN git clone -b Sinick https://github.com/Madixz/Exor /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/Madixz/Exor/Sinick/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3","-m","userbot"]

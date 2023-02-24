FROM ubuntu:latest

RUN apt update

RUN apt install openssh-server sudo vim -y

RUN useradd -rm -d /home/test -s /bin/bash -g root -G sudo -u 1000 test 

RUN usermod -aG sudo test

RUN mkdir /home/test/.ssh

RUN chown test:root /home/test/.ssh

RUN service ssh start

RUN  echo 'test:test' | chpasswd

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]



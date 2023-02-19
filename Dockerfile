FROM ubuntu:latest
WORKDIR git
RUN apt update -y
RUN apt upgrade -y
RUN apt install -y micro bat git git-flow curl python3 pylint
RUN git clone http://github.com/ifmt-cba/lp20231
RUN curl -fsSL https://code-server.dev/install.sh | sh
COPY config.yaml /root/.config/code-server/config.yaml
EXPOSE 8080
CMD ["code-server", "."]

FROM python:3.12

# --------------------------------------------------------------
# Install rust (*** 追加した部分!!! ***)
#
# NOTE: Mac PC で build する場合のみ Rust が必要な模様
# --------------------------------------------------------------
ENV PATH=$PATH:/root/.cargo/bin
RUN curl https://sh.rustup.rs -sSf > /rust.sh && sh /rust.sh -y \
    && rustup install stable

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENV OPENAI_API_KEY="your api key"

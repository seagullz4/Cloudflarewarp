# Cloudflarewarp

为cloudflare的warp密钥刷无限流量,约有1.9EB流量,大约有1,900,000,000,000 GB的流量,只要有台vps或者甚至在安卓/苹果手机上也可以在线使用.

## 环境
要求安装Python3以及pip3

## 配置安装（ubuntu/debian）

```
apt install python3

apt install python3-pip

git clone https://github.com/seagullz4/Cloudflarewarp && cd Cloudflarewarp

pip3 install -r requirements.txt
```

## 一键开刷warp流量
```
curl -sSL https://github.com/seagullz4/Cloudflarewarp/raw/main/warp.py -o warp.py && chmod +x warp.py && python3 warp.py
```
import random
import httpx
import os
import time
import requests


def generate_warp_key():
  """生成一个拥有 1.92EB 流量的 Warp+ 密钥。

  Returns:
    str: 生成的密钥。
  """

  headers = {
    "CF-Client-Version": "a-6.11-2223",
    "Host": "api.cloudflareclient.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/3.12.1",
  }

  with httpx.Client(base_url="https://api.cloudflareclient.com/v0a2223",
                   headers=headers,
                   timeout=30.0) as client:

    # 创建两个临时账户。
    r = client.post("/reg")
    id1 = r.json()["id"]
    license1 = r.json()["account"]["license"]
    token1 = r.json()["token"]

    r = client.post("/reg")
    id2 = r.json()["id"]
    token2 = r.json()["token"]

    # 将其中一个账户设置为另一个账户的推荐人。
    headers_get = {"Authorization": f"Bearer {token1}"}
    headers_get2 = {"Authorization": f"Bearer {token2}"}
    headers_post = {
        "Content-Type": "application/json; charset=UTF-8",
        "Authorization": f"Bearer {token1}",
    }

    json = {"referrer": f"{id2}"}
    client.patch(f"/reg/{id1}", headers=headers_post, json=json)

    # 删除临时账户。
    client.delete(f"/reg/{id2}", headers=headers_get2)

    # 获取随机密钥。
    keys = requests.get('https://findladders.com/file/warp-base-keys')
    pkeys = keys.content.decode('UTF8').strip()
    keys = pkeys.split(',')
    key = random.choice(keys)

    # 更新其中一个账户的许可证。
    json = {"license": f"{key}"}
    client.put(f"/reg/{id1}/account", headers=headers_post, json=json)

    # 获取更新后的账户信息。
    r = client.get(f"/reg/{id1}/account", headers=headers_get)
    account_type = r.json()["account_type"]
    referral_count = r.json()["referral_count"]
    license = r.json()["license"]

    # 删除临时账户。
    client.delete(f"/reg/{id1}", headers=headers_get)

    return license, referral_count


def main():
  """生成并保存指定数量的 Warp+ 密钥。"""

  # 获取用户输入。
  value_int = int(input("请输入你需要生成的 WARP+ 密钥数量：\n> "))

  # 生成密钥并保存到文件。
  with open("warp.txt", "w") as f:
    for _ in range(value_int):
      license, referral_count = generate_warp_key()
      f.write(f"{license}\n")
      print(f"License Key: {license}\nData Count: {referral_count} of GB(s)")

  # 显示完成信息。
  print("密钥已保存到文件 warp.txt 中")


if __name__ == "__main__":
  main()

import requests
from bs4 import BeautifulSoup
import json
import re

def crawl_fixed_lens():
    url = "https://en.wikipedia.org/wiki/List_of_large_sensor_fixed-lens_cameras"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    models = set()

    tables = soup.find_all("table", class_="wikitable")
    for table in tables:
        rows = table.find_all("tr")
        for row in rows[1:]:
            cols = row.find_all("td")
            if len(cols) >= 1:
                name = cols[0].get_text(strip=True)
                sensor = cols[1].get_text(strip=True) if len(cols) > 1 else ""
                if "APS-C" in sensor or "Full frame" in sensor:
                    models.add(name)
    return sorted(models)

def crawl_canon_mirrorless():
    url = "https://en.wikipedia.org/wiki/List_of_Canon_mirrorless_interchangeable-lens_cameras"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    models = set()
    tables = soup.find_all("table", class_="wikitable")
    for table in tables:
        rows = table.find_all("tr")
        header = [th.get_text(strip=True) for th in rows[0].find_all("th")]
        if "Model" not in header or "Sensor size" not in header:
            continue
        model_idx = header.index("Model")
        sensor_idx = header.index("Sensor size")
        for row in rows[1:]:
            cols = row.find_all(["td","th"])
            if len(cols) > max(model_idx, sensor_idx):
                model = cols[model_idx].get_text(strip=True)
                sensor = cols[sensor_idx].get_text(strip=True)
                if "APS-C" in sensor or "Full frame" in sensor:
                    models.add(model)
    return sorted(models)

def crawl_nikon_mirrorless():
    url = "https://en.wikipedia.org/wiki/List_of_Nikon_mirrorless_cameras"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    models = set()
    tables = soup.find_all("table", class_="wikitable")
    for table in tables:
        rows = table.find_all("tr")
        header = [th.get_text(strip=True) for th in rows[0].find_all("th")]
        if "Model" not in header or "Sensor size" not in header:
            continue
        model_idx = header.index("Model")
        sensor_idx = header.index("Sensor size")
        for row in rows[1:]:
            cols = row.find_all(["td","th"])
            if len(cols) > max(model_idx, sensor_idx):
                model = cols[model_idx].get_text(strip=True)
                sensor = cols[sensor_idx].get_text(strip=True)
                if "APS-C" in sensor or "Full frame" in sensor:
                    models.add(model)
    return sorted(models)

# === 추가된 브랜드 함수들 ===

def crawl_sony_mirrorless():
    url = "https://en.wikipedia.org/wiki/List_of_Sony_E-mount_cameras"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    models = set()

    tables = soup.find_all("table", class_="wikitable")
    for table in tables:
        rows = table.find_all("tr")
        header = [th.get_text(strip=True) for th in rows[0].find_all("th")]
        if "Model" not in header or "Sensor size" not in header:
            continue
        model_idx = header.index("Model")
        sensor_idx = header.index("Sensor size")
        for row in rows[1:]:
            cols = row.find_all(["td","th"])
            if len(cols) > max(model_idx, sensor_idx):
                model = cols[model_idx].get_text(strip=True)
                sensor = cols[sensor_idx].get_text(strip=True)
                if "APS-C" in sensor or "Full frame" in sensor:
                    models.add(model)
    return sorted(models)

def crawl_fujifilm_mirrorless():
    url = "https://en.wikipedia.org/wiki/List_of_Fujifilm_mirrorless_cameras"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    models = set()

    tables = soup.find_all("table", class_="wikitable")
    for table in tables:
        rows = table.find_all("tr")
        header = [th.get_text(strip=True) for th in rows[0].find_all("th")]
        if "Model" not in header or "Sensor size" not in header:
            continue
        model_idx = header.index("Model")
        sensor_idx = header.index("Sensor size")
        for row in rows[1:]:
            cols = row.find_all(["td","th"])
            if len(cols) > max(model_idx, sensor_idx):
                model = cols[model_idx].get_text(strip=True)
                sensor = cols[sensor_idx].get_text(strip=True)
                if "APS-C" in sensor or "Full frame" in sensor:
                    models.add(model)
    return sorted(models)

def crawl_canon_dslr():
    url = "https://en.wikipedia.org/wiki/List_of_Canon_DSLR_cameras"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    models = set()

    tables = soup.find_all("table", class_="wikitable")
    for table in tables:
        rows = table.find_all("tr")
        header = [th.get_text(strip=True) for th in rows[0].find_all("th")]
        if "Model" not in header or "Sensor size" not in header:
            continue
        model_idx = header.index("Model")
        sensor_idx = header.index("Sensor size")
        for row in rows[1:]:
            cols = row.find_all(["td","th"])
            if len(cols) > max(model_idx, sensor_idx):
                model = cols[model_idx].get_text(strip=True)
                sensor = cols[sensor_idx].get_text(strip=True)
                if "APS-C" in sensor or "Full frame" in sensor:
                    models.add(model)
    return sorted(models)

def crawl_panasonic_mirrorless():
    url = "https://en.wikipedia.org/wiki/List_of_Panasonic_mirrorless_cameras"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    models = set()

    tables = soup.find_all("table", class_="wikitable")
    for table in tables:
        rows = table.find_all("tr")
        header = [th.get_text(strip=True) for th in rows[0].find_all("th")]
        if "Model" not in header or "Sensor size" not in header:
            continue
        model_idx = header.index("Model")
        sensor_idx = header.index("Sensor size")
        for row in rows[1:]:
            cols = row.find_all(["td","th"])
            if len(cols) > max(model_idx, sensor_idx):
                model = cols[model_idx].get_text(strip=True)
                sensor = cols[sensor_idx].get_text(strip=True)
                if "APS-C" in sensor or "Full frame" in sensor:
                    models.add(model)
    return sorted(models)

# === 스펙 추출 함수 (변경 없음) ===

def fetch_camera_info(model):
    url = f"https://en.wikipedia.org/wiki/{model.replace(' ', '_')}"
    r = requests.get(url)
    if r.status_code != 200:
        print(f"[!] {model} 페이지를 찾을 수 없습니다.")
        return None

    soup = BeautifulSoup(r.text, "html.parser")
    info = {"name": model, "price": None, "raw": False, "sensor": None, "weight": None, "type": None}

    infobox = soup.find("table", class_="infobox")
    if not infobox:
        return info

    text = infobox.get_text().lower()

    info["raw"] = "raw" in text

    if "aps-c" in text:
        info["sensor"] = "APS-C"
    elif "full frame" in text:
        info["sensor"] = "Full frame"

    price_match = re.search(r"\$([\d,]+)", text)
    if price_match:
        usd_price = int(price_match.group(1).replace(",", ""))
        info["price"] = usd_price * 1300

    weight_match = re.search(r"(\d+)\s?g", text)
    if weight_match:
        info["weight"] = int(weight_match.group(1))

    if "dslr" in text:
        info["type"] = "DSLR"
    elif "mirrorless" in text:
        info["type"] = "Mirrorless"
    elif "compact" in text or "point-and-shoot" in text:
        info["type"] = "Compact"
    else:
        info["type"] = "Unknown"

    return info

# === 메인 함수 ===

def main():
    models = set()
    models.update(crawl_fixed_lens())
    models.update(crawl_canon_mirrorless())
    models.update(crawl_nikon_mirrorless())
    models.update(crawl_sony_mirrorless())
    models.update(crawl_fujifilm_mirrorless())
    models.update(crawl_canon_dslr())
    models.update(crawl_panasonic_mirrorless())

    print(f"총 {len(models)}개 모델을 크롤링했습니다.")

    data = []
    for i, model in enumerate(sorted(models), 1):
        print(f"[{i}/{len(models)}] {model} 정보 수집 중...")
        info = fetch_camera_info(model)
        if info and info["sensor"]:
            data.append(info)

    with open("cameras.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ 데이터 수집 완료! 총 {len(data)}개 모델 저장됨.")

if __name__ == "__main__":
    main()

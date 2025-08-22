from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Test API", version="1.0.0", description="API для тестирования различных эндпоинтов")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Test API запущен", "docs": "http://37.252.23.30:8000/docs"}

@app.get("/api/egrul")
async def get_egrul_data():
    """
    Тестовые данные ЕГРЮЛ
    """
    return {
        "content": [{
            "dataSved": "2025-02-11",
            "OGRN": "1027700251754",
            "dateOGRN": "2002-09-26",
            "INN": "7710044140",
            "KPP": "770501001",
            "sprOPF": "ОКОНХ",
            "codeOPF": "12300",
            "nameOPF": "Общества с ограниченной ответственностью",
            "fullOrgName": "ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ \"СИСТЕМА ПБО\"",
            "shortOrgName": "ООО \"СИСТЕМА ПБО\"",
            "region": "77",
            "adres": "115054, Г.МОСКВА , УЛ ВАЛОВАЯ, Д. Д. 26",
            "email": "",
            "statusCode": "",
            "statusName": "",
            "dateClose": "",
            "codeClose": "",
            "causeClose": "",
            "codeNO": "7705",
            "nameNO": "Инспекция Федеральной налоговой службы № 5 по г. Москве",
            "codePF": "",
            "namePF": "",
            "codeFSS": "",
            "nameFSS": "",
            "capitalKind": "УСТАВНЫЙ КАПИТАЛ",
            "capitalAmount": "10694064934.33",
            "ulOGRN": "",
            "ulINN": "",
            "nameUl": "",
            "dirFIO": "ПАРОБЕВ ОЛЕГ МРЬЕВИЧ",
            "dirINN": "774331952837",
            "director": "ГЕНЕРАЛЬНЫЙ ДИРЕКТОР",
            "osnovidKVED": "56.10",
            "nameOKVED": "Деятельность ресторанов и услуги по доставке продуктов питания",
            "verOKVED": "2014",
            "uchreditel": [{
                "OGRN": "1027700251754",
                "uchGRN": "2227705232346",
                "uchINN": "4252003977",
                "uchName": "ОБЩЕСТВО С ОГРАНИЧЕННОЙ ОТВЕТСТВЕННОСТЬЮ \"КЛУБ ОТЕЛЬ\"",
                "uchType": "ULR",
                "neddan": ""
            }]
        }]
    }

@app.get("/api/test")
async def test_endpoint():
    """
    Простой тестовый эндпоинт
    """
    return {"message": "Тестовый эндпоинт работает!", "timestamp": "2025-08-22"}

@app.get("/api/health")
async def health_check():
    """
    Проверка здоровья API
    """
    return {"status": "healthy", "service": "test-api"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

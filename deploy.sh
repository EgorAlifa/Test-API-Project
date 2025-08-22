#!/bin/bash
echo "🔄 Обновляем код с GitHub..."
git pull

echo "🐳 Останавливаем старый контейнер..."
docker rm -f test-api-container 2>/dev/null

echo "🔨 Собираем новый образ..."
docker build -t test-api .

echo "🚀 Запускаем контейнер..."
docker run -d \
  --name test-api-container \
  --restart=always \
  -p 8000:8000 \
  test-api

echo "✅ Готово! API доступен на http://37.252.23.30:8000"
docker ps | grep test-api

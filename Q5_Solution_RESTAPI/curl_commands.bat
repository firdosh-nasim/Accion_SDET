echo "COMMAND: curl -i -X GET  http://127.0.0.1:5000" " >> execution_result.txt
curl -i -X GET  http://127.0.0.1:5000 >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt 

echo "COMMAND: curl -i -X GET  http://127.0.0.1:5000/widgets"  >> execution_result.txt
curl -i -X GET  http://127.0.0.1:5000/widgets >> execution_result.txt 
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X POST -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets -d "{\"widget_name\": \"Test Widget\", \"description\": \"Description\"}" ">> execution_result.txt
curl -i -X POST -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets -d "{\"widget_name\": \"Test Widget\", \"description\": \"Description\"}" >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X POST -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets -d "{\"widget_name\": \"Test Widget\", \"description\": \"Description\"}" ">> execution_result.txt
curl -i -X POST -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets -d "{\"widget_name\": \"Test Widget\", \"description\": \"Description\"}" >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X GET  http://127.0.0.1:5000/widgets ">> execution_result.txt
curl -i -X GET  http://127.0.0.1:5000/widgets >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X POST -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets -d "{\"widget_id\": 50, \"widget_name\": \"Test Widget\", \"description\": \"Description\"}" ">> execution_result.txt
curl -i -X POST -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets -d "{\"widget_id\": 50, \"widget_name\": \"Test Widget\", \"description\": \"Description\"}" >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X GET  http://127.0.0.1:5000/widgets ">> execution_result.txt
curl -i -X GET  http://127.0.0.1:5000/widgets >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X GET  http://127.0.0.1:5000/widgets/1" >> execution_result.txt
curl -i -X GET  http://127.0.0.1:5000/widgets/1 >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X GET  http://127.0.0.1:5000/widgets/100 ">> execution_result.txt
curl -i -X GET  http://127.0.0.1:5000/widgets/100 >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X PUT -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets/1 -d "{\"description\": \"A new description\"}" ">> execution_result.txt
curl -i -X PUT -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets/1 -d "{\"description\": \"A new description\"}" >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X GET  http://127.0.0.1:5000/widgets ">> execution_result.txt
curl -i -X GET  http://127.0.0.1:5000/widgets >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X PUT -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets/100 -d "{\"description\": \"A new description\"}" ">> execution_result.txt
curl -i -X PUT -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets/100 -d "{\"description\": \"A new description\"}" >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X DELETE -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets/2 ">> execution_result.txt
curl -i -X DELETE -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets/2 >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X GET  http://127.0.0.1:5000/widgets ">> execution_result.txt
curl -i -X GET  http://127.0.0.1:5000/widgets >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X DELETE -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets/100 ">> execution_result.txt
curl -i -X DELETE -H "X-Auth-Token:5675309" -H "Content-Type:application/json" http://127.0.0.1:5000/widgets/100 >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt

echo "COMMAND: curl -i -X GET  http://127.0.0.1:5000/widgets ">> execution_result.txt
curl -i -X GET  http://127.0.0.1:5000/widgets >> execution_result.txt
echo "-------------------------------------------------------" >> execution_result.txt
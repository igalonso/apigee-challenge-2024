echo "get Orders:"
curl -u apigeechallenge:ApigeeChallenge2024 https://apigee-challenge-nz2wxjkrxa-no.a.run.app/orders

echo "post Orders:"
curl -u apigeechallenge:ApigeeChallenge2024 -X POST -H "Content-Type: application/json" -d '{"order_id": "1", "order_name": "order1", "order_description": "order1 description"}' https://apigee-challenge-nz2wxjkrxa-no.a.run.app/orders
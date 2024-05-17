# GET request

echo "Get a product:"
curl -X POST -H "Content-Type: text/xml" -d '
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:spy="spyne.examples.products">
   <soapenv:Body>
      <spy:get_products/>
   </soapenv:Body>
</soapenv:Envelope>
' https://apigee-challenge-soap-nz2wxjkrxa-no.a.run.app

echo "Post a product:"

# POST request
curl -X POST -H "Content-Type: text/xml" -d '
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:prod="spyne.examples.products">
   <soapenv:Header/>
   <soapenv:Body>
      <prod:post_product>
         <prod:product>
            <prod:id>1</prod:id>
            <prod:name>product1</prod:name>
            <prod:price>100</prod:price>
         </prod:product>
      </prod:post_product>
   </soapenv:Body>
</soapenv:Envelope>
' https://apigee-challenge-soap-nz2wxjkrxa-no.a.run.app

#get WSDL
echo "Get wsdl"
curl -X GET https://apigee-challenge-soap-nz2wxjkrxa-no.a.run.app/?wsdl
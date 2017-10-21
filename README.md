# tornado-simple-api
Simple API using Python3 and Tornado framework

# Install

pip install -r requirements.txt

# Run tornado 

python app.py

# Run tests

fab tests

## Rabbit Integration 

Should have a RabbitMQ installed and the queue names and exchange can be different in the example
 
# Run Publisher

python publisher.py < message to send >

# Run Subscriber 

python subscriber.py

## Redis integration

To use the example with redis, should have a redis configured to run


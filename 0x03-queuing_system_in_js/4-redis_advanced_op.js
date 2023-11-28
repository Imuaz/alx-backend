import { createClient } from 'redis';
const redis = require('redis');
const client = createClient();


client
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (err) => console.error(`Redis client not connected to the server: ${err.stack}`));

// Set hash key-value pairs in the 'HolbertonSchools' hash
client.hset('HolbertonSchools', 'Portland', '50', redis.print);
client.hset('HolbertonSchools', 'Seattle', '80',redis.print);
client.hset('HolbertonSchools', 'New York', '20', redis.print);
client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
client.hset('HolbertonSchools', 'Cali', '40', redis.print);
client.hset('HolbertonSchools', 'Paris', '2', redis.print);

// Retrieve all elements stored in the 'HolbertonSchools' hash
client.hgetall('HolbertonSchools', (err, result) => {
  if (err) {
    console.error(`Error retrieving value for ${Holbertonschools}: ${err.stack}`);
  } else {
    console.log(result);
  }
});

import { createClient } from 'redis';

const redisClient = createClient();

// Event handler for successful connection
redisClient.on('connect', function() {
  console.log('Redis client connected to the server');
});

// Event handler for connection errors
redisClient.on('error', function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});


// Function to publish a message after a specified time
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    redisClient.publish('holberton school channel', message);
  }, time);
}

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);

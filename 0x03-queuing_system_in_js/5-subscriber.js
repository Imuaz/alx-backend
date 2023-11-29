import { createClient } from 'redis';
const redis = require('redis');
const client = createClient();


client
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (err) => console.error(`Redis client not connected to the server: ${err.stack}`));

// subscribe to the channel Holberton School Channel
client.subscribe('holberton school channel');

client.on('message', (channel, message) => {
  console.log(`${message}`);
  if (message === 'KILL_SERVER') {
  //unsubscribe from channel and cancel server connection
    client.unsubscribe('holberton school channel');
    client.end(true);
  }
});

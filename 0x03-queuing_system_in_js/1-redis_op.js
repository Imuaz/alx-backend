import { createClient } from 'redis';
const redis = require ('redis');
const client = createClient();

client
    .on('connect', () => console.log('Redis client connected to the server'))
    .on('error', (err) => console.error(`Redis client not connected to the server: ${err.stack}`));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.error(`Error retrieving value for ${schoolName}: ${err.stack}`);
    } else {
      console.log(`${reply}`);
    }
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

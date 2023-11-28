import { promisify } from 'util';
import { createClient } from 'redis';
const redis = require('redis');
const client = createClient();


client
  .on('connect', () => console.log('Redis client connected to the server'))
  .on('error', (err) => console.error(`Redis client not connected to the server: ${err.stack}`));

const setNewSchool = (schoolName, value) => {  
  client.set(schoolName, value, redis.print);  
};

const getAsync = promisify(client.get).bind(client);

const displaySchoolValue = async (schoolName) => {
  try {
    const value = await getAsync(schoolName);
    console.log(`${value}`);
  } catch (err) {
    console.error(`Error retrieving value for ${schoolName}: ${err.stack}`);
  }
};


(async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
})();

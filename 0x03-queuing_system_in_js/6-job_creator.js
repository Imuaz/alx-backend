import { createQueue } from 'kue';

const queue = createQueue();

// Arrow function to dynamically obtain user's phone number
const getUserPhoneNumber = (phoneNumber) => phoneNumber;

// Arrow function to dynamically obtain user's message
const getUserMessage = (message) => message;

// Function to send a notification
function sendNotification(phoneNumber, message) {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

// Dynamically obtain values for phoneNumber and message
const userPhoneNumber = getUserPhoneNumber('4153518780');
const userMessage = getUserMessage('This is the code to verify your account');

// Create and save the job with dynamic data
const notificationJob = queue.create('push_notification_code', {
  phoneNumber: userPhoneNumber,
  message: userMessage,
}).save(err => !err && console.log(`Notification job created: ${notificationJob.id}`));

notificationJob.on('complete', () => console.log('Notification job completed'));
notificationJob.on('failed', () => console.error('Notification job failed'));

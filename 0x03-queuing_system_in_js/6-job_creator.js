import { createQueue } from 'kue';

const queue = createQueue();

// Function to send a notification
function sendNotification(phoneNumber, message) {
  //console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
}

function getUserPhoneNumber(phoneNumber) {
  return phoneNumber;
}

function getUserMessage(message) {
  return message;
}

// Dynamically obtain values for phoneNumber and message
const userPhoneNumber = getUserPhoneNumber();
const userMessage = getUserMessage();

// Create, save, and process the job with dynamic data
const notificationJob = queue.create('push_notification_code', {
  phoneNumber: userPhoneNumber,
  message: userMessage,
}).save(err => !err && console.log(`Notification job created: ${notificationJob.id}`));

notificationJob.on('complete', () => console.log('Notification job completed'));
notificationJob.on('failed', () => console.error('Notification job failed'));

queue.process('push_notification_code', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message);
  done();
});

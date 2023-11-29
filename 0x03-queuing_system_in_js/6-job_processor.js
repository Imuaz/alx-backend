import { createQueue } from 'kue';

const queue = createQueue();

// Function to send a notification
const sendNotification = (phoneNumber, message) => console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);

// Queue process for 'push_notification_code' jobs
queue.process('push_notification_code', (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message);
  done();
});

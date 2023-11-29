import { createQueue } from 'kue';

const blacklist = new Set(['4153518780', '4153518781']); // Use Set for faster lookups

const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  job.progress(0, 100);

  if (blacklist.has(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});
